# Brief L-02: Latvia's state software work leaves the catalogue from 2027

Latvia, public sector IT. Written 2026-11-16 from candidate L4; rewritten the same day
after the red team's report.

Marks: **[P]** primary document read. **[C]** computed from the state e-procurement
system's open data (scripts `data/it_catalogue_orders.py`, `data/it_cliff_buyers.py`,
`data/it_tenders_2025.py`). The red team recomputed every [C] figure with its own code;
all but one reproduced, and that one is corrected below. **[R]** official page or news
article read through a text extraction tool. **[RT]** found or verified by the red
team; I have not read the source myself. **[S]** search summary.

## The problem

Latvian state bodies ordered most custom software by the hour from a closed e-catalogue
of approved suppliers. A regulation adopted on September 22, 2026 caps that at under
€140,000 a year per buyer from January 1, 2027, with exceptions that run to the end of
2027. The work above the cap must move to announced procurement procedures.

The first version of this brief claimed the buyers are unpractised at tendering
software. The red team showed that claim does not hold. What remains is a dated change
of buying channel, not a measured failure.

## Who has it

- **Buyers.** 197 bodies ordered from the two software catalogues in 2025. Between 30
  and 49 are over the cap: 30 ordered more than €140,000 of items named "development"
  [C], and the finance ministry counts 49 that ordered more than €140,000 of software
  services of any kind [P]. The cap covers maintenance too, so the true count lies
  between. The largest are the tax authority (€5.7M), the state digital agency
  (€4.6M), the digital health centre (€4.1M), and the welfare ministry (€4.1M). [C]
- **Suppliers.** 67 firms sold through the catalogues in 2025. The top five took 54%
  of all software services and 69% of development. [C], [RT]
- **Who pays.** Public bodies, from the state budget and EU funds.

## The workflow and where it changes

A buyer picked a supplier in the catalogue and ordered a block of hours on a named
technology stack, at a median of €57.50 an hour [C]. The figures below are orders
placed, which are ceilings on hours; 57% of the 2025 value sits in orders not yet
marked fully executed [RT].

| Fact | Figure | Mark |
|---|---|---|
| The catalogue cannot be made competitive | The finance ministry: in a catalogue "based on specific suppliers, products and technologies" raising competition "is not possible" | [P] council deck, July 27, 2026 |
| Orders are concentrated | 49 of 197 buyers placed 95% of catalogue software orders in 2025, of €56.66M | [P] same; my total matches to €8,500 |
| Fraud case | European prosecutors detained 20 people on March 17, 2026 over at least six rigged IT procurements worth up to €1.5M, funded by the EU regional fund. All are presumed innocent | [R], confirmed [RT] |
| Freeze | On June 15, 2026 the prime minister paused new IT development contracts above €142,999, in any procedure, for ministries and state companies. Extended to November 16, 2026; no later extension found. Exceptions need the finance minister's written consent. Municipalities are outside it | [R], [RT] |
| The cap | Regulation No. 580: a buyer may order from the catalogue only if its orders in the calendar year total "less than €140,000" for "development, maintenance or evolution" of a system it runs. Standard services with no custom software are outside the cap. Each order must name the system it serves | [P] |
| The exceptions | Until December 31, 2027 the cap does not apply to work for which a procurement is announced by December 31, 2026, nor to bodies that centrally maintain shared systems for others | [P] |
| Size of the shift | €36.3M of 2025 orders for development items sat above €140,000 per buyer. Most of those items are hybrid "development, improvement, maintenance" lines | [C], [RT] |
| Effect of the freeze | Catalogue software orders, January to October: €47.7M in 2025, €38.2M in 2026. The whole gap opened after June; January to May 2026 ran 53% above 2025. Bodies under a ministry fell 70% from June to October; others fell 33% | [RT] |
| Savings claimed | The finance ministry reports €21.2M of IT spending averted through withdrawn or suspended requests | [RT] |
| Open tenders draw few bids | Software lots (CPV 722) in 2025: 196 lots from 95 buyers, 52% with one bid, against 27.7% for all other lots. In 2026 to date: 40.8% | [C], [RT] |
| No shift to tenders yet | Software lots opened per month from June to October: 13, 12, 13, 13, 19 in 2026; 14, 23, 13, 13, 21 in 2025 | [RT] |
| EU-funded state IT | The main measure has 17 contracts worth €45.9M of EU money; 9 of them (€25.2M) were signed between August 27 and November 10, 2026 and end in 2028 or 2029 | [C], corrected by [RT] |

