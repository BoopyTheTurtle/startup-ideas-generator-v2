# Career change, Europe: hunt on Edgar's app idea

Written 2026-11-24. No brief yet; nothing red-teamed.

The idea arrived as a solution: an app that consolidates courses, apprenticeships, and
continuing education, with an AI-assisted assessment of skills and interests. This hunt
looked for the measured problem and the payer behind it. It skipped `/map-work`, and it
ran Europe-wide at Edgar's request, against the skill's one-country rule. Money evidence
turned up in France only.

Marks: **[P]** primary source read, **[C]** computed by me from primary data (script in
`data/`), **[S]** search summary or secondary source, unverified at the page.

## Summary

| ID | Candidate | Evidence | Money tied to it | My reading |
|---|---|---|---|---|
| C1 | France pays €1,945 for a career assessment, about €162M a year, and the state capped it at €1,600 in 2026 | Three primary sources | Yes, per assessment, France only | Best opening. Ready for a brief; crowded |
| C2 | France buys career counselling for employed adults by tender | France compétences report read | Yes: €90.96M in 2024, €478 per entry | Real payer, one buyer, contract just renewed |
| C3 | Adults cannot find information on courses | Eurostat computed | None | No measure found; the one measure contradicts it |

The app as described matches C3, the weakest of the three. The money sits in the
assessment (C1) and in counselling (C2), not in the catalogue.

A second pass on 2026-11-24 covered Germany, the UK, the Netherlands, Italy, Spain, and
Poland; see "By country" below. Its main finding: every large state that funds career
advice gives it away, and the one measure of what people would pay themselves is €145
of a €700 service (Netherlands).

## C1. A career assessment costs about €1,950, and the state now caps what it pays

France funds a *bilan de compétences*, a 20-hour guided assessment of skills and career
options, from each worker's training account (CPF). It is the service Edgar's AI
feature would replace or cheapen.

| Claim | Figure | Kind | Source, date, URL | Mark |
|---|---|---|---|---|
| CPF spend, all actions | 1.391 million dossiers validated in 2024; €2.215 billion committed, net | Money (sector total, not problem evidence) | France compétences, *Rapport sur l'usage des fonds*, 2025 edition, CPF chapter, p. 1. https://www.francecompetences.fr/app/uploads/2026/02/RUF25_ComptePersonnelFormation.pdf | [P] |
| Assessments as a share of CPF dossiers | 6% of training actions bought in 2024 | Money | Caisse des Dépôts, *Mon Compte Formation, rapport annuel 2024*, section 1.1.4. https://politiques-sociales.caissedesdepots.fr/sites/default/files/Rapport-Annuel-MCF_2024-SA.pdf | [P] |
| Average cost of an assessment bought | €1,945 in 2024. Catalogue offers average €1,790 for 19 hours | Money | Same, sections 1.1.1 and 1.1.4 | [P] |
| Assessments funded and their cost, 2024 | About 83,000 dossiers and €162M, from 6% of 1.391 million at €1,945. The share is rounded, so allow 8% either way | Money | `data/unit_costs.py` | [C] |
| Hourly price of an assessment | Up 6% from 2023 to 2024, at constant characteristics | Money | Same, p. 10 | [P] |
| Hourly cost against certified training | An hour of assessment costs ten times an hour of training for a registered qualification (CDC, quoted by France compétences). Registered-qualification training cost €10 an hour in 2024 | Money | Same, pp. 9 and 11 | [P] |
| Hourly price | €93.20 an hour in 2024 | Money | Caisse des Dépôts figures as reported by Escale Learning. https://escale-learning.fr/cpf-ce-que-revele-le-dernier-bilan-sur-les-prix-et-les-pratiques-de-formation-en-2024/ | [S] |
| Worker's own contribution | €100 per CPF purchase since May 2, 2024; €102.23 for 2025. Jobseekers and employer-topped-up purchases exempt | Money | France compétences CPF chapter, p. 3 and note 3 | [P] |
| State cap on assessments | €1,600 of CPF rights per assessment (decree 2026-127, new article D. 6323-1 A of the labour code) | Risk | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053568407 | [P], read through a fetch agent that summarised the articles |
| Limits on what counts | CPF pays only for hours of accompaniment delivered by a registered provider, and only if no funder paid for an assessment in the five years before (decree 2026-126, article D. 6323-6). Both decrees took effect February 26, 2026 | Risk | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053568399 | [P], same caveat |
| Near-removal | The 2026 budget bill proposed dropping assessments from CPF eligibility | Risk | France compétences CPF chapter, note 7 | [P] for the proposal; [S] that it was withdrawn |

