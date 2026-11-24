# Latvia: three openings examined

Written 2026-11-16, from the longlist in `scan.md`. None is a brief yet and none has
been red-teamed.

Marks: **[C]** computed by me from primary open data (scripts in `data/`), **[P]**
primary document read, **[R]** official press release or article read through a text
extraction tool, so wording and figures are unverified against the page itself, **[S]**
search summary.

## Summary

| ID | Opening | Evidence | Money tied to it | My reading |
|---|---|---|---|---|
| L2 | Public tenders with few or no bidders | Computed from all 2025 e-tenders | Yes, by category | Best evidenced; usable two ways |
| L1 | Apartment-block renovation stalls before the loan | Audit office release, new programme of November 10, 2026 | Yes, per building | Audit report read: gap confirmed (37% of projects die), about €7,000 a building, small market, state moving in |
| L3 | Electronic freight documents by July 9, 2027 | Draft law, carrier counts | None | Closed: carriers are allowed, not obliged (draft law read 2026-11-16) |

## L2. Public tenders with few or no bidders

> **Superseded 2026-11-16.** The red team found a bug in the figures below (lots
> answered only by private individuals were counted as unanswered) and two Latvian
> companies already selling the product. Use the corrected figures and conclusions in
> `briefs/01-uncontested-tenders.md`. The tables below are kept as first computed.

Source: the state e-procurement system's open data on bid openings, all of 2025 (79,928
bid records, 27,955 lots). Planned contract value is recorded for about half of the
lots, so money figures are floors.

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Lots that drew no bid at all | 2,029 of 27,955 (7.3%) | Risk | [C] |
| Lots that drew one bid | 7,784 (27.8% of all lots; 30.0% of lots with a bid) | Risk | [C] |
| Typical competition | Median 2 bidders, mean 2.96 | Risk | [C] |
| By type | Single-bid share 32% for supplies and for services, 17% for construction works | Risk | [C] |
| By size | 34% single-bid below €42,000 planned value, 18% above €1M | Risk | [C] |

Where bidders are scarcest (CPV divisions with 150 lots or more):

| Category | Lots | Single-bid | Planned value | Of which single-bid |
|---|---|---|---|---|
| Health and social services (85) | 162 | 69.8% | €55M | €12M |
| Recreation, culture, sport services (92) | 309 | 62.5% | €6M | €3M |
| IT services (72) | 390 | 56.7% | €58M | €25M |
| Radio, TV, telecom equipment (32) | 219 | 47.0% | €17M | €7M |
| Research and development services (73) | 215 | 46.0% | €15M | €3M |
| Hotel, restaurant, catering services (55) | 298 | 44.3% | €126M | €9M |
| Laboratory and precision equipment (38) | 649 | 44.2% | €34M | €9M |
| Repair and maintenance services (50) | 1,267 | 42.1% | €79M | €36M |
| Education and training services (80) | 630 | 38.6% | €30M | €10M |
| Medical equipment and pharmaceuticals (33) | 4,276 | 38.2% | €302M | €60M |
| Construction works (45) | 3,943 | 17.1% | €596M | €43M |
| Architecture and engineering services (71) | 1,809 | 13.9% | €43M | €8M |

Narrower groups: medical equipment repair 71% single-bid (108 lots); software packages
71% (58); software maintenance 73% (22); medical devices 50% (870 lots, €49M planned);
public catering 51% (83 lots, €42.5M planned); bus hire with driver 41% (191 lots).

- **Who pays:** the public buyer pays through weak price competition and through
  re-running the 7.3% of lots that drew nothing.
- **The opening, read two ways.** For a supplier, some categories are close to
  uncontested: training, catering, events, bus hire, business services. For a product,
  buyers need bidders and small firms need help finding and answering tenders.
- **Caution:** much single bidding is lock-in, not absence. Only the original vendor
  can maintain its software or service its medical device, so a newcomer cannot simply
  turn up. The IT and medical rows overstate the open door.
- **Gaps:** no price premium measured for single-bid lots; existing tender-alert
  services in Latvia unchecked; the 2025 reform's effect unknown.
- **Earlier figure for comparison:** ministry presentations cite about 25% single-bid
  procurements and 19.8% terminated [S]; my 2025 count by lot is higher.

