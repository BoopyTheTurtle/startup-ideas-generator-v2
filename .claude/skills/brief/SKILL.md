---
name: brief
description: Step 4 of the engine. Turn one candidate's evidence ledger into a one-page problem brief with solution directions and kill criteria. Use after /hunt, e.g. "/brief architecture-fr <candidate>".
---

# Write the brief

Input: one candidate and its ledger from `verticals/<vertical>-<cc>/candidates.md`.
Output: `verticals/<vertical>-<cc>/briefs/NN-slug.md`.

Follow the format of `research/worked-example-permit-completeness.md`. Sections, in
order:

1. **The problem.** Two or three sentences.
2. **Who has it.** Role, firm type, size, and a count of them in the country. Name who
   carries the cost if that is someone else.
3. **The workflow and where it breaks.** The measured failures, each with source and
   mark.
4. **What it costs now.** A table by kind: money, time, risk. Show gaps as gaps.
5. **How they cope today.** Tools, hires, workarounds.
6. **Who already sells a fix.** Company, what it does, why it leaves room. Include public
   bodies that may build the fix themselves.
7. **Why now.** What changed that makes it solvable or urgent.
8. **Neighbours.** One short check each for Belgium, Luxembourg, Switzerland, and Monaco:
   same rule or a different regime, and any figure found. Claim nothing unchecked.
9. **Solution directions.** Three to five, each one or two sentences. Include one
   service-first direction that needs no product. Do not rank them; the team picks.
10. **The weakest points.** Lead with the one most likely to kill the brief.
11. **Kill criteria.** Thresholds that can be checked, written before any test.
12. **My own grade.** Junk, plausible, or worth testing, with the reason. "Worth testing"
    requires a money-kind entry in the ledger.
13. **Sources.** Title, date, URL.

## Rules

- One page of substance; cut what does no work.
- Every figure carries `[P]` or `[S]`. Quote sources in French where the wording
  matters, with an English gloss.
- Public buyers stay in but are not the focus: say plainly when the payer is a public
  body.
- Assume nothing about the team's skills, capital, or contacts.
- Follow `C:\Users\Edgar\Claude\Writing\STYLE.md`.
- Then run `/redteam` on the brief before showing it to Edgar.