- **Who pays:** the state, through France compétences and the Caisse des Dépôts, for
  about 90% of CPF funds; the worker for 5.2% in 2024 [P].
- **Money tied to the problem:** yes. A price per assessment and a state cap below the
  average price.
- **What the decree means for an AI product:** the state pays for hours a registered
  provider spends with the person. Software time earns nothing from CPF, so an
  AI-led assessment sells either to providers, to cut their cost under the cap, or to
  individuals at their own expense.
- **Gaps:** the decree wording read with my own eyes; the average price since the cap;
  any outcome measure for assessments.
- **Crowding:** heavy. Chance sells an online assessment funded by CPF and raised €12M
  in February 2022 [S]. The CPF catalogue held 13,700 training bodies in 2024 [S]; how
  many sell assessments is a gap. Roleo (Estonia) raised €2.9M in November 2026 for an
  AI career agent aimed at tech workers [S].
- **Sources toward a brief:** three primary: France compétences, the Caisse des Dépôts
  annual report, and the two decrees. C1 passes the three-source gate.

## C2. France buys counselling for employed adults at about €478 an entry

The *conseil en évolution professionnelle* (CEP) is a free state counselling service.
France compétences buys the part for employed adults from regional operators, the
Avenir Actifs network, through a public tender.

| Claim | Figure | Kind | Source, date, URL | Mark |
|---|---|---|---|---|
| Spend on counselling for employed adults | €90.96M committed in 2024, up from €72.99M in 2023 and €50.56M in 2020 | Money | France compétences, 2025 edition, CEP chapter, p. 4. https://www.francecompetences.fr/app/uploads/2026/02/RUF25_ConseilEnEvolutionProfessionnelle.pdf | [P] |
| Entries, employed adults | 190,488 in 2024; 176,288 in 2023 | Money | Same, p. 4 | [P] |
| Cost per entry | €478 in 2024, €414 in 2023. The 2024 figure includes a €2.3M start-up phase and files closed and reopened at the change of contract | Money | Division of the two rows above | [C] |
| All CEP entries | 3.37 million in 2024, across five networks; 92% were jobseekers and 8% employed. France Travail delivered 78% | Risk | Same, pp. 1, 5, 8 | [P] |
| Cost outside the tendered part | Unmeasured: no source gives a unit cost for the other four networks | Gap | Same, p. 5 | [P] |
| Outcomes | France compétences reports no employment or career-change rate for CEP and argues against judging it by one | Gap | Same, pp. 9 and 10 | [P] |

- **Who pays:** France compétences, from employers' training contributions.
- **Money tied to the problem:** yes, but the buyer is one agency and the product would
  be a tool for the contracted operators, or a bid against them.
- **Gaps:** the operators' names, lot values, and contract end date (search the French
  contract data and TED by buyer); whether rising cost per entry worries the buyer.
- **Germany:** the federal employment agency has run free counselling for employed
  adults since 2020 [S]. I found no count, cost, or outcome figure after two searches.
  `no measure found`.

## C3. "Information on courses is scattered": no measure found

