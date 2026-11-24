# Proposal: the engine

Draft 1, 2026-11-16. Accepted; Edgar's decisions close this file. The skills are built.

## What it is

The engine is a research procedure with strict gates, run by Claude in this folder, that
turns a vertical into graded problem briefs. It has no database, interface, or scheduler.
Its value lies in three rules v1 lacked: start from the work, accept only measured
evidence, and try to kill every brief before Edgar reads it.

One session produced the worked example
(`research/worked-example-permit-completeness.md`) with this procedure done by hand. v1
produced no brief in five weeks.

## The procedure

| Step | Name | Input → output | Gate |
|---|---|---|---|
| 1 | Map the work | Vertical + country → 10 to 15 core workflows, each with who does it and what it produces | Core work only. Marketing, generic admin, and thin-wrapper problems are dropped unless they recur across many firms |
| 2 | Hunt for measured failure | Workflow → candidate problems with numbers | A candidate needs one measured figure (rate, days, money) from a source ranked 1 to 5 in `research/source-map.md` |
| 3 | Build the evidence ledger | Candidate → table of claims, each with source, date, kind (money, time, risk, words), and whether the primary source was read | Three independent sources; one of kind money for "worth testing"; words never count |
| 4 | Write the brief | Ledger → one page in the worked example's format, with 3 to 5 solution directions and kill criteria | Every figure carries a mark: primary read, or secondary |
| 5 | Red team | Brief → attack by a fresh session that sees only the brief: refetch each citation, look for the reason it fails, look for the product that already exists | A misread or unreachable citation sends the brief back to step 3 |
| 6 | Grade | Edgar marks junk, plausible, or worth testing, with one line of reason | Grades and reasons go in `grades.md`; each batch's reasons revise steps 1 and 2 |

Step 1 uses documents that already list a profession's work: fee scales and scopes of
service (for German architects, the nine HOAI service phases), accreditation standards,
job descriptions. Step 2 searches in the language of the target country.

## After the grade

A brief graded worth testing climbs the ladder agreed in the interview, with kill
criteria written before each rung:

1. **Desk validation.** Competitors and prices, a bottom-up count of EU buyers, a search
   for earlier failed attempts.
2. **Practitioner check.** Five to ten short conversations; the engine drafts the
   messages and questions, the team sends them.
3. **Smoke test.** The engine prepares the landing page and outreach; the team launches
   and measures against a preset threshold. Only this rung can cost money, and only once
   the engine has passed its bar.

## The bar

For architecture, the engine delivers 10 briefs. It passes if Edgar grades 3 or more
worth testing and none rests on fabricated or misread evidence. Until it passes, it costs
nothing beyond the Claude subscription.

## What gets built

Four skill files in `.claude/skills/`, each a page of instructions, and three folders:

```
.claude/skills/map-work, hunt, brief, redteam
verticals/architecture-fr/   workflows.md, candidates.md, briefs/NN-slug.md
research/                    source-map.md, worked example
grades.md
```

The red team runs as a subagent so that it starts without the author's context. Code
enters only where a source has a free API and a brief has already used it by hand; the EU
tender search is the first candidate. Scheduling, storage, and a viewer wait until the
bar is passed, and v1's research on them remains available then.

## Expected effort

The worked example took one session. Ten briefs with red-team passes should take five to
eight sessions, plus about two hours of Edgar's time to grade.

## Risks

- **The model fabricates or misreads a figure.** Step 5 exists for this, and the marks in
  step 4 show which claims no one has checked at the source.
- **Briefs converge on what is already funded.** The worked example sits beside five
  funded startups. The crowding check runs in step 3, before the brief is written.
- **Public-record problems skew toward regulated, slow markets.** Measured failures are
  published mostly where the state is a party. The grades will show whether Edgar's team
  wants those markets.
- **One worked example proves little.** It showed that the procedure reaches a specific,
  evidenced, non-trivial problem. It did not show a hit rate of 3 in 10.

## Decisions (Edgar, 2026-11-16)

1. **Worked example:** plausible. The procedure becomes skills.
2. **Country and language:** France, searched in French. One country per run, because
   the evidence is national. Belgium, Luxembourg, Switzerland, and Monaco share the
   language and get a neighbour check in each brief; their rules differ, so a brief
   claims nothing about them unchecked.
3. **Public buyers:** they stay in, outside the main focus. A brief says plainly when
   the payer is a public body.

The pilot folder is therefore `verticals/architecture-fr/`.
