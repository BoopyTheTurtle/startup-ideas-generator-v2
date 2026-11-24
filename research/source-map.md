# Source map: which public sources reveal real business problems

Written 2026-11-16 from one exploratory session on architecture. "Tested" means I
queried the source type in that session and say what came back. Untested rows are
hypotheses, ranked lower until a brief uses them.

## The finding

The sources that found a real problem were official records that measure a failure, not
places where people complain. A city published the share of permit applications it sends
back; a professional chamber surveyed 15,000 members on the same procedure. Neither is a
complaint, both carry numbers, and both are free.

Two consequences follow. First, discovery starts from a workflow and asks "who measures
how often this goes wrong?", where v1 started from a text stream and asked "who is
unhappy?". Second, for an EU market the best records are in the local language: every
strong source in the worked example is German. Round 2 settled on English-language
discovery; the evidence argues for searching in the language of the target country, which
costs nothing because the model reads it.

## What each kind of evidence proves

| Kind | Meaning | Weight |
|---|---|---|
| Money | Someone pays today: a purchase, a hire, a fee, a fine, a tender, a budget line | Required for "worth testing" |
| Time | Measured hours or days lost in a workflow | Strong |
| Risk | A deadline, sanction, rejection rate, or liability | Strong |
| Words | Complaints, wishes, opinions | Colour only; never qualifies a problem |

## Ranked source types

| Rank | Source type | Proves | Free | Tested | Result |
|---|---|---|---|---|---|
| 1 | Performance records of authorities and regulators (permit offices, inspectorates, ombudsmen) | Time, risk | Yes | Yes | Dortmund: 64% of applications incomplete, 50 days lost. English regulator: 273 of 639 closed applications invalid. The best source found |
| 2 | Member surveys by chambers and professional associations | Time, risk, size of group | Yes | Yes | Architects' chamber survey, 15,659 respondents, with timings per procedure step. The ACE sector study gives firm counts for 30 countries |
| 3 | Parliamentary papers and government progress reports | Risk, public money, volume | Yes | Yes | Surfaced unprompted: national application volume, a federal AI pilot, a state's stated intent to buy a check |
| 4 | Procurement notices (TED for the EU) | Money, public side | Yes; the search API needs no key | Yes | Query ran from the command line and returned two software awards for digital permit filing. Shows what public bodies already buy and from whom |
| 5 | Regulation with a compliance date | Risk, forced demand | Yes | Yes | EU buildings directive: life-cycle carbon figures required for large new buildings from 2028, all from 2030. Real, but incumbents publish the guides, so the demand is already contested |
| 6 | Startup funding news | Crowding; that investors believe | Yes | Yes | Five funded companies near the worked example in one search. A check, never a discovery source |
| 7 | Job postings | Money: a salary paid for manual work | Free APIs with a key (Adzuna); EURES | Tried once | One search returned nothing usable. Needs a proper query against a postings API before I rate it |
| 8 | Court and tribunal decisions | Risk; that disputes reach litigation | Yes | Seen | Administrative court rulings on document requests appeared in results. Unexplored |
| 9 | Vendor and industry reports (Deltek, NBS, manufacturers) | Time, with numbers | Yes | Yes | Useful figures (four hours a week checking product claims, from an 80-architect survey), but the publisher sells the cure |
| 10 | Insurance claims reports | Risk, by cause | Yes | Yes | Weak: broker marketing, no cause breakdown, UK and US only |
| 11 | Freelance and outsourcing markets | Money: work firms pay others to do | Yes, by hand | No | Hypothesis: gigs and outsourcing firms mark work that is costly and separable |
| 12 | Software review sites | Money; where current tools fail | By hand only; scraping breaches terms | No | For the competitor section of a brief |
| 13 | Practitioner forums | Words | Yes | No | Colour and vocabulary. v1 lived here and found nothing |

## Added after the France pilot (2026-11-16)

