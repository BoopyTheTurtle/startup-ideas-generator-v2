# Architecture, France: candidate problems

Step 2 and 3 output, first pass, 2026-11-16. Five candidates, six workflows with no
measure yet. Marks: **[P]** primary source read and figure seen in it, **[S]** search
summary or secondary source.

No candidate has had its full crowding check or a red-team pass. None is a brief yet.

## Summary

| ID | Candidate | Workflow | Sources | Money entry | State |
|---|---|---|---|---|---|
| C3 | Water gets in: decennial claims concentrate on leaks, and windows now lead | 6, 8, 9 | 3 primary | Yes, large | Narrowed to the window-wall junction and written up as `briefs/01-window-wall-junction-leaks.md` |
| C1 | New housing fails the state's construction-rule inspection | 5 | 4 primary | Partial | Strong measure; inspection is rare; funded competitors exist |
| C2 | The thermal study no longer matches the building by completion | 3 | 4 primary | Gap | Clear and recurring; consequences look mild |
| C4 | Handover snag lists repeat the same defects | 11 | 2 secondary | Gap | Crowded; vendor-sourced figures |
| C5 | Works undeclared to the insurer lose their cover | 13 | 1 primary | Gap | No size measure; likely trivial |
| C6 | Public building works contracts grow after signature | 6, 9 | 1 dataset, computed | Yes, tied to the event | Money and payer clear; cause unknown |
| C7 | Architects' public contracts amended one time in seven; 5.9 bids per contract | 12 | 1 dataset, computed | Partial | Fee amendments are partly routine; bid counts are new |
| C8 | One public building lot in five draws a single bid | 7 | 1 dataset, computed | Gap | Public buyer's problem; no price premium measured |

## C3. Water gets in

Leaks dominate the ten-year liability claims that architects and their insurers pay, and
exterior windows have become the leading defect.

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Claim files opened at the architects' mutual insurer in 2025 | 9,811 (10,859 in 2024) | Risk | MAF annual report 2025, published 2026 | [P] |
| Claims paid by that insurer in 2025, net of recoveries | €215.9M, including €24.1M of handling costs | Money | Same | [P] |
| Its provisions for claims | €3,733M at end 2025 | Money | Same | [P] |
| Share of its claims under ten-year liability | 66% | Risk | Same | [P] |
| Most frequent cause of its ten-year claims | Infiltration, 34% | Risk | Same | [P] |
| Works its members declared for 2024 | €66.28bn | Volume | Same | [P] |
| National premiums, ten-year liability insurance (RCD), 2024 | €2,341M | Money | AQC observatory report 2026, citing France Assureurs | [P] |
| National premiums, building-damage insurance (DO), 2024 | €836M | Money | Same | [P] |
| Building-damage claims paid, 2024 | €1,291M, up 20% in a year; +6.6% a year on average 2015-2024 | Money | Same | [P] |
| Leading ten-year defect | Exterior windows and French windows; rate nearly doubled in ten years in apartment buildings | Risk | Press summary of the AQC 2026 report | [S] |
| Causes of window claims | Sill construction over 22%, joint with the structure 11%, manufacturing defects 17% | Risk | AQC observatory report 2026 | [P] |
| Annual cost of non-quality | About 10% of construction turnover | Money | DREAL Grand Est 2024 report, attributing it to AQC members | [P] for the statement, origin unchecked |

- **Who pays:** insurers, and through premiums and penalties (*malus*) the architects and
  contractors. The insurer says it reviews members whose claims outrun their premiums. [P]
- **Gap:** the defect is made on site by the installer; the architect's part (detail
  drawings, review of execution drawings, site checks) is not separated in the data.
- **Crowding:** unchecked for France. Site-inspection apps exist (see C4).
- **Next:** read the AQC window study and the MAF prevention material; find what share of
  claims trace to design or supervision; check who sells installation checks.

## C1. New housing fails the state's construction-rule inspection

