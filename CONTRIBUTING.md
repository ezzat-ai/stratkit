# Contributing to StratKit

Thanks for helping build a consulting-grade open-source toolkit!

## Easiest contribution: a new skill
1. Add one file under `skills/` (`excel/`, `claude/`, or `prompts/`).
2. Include a short **worked example** so others can see it in action.
3. Add a row to `skills/README.md`.

## Code contributions
- Keep workflows **UI-agnostic** (logic in `stratkit/`, never in `app.py`).
- Low temperature by default — we want defensible, consistent structure.
- Never hard-code secrets; read from the environment.

## Ground rules
- Ship **original** frameworks only. Do not paste proprietary materials from
  any consulting firm.
- Be explicit about assumptions — that's the whole point of the craft.

Open an issue to discuss anything bigger before a large PR. 🙌