This is the app's stated premise. The one measure I found runs against it.

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Adults who searched for information on learning | 26.9% of EU adults aged 25 to 64 in 2022; 21.1% in 2016 | Size of group | Eurostat `trng_aes_182`; `data/aes_information_search.py` | [C] |
| Searchers who failed to find it | 2.2% of adults looked and did not find, against 19.2% who found, in 2011: 10.3% of searchers. Eurostat stopped publishing the measure after 2011 | Risk | Eurostat `trng_aes_186`; same script | [C] |
| Who pays for adult learning | 71.2% of non-formal learning activities in 2022 were job-related and employer-sponsored; 10.6% were job-related and self-directed | Size of group | Eurostat `trng_aes_188`; same script | [C] |
| Participation against target | 39.5% of adults in learning in 2022, against EU targets of 47% for 2025 and 60% for 2030 | Risk | Cedefop overview. https://www.cedefop.europa.eu/en/data-insights/adult-education-and-training-statistics-overview | [S] |
| Why adults stay out | Of those who wanted to learn and could not: schedule 25.3%, family 16.0%, cost 15.2%. Of non-participants, 42.4% did not want to | Risk | Same | [S] |
| Why adults skip guidance | 57% of non-users felt no need; about 20% did not know the service existed (six-country OECD survey, 2020) | Words | OECD, *Career Guidance for Adults in a Changing World of Work*, 2021. The site refused automated reading | [S] |

- **Reading:** nine in ten searchers found what they sought in 2011, and the barriers
  adults name are time, family, and cost. Information does not appear among the three
  leading barriers in the summary I read. Employers choose and fund seven in ten learning
  activities, so the self-directed career changer is the small segment.
- **States already build the catalogue.** Germany's employment agency runs the national
  portal *mein NOW* [S]; France runs Mon Compte Formation [P]. A private catalogue
  competes with free state products.
- **Procurement:** two TED searches for career-guidance platforms since January 2024
  returned 15 notices, none for a guidance platform bought by a European employment
  service for domestic use. The exact queries are in the hunt transcript, not yet in a
  script.
- **Audit:** the European Court of Auditors found that member states could show no
  evidence of results for about half of the labour-market reforms it examined in
  national recovery plans, lifelong learning among them (special report 10/2025) [S].

## By country (second pass, 2026-11-24)

| Country | What the state pays for career advice | Unit price | Mark | Outcome measured |
|---|---|---|---|---|
| France | Assessments from training accounts; counselling by tender | €1,945 per assessment; €478 per counselling entry | [P], [C] | None for either |
| Netherlands | Free "development advice" from a career adviser, 2020 to 2022 | €700 fixed per track; 68,000 tracks, €47.6M | [P], [C] | Sector change 14 points above the control group |
| UK (England) | National Careers Service, nine prime contractors, paid by outcome | £15 to £105 per outcome; about £167 per customer overall | [P] for rates; [S], [C] for the average | 59% of customers reached a job or learning outcome in 2023-24 [S] |
| Germany | Counselling for employed adults by the employment agency's own staff; 91,746 people entered in 2021 | Unpublished | [P] for the count | None published |
| Italy | The GOL programme: 3.29 million people reached by January 2025; specialist guidance is a priced service within it | €37 an hour, one to one; €77 an hour for a group | [P] | 35.8% employed at the reference date; 17.9% on the reskilling path |
| Spain | Guidance inside €6.1 to €6.5 billion of active labour policy (2019) | `no measure found` | [S] | The fiscal authority called the spending unevaluated [S] |
| Poland | Training vouchers through district labour offices | `no measure found` for guidance | [S] | |

### Netherlands: the only measure of willingness to pay

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| State price for career advice | €700 per development-advice track, paid to the adviser | Money | SEO Economisch Onderzoek for the Ministry of Social Affairs, *Leren en ontwikkelen in crisistijd*, September 2024, table in chapter 4. https://open.overheid.nl/documenten/a4d9f822-5186-4401-ac1c-9925a5f0fcc0/file | [P] |
| Volume | 68,000 development-advice tracks | Money | Same, annex B | [P] |
| What participants and their employers would have paid | €145 of the €700, on average, asked after the track: 21% | Money | Same, chapter 4 | [P] |
| Effect | Participants were 14 percentage points likelier to change sector than the control group; the report says they may have planned to move anyway | Risk | Same, summary and chapter 3 | [P] |
| Advice under the later STAP training budget | 2% of STAP users took the free advice; 58% of those used it to choose a course. An advice gave no guarantee of a training grant | Risk | SEOR and Ockham IPS, *Evaluatie en monitoring STAP-regeling*, December 2025. https://zoek.officielebekendmakingen.nl/blg-1266416.pdf | [P] |
| STAP money | €160M for 2022; about half of users say they would have trained without it | Money (sector total) | Same, chapters 3 and 9 | [P] |
| STAP running cost | €21.5M a year estimated for the agencies, of which €3.9M for the online platform | Money | Same, chapter 2 | [P] |