## L1. Apartment-block renovation stalls before the loan

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Stock | Over 39,500 apartment buildings; at least 26,600 need renovation; about 4% renovated | Volume | [R] audit office, December 9, 2025 |
| Cost of doing nothing | Residents pay €360M to €390M a year for heating | Money | [R] |
| Cost of a project | €880,000 per building on average; eligible cost per m² up 127% since 2017 against 52% for construction generally | Money | [R] |
| Payback | In 54% of completed projects, heating savings do not cover the loan payment | Money | [R] |
| Demand for subsidy | The support programme's funding was reserved in under six weeks | Risk | [R] |
| Where it stalls | "Professional project management is available only after the loan is received," though preparation comes first; 44.4% of owner decisions need three or more meetings; projects often stall before technical work starts | Time | [R] |
| Owners' knowledge | 57.8% were never approached about renovating; 8% know the approximate cost; 42% would not pay more than €0.50 per m² | Risk | [R], owner survey in the audit |
| Who carries the work | Owners' associations, "often run by volunteers without professional expertise"; one project had to be redone after poor documents | Risk | [R] |
| New rules | Since 2026 owners' communities can sign loans in their own name | | [S] |
| New programme | Approved November 10, 2026, open from January 4, 2027: no grant; an interest subsidy of 1.6 to 2 percentage points and a guarantee up to 80%; the loan comes from a commercial bank. €14.4M of EU money plus up to €34.3M of recycled funds by 2042; target of 9,000 apartments by 2030 | Money | [R] |

- **Who pays:** owners, through the loan. No one pays for preparation before the loan,
  which is the gap the audit names.
- **The opening:** from January 2027 commercial banks become the lenders, so banks and
  building managers need a supply of prepared buildings, and owners need a guide from
  first meeting to application.
- **Against it:** the grant is gone, so the payback problem gets worse; 9,000
  apartments by 2030 is perhaps 200 buildings, a small market; a regional one-stop
  agency model (RenoWave, Vidzeme) and the Riga municipal manager already offer
  project management [S].
- **Gaps:** the audit report itself is unread; no price for preparation; no count of
  buildings that started and stalled.

### Audit report read, 2026-11-16

I read the State Audit Office's interim report "Neizmantotās iespējas mājokļu
siltināšanā" (audit 2.4.1-69/2024, 90 pages), saved as
`data/29824-Yn7suWH1yrf8azs0P-BFWXFLL8ABKZMo.pdf`. The table above came from the
press release; the rows below are from the report, with page numbers. DME1, DME2, and
DME3 are the three successive Altum support programmes.

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Projects that never finish | DME1: 621 completed, 366 withdrawn, interrupted, or rejected by Altum; the report calls this 37% not carried forward | Risk | [P] p. 27 |
| Rejected for paperwork | DME2: 136 projects under way, 144 not; of those Altum rejected 108, "mostly" for unsigned or incomplete documents, cancelled 10, and applicants withdrew 26. Some buildings applied three to five times | Risk | [P] p. 28 |
| Price of project management | DME2 average €7,000 per project (range €1,800 to €30,000), on average 1.91% of eligible costs (range 0.21% to 3%); the programmes allow up to 3% | Money | [P] pp. 25, 28 |
| When it is paid | Funding for project management is available "only from step 8," on signing the loan with Altum or a bank. Until then owners pay from their own funds or run the project themselves | Money | [P] p. 24 |
| Help with documents | A grant covers 90% of technical documentation at step 3, with an owner co-payment | Money | [P] p. 24 |
| Who starts unprepared | 245 of 357 DME3 applicants (about 70%) applied without technical documentation | Volume | [P] p. 24 |
| Cost of selling | Riga's municipal manager runs 3,400 buildings; of 400 owner meetings it held, 50 buildings decided to renovate. It charges the 3% maximum to recover that cost, and loses buildings to cheaper project managers after the decision | Money | [P] pp. 25, 26 |
| Who manages projects | In DME1, municipal managers acted for the owners in 186 of 621 projects; four projects hired an outside project manager by tender. The Riga manager led 22 of 88 Riga projects | Volume | [P] pp. 26, 28 |
| Time | From energy audit to Altum's first opinion: 299 days in Liepāja, 475 in Riga. From that opinion to the grant decision: 306 and 421 days | Time | [P] p. 27 |
| Demand | 122 applications on the programme's first day; the 2025 funding was reserved in under six weeks | Risk | [P] pp. 3, 24 |
| State response | Recommendation 2 tells the ministry to fund project management from the early stage, "for example as technical assistance." The energy plan turns Altum into a one-stop agency, and the Social Climate Fund plan for 2026 to 2032 funds that function | Risk | [P] pp. 20, 65 |
| Private finance | One energy-service company works on apartment blocks (RenEsco); the report calls that market inactive | Volume | [P] p. 64 |

