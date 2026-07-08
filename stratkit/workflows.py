"""The three flagship workflows, kept UI-agnostic so they can power the
Streamlit app, a CLI, or a future API equally well."""

from __future__ import annotations

import json

from .llm import Client
from . import prompts


def _json(text: str) -> dict:
    """Parse model output as JSON, tolerating stray prose or code fences."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1].lstrip("json").strip()
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model output.")
    return json.loads(text[start:end + 1])


def issue_tree(question: str, context: str = "", client: Client | None = None) -> dict:
    """Decompose a business question into a MECE, hypothesis-driven issue tree."""
    client = client or Client()
    resp = client.complete(
        system=prompts.ISSUE_TREE_SYSTEM,
        user=prompts.format_prompt(prompts.ISSUE_TREE_USER, question=question, context=context),
        max_tokens=2500,
    )
    return _json(resp.text)


def market_sizing(question: str, scope: str = "", client: Client | None = None) -> dict:
    """Estimate a market size via top-down + bottom-up triangulation."""
    client = client or Client()
    resp = client.complete(
        system=prompts.MARKET_SIZING_SYSTEM,
        user=prompts.format_prompt(prompts.MARKET_SIZING_USER, question=question, scope=scope),
        max_tokens=2000,
    )
    return _json(resp.text)


def synthesize(content: str, client: Client | None = None) -> str:
    """Turn raw source material into an insight-structured, client-ready synthesis."""
    client = client or Client()
    resp = client.complete(
        system=prompts.SYNTHESIZE_SYSTEM,
        user=prompts.format_prompt(prompts.SYNTHESIZE_USER, content=content),
        max_tokens=1800,
    )
    return resp.text