- **Reading:** the state valued an advice at €700 and its users at €145. Both Dutch
  schemes have ended, so the public payer has gone. Training providers told the
  evaluators that a subsidy needs a search engine and choice support around it, which is
  words, but it is the app's premise stated by the supply side.

### UK: a price list per outcome, and a service being absorbed

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Outcome prices | Career-management outcome up to £55 (priority group) or £15; learning outcome £70 or £20; job outcome £105 or £32 | Money | Department for Education, *Funding rules for the National Careers Service*, version 13, April 2026, table 1. https://assets.publishing.service.gov.uk/media/67e137aed8e313b503358c97/National_Careers_Service_funding_rules_2025_to_2026_version_12.pdf | [P] |
| Fixed fee | Up to 33% of contract value; phone and webchat are paid from it, not by outcome | Money | Same | [P] |
| Budget and volume | About £55M a year; 328,998 customers in 2023-24; nine prime contractors, more than 50 subcontractors | Money | FE Week, late 2025. https://feweek.co.uk/new-look-jobcentres-to-swallow-up-1000-careers-advisers/ | [S] |
| Cost per customer | About £167 | Money | `data/unit_costs.py`, from the row above | [C] from [S] |
| The buyer is changing | The service is to merge into Jobcentres as a Jobs and Careers Service; up to 1,000 subcontractor staff move into the civil service | Risk | Same, and the Work and Pensions Committee report. https://publications.parliament.uk/pa/cm5901/cmselect/cmworpen/1286/report.html | [S] |

- **Reading:** a learning outcome earns a contractor £20 to £70. At those prices a
  contractor cannot afford much adviser time per person, which is where software earns
  its place. The outsourced market is shrinking as the state takes the work in-house.

### Germany: a free state service with a count and no price (third pass)

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| People entering counselling for working-age adults (BBiE) | 91,746 with a recorded first contact in 2021, all statuses. The analysis sample held 44,786 employees, 8,946 unemployed, and 17,501 others | Size of group | IAB-Forschungsbericht 21/2023, section 3. https://doku.iab.de/forschungsbericht/2023/fb2123.pdf | [P] |
| Trend | Employees advised for the first time rose from about 45,000 in 2021 to just under 60,000 in 2024 | Size of group | IAB evaluation as reported by Servicestelle Weiterbildungsagenturen | [S] |
| Staff | 350 posts planned for 2020 | Money (indirect) | Bundestag paper 19/17878; the Bundestag server refused download | [S] |
| Awareness | Advisers and outside partners all rated the service's awareness as low; some firms visited had never heard of it. City advisers reported long waits, rural ones a shortage of clients | Words | IAB-Forschungsbericht 22/2025 (qualitative, interviews in 2024). https://doku.iab.de/forschungsbericht/2025/fb2225.pdf | [P] |
| The state catalogue | *mein NOW* "bundles a large part" of course offers, funding, and counselling. No usage or cost figure | Crowding | Employment agency annual report 2024, p. 28 of the text | [P] |
| Outsourced activation and coaching (MAT, including coaching vouchers) | The agency's own audit judged the support process unfit for a purposeful route to work in 70% of 120 cases audited; 29% ended early, mostly because the person found work | Risk | Bundesagentur für Arbeit, Interne Revision, May 2025. https://www.arbeitsagentur.de/datei/betreuung-in-massnahmen-zur-aktivierung-und-beruflichen-eingliederung_ba056214.pdf | [P] |
| Spend per funded case on those measures, 2024 | €961 under unemployment insurance; €2,357 under basic income support | Money | Bundestag paper 21/2498, October 2025 | [S] |
| Federal audit of coaching vouchers | Job centres complained in 2019 that the market for voucher-funded measures lacked transparency | Words | Bundesrechnungshof, March 20, 2019; summary only | [S] |
| Training budget | €3.4 billion for vocational training in the 2024 budget, €1.3 billion for employed people | Money (sector total) | Agency press release | [S] |