State inspectors find a regulatory breach in nearly every housing development they
visit, and a breach is a criminal offence for which architects can be prosecuted.

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Inspected operations with one breach or more, France, 2020 | 85% (88% in Hauts-de-France: 44 of 50) | Risk | DREAL Hauts-de-France, February 8, 2021 | [P] |
| Breaches per inspected operation, Hauts-de-France | 7 in 2020; 9 on average 2018-2020; accessibility alone near 5 | Risk | Same | [P] |
| Operations inspected nationally | 453 in 2020; more than 600 buildings visited a year | Volume | Same | [P] |
| Penalty | Fine up to €45,000, €75,000 on repeat; conformity works or demolition; ban from practice | Risk | Same | [P] |
| Who can be prosecuted | Clients, architects, contractors, anyone responsible for design or execution | Risk | Same; DREAL Pays de la Loire, November 14, 2025 | [P] |
| Grand Est, 2024 | 61 site inspections, 28 offence reports sent to prosecutors, 142 file-based inspections; "inspections finding no breach are still rare"; the same breaches "repeat year after year" | Risk | DREAL Grand Est, *Bilan 2024*, March 2025 | [P] |
| Pays de la Loire, 2024 | 8 of 12 operations failed the acoustic measurement; breaches flagged by technical inspectors that the client never corrected | Risk | DREAL Pays de la Loire, November 14, 2025 | [P] |
| Coming change | Ordinance of July 29, 2022 extends inspectors' powers to administrative fines; a national platform will collect attestations | Risk | DREAL Grand Est, *Bilan 2024* | [P] |
| Paid today | Attestations at completion, by a technical inspector, engineering office, or architect, required by law | Money | Same | [P] for the obligation; no price seen |

- **Who pays:** the client (developer, social landlord) pays for attestations and
  corrections. The architect carries criminal exposure.
- **Gap:** the chance of inspection is small (hundreds of operations a year), so the
  expected penalty is low. No figure for the cost of corrections.
- **Crowding:** Freeda (Paris, €3.4M, AI review of construction plans, claims 10,000
  plans checked), Temelion (€3.2M, lists regulatory compliance as a use), Davis (€4.6M,
  code-compliant plan generation, beta in France). All [S].
- **Next:** check what Freeda covers in French housing rules; find the cost of putting
  breaches right after delivery; find whether the coming attestation platform raises
  the inspection rate.

## C2. The thermal study no longer matches the building by completion

The regulatory energy calculation is made early and not updated as the design and the
site change, so the attested performance describes a different building.

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Inspected operations with breaches from modelling that does not match the project | 48% (600 operations, 20,000 dwellings, 2017-2018) | Risk | Cerema, presentation of June 29, 2023 | [P] |
| Stated origin | Modelling and description errors; study not updated during the operation | Risk | Same | [P] |
| Still found in 2024 | Wrong glazed areas, heating and ventilation equipment different from installed, wrong wall areas, wrong number of dwellings, wrong insulation performance | Risk | DREAL Grand Est, *Bilan 2024* | [P] |
| Still found in 2024 | Study not updated between permit and completion; attestations unsuited to the building; missing XML file; outdated calculation software | Risk | DREAL Pays de la Loire, November 14, 2025 | [P] |
| Named as a frequent error by the quality agency | Study made early and not updated after site changes | Risk | AQC regulatory quality sheets, 2024 | [S] |
| Price of a study | €500 to €2,000 for a single house; no figure for apartment buildings | Money | Consumer guides | [S] |

- **Why it grows:** RE2020 adds a life-cycle carbon calculation that depends on the
  products installed, so each substitution on site changes the result. No RE2020
  operation had been inspected in Grand Est by 2024. [P]
- **Gap:** the breaches "are generally lifted after the inspection, once the calculation
  is redone" (Cerema) [P]. The cost of failure looks like one recalculation.
- **Crowding:** one search found no product that keeps the study in step with the
  design; the search was not thorough.
- **Next:** find whether a wrong completion attestation blocks handover or sale; ask
  what recalculation costs on a 50-dwelling building.

## C4. Handover snag lists repeat the same defects

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Reserves per dwelling at handover, social housing | 17 on average, half the private-sector figure | Time | FinalCad study reported by Banque des Territoires | [S], vendor data |
| New homes delivered without reserves | One in five; the rest average 12 | Time | UFC-Que Choisir, about 2017, cited in a parliamentary question | [S] |
| Disputes over unlifted reserves | 8% of 320 dispute files | Words | CLCV survey 2017 | [S] |

