# StratKit Skills Library

Consulting-grade [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
you can drop straight into Claude. Each skill is a kebab-case folder with a
`SKILL.md` (YAML frontmatter `name` + `description`, then the method). Claude
reads the description and loads the skill only when your prompt matches.

| Skill | Folder | Use for |
|-------|--------|---------|
| MECE issue tree | [`issue-tree/`](issue-tree/SKILL.md) | Structuring a problem |
| Market sizing | [`market-sizing/`](market-sizing/SKILL.md) | TAM / SAM, "how big is the market" |
| DCF valuation | [`dcf-valuation/`](dcf-valuation/SKILL.md) | Company valuation (also Copilot in Excel) |

## Use them in Claude

**Claude apps (claude.ai)** — zip the folder, then upload it:

```bash
cd skills
zip -r issue-tree.zip issue-tree/        # the zip must contain the folder
```

Then in Claude: **Settings → Capabilities → Skills → Upload**, pick the zip.
Ask your question in chat and Claude loads the skill automatically when it fits.

**Claude Code** — drop the folder into your skills directory:

```bash
cp -r issue-tree ~/.claude/skills/       # or .claude/skills/ in your project
```

Claude Code discovers it on the next run. No restart needed.

## Contributing

New skills are the easiest way in: one kebab-case folder, one `SKILL.md` with
`name` + `description` frontmatter and a worked example. See `CONTRIBUTING.md`.