**What the report changes.** The gap is confirmed and measured: more than a third of
projects die, and bad paperwork is the named cause in the second programme. The money
tied to the problem is small. At €7,000 a building, or at most 3% of an €880,000
project (about €26,000 [C]), and with the ministry's target of 400 buildings by the end
of 2029 [S], the whole Latvian market for project management is roughly €3M to €10M
over four years [C]. Municipal managers already hold most of it, and the state has been
told to fill the early-stage gap itself through Altum.

**The narrower opening.** The party with a measured cost is the building manager, not
the owners: one decision per eight meetings in Riga. A tool that lowers a manager's
cost of reaching a decision and producing clean documents has a buyer who already
charges 3% for the work. That is unproven: no source shows a manager paying for such a
tool.

**Crowding check, thin.** Two searches found no company selling renovation project
software to managers or owners in Latvia, and Altum itself notes that few project
manager consultants exist [S]. Ēkubirojs runs a one-stop agency (named in the report,
p. 21). The check did not cover Lithuanian or Estonian tools.

**My reading:** real and well evidenced, small, and the state is moving into the gap.
A brief would likely grade plausible, not worth testing.

## L3. Electronic freight documents by July 9, 2027

> **Closed 2026-11-16: no deadline falls on carriers.** I read the EU regulation and the
> Latvian draft law. Both are conditional. Electronic freight information stays the
> carrier's choice; the duty falls on authorities, who must accept it.
>
> | Claim | Text | Mark |
> |---|---|---|
> | EU regulation 2020/1056, Article 4(2) | "Where the economic operators concerned make regulatory information available electronically to a competent authority, they shall do so on the basis of data processed on a certified eFTI platform" | [P] |
> | Same, Article 5(1) | "competent authorities shall accept regulatory information made available electronically by the economic operators concerned" | [P] |
> | Draft law 25-TA-1072, new Article 8(6) | "Ja kravu pārvadājumu regulatīvā informācija ir elektroniska, tad tā jānodrošina pieejama kompetentajai iestādei" (if the information is electronic, it must be made available to the authority) | [P] |
> | Draft's explanatory note | "Likumprojekts pats par sevi neparedz stingrākas prasības salīdzinājumā ar regulu" (the draft sets no stricter requirements than the regulation) | [P] |
> | Draft, transitional point 56 | Authorities get access to the information from August 21, 2027 | [P] |
> | Stage | Fourth round of ministry review closed October 29, 2026; cabinet and parliament still to come. The same draft carries taxi rules and a ban on bus routes to Russia and Belarus | [P] |
> | State spending | Up to €450,500 for 2026 to 2028 for Latvia's part in the EU pilot eFTI4LIVE, run by the road transport authority (report 26-TA-759) | [P] |
> | Later mandate | The regulation's review, reported as due in February 2029, is to weigh an obligation on operators | [S] |
>
> The iFinanses sentence "transport information must be submitted digitally" misreads
> the draft. The explanatory note estimates no cost to carriers from the freight
> provisions. What remains is a slow voluntary adoption curve, a state gateway built by
> the road transport authority, and a possible EU mandate after 2029. I did not run the
> crowding check, because the candidate fails before it. The table below is kept as
> first written.
>
> Sources: https://www.legislation.gov.uk/eur/2020/1056/body/adopted ;
> https://tapportals.mk.gov.lv/legal_acts/ef1698d0-dd5d-4fe1-ac09-93ee4cc80fc1 ;
> https://tapportals.mk.gov.lv/legal_acts/5ba0f4c7-3f29-4523-8efc-118373dd3001

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Rule | EU regulation 2020/1056 (eFTI); the transport ministry has drafted changes to the road transport law; ministries are reviewing them; cabinet and parliament have yet to adopt | Risk | [R] iFinanses, September 23, 2026 |
| Date | "From July 9, 2027, freight transport must move from paper documents to electronic data exchange" | Risk | [R] |
| Who | Carriers, forwarders, logistics firms; authorities receive the data electronically | | [R] |
| How many | 4,091 licensed freight carriers on March 31, 2026 (4,853 in 2022); about 22,300 licensed freight vehicles | Volume | [P] road transport authority, April 2026; the chart labels lost in extraction, so the series reading needs a check |
| Current use | Electronic consignment notes cover under 1% of international shipments; inspectors in Latvia still ask for paper | Risk | [S] |
| State plans | A ministry study of December 2024 designs a national e-consignment register and eFTI gateway | | [S] |

