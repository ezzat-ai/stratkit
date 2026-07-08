<p align="center">
  <img src="assets/logo.png" alt="StratKit logo" width="84" height="84">
</p>
<h1 align="center">StratKit</h1>
<p align="center"><b>An open-source AI copilot for strategy consultants.</b><br>
<i>Built by a strategy consultant, not just an AI engineer.</i></p>

<p align="center">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="python" src="https://img.shields.io/badge/python-3.10%2B-blue">
<img alt="LLM" src="https://img.shields.io/badge/LLM-provider--agnostic-8A2BE2">
<img alt="version" src="https://img.shields.io/badge/version-v1.0.0-2159D8">
</p>

---

## Why StratKit?

Generic "chat with your data" tools don't know the consulting craft. StratKit
does one thing well: it brings a **consultant's method** to AI-assisted work —
MECE decomposition, hypothesis-driven issue trees, top-down × bottom-up market
sizing, and insight-first synthesis.

> **Philosophy:** AI drafts the first version — *the consultant owns the judgment.*

## What's inside

| Workflow | What it does |
|----------|--------------|
| <img src="assets/icons/issue-tree.png" width="17" valign="middle"> **Issue Tree** | Turns a business question into a MECE, hypothesis-driven tree — each leaf with a falsifiable hypothesis and the analysis to test it. |
| <img src="assets/icons/market-sizing.png" width="17" valign="middle"> **Market Sizing** | Triangulates a market with top-down **and** bottom-up, then reconciles into a defensible range with sensitivities. |
| <img src="assets/icons/synthesize.png" width="17" valign="middle"> **Synthesize** | Structures raw source material by insight, with a "so what" for every finding — never inventing facts. |
| <img src="assets/icons/skills.png" width="17" valign="middle"> **Skills library** | Drop-in [Agent Skills](skills/) (`SKILL.md`) for Claude: issue tree, market sizing, DCF (also Copilot in Excel). |

## Quickstart

```bash
git clone https://github.com/<your-user>/stratkit.git
cd stratkit
pip install -r requirements.txt
cp .env.example .env        # add your ANTHROPIC_API_KEY
streamlit run app.py
```

Use it as a library too:

```python
from stratkit import issue_tree
tree = issue_tree("Why are our margins declining?", context="Retail, EU, FY26")
```

## Design principles

- **Provider-agnostic** — Claude by default, one env var to switch (`STRATKIT_PROVIDER`).
- **Method over magic** — the value is in [`stratkit/prompts.py`](stratkit/prompts.py), where the consulting rigor is encoded.
- **UI-agnostic core** — workflows power the app, a CLI, or a future API equally.
- **Responsible by design** — the app reminds users never to paste confidential
  client data into a shared tool, and that AI output is a first draft, not a deliverable.

## Roadmap

- [ ] Slide storyliner ("so what" + pyramid principle)
- [ ] Competitor tear-down template
- [ ] Export issue trees to Markdown / PowerPoint
- [ ] Community skills library (PRs welcome)

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). New skills are the easiest way in —
one file, one worked example.

## License

[MIT](LICENSE) © 2026 Ayoub Ezzati — free to use, fork and build on.

---

<p align="center"><sub>StratKit is an independent open-source project. It ships original
frameworks and does not reproduce any firm's proprietary material.</sub></p>
