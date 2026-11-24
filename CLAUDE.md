# Startup ideas generator v2

A research procedure, run by Claude in this folder, that turns a vertical into graded
problem briefs for Edgar's team. `PROPOSAL.md` gives the design and its reasons.

## Run order

`/map-work <vertical> <cc>` → `/hunt <vertical>-<cc>` → `/brief` per candidate →
`/redteam` per brief → Edgar grades → record in `grades.md`.

Current focus (since 2026-11-16): Latvia, all sectors, searched in Latvian
(`verticals/latvia/`). `scan.md` there is a longlist of openings; the next step is to
turn chosen openings into candidates with ledgers, then briefs. Lithuania and Estonia
get the neighbour check. For a whole-country scan, `/map-work` is replaced by a source
sweep: start from the state audit office, open data portals, and dated legal
obligations.

Paused: architecture, France (`verticals/architecture-fr/`): one brief graded
plausible, eight candidates, none briefed further.

## Rules that must hold

- **No infrastructure.** No database, interface, scheduler, or eval harness until the
  engine passes its bar (`grades.md`). Code enters only for a free API that a brief has
  already used by hand. v1 failed by building first.
- **Nothing paid** beyond the Claude subscription until the bar is passed.
- **Measured evidence only.** A problem needs money, time, or risk evidence from a
  source; complaints are colour. Never state a figure you have not seen in a source.
- **Mark every figure** `[P]` (primary source read), `[S]` (secondary), or `[C]`
  (computed from primary open data; keep the script in the vertical's `data/` folder).
- **Money must be tied to the specific problem.** Sector totals show market size only.
- **Core work only**, except trivial problems that recur across most firms.
- **Assume nothing about the team's constraints.** They apply those themselves.
- Edgar launches anything that spends money or contacts people.

## Reference

- `research/source-map.md`: ranked source types; revise it as verticals teach more.
- `research/worked-example-permit-completeness.md`: the brief format.
- v1 lives in `..\Startup ideas generator` as a record of mistakes. Reuse none of its
  code.