- **Reading:** Germany's counselling for the employed is done by salaried staff, so it has
  no price and no outside buyer. The paid market is activation and coaching for
  jobseekers, at €961 to €2,357 a case, sold by certified providers. That is where a
  tool could be sold, and the agency's own audit says its follow-up there fails.
- **Gaps:** total spend and entries on coaching vouchers; the 2019 federal audit's
  figures; any outcome for the counselling. Three Bundestag papers returned an error to
  two fetch methods.

### Italy: guidance has a tariff, and reskilling has the weakest outcome (third pass)

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Tariff for specialist guidance, including a skills assessment | €37 an hour one to one; €77 an hour per group session | Money | ANPAL, GOL annex C, *Standard dei servizi e unità di costo standard*, May 2022. Later revisions (2023) unread. https://www.lavorosi.it/wp-content/uploads/documenti/PRASSI_2022/anpal-delibera-n-5-del-09-05-2022-programma-gol-livelli-essenziali-prestazioni.pdf | [P] |
| Tariff for basic guidance | €35.50 an hour, three hours at most | Money | Same | [P] |
| People reached | 3,286,912 by January 31, 2025; 699,294 on the reskilling path, 814,891 on upskilling | Size of group | INAPP for the Ministry of Labour, GOL monitoring note, data to January 31, 2025. https://www.lavoro.gov.it/temi-e-priorita/occupazione/nota-monitoraggio-gol-al-31-gennaio-2025 | [P] |
| Employed at the reference date, by path | Reinsertion 44.5%; upskilling 36.3%; reskilling 17.9%; all paths 35.8%. The reskilling group is 95.2% vulnerable, so the gap reflects who enters as well as what the path does | Risk | Same, table 2.2 | [P] |
| People with any measure started | 61.8% of those reached. The wait from intake to first measure fell from about 126 days (intakes of late 2022) to 8 | Time | Same, section 2.1 | [P] |
| Programme money | About €4.6 billion for active labour policy and training under the recovery plan | Money (sector total) | Openpolis-Assonime report, via La Gazzetta degli Enti Locali | [S] |
| The state's own AI adviser | AppLI, free, built by the ministry with INPS; more than 60,000 registered users, date unstated | Crowding | Ministry of Labour pages | [S] |

- **Reading:** Italy pays accredited providers €37 an hour for the service the app
  would automate, inside a programme that ends with the recovery plan in 2026. Fewer
  than one in five people on the reskilling path were in work at the count. The
  ministry launched a free AI assistant in October 2025.
- **Gaps:** hours of specialist guidance delivered and paid; the audit court's view;
  what replaces GOL after 2026.

## The numbers, sized (fourth pass, 2026-11-24)

| Market | Yearly spend | Units | Per unit | Mark | Trend |
|---|---|---|---|---|---|
| France, assessments from training accounts | About €162M (2024) | About 83,000 | €1,945 | [C] from [P] | Capped at €1,600 and one per five years since February 2026 |
| France, counselling for employed adults | €90.96M (2024) | 190,488 entries | €478 | [P], [C] | Up 80% since 2020 |
| UK, National Careers Service | About £55M; nine contracts tendered at £186M in total, period unread | 328,998 customers (2023-24) | About £167 | [S], [C] | Moving in-house |
| Netherlands, development advice | €47.6M over 2020 to 2022 | 68,000 tracks | €700 | [P], [C] | Ended |
| Germany, provider-run activation in job centres | €874.6M (2024, joint job centres only) | 436,400 entries | €2,004 an entry; €1,014 a participation month | [P] | Entries down a third since 2018, cost per month up 44% |
| Italy, specialist guidance in GOL | Unknown: hours paid are unpublished | | €37 an hour | [P] | Programme ends 2026 |