- **Crowding:** heavy. FinalCad itself, Archireport, BatiScript, Kaliti sell snagging
  apps. The measure comes from a vendor.
- **State:** parked unless C3 points to a specific unserved check.

## C5. Works undeclared to the insurer lose their cover

Architects declare each year's works to the insurer; a mission left out can lose its
cover when a claim arrives. The insurer's claims committee rules case by case on such
files and calls its own declaration system in need of work. [P] (MAF annual report 2025)
The report gives no count. Without a size measure this stays a note.

## Candidates from the public contract data

Source for C6 to C8: the consolidated open data on French public contracts (*données
essentielles de la commande publique*, data.gouv.fr, file of November 16, 2026). I
computed the figures myself with the two scripts in `data/`; no one has reviewed them.
Mark: **[C]** computed from primary data.

Method and limits. One row per contract lot, initial amount between €10,000 and €100M,
framework agreements and amounts the publisher flags as abnormal excluded. Building
works are lots whose CPV code starts 4500, 4521, 4526, 453, or 454. A price increase is
a recorded amendment raising the amount by 0.1% to 100%. Buyers under-report
amendments, so every rate is a floor. The data gives no cause for an amendment.

### C6. Public building works contracts grow after signature

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Building works lots notified 2019-2023 | 265,075 lots, €91.5bn | Volume | [C] |
| Lots with a recorded price increase | 12.6% (33,276); 23.5% of lots above €5M | Risk | [C] |
| Size of the increase where one occurs | Median +5.7%, top tenth above +23%; median €8,060 | Money | [C] |
| Total added by those amendments | €1.22bn over the five cohorts, 1.3% of all spend | Money | [C] |
| Trend | Share of lots with an increase rose from 9.1% (2019) to 15.4% (2024) | Risk | [C] |

- **Who pays:** the public client. The payer is named and the money is tied to the
  event.
- **Gap:** cause. An amendment can come from a specification error, an unforeseen site
  condition, a client change, or price indexation after 2021. Nothing here ties the
  money to the architect's documents.
- **Next:** read a sample of amendment notices for stated reasons; audit-court reports
  name causes case by case.

### C7. Architects' own public contracts are amended one time in seven

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Architecture and engineering service contracts (CPV 712) notified 2019-2023 | 25,802 contracts, €7.65bn | Volume | [C] |
| With a recorded fee increase | 13.9%; median +16.7%, a quarter above +33% | Money | [C] |
| Bids received per contract, 2022-2025 | Median 3, mean 5.9; 39% draw five or more; 19% draw one | Time | [C] |

- **Caution:** French design fees start provisional and become final once the works
  cost is fixed, so a fee amendment is partly routine. This is not yet a failure
  measure.
- **Use:** the bid counts are the first measure found for workflow 12. A mean of 5.9
  bids per contract means most bidding effort is lost; the cost of one bid is still
  unknown.

### C8. One public building lot in five draws a single bid

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Building works lots with a bid count, 2022-2025 | 127,099 | Volume | [C] |
| Lots with one bid | 19.7% | Risk | [C] |
| Lots with two bids or fewer | 38.2%; median 3 | Risk | [C] |

- **Who pays:** the public client, through weak price competition, and the architect,
  who analyses the bids and re-runs failed lots. Lots with no bid at all do not appear
  in the data.
- **Gap:** no price premium measured for single-bid lots. It could be computed from
  this data only with an estimate to compare against, which the data lacks.

## Workflows with no measure found

Second pass, 2026-11-16: nine more searches and three reports reread, under the rule
that a candidate needs a cost per incident and a named payer. No new candidate.

