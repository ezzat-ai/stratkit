---
name: dcf-valuation
description: Build a Discounted Cash Flow (DCF) valuation from a revenue and margin outlook, with terminal value, a sensitivity table, and guardrails. Use for company valuation, enterprise / equity value, or when building a DCF in Excel or a spreadsheet.
compatibility: Works standalone in Claude, and as an instruction set for Microsoft Copilot in Excel.
---

# DCF valuation

Build a Discounted Cash Flow valuation from a revenue and margin outlook.

## Process
1. **Inputs block** (clearly labelled, one place): base-year revenue, growth per
   year (explicit horizon), EBIT margin path, tax rate, D&A, capex, change in NWC,
   WACC, terminal growth `g`.
2. **Free Cash Flow to Firm** per year: `FCFF = EBIT*(1-tax) + D&A - Capex - ΔNWC`.
3. **Discount** each FCFF at WACC; sum the PV of explicit years.
4. **Terminal value** (Gordon): `TV = FCFF_last*(1+g)/(WACC-g)`, discounted back.
5. **Enterprise Value** = PV(explicit) + PV(terminal). Bridge to Equity Value
   (minus net debt), then per share if shares are given.
6. **Sensitivity table**: EV against WACC (rows) x terminal g (columns).

## Guardrails
- Flag if `g >= WACC` (terminal value breaks).
- Keep every assumption in the inputs block. No hard-coded numbers in formulas.
- State the terminal value's share of EV; warn if it exceeds ~75%.