**Withdrawn: "sixteen of thirty buyers ran no open software tender."** The count is
right for one year and one CPV prefix and nothing more. Across 2024 to 2026, 7 of the
30 have no software lot. All 30 ran tenders of some kind in 2025. One "zero" buyer
opened a €6.38M software tender on October 27, 2026 and drew three bids. [RT]

## What it costs now

| Kind | Evidence | Mark |
|---|---|---|
| Money, real spend on a fix | Buyers already pay for requirements and "procurement support" by the hour through the catalogue: €251,255 in 2025, €123,722 in 2026 to date, to Agile & Co, PwC, EY, and others. Four 2025 tenders bought specification drafting, planned at €14,000 to €216,116 | [RT] |
| Money, changing channel | €36.3M a year of orders above the cap. This is work that moves, not money spent on the move | [C] |
| Money, running | Over €108M a year on IT maintenance and co-payments; "no one really tracked implementation costs" (minister Tavars) | [R], attribution corrected by [RT] |
| Time | Each exception request under the freeze needs a budget, a case for urgency, alternatives weighed, and market research; 83 filed by November 13, 2026. The freeze is temporary | [R] |
| Gap | No failed, late, or costly software tender is shown to result from the change. No figure for what one tender costs a buyer to prepare |  |

## How they cope today

Buyers tender routinely; the tax authority opened 86 lots in 2025 [RT]. For software
they hire requirements and procurement support from catalogue suppliers or tender for
a specification [RT]. Those with shared systems can rely on the 2027 exception.
Others can announce a procurement before December 31, 2026 and keep ordering through
2027.

## Who already sells a fix

| Player | What it does | Mark |
|---|---|---|
| Catalogue suppliers (Agile & Co, PwC, EY, CETERA, iSERVS, RIX Technologies) | Requirements, architecture, and procurement support by the hour, already bought by the interior ministry's digital centre, the University of Latvia, the digital agency, and others | [RT] |
| Agile & Co | Tendered in late 2025 for an "AI solution for system development lifecycle support", up to €300,000, part EU-funded | [RT] |
| The state | A digital investment commission due by December 1, 2026; the digital agency proposed as a competence centre giving method support; 1,664 IT posts in 150 bodies to move into 10 to 12 sector centres; IT sourcing guidelines reported due by December 1, 2026 | [RT]; the guidelines from a search summary only |
| The catalogue itself | Being re-tendered, not closed: the new framework competition drew 21 bidders on the services lot in March 2026 | [RT] |
| Hankelooja (Estonia) | A state-built tender generator for small procurements; no sign of use in Latvia | [RT] |

## Why now

The cap is law and starts in six weeks, with a second date on January 1, 2028 for the
exceptions. The freeze's status after November 16, 2026 is unknown. The 2028 to 2034
EU envelope for Latvia is an indicative €9.3bn [P] finance ministry half-year report,
March 2026, slide 17.

## Neighbours

Not checked to a standard worth reporting. The first version's lines on Lithuania and
Estonia rested on search summaries with no figure, and I have removed them.

## Solution directions

- **Bid for the work as a supplier.** About €36M a year moves from catalogue orders to
  announced procedures by 2028, and software tenders draw one bid in 41 to 52% of
  lots.
- **Tender desk as a service.** Requirements and procurement support for state bodies,
  the service incumbents already sell by the hour.
- **System cost ledger.** Every order must now name its system, and a new commission
  will assess IT spending above €140,000; buyers need the cost of each system over its
  life.
- **Handover documentation.** Document incumbent-built systems so a second supplier can
  bid; software maintenance lots drew one bid in 13 of 19 cases in 2025.

## The weakest points

1. **The problem is not evidenced.** Buyers are practised, they already buy help, and
   no failed tender is shown.
2. **Incumbents already sell the fix, and one is building the AI version.**
3. **The state is building the rest:** commission, competence centres, guidelines.
4. **The date is soft.** The exceptions push much of the change to 2028, and they
   reward buyers who announce tenders before December 31, 2026, too soon for a new
   entrant.
5. **The payer's budget is gated.** Any IT purchase above €140,000 needs consent, and
   a tool sold to these bodies is itself an IT purchase under review.
6. **Thirty to forty-nine buyers,** each reached through its own procurement.

## Kill criteria

- An existing service already sells requirements and procurement support to these
  buyers. *Met.*
- The state publishes sourcing guidelines and opens a competence centre for IT
  procurement before July 2027.
- Fewer than five of the affected buyers publish a software tender above €140,000 in
  the first half of 2027.

## My own grade