- **Critical doubt:** the EU regulation, as I understand it, obliges authorities to
  accept electronic information and leaves its use by firms voluntary. The article's
  "must move" may overstate the draft. If carriers are merely allowed, this is a slow
  adoption curve, not a deadline. Reading the draft law settles it.
- **Who pays:** carriers, about five vehicles each on average, with thin margins. No
  cost or price found.
- **Against it:** certified international platforms will serve the same carriers;
  Lithuania subsidises adoption and Latvia has announced nothing.

## What I would do next

Take **L2** to a brief. It has the only problem-specific money in the three, the data
is complete and free, and one more query separates lock-in from true absence of
suppliers (repeat winners by buyer). It also tells the team where a new supplier meets
the least resistance, whatever it ends up selling.

**L1** deserves one read of the audit report before deciding. **L3** deserves one read
of the draft law.

*Update 2026-11-16:* L2 was briefed and graded junk. L3 is closed after the read. L1's
audit report is read: the gap is confirmed, but the market is roughly €3M to €10M over
four years and the state is moving into it.

## L4. EU funds: slow absorption, and connecting small firms to the money

Added 2026-11-16 on Edgar's suggestion. A first look, not a brief, and not red-teamed.
Marks as above. [C] figures come from two sources: the European Commission's cohesion
open data, read through its API on November 16, 2026, and the Latvian agency's open
list of 2021 to 2027 project contracts (script `data/eu_funds_direct_contracts.py`).

### Is absorption low?

Against the EU, no. Against the neighbours, yes.

| Measure, 2021 to 2027 funds | Latvia | EU | Estonia | Lithuania | Mark |
|---|---|---|---|---|---|
| EU payments received, share of plan (November 16, 2026) | 36.6%, 12th of 28 | 30.4% | 57.4% | 47.3% | [C] |
| Same, interim payments only, without advances | 21.1% | 21.6% | 39.9% | 31.7% | [C] |
| Spending declared by projects, share of plan (August 2026) | 22.4%, 21st of 30 | 24.3% | 41.1% | 30.7% | [C] |
| Selected into projects, share of plan (August 2026) | 86.8% | 76.5% | 111.9% | 102.3% | [C] |

The first two rows cover cohesion funds; the last two add the home-affairs funds, and
their 30 "countries" include cross-border programmes. The finance ministry reports
contracts signed for €3.1bn of €4.2bn (74%) in June 2026, and the 2026 minimum
spending target met at 102%, so no money was lost this year [R], [P].

### Where the money is slow

| Spending field (Latvia, August 2026) | Plan | Selected | Spent | Mark |
|---|---|---|---|---|
| Railway, core network | €445M | 93.7% | 6.7% | [C] |
| Energy efficiency in public buildings | €273M | 70.1% | 10.8% | [C] |
| Border surveillance systems | €256M | 48.7% | 25.2% | [C] |
| Government IT and e-services | €184M | 22.9% | 1.7% | [C] |
| Primary and secondary education | €172M | 99.3% | 13.8% | [C] |
| **SME business development and export** | €211M | 104.5% | **75.5%** | [C] |
| Business infrastructure for SMEs | €228M | 67.2% | 26.3% | [C] |
| Research and innovation in SMEs | €59M | 110.2% | 20.4% | [C] |

The slow money sits with public bodies. The main SME line is the fastest large line in
the programme.

### Who holds the contracts

- Of €3.48bn of EU money under contract, €2.85bn (82%) went through restricted
  selection, where the recipient is named in advance. Open calls carried €0.63bn. [C]
- State bodies, municipalities, and their agencies hold most of it. The "companies" at
  the top of the list are the state railway, university hospitals, the road authority,
  and the state property company. [C]
- Private firms rarely hold a contract. They receive EU money as clients of two state
  bodies: the investment agency (LIAA) for grants and the development bank (ALTUM) for
  loans with a rebate. [C], by reading the list
