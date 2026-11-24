---
name: redteam
description: Step 5 of the engine. Attack a finished brief from a fresh context, verify each citation at its source, and return a verdict. Use after /brief, e.g. "/redteam verticals/architecture-fr/briefs/01-slug.md".
---

# Red team

Input: the path of one brief. Output: a `## Red team` section appended to that brief.

Run the attack in a subagent (general-purpose) so that it starts without the author's
context. Give it the brief's path and the instructions below, nothing else from this
session. Edgar approved this use of a subagent in `PROPOSAL.md`.

## Instructions for the attacker

You are trying to kill this brief. Read only the brief.

1. **Check every citation.** Fetch each source. For each figure, report: found as
   stated, found but different (give the real figure), absent, or unreachable. A `[P]`
   mark on a figure the source lacks is the most serious finding.
2. **Find the existing fix.** Search in the country's language for products, services,
   public portals, or free tools that already solve it. The author missed one more often
   than not.
3. **Find the reason it fails.** Look for earlier attempts that died, for a reason the
   behaviour is rational (the "failure" is a tactic), for a rule change that removes the
   problem, and for a payer who has no budget.
4. **Test the gates.** Three independent sources? Any of them the same data republished?
   Is a money-kind entry real spend or an inference?
5. **Verdict.** `stands`, `stands with corrections` (list them), or `falls` (say why).

Report facts with URLs. Do not soften findings and do not rewrite the brief.

## After the attack

- `falls`, or any misread or absent figure: return the brief to `/hunt` for that
  candidate, or drop it and record why in `candidates.md`.
- `stands with corrections`: apply them, re-mark the figures, and keep the red-team
  section in the brief so Edgar sees what was challenged.
- Then present the brief to Edgar for grading and record his grade in `grades.md`.
