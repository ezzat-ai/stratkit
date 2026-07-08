"""StratKit — an AI copilot for strategy consultants.

Built by a strategy consultant, not just an AI engineer.
"""

from .llm import Client, LLMError
from .workflows import issue_tree, market_sizing, synthesize

__version__ = "1.0.0"
__all__ = ["Client", "LLMError", "issue_tree", "market_sizing", "synthesize"]
