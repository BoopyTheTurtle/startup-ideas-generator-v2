# Brief L-01: a third of Latvian public tender lots draw one bid or none

Latvia, public procurement. Written 2026-11-16 from candidate L2; rewritten the same day
after the red team's report.

Marks: **[C]** computed from the state e-procurement system's open data (scripts
`data/tenders_single_bid_2025.py` and `data/tenders_incumbency_2024_2025.py`). The red
team recomputed every [C] figure with its own code, found one bug, and I reran the fixed
scripts; the figures below are the corrected ones. **[RT]** found or verified by the red
team; I have not read the source myself. **[S]** search summary.

## The problem

In 2025, 27.9% of lots in Latvia's electronic tenders drew exactly one bid and 6.4% drew
none. The single-bid share is real, stable, and officially acknowledged. The reasons
firms stay away have not been measured by anyone.

## Who has it

- **Buyers:** 530 public bodies ran e-tenders in 2025. Of the 313 that opened ten lots
  or more, about a fifth saw half or more of their lots draw one bid or none. [C]
- **Suppliers:** 6,397 registered entities and about 504 private individuals bid in
  2025. A third of the entities bid once; the top 1% placed 24% of all bids; 35% had
  not bid the year before; 6.9% were foreign. [C]

## Where it breaks

| Measure | 2024 | 2025 | Mark |
|---|---|---|---|
| Lots opened | 25,173 | 27,955 | [C] |
| Drew no bid | 6.1% | 6.4% | [C] |
| Drew one bid | 27.1% | 27.9% | [C] |
| Median bidders per lot | 2 | 2 | [C] |

The data covers tenders run through the state system: open tenders, small procurements,
light-touch services, utilities. It omits purchases under €10,000, catalogue orders, and
most unpublished negotiated awards. Counted by whole procurement instead of by lot, 3.6%
drew no bid and 23.4% drew a single bidder across all lots [RT].

By category (2025, divisions with 150 lots or more):

| Category (CPV division) | Lots | No bid | One bid, among lots with a bid |
|---|---|---|---|
| Recreation, culture, sport services (92) | 452 | 20.6% | 49.3% |
| Health and social services (85) | 239 | 20.5% | 68.4% |
| Education and training services (80) | 844 | 14.8% | 37.8% |
| Research and development services (73) | 248 | 12.5% | about 46% |
| Hotel, restaurant, catering services (55) | 336 | 11.0% | about 44% |
| IT services (72) | about 400 | low | about 57% |
| Repair and maintenance services (50) | 1,420 | about 11% | about 42% |
| Medical equipment and pharmaceuticals (33) | 4,646 | about 8% | about 38% |
| Construction works (45), for contrast | about 4,000 | 3.6% | 16.7% |

What the unanswered lots are. Most are fragments: 78% of no-bid lots sit inside
multi-lot procurements, a quarter of them in 55 procurements of 21 lots or more. The
unanswered service lots are micro-lots meant for individuals: municipal dance, Pilates,
and infant-swimming classes at €744 to €3,719 a lot, police psychologists at €3,600 for
two years per town. Buyers split EU-funded health-promotion projects into dozens of
tiny local lots [RT, by sampling the data]. Firms that would buy a tool are not the
suppliers of these lots.

Single-bid lots also fail more often: about 22% ended interrupted or without result,
against about 9% of lots with two or more bids [RT].

## What it costs now

| Kind | Evidence | Mark |
|---|---|---|
| Risk | Single-bid share of 27 to 28% by lot, two years running; officials report 25 to 26% on their own count, and the head of the procurement office calls insufficient competition the main problem | [C], [RT] |
| Money, weak | Single-bid lots carry about €346M of planned value, but a value is recorded for only 46% of lots, the top 20 lots hold €77M of it, and it includes €15M of banking and deposit services. Planned value in a single-bid lot is exposure, not loss | [C], [RT] |
| Money, official estimate | The government expects the reform to save 2 to 4% of procurement spending. The European Commission's rule of thumb, quoted by the procurement office, is about 2.5% lower cost per additional bid | [RT] |
| Gap | No measured price premium in Latvia, no cost of a failed lot, and no evidence that a buyer or supplier pays for a fix |  |

## Who already sells a fix

| Player | What it does | Mark |
|---|---|---|
| Sorsera (Mārupe, Latvia; raised €1.27M) | Tender monitoring and "tender intelligence" for the Baltics and Nordics: buyer and supplier profiles from award history, competitor tracking of bids, prices, and win rates | [RT], from third-party pages |
| Otnox (Riga) | Scores each tender 0 to 100 against a company profile; shows bid counts, prices against estimate, winners, repeat suppliers per buyer; reads tender files with AI. €98 a month | [RT], from a directory and a press release; Latvian coverage unconfirmed |
| iepirkumi.lv (since 2007) | Alerts from over 3,000 sources, results, statistics, a personal consultant | [RT] |
| Mercell | Monitoring in Latvia | [RT] |
| Procurement office dashboard; the state system's open data | Free indicators by buyer, supplier, and category; bidders per lot | [RT], [C] |
| Regional tools | Tendios and Tenderglass (Lithuania), Hankelooja (Estonia, buyer-side drafting) | [RT], vendor claims |

Two companies based in Latvia already sell the "fit and odds" product this brief first
proposed. Nothing was found that drafts bids for suppliers, and no bid-writing service
with public prices.

## What changes

Parliament passed the procurement reform on May 14, 2026. From **January 1, 2028** the
full procedure applies only from €140,000 for goods and services, €750,000 for social
and other special services, and €1M for works. Between €20,000 and those thresholds a
purchase is "simplified": the buyer announces it five days ahead, may negotiate, and
may choose a supplier outside the bids received. Plans and actual spending are published
whatever the amount. [RT, read at source]