- Caveat: the registration number is blank in 1,185 of 2,560 rows, so I identified
  holders by name and could not separate private from state-owned companies by code.

### Small firms: demand exceeds the money

| Claim | Figure | Mark |
|---|---|---|
| Oversubscription | "In several programmes demand exceeds available funding by up to two and a half times" (economics minister, August 7, 2026) | [R] |
| Digitalisation grants | Closed November 7, 2025 after 857 firms asked for more than the €18.55M available. Two sources give the amount requested as €20.9M and €25.5M | [S] |
| Productivity loans | €100M budget; applications suspended since March 2, 2026 | [S], from an accounting firm's blog |
| Incubation intake, spring 2026 | 297 applications, 2.3 times the year before | [S], same blog |
| Reach so far | Digitalisation support reached over 15,700 firms; productivity and export programmes over 3,900 | [R] |
| Firms that do not apply | An economics ministry paper of April 2026 describes "discouraged" firms that expect refusal | [S], unread |

### Who already sells help

| Player | What it does | Mark |
|---|---|---|
| LIAA and its regional offices | Free advice and the application portal | [S] |
| KPMG Latvia | Writes applications, fully outsourced or alongside the client | [S] |
| BASKA, Balansis, and similar small firms | Assess the idea, write the plan and application; no prices published | [R] |
| Granter (Portugal) | AI grant consultant for SMEs; raised €1.6M in November 2026 to expand across Europe | [S] |

The check was thin: four searches. I found no Baltic AI grant tool and no published
consultant fee.

### My reading

- **The premise is half right.** Latvia trails Estonia and Lithuania badly, but sits at
  the EU average, and has lost no money so far.
- **Small firms are not the bottleneck.** Their lines fill and close early. A tool that
  connects more firms to the money adds applicants to calls that already run out. The
  scarce thing is funding, and for some firms the confidence to apply.
- **The measured failure is in public bodies.** Government IT has selected 23% of its
  €184M and spent under 2%. That overlaps the longlist item on state IT buying.
- **Timing.** The recovery fund closed on August 31, 2026. The next period, 2028 to
  2034, carries an indicative €9.3bn for Latvia [P], with rules still being written.
- **Gaps:** why public projects run late (no source read gives reasons); the rejection
  rate for firms; what firms pay consultants; how many eligible firms never apply.

Sources: https://cohesiondata.ec.europa.eu (datasets ue97-5sq6 and 3git-md5z) ;
https://www.em.gov.lv/lv/jaunums/em-es-fondu-investiciju-rezultati-apliecina-nepieciesamibu-paplasinat-atbalsta-programmas ;
https://lvportals.lv/dienaskartiba/391174-es-fondu-investiciju-temps-turpina-pieaugt-finansu-ministrija-informe-saeimas-komisiju-2026 ;
finance ministry half-year report, March 2026, on esfondi.lv ;
https://balansis.lv/en/blog/eu-funding-latvia-small-business-2026 ; https://baska.lv/ ;
https://tech.eu/2026/11/03/portuguese-ai-startup-granter-bags-eur16m-to-expand-across-europe/

### L4 follow-up: why state IT money is not moving (2026-11-16)