Junk as a product opening; a market-entry note for a software supplier at most. Before
the red team I graded it plausible. The channel change is real, law, and measured from
complete data. But the failure I built the brief on was an artefact of one year and one
code, the fix is sold today by the catalogue's own suppliers, and the first kill
criterion is met.

## Red team

Run 2026-11-16 by a fresh subagent that read only this brief and its scripts. Verdict:
**stands with corrections**, with the note that the stated problem is not evidenced.
All fourteen corrections are applied above.

- **Computation:** every catalogue and tender figure reproduced. One error: I wrote
  that 12 EU-funded IT contracts were signed between August 27 and November 10, 2026.
  The count is 9. I miscounted a printed list and no script supported the row.
- **Withdrawn:** "sixteen of thirty ran no open software tender," and with it the
  problem statement.
- **Misread:** I wrote that the cap exempts maintenance. The regulation covers it. I
  have now read the regulation.
- **Baseline:** I compared June to October only, which overstated the freeze's effect
  at €19.3M. Over January to October the gap is €9.5M.
- **Missed:** the catalogue position for procurement support, the specification
  tenders, the Agile & Co AI procurement, the 2027 exceptions, the €21.2M averted, and
  the state's planned commission and guidelines.
- **Attribution:** the cost-tracking quote is minister Tavars's, not the prime
  minister's. The staff figure is 1,664 posts in 150 bodies.
- **Unsourced lines removed:** the procurement office's view on specifications, and
  the Lithuania and Estonia lines.

## Sources

- Regulation No. 580, September 22, 2026: https://likumi.lv/ta/id/371094
- Information Society Council deck, July 27, 2026: https://mk.gov.lv/lv/media/27471/download?attachment=
- Cabinet office on the prime minister's resolution, June 15, 2026: https://www.mk.gov.lv/lv/jaunums/ministru-prezidents-uzdod-30-dienu-laika-sagatavot-priekslikumus-ikt-iepirkumu-sistemas-un-projektu-parvaldibas-sakartosanai
- Procurement office on the moratorium, updated November 14, 2026: https://www.iub.gov.lv/lv/jaunums/pagarinats-moratorijs-ikt-iepirkumiem-pasutitaji-aicinati-iepazities-ar-ministru-prezidenta-rezoluciju-un-jautajumiem-un-atbildem
- Public broadcaster on the cap, September 22, 2026: https://www.lsm.lv/raksts/zinas/ekonomika/22.09.2026-nosaka-140-000-eiro-gada-limitu-programmaturas-izstrades-iepirkumiem-elektronisko-iepirkumu-sistema.a664304/
- Reform of IT project governance, July 27, 2026: https://www.lsm.lv/raksts/zinas/latvija/27.07.2026-reformes-ikt-projektu-parvaldibu-valsti.a656512/ and https://lvportals.lv/dienaskartiba/392587-isp-atbalsta-e-tavara-virzito-valsts-ikt-parvaldibas-reformu-2026
- Ministry deck on IT posts and centres [RT]: https://www.mk.gov.lv/lv/media/27465/download
- Finance ministry on €21.2M averted [RT]: https://lvportals.lv/dienaskartiba/394355-fm-pec-ikt-iepirkumu-izvertesanas-valsts-budzetam-ietaupiti-212-miljoni-eiro-2026
- Digital investment commission [RT]: https://lvportals.lv/dienaskartiba/394867-varam-virzita-valsts-ikt-investiciju-parvaldibas-kartiba-mazinas-sadrumstalotibu-2026
- Agile & Co AI procurement [RT]: https://eformsb.pvs.iub.gov.lv/show/1030104/file/99b6f6b1-85be-4fdd-b6d9-ee54870a0646
- Hankelooja [RT]: https://oecd.ai/en/dashboards/policy-initiatives/ai-assisted-tender-generator-solution-hankelooja
- European Public Prosecutor's Office, March 18, 2026: https://www.eppo.europa.eu/media/news/latvia-20-suspects-detained-over-eur15-million-it-procurement-fraud-2026-03-18_en
- E-catalogue orders, open data: https://data.gov.lv/dati/lv/dataset/pirkuma-pasutijumu-datu-grupa
- Bid openings, open data: https://data.gov.lv/dati/dataset/7cfac5a8-8e54-4151-b263-4ca9e51065e9
- Finance ministry half-year report on EU funds, March 2026: https://www.esfondi.lv/assets/ziņojumi/mk/2026/2_2026_pusgada_iesn_lidz_aprilim/fmzin_24.02.2026_esif.pdf