| Workflow | What was tried | Result |
|---|---|---|
| 1. Survey of existing buildings | Searches on insufficient diagnosis and extra works in renovation; on survey and 3D scan prices | No rate or cost of failure. The quality agency says renovation diagnoses are "incomplete or absent" [P], without a figure. Scan prices of €0.80 to €4 per m² come from a vendor [S] |
| 4. Permit file | Three searches: incomplete files, real processing times and refusal rates, appeals | No statistic on incomplete files or real processing times. Appeals against permits took about 24 months at first instance and 16 to 18 on appeal in a 2018 government report [S], too old to use |
| 6. Specifications | Search on contract amendments traced to specification errors, audit-court reports | Legal thresholds and single cases only (one amendment of 60%). No distribution |
| 7. Contractor tenders | Search on failed tender lots in building works | No building figure. The open data on public contracts may hold one |
| 9. Payment and final accounts | Two searches; national payment-delay observatory | Nothing on architects or final accounts. The detailed agency survey has no question on unpaid fees [P] |
| 10. Scheduling | Search on late deliveries and penalties | An unsourced "15 to 20% of sites late"; single court cases |
| 12. Winning public work | Two searches; ministry study; detailed agency survey | No cost per bid or success rate. The survey asks only whether bidding activity rose or fell [P] |

One finding bears on brief 01. The quality agency's 2026 report calls junctions between
trades "an unthought part of renovation": "most often absent from the contract
documents," among the most frequent non-conformities in audits of certified renovation
contractors, and one of the main sources of defects across 800 renovations it reviewed
[P]. The agency answers with 100 free worked solutions that leave aside who is
responsible for what. The mechanism of brief 01 therefore extends from new windows to
energy renovation, which is most of what agencies now do, and still lacks a money
figure.

**Reading of the second pass.** France measures construction failure where the state
inspects or an insurer pays, and those are the five candidates above. For permits,
tenders, schedules, and payments, either no one publishes a measure or it sits in raw
open data (public contract records, permit registers) that a search cannot read. One
dig by hand into the public contract data, for amendments to building works contracts,
is the remaining cheap test.

## What this pass taught about sources

- Regional state reports on rule inspections (DREAL, DDT) are the French counterpart of
  the Dortmund permit statistics: official, repeated yearly, and specific down to the
  recurring breach.
- The insurer's annual report and the quality agency's observatory give money figures,
  which Germany's brief lacked.
- French agencies publish as PDF slide decks. Text extraction works; charts lose their
  labels, so several rates by category remain unread.

## Sources

- MAF, *Rapport annuel 2025* (published 2026): https://maf.fr/sites/default/files/2026-06/Rapport%20MAF%202026%20WEB%20PAGES_compressed.pdf
- AQC, *Rapport de l'Observatoire de la qualité de la construction 2026*: https://qualiteconstruction.com/wp-content/uploads/2026/06/Rapport-Observatoire-Qualite-Construction-2026-AQC.pdf
- DREAL Hauts-de-France, *Le contrôle du respect des règles de construction*, February 8, 2021: https://www.hauts-de-france.developpement-durable.gouv.fr/IMG/pdf/controle_des_regles_de_la_construction_bilan_2020.pdf
- DREAL Grand Est, *Contrôle du respect des règles de construction, bilan 2024*, March 2025: https://www.grand-est.developpement-durable.gouv.fr/IMG/pdf/bilancrc24-vdef_042025.pdf
- DREAL Pays de la Loire, *Bilan régional du contrôle des règles de construction*, November 14, 2025: https://www.pays-de-la-loire.developpement-durable.gouv.fr/IMG/pdf/2_crpb_dreal_crc_20251114.pdf
- Cerema, *Contrôles du respect des règles de construction: thermique*, June 29, 2023: https://www.occitanie.developpement-durable.gouv.fr/IMG/pdf/2-2-crc_thermique_ls.pdf
- AQC regulatory quality sheet on RE2020 energy performance: https://qualiteconstruction.com/wp-content/uploads/2024/05/Fiche-Qualite-Reglementaire-C03-RE2020-Performance-Energetique-AQC.pdf
- Press summary of the AQC 2026 report (windows): https://www.france-epargne.fr/news/menuiseries-exterieures-premier-poste-de-desordres-decennaux-au-moment-ou-maprimerenov-vacille
- tech.eu on Freeda, November 5, 2025: https://tech.eu/2025/11/05/freeda-raises-eur34m-to-transform-construction-plan-reviews-with-ai/
- FrenchWeb on Temelion: https://www.frenchweb.fr/temelion-leve-32-millions-deuros-pour-simplifier-la-conception-du-batiment-grace-a-lia/457096
- Banque des Territoires on the FinalCad reserves study: https://www.banquedesterritoires.fr/trop-beaux-les-logements-sociaux