State IT is slow for a named reason: the prime minister froze large IT purchases in
June 2026, and the freeze still runs.

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| The freeze | On June 15, 2026 the prime minister ordered a 30-day pause on new IT development orders above €142,999 in the state e-procurement system, and on sending new EU-funded IT projects to cabinet | Risk | [R] cabinet office release |
| Reasons given | A criminal case opened by the European Public Prosecutor's Office over IT procurement; use of the e-catalogues "to limit the circle of suppliers"; "unjustified dependence on a single supplier" | Risk | [R] same |
| Still in force | Extended on July 10, in August, and by a resolution of November 3 to November 16, 2026. It covers ministries, their agencies, and state companies, above €140,000, in any procurement regime. Municipalities are outside it | Risk | [R] procurement office page, updated November 14 |
| The gate | An exception needs the finance minister's written consent. The buyer files a description and budget, the reason for urgency, the risk of delay, the alternatives weighed, and its market research. 83 requests filed and reviewed by November 13 | Time | [R] same |
| Early results | By July 27: 27 applications, 9 approved, 7 sent back for more information, 3 closed without result, 8 let through. Three projects cancelled, saving about €5M of about €22M reviewed | Money | [R] two releases |
| Size of state IT buying | €277.65M in 2025, 9.24% of public procurement, up 58.5% from €175.19M in 2024 | Money | [S] news site citing the ministry |
| Running costs | Over €108M a year in IT co-payments and maintenance; long-run cost was often estimated as a flat 15% of build cost; "no one really tracked implementation costs" (prime minister) | Money | [R] public broadcaster, July 27 |
| State IT staff | Over 1,600, "scattered across all institutions" | Volume | [R] same |
| The reform | Twelve measures in three areas: one body to assess and monitor large projects, with a public project register; state competence centres; more open IT procurement, with a €140,000 cap on buying software development through e-catalogues. The catalogue review was due October 1, 2026. I found no cabinet decision adopting it | Risk | [R] release of July 27 |
| EU-funded IT projects | The main measure (1.3.1.1) has 17 contracts worth €45.9M of EU money. Twelve were signed between August 27 and November 10, 2026, with end dates in 2028 and 2029 | Time | [C] |

Competition in tendered IT services, 2025 [C] (script `data/it_tenders_2025.py`):

| Measure | IT services (CPV 72) | All other lots |
|---|---|---|
| Lots | 411, from 135 buyers | 27,544 |
| Drew one bid | 54.0% | 27.5% |
| Median bidders | 1 | 2 |

The 54% overstates the software problem. Internet connections draw one bid in 89.5% of
57 lots, and two telecoms firms top the bidder list. Software development proper draws
one bid in 29 to 41% of lots, depending on the code. Software maintenance and support
draw one bid in 68 to 71%, which fits lock-in to the original builder. 317 firms bid on
IT lots; 185 of them bid once. This file omits e-catalogue purchases, which are the
ones the freeze targets, so the closed part of the market is not measured here.

**What this means.**

- The delay is real, dated, and official. Its cause is governance and a fraud case, not
  a shortage of suppliers or of money.
- State buyers now carry a new paperwork duty for every IT purchase above €140,000:
  justify urgency, weigh alternatives, show market research. That is a measured,
  recurring task with a named gatekeeper.
- The reform's stated aim is to let more suppliers in. If the €140,000 catalogue cap
  holds, development work above it moves to open tenders.
- Projects contracted late must still finish by 2029, so the money has to be spent
  faster than planned.

**Openings, none proven.**

1. *For a supplier:* state IT work is reopening to firms outside the catalogue
   incumbents. This is a market entry, not a product.
2. *For a product, buyer side:* tools for the new gate: cost tracking over a system's
   life, market research, the public project register. The state may build these
   itself; the reform names a central body and competence centres.
3. *For a product, vendor side:* nothing found.

**Gaps.** Who holds the e-catalogue contracts and how concentrated they are; the State
Audit Office's findings (its site is unreachable from here); what the criminal case
alleges; whether the reform was adopted after November 3; any spending by a buyer on
help with the new approval step. Crowding check not run.

Sources: https://www.mk.gov.lv/lv/jaunums/ministru-prezidents-uzdod-30-dienu-laika-sagatavot-priekslikumus-ikt-iepirkumu-sistemas-un-projektu-parvaldibas-sakartosanai ;
https://www.iub.gov.lv/lv/jaunums/pagarinats-moratorijs-ikt-iepirkumiem-pasutitaji-aicinati-iepazities-ar-ministru-prezidenta-rezoluciju-un-jautajumiem-un-atbildem ;
https://lvportals.lv/dienaskartiba/392587-isp-atbalsta-e-tavara-virzito-valsts-ikt-parvaldibas-reformu-2026 ;
https://www.lsm.lv/raksts/zinas/latvija/27.07.2026-reformes-ikt-projektu-parvaldibu-valsti.a656512/ ;
https://puaro.lv/ietekme-un-nauda/ikt-iepirkumu-apjoms-gada-laika-audzis-par-vairak-neka-100-miljoniem-eiro/

> **L4 briefed 2026-11-16** as `briefs/02-state-software-leaves-the-catalogue.md` and
> red-teamed. Use the brief's figures over the L4 notes above: 9 EU-funded IT contracts
> were signed late, not 12; the cap covers maintenance; the freeze's effect over
> January to October is €9.5M, not €19.3M.