| Source type | Proves | Free | Tested | Result |
|---|---|---|---|---|
| Open contract data (France: *données essentielles de la commande publique* on data.gouv.fr) | Money tied to an event, with a named payer | Yes; a remote query reads the file without downloading it | Yes | 731,000 works contracts. Gave amendment rates, amounts added, and bids per contract in one query. It gives no causes. Belongs at rank 2 or 3 |
| Insurer annual reports and insurer-funded observatories | Money, sector-wide; risk by cause | Yes | Yes | Good for market size, weak for a single problem: brief 01's red team showed sector totals passing as problem evidence |
| Regional state inspection reports | Risk, specific and yearly | Yes | Yes | The French counterpart of a city's permit statistics. Rank 1 |

Search summaries failed on seven workflows where raw data later answered. When a search
finds no measure, look for the dataset before concluding that none exists.

## What v1 got wrong about sources

v1's own research ranked complaint streams first and placed labour, regulation, and
procurement in a "next wave" it never reached. It then collected what had an API (Hacker
News, browser add-on reviews, plugin support threads), so the engine saw developers and
consumers and never a business in any target vertical.

## Added after Latvia's L3 (2026-11-16)

- **Read the draft law before trusting a dated obligation.** A trade article said
  carriers "must" file freight data electronically from July 9, 2027. The draft and the
  EU regulation both say "where" and "if". Twenty minutes of reading closed the
  candidate.
- **Latvia's draft-law portal** (`tapportals.mk.gov.lv/legal_acts?search[query]=...`)
  serves each draft, its explanatory note, and the ministries' review rounds as plain
  HTML. The note states whether the draft exceeds the EU text and estimates the cost to
  firms, which is a problem-specific money figure when one exists.

## Added after the career-change hunt (2026-11-24)

- **A programme's closing report beats every search about it.** Latvia's draft-law
  portal held the ministry's report on an EU-funded pilot and a 146-page independent
  evaluation: usage funnels, a population survey, costs, and the funding plan. Search
  the portal for the programme's name when a pilot nears its end date. Rank 1.
- **State unit-cost tables and funding rules price a service.** The UK's funding rules
  and Italy's standard-cost annex gave prices per outcome and per hour for career
  guidance. Look for them wherever the state pays private providers. Rank 2.
- **Evaluations commissioned by ministries carry willingness-to-pay figures.** The
  Dutch evaluation asked participants what they would have paid. Rank 2.
- **Fetch agents return PDFs as raw bytes.** Extract the saved file with pypdf. Some
  official servers (Bundestag, UK Find a Tender, OECD) refuse automated reading.

## Added after the Latvian education sweep (2026-11-24)

- **Agencies publish results as slide decks and yearly reviews, reachable only as
  PDFs.** The exam agency's results deck, the ministry's vocational admissions review,
  and the welfare ministry's training review each gave counts, reasons, and unit costs
  that no search summary carried. Find the agency's `media/.../download` links, save
  the file, and extract it. Rank 1.
- **Read the breakdown behind a headline count.** 2,591 secondary pupils failed
  mathematics; the same slide showed that 332 were ordinary grade 12 pupils.
- **oecd.org refuses every automated read.** Ministries often publish a national
  summary of the same tables, and third-party copies of single tables exist.

## Limits of this map

It rests on one vertical, one country, and one problem. Defense will stress it: complaint
and survey data are scarce there, so ranks 3 to 5 (parliamentary papers, procurement,
regulation) must carry the load. The ranking should be revised after each vertical.

## Sources

- TED search API documentation: https://docs.ted.europa.eu/api/latest/search.html
- ACE 2024 sector study: https://build-up.ec.europa.eu/en/resources-and-tools/publications/ace-2024-sector-study
- European Commission on life-cycle carbon in the buildings directive: https://energy.ec.europa.eu/topics/energy-efficiency/energy-performance-buildings/energy-performance-buildings-directive/global-warming-potential-buildings_en
- Deltek Clarity studies, May 2026: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
- NBS on the cost of compliance, June 11, 2026: https://www.thenbs.com/knowledge/the-hidden-cost-of-compliance-why-architects-are-demanding-a-new-era-of-product-transparency
- PolicyBee claims report via the Construction Industry Council: https://www.cic.org.uk/news/architects-made-over-a-third-of-all-pi-claims-in-2020
- The worked example's sources are listed in `worked-example-permit-completeness.md`.
