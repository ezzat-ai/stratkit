"""StratKit — Streamlit demo app.

Run: streamlit run app.py
Needs ANTHROPIC_API_KEY in the environment (see .env.example).
"""

import streamlit as st

from stratkit import LLMError, issue_tree, market_sizing, synthesize

st.set_page_config(page_title="StratKit — AI copilot for strategy consultants",
                   page_icon="🧭", layout="wide")

st.sidebar.title("🧭 StratKit")
st.sidebar.caption("An AI copilot for strategy consultants.\n\n"
                   "_Built by a strategy consultant, not just an AI engineer._")
tool = st.sidebar.radio("Workflow", ["Issue Tree", "Market Sizing", "Synthesize a document", "About"])
st.sidebar.divider()
st.sidebar.caption("⚠️ AI drafts a first version — you own the judgment. "
                   "Never paste confidential client data into a shared tool.")


def _run(fn, *args):
    try:
        with st.spinner("Thinking like a consultant…"):
            return fn(*args)
    except LLMError as e:
        st.error(f"Config error: {e}")
    except Exception as e:  # noqa: BLE001
        st.error(f"Something went wrong: {e}")
    return None


# ---------------------------------------------------------------- Issue Tree
if tool == "Issue Tree":
    st.header("Issue Tree — MECE problem structuring")
    st.write("Decompose a business question into a MECE, hypothesis-driven tree.")
    q = st.text_input("Business question", "Why are our margins declining?")
    ctx = st.text_area("Context (optional)", height=80,
                       placeholder="Industry, recent events, constraints…")
    if st.button("Build issue tree", type="primary"):
        tree = _run(issue_tree, q, ctx)
        if tree:
            st.subheader(f"❓ {tree.get('question', q)}")
            for br in tree.get("branches", []):
                st.markdown(f"### 🔹 {br['label']}")
                for sq in br.get("sub_questions", []):
                    with st.expander(sq["question"]):
                        st.markdown(f"**Hypothesis:** {sq['hypothesis']}")
                        st.markdown(f"**Analysis to run:** {sq['analysis']}")

# ------------------------------------------------------------- Market Sizing
elif tool == "Market Sizing":
    st.header("Market Sizing — top-down × bottom-up")
    st.write("Triangulate a market size with two independent approaches.")
    q = st.text_input("Market to size", "Electric scooters in Morocco")
    scope = st.text_input("Geography / segment", "Morocco, urban, annual")
    if st.button("Estimate market", type="primary"):
        res = _run(market_sizing, q, scope)
        if res:
            c1, c2 = st.columns(2)
            for col, key, title in [(c1, "top_down", "⬇️ Top-down"),
                                    (c2, "bottom_up", "⬆️ Bottom-up")]:
                with col:
                    block = res.get(key, {})
                    st.subheader(title)
                    for s in block.get("steps", []):
                        st.markdown(f"- **{s['driver']}** — {s['assumption']} → `{s['value']}`")
                    st.success(f"Estimate: {block.get('estimate', '—')}")
            st.info(f"**Reconciled range:** {res.get('reconciled_range', '—')}")
            st.caption("Most sensitive to: " + ", ".join(res.get("key_sensitivities", [])))

# --------------------------------------------------------------- Synthesize
elif tool == "Synthesize a document":
    st.header("Synthesize — from raw source to insight")
    st.write("Structure raw material by insight, with a 'so what' for each finding.")
    content = st.text_area("Paste source material", height=260,
                           placeholder="Paste a report, notes, an article…")
    if st.button("Synthesize", type="primary") and content.strip():
        out = _run(synthesize, content)
        if out:
            st.markdown(out)

# -------------------------------------------------------------------- About
else:
    st.header("About StratKit")
    st.markdown(
        "**StratKit** brings a consultant's method to AI-assisted analysis: "
        "MECE decomposition, hypothesis-driven issue trees, top-down × bottom-up "
        "market sizing, and insight-first synthesis.\n\n"
        "It is **provider-agnostic** (Claude by default), **MIT-licensed**, and "
        "meant to be extended. See the `skills/` folder for prompt & Copilot "
        "skill templates you can drop into your own workflow.\n\n"
        "The philosophy: *AI drafts the first version — the consultant owns the judgment.*")
