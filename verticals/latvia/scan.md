# Latvia, all sectors: first scan for an opening

Written 2026-11-16. One session: 17 searches in Latvian, one audit summary read, three
open datasets queried. This is a longlist to choose from, a step before candidates and
briefs.

Marks: **[P]** primary source read, **[C]** I computed it from primary open data (script
in `data/`), **[S]** search summary or secondary report, not yet read at the source.
Nearly everything here is [S]; nothing has been red-teamed.

## What "an in" means here

An opening for a new entrant, as distinct from a problem that merely exists. Five kinds
turned up:

1. **A dated obligation.** A law forces firms to change by a fixed day.
2. **Public money stuck behind a bottleneck.** Funds are allocated and something else
   limits how fast they are used.
3. **Thin competition.** Few suppliers show up.
4. **A fast-growing buyer** with a rule that favours local suppliers.
5. **A shortage** that money alone has failed to fill.

## The longlist

| No. | Opening | Kind | What is measured | What is missing |
|---|---|---|---|---|
| 1 | Apartment-block renovation is stuck at about 4% | 2 | 39,500 apartment buildings, at least 26,600 need renovation, about 4% renovated; national target of 2,000 by 2030. Cost per m² rose from €147 (2017) to €570 (2025). The €170M support programme is fully reserved; the government allowed up to €70M more in September 2026. The State Audit Office names the obstacles: rising cost, insufficient funding, residents delaying decisions [S] | Where exactly a building stalls (owners' vote, technical documents, application, finding a builder) and what preparation costs per building |
| 2 | Freight documents must go electronic on July 9, 2027 | 1 | EU rule (eFTI); the transport ministry drafted the Latvian law changes in September 2026, not yet adopted. Lithuania subsidises carriers' switch [S] | How many Latvian carriers still run on paper; which platforms already serve them; whether Latvia will subsidise |
| 3 | Timber and wood products need deforestation due-diligence filings. **Downgraded November 24, 2026:** the state already carries most of the burden for Latvian wood | 1 | EU rule (EUDR): medium and large firms from December 30, 2026, micro and small from June 30, 2027 [P, ministry slides, October 5, 2026]. The May 2026 review ruled out a further delay [S]. Scale in 2024: 52,331 felling permits covering 95,891 felling areas, of which 37,705 permits and 65,346 areas in non-state forests; 16.0 million m³ felled, 54% outside state forests [P, State Forest Service annual report]. The Service supplies a geolocation file per felling area through a free lookup and an API; one statement a year can cover all of an owner's felling areas; a micro owner may authorise the buyer to file; small processors only pass reference numbers on; Latvia is low risk, so risk assessment is skipped and 1% of operators are checked [P, Service presentation, June 2025]. Micro and small primary operators file one simplified declaration, and a postal address can replace geolocation [P, ministry slides]. The state forest company files for itself and passes numbers to buyers through the industry data exchange (Koksnes plūsmas datu centrs); it suspended its TRACES integration after access limits from February 16, 2026 [S] | Number of forest owners and firms in scope; cost or hours per filing; penalty amounts; how many firms import wood from standard-risk countries, where full due diligence remains; whether the TRACES integration has resumed |
| 4 | Every company must issue structured e-invoices from January 1, 2028 | 1 | Delayed from 2026; public-sector invoicing has been mandatory since January 1, 2026. 42,853 companies (32%) reported for 2022 that a board member keeps the books [S] | Which accounting products already cover it (several local vendors do); what is left for the 43,000 self-keepers |
| 5 | A quarter of public tenders draw one bidder | 3 | About 25% of procurement lots with a single bidder, 19.8% of procurements terminated, 3.7 bidders per lot on average; EU guidance treats above 20% single-bid as bad. A procurement reform passed first reading in 2025 [S, year of the figures unclear] | Which categories have the fewest bidders. The procurement office's open data or the EU tender API would show it |
| 6 | The state is reorganising how it buys IT | 3, 4 | Prime minister ordered proposals on IT procurement and project management (2026). A moratorium review covered 27 applications worth about €22M and cancelled three, saving about €5M. Audits found no AI strategy in public administration and untargeted cloud adoption; an audit of municipal IT spending is planned for 2026. EU funds: 17 state ICT projects worth €54M [S; the last figure C] | Whether the reform opens the market to small suppliers or closes it |
| 7 | Hospitals and care homes cannot fill nursing posts | 5 | Of 1,271 vacancies open at the state employment agency on November 16, 2026, 434 (34%) are in health and social care; "nurse" is the most common title (99), then nurse's aide (31), carer (24) [C]. Median starting pay offered in the category: €1,004. Hospitals cost over €700M a year, about 40% of the health budget, in a network the audit office calls fragmented. Children wait 45 to 127 days for dentists, eye doctors, and psychiatrists depending on region. A single national e-booking system is a 2026 government priority [S] | The agency's list skews to public employers. No measure yet of what a missing nurse costs a hospital, or of time lost to paperwork |
| 8 | Schools cannot fill teaching and support posts | 5 | 325 of the 1,271 vacancies (26%) are in education [C]: teachers, then speech therapists (17), school psychologists (16), special educators (15). About 3% of teaching posts unfilled; 12% of qualified secondary teachers left the profession in 2024 [S] | Money: who pays for a substitute or a tool, the school or the municipality |
| 9 | Defence buys more and must buy locally | 4 | 123 companies licensed for military goods in 2026 (five in 2012); at least 10% local industry share in ministry-funded projects; nine localisation contracts involving 31 firms; €20M of drone orders to eight Latvian makers; nine projects won €7M from the European Defence Fund; a ministry grant competition exists [S, ministry press material] | Any measured failure. This is an opening by growth, with no problem named yet |
| 10 | Firms cite labour and red tape | Context | Chamber survey, late 2025: talent shortage worries 17% of managers (12% a year before), bureaucracy 15% (21% before). Business index: administrative burden scores worst [S] | Too general to act on |

## Checked and closed

**Building permits are quick in Latvia.** The national construction system's open data
(292,000 e-service records) shows a median of 32 days from filing a building
application to the authority's decision in 2024-2026, with a tenth taking over 127
days; simpler notices take 10 to 14 days [C]. The system already has an AI assistant
and a single registration service since January 2026 [S]. The problem behind the German
worked example does not exist here in that form.

**EU-fund digitalisation grants for firms** (up to €200,000, for at least 1,750 firms)
closed to applications on June 30, 2026 [S]. Whether a successor exists is unchecked.

## Latvian sources worth knowing

| Source | Gives | Access |
|---|---|---|
| data.gov.lv (national open data portal) | Daily vacancy list; the whole construction information system (48 datasets); EU-fund projects 2021-27; insolvency proceedings; company register | Free CSV, queried directly this session |
| State Audit Office (Valsts kontrole, lrvk.gov.lv) | 46 reports in 2025, each naming a failure and often its cost. Its 2026 topics: defence, health, human resources, public administration, digital transformation | Free PDFs; read as summaries only so far |
| Procurement Monitoring Bureau (IUB) and the EU tender API | Tender counts, bidders per lot, terminated procedures | IUB open data not yet located; the EU API works without a key |
| State Revenue Service (VID) | Compliance obligations and their dates; counts of firms by bookkeeping arrangement | Free PDFs |
| lvportals.lv | Official press releases of every ministry and agency in one place | Free |
| Chamber of commerce (LTRK), Turība business index, FICIL | Yearly business surveys | Free; FICIL not yet found |
| National Health Service (NVD), education ministry (IZM) | Waiting times; teacher vacancies | Published irregularly as PDFs |

Latvia concentrates its official publishing in few places and exposes far more raw data
than France, so a scan covers more ground per hour. The price is size: 1.9 million
people (my prior knowledge), so each opening needs a view on Lithuania and Estonia
before it justifies a product. Openings 2, 3, and 4 rest on EU rules or regional
practice and travel well; opening 1 is national.

## Where I would dig first

1. **Renovation (1).** The largest measured gap between money available and work done,
   an audit that names obstacles, and a legal change in 2026 that lets owners'
   communities sign loans in their own name. The audit report itself is the next read.
2. **Single-bid tenders (5).** Cheap to verify with data, and it doubles as market
   intelligence for anything the team later sells to the public sector.
3. **Electronic freight documents (2).** A fixed date eight months out and a law still
   in draft.

Opening 3 was checked on November 24, 2026 and downgraded: only wood importers keep
real work. Opening 4 looks crowded; 7 and 8 are real and slow, with public buyers.