By planned value, 84 to 88% of 2025 supply and service lots, and 89% of single-bid lots,
fall under the new thresholds [RT]. From 2028 most of the lots counted here leave the
formal procedure, and whether their bids will still appear in open data is unknown.

## Neighbours

- **EU scoreboard, 2024:** Latvia 22% single-bidder procedures against an EU average of
  28%, and 8% with no call for bids against 5% [RT, read at source]. On the EU's own
  measure Latvia is better than average.
- **Lithuania:** 44% in 2024 on the same scoreboard [S].
- **Estonia:** 26% in an undated older edition [RT].

Lithuania looks the larger version of this problem.

## Solution directions

- **Bid drafting for suppliers.** The one gap no existing tool was found to fill.
- **Supplier finder for buyers under the 2028 rules.** When a buyer may pick any
  supplier for purchases up to €140,000, it needs a defensible way to find and compare
  them, and suppliers need to be findable.
- **Bid desk as a service.** Prepare compliant bids for firms for a fixed or success
  fee; no product needed.
- **Lot design check for buyers.** Warn a buyer that a lot is too small or too
  specific to draw a bid, using the history of similar lots.

## The weakest points

1. **The proposed product exists.** Sorsera and Otnox sell scoring and competition
   history from Latvia. My third kill criterion named only iepirkumi.lv and the state
   system; read by its intent, it is met.
2. **No one has asked firms why they do not bid.** Officials cite small contract
   values, over-specific requirements, and firms earning well elsewhere; 90% of
   exclusions are for tax debts [RT]. None of that is awareness.
3. **The unanswered lots are not a market.** They are micro-lots for individual
   instructors.
4. **The 2028 rules let buyers choose freely below €140,000.** The formal tender that
   this opening depends on shrinks to a small share of purchases.
5. **No money is tied to the problem and no one is shown to pay.**
6. **Small market**, and Latvia sits below the EU average on single bidding.

## Kill criteria

- Six of ten firms that could have answered a no-bid lot say price or contract terms
  kept them out, not awareness or effort.
- An existing service already scores fit, shows past competition, or drafts bids.
  *Met for scoring and competition history.*
- The final law removes lots under about €140,000 from the formal procedure. *Met from
  2028.*

## My own grade

Junk as first written; plausible only in a narrower form. Before the red team I graded
it worth testing. Two of three kill criteria are now met for the original idea of
telling suppliers where competition is thin. What survives is a question about 2028:
when buyers may choose suppliers freely for most purchases, who helps them find and
justify the choice? That is a different brief and needs its own evidence.

## Red team

Run 2026-11-16 by a fresh subagent that read only this brief and its two scripts.
Verdict: **stands with corrections**, and it noted that the verdict is "falls" if the
third kill criterion is read by intent. All twelve corrections are applied above.

- **Computation:** every figure reproduced under my method. One bug: the data blanks
  the registration number of private individuals, so I counted lots answered only by
  individuals as unanswered. That inflated no-bid lots from 1,803 to 2,029 and created
  most of the "concentration in services" and the 2024-to-2025 rise. Both scripts are
  fixed and rerun.
- **Withdrawn:** "lock-in explains about half." In lots with two or more bids, 52.6% of
  bids also come from firms that bid to the same buyer the year before, so the 57.5%
  for sole bidders says almost nothing.
- **Withdrawn:** "about 133,000 companies" and "under 5% bid." The cited article does
  not contain the 32.2% I relied on from a search summary.
- **Corrected:** the reform's final thresholds and dates; Latvia's scoreboard figure.
- **Added:** Sorsera, Otnox, the nature of the unanswered lots, the procurement-level
  rates, the failure rate of single-bid lots.

## Sources

- State e-procurement system open data, bid openings: https://data.gov.lv/dati/dataset/7cfac5a8-8e54-4151-b263-4ca9e51065e9
- Reform in force in stages, thresholds from 2028: https://lvportals.lv/skaidrojumi/390826-stajas-speka-izmainas-publisko-iepirkumu-sistema-lielaka-atklatiba-mazak-birokratijas-un-no-2028-gada-augstakas-ligumcenu-robezvertibas-2026
- Parliament adopts the reform, May 2026: https://lvportals.lv/dienaskartiba/389746-saeima-atbalsta-publisko-iepirkumu-reformu-efektivakam-un-caurskatamakam-publisko-lidzeklu-izlietojumam-2026
- Government proposal of 2025: https://lvportals.lv/dienaskartiba/379721-valdiba-atbalsta-strukturalo-reformu-publisko-iepirkumu-sistemas-efektivizesanai-2025
- EU single market scoreboard, Latvia: https://single-market-scoreboard.ec.europa.eu/node/317_en
- Head of the procurement office on competition, January 2026: https://en.bb.lv/article/politics/2026/01/21/the-main-problem-in-procurement-is-insufficient-competition-85347
- State Audit Office on procurement rules, 2024: https://lvportals.lv/norises/370531-valsts-kontrole-publisko-iepirkumu-veiksmigu-norisi-kave-sarezgitais-un-neelastigais-normativais-regulejums-2024
- LSM on purchases leaving the transparency zone, March 29, 2026: https://www.lsm.lv/raksts/zinas/latvija/29.03.2026-iepirkumi-miljoniem-eiro-vertiba-var-palikt-arpus-atklatibas-zonas.a640935/
- Sorsera funding: https://business.gov.lv/en/news/sorsera-attracts-eu127-million-ai-driven-tools-supply-chain-and-procurement
- Otnox: https://europeanpurpose.com/tool/otnox
- iepirkumi.lv service description: https://www.iepirkumi.lv/en/for-suppliers/service-description/
- FICIL report citing scoreboard figures: https://www.ficil.lv/?p=23524