- The German row comes from Wolff, *Kosten und Nutzen von Maßnahmen zur Aktivierung*,
  IAB 2025, table 1 (https://doku.iab.de/grauepap/2025/Wolff_KNA_MAbE.pdf). It covers
  all provider-run activation, of which career coaching is an unmeasured part, so read
  it as a ceiling.
- France spends €253M a year on the two services together, €7.60 per adult aged 25 to
  64 (`data/market_size.py`). It is the only country where both figures are primary.
- The UK tender figure comes from a tender-tracking site; the official notice refused
  automated reading.

## The Baltic market (fourth pass, 2026-11-24)

All three states already run what the app describes: a national platform joining a
course catalogue to a personal learning budget, plus free career counselling. EU funds
built each one.

| | Estonia | Latvia | Lithuania | Mark |
|---|---|---|---|---|
| Adults aged 25 to 64 (2024) | 725,000 | 970,000 | 1,604,000 | [C] |
| Searched for learning information (2022; EU 26.9%) | 34.4% | 24.9% | 16.0% | [C] |
| Took part in learning, including guided on-the-job (2022; EU 46.6%) | 48.1% | 52.2% | 31.4% | [C] |
| State platform | Unemployment fund's services; training card up to €2,500 over three years | STARS, with individual learning accounts of €500 | Kursuok, voucher up to €500 | [S], [S], [P] |
| Free career counselling | For everyone, 45-minute sessions | Employment agency, plus 19 municipal consultants booked through STARS | 14 regional career centres open to all ages since 2024 | [S] |

### Latvia

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Learning-account pilot | €14,725,025 total, July 1, 2023 to November 30, 2026; targets of 3,500 account users and 3,500 adults helped to digital skills | Money | VIAA project page, read through a fetch agent. https://www.viaa.gov.lv/lv/eiropas-savienibas-atveselosanas-fonda-projekts-individualo-macibu-kontu-pieejas-attistiba | [P] |
| Uptake | More than 10,000 accounts registered on STARS by February 2025 | Size of group | stars.gov.lv news | [S] |
| Training that changes nothing | 44% of participants in state-funded adult training took programmes with no effect on their employment: €12.7M over three years | Money | State Audit Office, November 2023, as reported by LSM. The audit PDF dropped the connection twice | [S] |
| Who gets the support | 28% of participants had low education, the priority group | Risk | Same | [S] |
| Programmes nobody ran | Over half of the employment agency's and three quarters of VIAA's vocational programmes drew no provider | Risk | Same | [S] |
| Money in scope | €164.3M allocated to the two agencies' projects | Money (sector total) | Same | [S] |
| Employment agency clients | 66,945 started a measure in 2024; no count of career consultations | Size of group | Agency news on its 2024 public report | [P] |

- **Reading:** Latvia has the strongest problem evidence of the three, and it is about
  choice, not information: the state pays for courses that leave employment unchanged.
  The payer is the state.

#### What funds STARS after November 30, 2026 (fifth pass, 2026-11-24)

Source for every row: the Education Ministry's report to the Cabinet, *Par individuālo
mācību kontu pieejas un prasmju pārvaldības platformas STARS ilgtspējības
nodrošināšanu*, draft 26-TA-1582, status "submitted", review rounds September 17 to
October 26, 2026, and its annex, the 146-page independent final report. Both read;
copies in `data/sources/`.
https://tapportals.mk.gov.lv/legal_acts/f4084194-a7c9-4327-ac94-6aa8d2ea3239

| Claim | Figure | Kind | Mark |
|---|---|---|---|
| Legal status | The learning-account system is part of the State Education Information System by article 18.2 of the Education Law, in force March 6, 2026. The Cabinet must still set its funding rules (draft 26-TA-1241) | Risk | [P] |
| Platform money, December 2026 to November 2029 | €120,000 from an ESF+ project and €80,000 from a Just Transition Fund project, for development and upkeep. Existing staff maintain it; no new posts | Money | [P] |
| Platform money from 2030 | About €125,000 a year from the state budget, provisional and unallocated | Money | [P] |
| What the build cost in staff | €627,063.32 to August 31, 2026; 18 posts on the pilot, 6 on the platform. Built in-house on a 2018 system | Money | [P] |
| Money for the accounts themselves | None committed. Three scenarios (state budget for vulnerable groups; STARS as the tool for all EU-funded adult training; a universal account with state, EU, and private money). The ministry will "assess" continuing in the 2028–2034 EU funding period | Gap | [P] |
| Results | 64,000 accounts by July 7, 2026; 15,453 certificates to 14,110 adults by June 17, against a target of 3,500 | Size of group | [P] |
| Grants used | 74% of €500 grants were used; 19% were annulled for non-use or dropping out | Risk | [P] |
| The catalogue is what people use | 165,013 unique visitors and 407,000 catalogue views to end 2025; career-support and skills-assessment pages were "proportionally very little visited" | Risk | [P] |
| Guidance tools on the platform | 3,985 people took a test to end 2025, 9.2% of the 43,127 who registered; learning-path planning is "largely unused" and seen as a formality | Risk | [P], [C] |
| The platform cannot see its own funnel | Views of the personalised catalogue, funding pages, and learning history are not recorded | Gap | [P] |
| Catalogue is hard to read | Users struggle with formal language, long texts, and several projects shown at once; about 25% of visitors register | Risk | [P] |
| How Latvians plan careers (population survey, SKDS, May 2026) | 17% have used AI tools for career development and 20% would in future; 13% online tests and tools (23% would); 2% a private career consultant (9% would); 4% a consultant at an education institution | Size of group | [P] |
| Career consultants as an information channel | Named by 3% to 4% of respondents, the least used channel | Risk | [P] |
| Employers | Employer co-financing in the pilot was low | Risk | [P] |
| Wider role | The Cabinet decided on September 8, 2026 that STARS becomes the single tool for all publicly funded adult training, exchanging data with the employment agency. State-language courses for adults move onto it | Crowding | [P] |

- **Answer:** the platform survives and the money for learners does not. STARS runs
  on €200,000 over three years, then €125,000 a year. The €500 accounts end with the
  pilot unless another EU project loads money onto the platform.
- **What this means for the idea in Latvia:** the state owns the catalogue by law and
  has no budget to improve it. Its own evaluators say the guidance tools go unused and
  the catalogue confuses people. Meanwhile 17% of the population already use AI tools
  for career planning, eight times the share who have paid a private consultant.
- **Two readings, both unproven.** A product could sit on top of STARS as the guidance
  layer the state cannot fund, if STARS opens its catalogue data. Or the 17% shows that
  general chatbots already serve the need for free. Whether the catalogue is open data
  and whether anyone would pay are the two facts to establish.
- **Gaps:** no procurement record for STARS found; private consultants' prices; the
  2028–2034 funding decision; whether the catalogue has an open interface.
- A Latvian AI career coach for pupils exists (*Nākotnes darbs*, built in a World
  Economic Forum education accelerator) [S]. I found none for adults.

### Lithuania

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| What the state pays | Voucher up to €500; contact hours only, at €9 an hour for 18 to 35 hours down to €6 for 400 or more; the learner pays any excess | Money | kursuok.lt, "Apie paslaugą", read through a fetch agent | [P] |
| Volume | 23,200 people completed training since launch (to August 2026) | Size of group | ESF agency and platform home page | [S] |
| Budget | €5.42M in 2025; €53M planned to 2030 for more than 100,000 people | Money | Press reports | [S] |
| Guidance on the platform | A "direction compass" section with "consult" and "know yourself" | Crowding | kursuok.lt menu | [P] |
| Quality | Press criticised vouchers spent on boxing and couples' courses; a minister ordered an audit of the platform | Risk | LRT | [S] |
| Career centres | More than 115,400 uses of career-planning services and 28,200 individual consultations in a year the sources leave unclear | Size of group | Employment Service press | [S] |

### Estonia

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Counselling volume | 120,513 people received work-focused or career counselling in 2021; 14% were employed or inactive, 31% pupils | Size of group | Unemployment fund annual report 2021, via search summary | [S] |
| Awareness | 41% of surveyed users did not know, or were unsure, that the fund pays for employed people's training | Words | Ministry of Economic Affairs analysis of "Tööta ja õpi", June 2026; the PDF refused download | [S] |
| Outcome | The National Audit Office found the fund had no overview of whether training helps people find work; €32.7M went on vocational training | Risk | Riigikontroll, about 2022, press coverage | [S] |

### Baltic reading

- **Size:** 3.3 million adults. At France's spending rate the three markets together
  would be worth about €25M a year (Lithuania €12.2M, Latvia €7.4M, Estonia €5.5M).
  This scales one country's rate and is no evidence that anyone spends it.
- **Payer:** only the state, with EU money. I found no price for private career advice
  in any Baltic language and no consumer payment.
- **Crowding:** the state platforms are the competitors. Roleo (Estonia, €2.9M) sells
  to tech workers.
- **Opening, if any:** the audits in Latvia and Estonia and the Lithuanian audit order
  all say the states cannot tell which training works. A product that proves or
  improves the choice sells to three ministries, not to career changers.
- **Gaps:** every Baltic outcome figure is secondary; private prices; what follows the
  Latvian pilot; Kursuok's statistics page; the Estonian fund's 2024 report.

### Spain, Poland

One or two searches each found programme totals and no price or outcome for guidance.
Spain's fiscal-authority studies are the dataset to open next.

## AI career advisers already on the market (crowding check, 2026-11-24)

All rows are [S]: one or two searches per country, company claims unverified.

| Country | Provider | What it sells | Funding found |
|---|---|---|---|
| France | Chance | Online assessment with human coaches, CPF-funded | €12M, February 2022 |
| France | Hipow | AI assessment with optional human coach: free, €155, or €1,220 | None found |
| France | Rewayz | AI-supported assessment for employees and firms | Raising €1M, about 2023 |
| France | Weelife, MyTalents | AI "pre-assessment"; AI career recommendations | None found |
| Germany | WhyBrilliant | Voice AI agent that interviews tech candidates and matches jobs | About $1.2M, June 2026 |
| Germany | State: *mein NOW* | Course catalogue with decision support | Public |
| UK | Indeed Career Scout | AI career coach for career changers, launched July 2026 | Indeed |
| UK | Morrisby; Multiverse Atlas | Guidance for pupils and colleges; AI coach for apprentices | Multiverse $70M, 2026 |
| Netherlands | SkillLab | AI skills interview on the EU skills taxonomy, sold to city and public employment services. It says it avoids AI career recommendations | €1.5M seed |
| Netherlands | Unnamed start-up (September 2025) | AI job-search agent growing into a career coach | None found |
| Italy | Jobiri | "AI career consultant", claims 70,000 users, sells to institutions | Prize and soft loan, 2018 |
| Italy | State: AppLI | Free AI assistant for job search and training | Public |
| Spain | Growth Road; Taalentfy | AI vocational guidance; AI employability guidance for schools and firms | €300,000; €1.5M |
| Poland | Jobbli | AI career adviser with a free profiling test, aimed at career changers | None found |
| Estonia | Roleo | AI career agent for tech workers | €2.9M, November 2026 |
| Any | Kickresume and similar | Generic AI career coach in local languages | — |
| Any | General chatbots | A French paper ran an assessment in ChatGPT and noted it gives no official attestation | — |

- **Reading:** every country checked has an AI career adviser, and none found has
  raised more than Chance's €12M. Three are free and large: Indeed, the Italian state,
  and general chatbots.
- **What I did not find:** a product that joins an assessment to a consolidated
  catalogue of courses and apprenticeships with funding eligibility. France's and
  Germany's state portals hold the catalogue; the start-ups hold the assessment. Two
  searches per country cannot prove the gap exists.
- **Not checked:** app-store listings, each company's current status, the Nordics.

## Gates

- **Core work:** fails as posed. The idea serves consumers, not a vertical's core
  workflow. It passes if reframed as a tool for assessment providers or counselling
  contractors, whose core work this is.
- **Three sources:** C1 passes with three primary sources. C2 has one.
- **Money tied to the problem:** C1 and C2 yes, French. The Netherlands and the UK add
  unit prices for the same service. C3 none.
- **Consumer payment:** the one measure is €145, about a fifth of the Dutch state price.

## Not done

- The OECD report is unread at the source (the site refuses automated reading). The two
  French decrees were read by a fetch agent that summarised the articles.
- Spain and Poland have no unit price. The Nordics are unsearched.
- The crowding check is one or two searches per country; no provider's claims were
  verified at its own site.
- The two TED queries are not in a script.
- Sources that refused reading: three Bundestag papers, the Latvian audit PDF, the
  Estonian ministry analysis, the UK tender notice.
