"""Provider-agnostic LLM client.

StratKit defaults to Anthropic Claude but is designed so you can swap the
backend without touching the workflow logic. Keep the surface tiny on purpose:
one `complete()` call is all the workflows need.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

# Default model — override with STRATKIT_MODEL.
DEFAULT_MODEL = os.getenv("STRATKIT_MODEL", "claude-sonnet-5")


@dataclass
class LLMResponse:
    text: str
    model: str


class LLMError(RuntimeError):
    """Raised when the LLM backend is missing config or fails."""


class Client:
    """Minimal wrapper over a chat/completions backend.

    Provider is chosen from STRATKIT_PROVIDER (``anthropic`` by default).
    Only the pieces the workflows actually use are exposed.
    """

    def __init__(self, provider: str | None = None, model: str | None = None):
        self.provider = (provider or os.getenv("STRATKIT_PROVIDER", "anthropic")).lower()
        self.model = model or DEFAULT_MODEL

    def complete(self, system: str, user: str, *, max_tokens: int = 2000,
                 temperature: float = 0.2) -> LLMResponse:
        """Run a single-turn completion. Low temperature by default: in
        consulting we want consistent, defensible structure, not creativity."""
        if self.provider == "anthropic":
            return self._anthropic(system, user, max_tokens, temperature)
        if self.provider == "openai":
            return self._openai(system, user, max_tokens, temperature)
        raise LLMError(f"Unknown provider: {self.provider!r}")

    # --- backends -------------------------------------------------------
    def _anthropic(self, system, user, max_tokens, temperature) -> LLMResponse:
        try:
            import anthropic
        except ImportError as e:  # pragma: no cover
            raise LLMError("Install the SDK: pip install anthropic") from e
        if not os.getenv("ANTHROPIC_API_KEY"):
            raise LLMError("Set ANTHROPIC_API_KEY (see .env.example).")
        client = anthropic.Anthropic()
        msg = client.messages.create(
            model=self.model, max_tokens=max_tokens, temperature=temperature,
            system=system, messages=[{"role": "user", "content": user}],
        )
        return LLMResponse(text=msg.content[0].text, model=self.model)

    def _openai(self, system, user, max_tokens, temperature) -> LLMResponse:
        try:
            from openai import OpenAI
        except ImportError as e:  # pragma: no cover
            raise LLMError("Install the SDK: pip install openai") from e
        if not os.getenv("OPENAI_API_KEY"):
            raise LLMError("Set OPENAI_API_KEY (see .env.example).")
        client = OpenAI()
        resp = client.chat.completions.create(
            model=self.model, max_tokens=max_tokens, temperature=temperature,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}],
        )
        return LLMResponse(text=resp.choices[0].message.content, model=self.model)
