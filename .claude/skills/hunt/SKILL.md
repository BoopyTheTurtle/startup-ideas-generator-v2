---
name: hunt
description: Step 2 and 3 of the engine. For a mapped vertical, hunt for measured failures in its workflows and build an evidence ledger per candidate problem. Use after /map-work, e.g. "/hunt architecture-fr".
---

# Hunt for measured failure

Input: `verticals/<vertical>-<cc>/workflows.md`. Output:
`verticals/<vertical>-<cc>/candidates.md`, one section per candidate with its ledger.

## Procedure

1. Read `research/source-map.md` and `grades.md`. Past grades and their reasons steer
   which workflows and sources to favour.
2. For each workflow, ask: who measures how often this goes wrong, how long it takes, or
   what it costs? Search in the country's language, source types in ranked order:
   authority and regulator performance records, chamber and association surveys,
   parliamentary papers and government reports, procurement notices, regulation with a
   compliance date. Use lower-ranked types to fill gaps.
3. Procurement: the EU tender search needs no key.
   `POST https://api.ted.europa.eu/v3/notices/search` with JSON
   `{"query": "FT ~ (\"terme\" AND logiciel) AND PD >= 20250101", "fields": ["notice-title","buyer-name","publication-date","notice-type"], "limit": 25, "page": 1}`.
   Send the body as UTF-8 from a file when it has accented characters.
4. A workflow with no measured figure after a fair search yields no candidate. Record it
   as `no measure found` and move on.
5. For each candidate, build the ledger and run the crowding check: search for funded
   startups and incumbents that sell a fix in this country.

## The ledger

| Claim | Figure | Kind | Source, date, URL | Mark |
|---|---|---|---|---|

- **Kind** is money (someone pays today: purchase, hire, fee, fine, tender, budget),
  time (measured hours or days lost), risk (deadline, sanction, rejection rate,
  liability), or words (complaints, wishes, opinions).
- **Mark** is `[P]` when you read the primary source and the figure is in it, `[S]`
  otherwise. Read the primary source whenever it is reachable. A PDF that WebFetch
  returns as binary can be read with
  `uv run --with pypdf python -I -c "..."` on the saved file.

## Gates

- A candidate needs one measured figure from a source ranked 1 to 5.
- It advances to a brief with three independent sources. Words never count toward three.
- Record whether a money-kind entry exists that is tied to this problem. Sector totals
  (all premiums, all claims paid) show the market's size and do not count. Look for a
  cost per incident and for who bears it. Without a problem-specific money entry, the
  brief can reach "plausible" and no higher.
- Keep every qualifier the source gives: net or gross, count or cost, the base of each
  percentage, the year, and whether the figure rose or fell. Brief 01's red team found
  four dropped qualifiers and one claim the source did not make.
- Apply the core-work filter from `/map-work` again; drop what fails it.

## When you compute from raw data

- Before trusting a rate, check how the data encodes absence: a blank identifier may
  mean "private individual", not "nobody". Brief L-01 counted 226 lots as unanswered
  for that reason.
- Give every comparison its baseline. "57% of sole bidders were known to the buyer"
  meant nothing once 53% of all bidders turned out to be.
- Sample twenty raw rows behind any striking number and say what they are.
- Run the crowding check before the brief, with the product's function as the search
  term ("tender intelligence"), not only the incumbents you already know.

- Test a "they never do X" count across years and definitions before building on it.
  Brief L-02 said 16 of 30 buyers ran no software tender; over three years it was 7.
- Read the rule's own text for scope and transitional exceptions before writing a
  date into a brief. L-02 took a cap's scope from a news article and got it wrong.
- Search the dataset itself for the fix being sold. L-02's catalogue data contained a
  "procurement support" position that buyers already paid for.
- Put every count in a script. L-02's one wrong number was counted by eye from a list.

## Rules

- Never state a figure you have not seen in a source. Write `gap` where evidence is
  missing; gaps are findings.
- The evidence base is one country. Leave neighbours to the brief's last check.
- Update `research/source-map.md` when a source type proves better or worse than ranked.
