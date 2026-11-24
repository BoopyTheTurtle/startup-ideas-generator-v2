# Research plan: measured failures in Latvian education that a mindset solution could target

Written 2026-11-24. A plan only: no source below has been read for this purpose, and
every institution, programme, and regulation number named here comes from memory and
needs checking at its source.

## The question

Which failures in Latvian education are measured, cost a named payer money, and have
student or teacher beliefs as a documented cause? A failure that passes all three tests
becomes a candidate in `candidates.md`. A failure that passes the first two and fails
the third is still a finding, and goes to the longlist in `scan.md` without the mindset
label.

## The bias to guard against

This hunt starts from a solution, which the engine normally forbids. The risk is fitting
evidence to the idea. Three guards hold it off:

- Record every cause a source names for a failure, structural ones first (funding,
  teacher supply, language of instruction, school size, family income).
- Count a belief-related cause only when a source measures it. An author's opinion that
  pupils lack motivation is words.
- Apply the ceiling test in stage 5 before any brief. The best trials put the effect of
  mindset teaching on grades between d = 0.02 and d = 0.10 [S], so a candidate must
  survive on a small share of the failure's cost.

## Failures to test

Each row is a hypothesis. The sweep in stage 2 confirms or drops it.

| # | Failure | Who should measure it | Who should pay |
|---|---|---|---|
| F1 | Pupils leave general or vocational school early | Education quality service (IKVD), statistics office (CSP), the closing report of the EU-funded early-leaving project *PuMPuRS* | State and municipality, since funding follows the pupil; EU funds |
| F2 | First-year students drop out of university and college | Ministry's yearly review of higher education; university self-assessment reports | The institution, which loses the funded place or the fee |
| F3 | Pupils fail or barely pass the centralised mathematics exam | Exam centre results by school and year | Municipality and school; parents, through private tutoring |
| F4 | Adults abandon state-funded training | Employment agency (NVA) and the adult-learning programme's reports | State, EU funds, employers |
| F5 | Teachers leave the profession | Already in `scan.md` row 8 | Parked: the link to mindset is weakest here |

## Stages

**Stage 1. Find Latvia's mindset baseline (one session).** PISA 2018 asked pupils whether
intelligence can change and reported the answer by country. Read the OECD volume and the
University of Latvia's national PISA report for Latvia's share, its gap to Estonia and
Lithuania, and its link to scores. Check PISA 2022 and TALIS for newer items. A high
baseline leaves little to change and weakens every row above. *Stop rule:* no Latvian
figure exists; record the gap and continue, because the failures stand on their own.

**Stage 2. Sweep for the measure (two sessions).** For F1 to F4, search in Latvian, in
source-map order:

1. State Audit Office reports on education (`lrvk.gov.lv`).
2. Closing reports and evaluations of EU-funded programmes, searched by programme name
   on the draft-law portal (`tapportals.mk.gov.lv`). The career-change hunt ranked these
   first.
3. The education development guidelines for 2021–2027 and their mid-term review: target
   indicators, the values reached, and the money assigned to each.
4. Open data: the state education information system (VIIS) on `data.gov.lv`, exam
   results by school, CSP tables on early leavers.
5. Regulation: the basic and secondary education standards list self-directed learning
   as a required transversal skill. Read the text for what schools must show an
   inspector.

Each failure needs a rate, a count, a year, and a trend. *Stop rule:* a failure with no
measured figure after the dataset check is recorded as `no measure found`.

**Stage 3. Attribute causes (one session).** For each surviving failure, list the causes
its sources measure and the share each explains. Look for exit surveys of leavers,
PuMPuRS risk-factor records, and regressions in the national PISA report. *Gate:* a
failure advances only when a source measures a belief, motivation, or self-efficacy
cause. The rest go to `scan.md` unlabelled.

**Stage 4. Tie money to the failure (one session).** Find the cost per incident and the
payer: funding lost per departed pupil or student, cost per PuMPuRS support plan, cost
of a repeated year, NVA cost per unfinished course. Then find what payers already buy.
Run the e-procurement data (scripts in `data/`) for CPV division 80, and the EU funds
project list, for motivation, social-emotional, and study-skills programmes. Existing
purchases prove a budget line and name the incumbents.

**Stage 5. Ceiling test (computed, script in `data/`).** For each candidate:
incidents per year × cost per incident × the share a mindset effect could plausibly
move. Use the trial effect sizes read at their primary sources, taking the at-risk
subgroup figure only when the Latvian population matches it. *Gate:* a ceiling below the
price a payer already pays for comparable programmes closes the candidate.

**Stage 6. Ledger, crowding, neighbours.** Build the ledger per `/hunt`: three
independent sources, one money entry tied to the problem. Search for Latvian sellers by
function (motivation programme, study-skills course, early-leaving prevention), and
check Lithuania and Estonia for the same failure and the same sellers.

## Output

- Sections in `candidates.md` for each failure that passes stage 5, each with a ledger.
- A row in `scan.md` for each measured failure that failed the belief test.
- Additions to `research/source-map.md` for each source type that proved its rank.

Nothing in this plan spends money or contacts anyone. Interviews with schools or IKVD
would sharpen stage 3; Edgar launches those.

## What would end the hunt early

- Stage 3 finds no failure with a measured belief cause.
- Stage 4 finds that payers buy such programmes only with EU project money that ends
  with the programme.
- Stage 5 leaves every ceiling below existing programme prices.

Each ending is a result worth recording in `grades.md`.

---

# Stage 1 findings: Latvia's mindset baseline

Done 2026-11-24. Marks follow `candidates.md`: **[P]** primary document read, **[R]**
official release read through text extraction, **[C]** computed, **[S]** search summary.

## Result

Latvia has a measured baseline, and it leaves room. On the general question Latvian
15-year-olds sit at the OECD average; on mathematics they sit well below it, and the
ministry's own summary names growth mindset in mathematics as a thing to build. The stop
rule did not fire.

## Ledger

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Pupils who reject "your intelligence is something about you that you cannot change very much", 2022 | Latvia 58.8%; OECD 57.8%; Estonia 73.9%; Lithuania 57.5%; Finland 59.2% | Words (survey) | OECD, *PISA 2022 Results (Volume V)*, Table V.2 | [P] |
| Pupils who reject "some people are just not good at mathematics, no matter how hard they study", 2022 | Latvia 26.8%; OECD 34.5%; Estonia 33.3%; Lithuania 25.2% | Words (survey) | Same table | [P] |
| Boys reject the mathematics statement more often than girls | Latvia 9.8 points; OECD 6.6 | Words (survey) | Same table; the ministry rounds to 10 | [P] |
| Pupils who like school work that is challenging, 2022 | Latvia 28.0%; OECD 46.9%; Estonia 40.0%; Lithuania 35.9% | Words (survey) | Same table; ministry summary states 28%, 19 points below the OECD | [P] |
| Pupils who love learning new things in school, 2022 | Latvia 44.2%; OECD 50.1% | Words (survey) | Same table | [P] |
| Pupils who reject the fixed-intelligence view, 2018 | Latvia 72.6%; OECD 62.6%; Estonia 77% | Words (survey) | Ministry release of April 8, 2021 on the OECD's 2018 mindset report | [R] |
| Change in Latvia, 2018 to 2022 | −13.8 points (Estonia −3.1) | Words (survey) | 72.6 − 58.8, from the two rows above | [C] |
| Pupils who skipped a whole school day in the two weeks before the test, 2018 | Latvia 28.7%; OECD 21.2%; Estonia 17.4%; Latvia up 3.9 points on 2015 | Risk | Latvia's national PISA 2018 report | [P] |
| Reading score linked to skipping a whole day, Latvia, 2018 | 39 points lower, after adjusting for pupil and school socio-economic status | Risk | Same report | [P] |
| Sense of belonging at school, 2018 index | Latvia −0.26; Estonia −0.13; Lithuania −0.13; OECD 0 | Words (survey) | Same report | [P] |
| Teachers who feel able to support pupils' social and emotional learning, 2024 | Latvia 88%; OECD 73% | Words (survey) | TALIS 2024 country note | [S] |

## Qualifiers

- The OECD flags Latvia's 2022 estimates: one or more sampling standards were unmet.
- I read Table V.2 in a copy on a Romanian news site, because oecd.org refuses automated
  reading. The copy lost the bold that marks significance, so I cannot say whether 58.8%
  differs from the OECD's 57.8%.
- The 13.8-point fall joins a press release to a primary table and needs the OECD's
  2018 table before a brief uses it. If it holds, it is the largest finding here.
- Every figure above is a self-report at age 15 and a correlation. None shows that a
  belief causes a failure, and none is money.

## Gaps

- The score gap in Latvia between pupils with and without a growth mindset, and its
  size by family income. It sits in OECD annex tables V.B1.3.40 and V.B1.3.42, which I
  could not reach. Edgar can open them in a browser, or stage 3 can compute them from
  the public PISA 2022 student file.
- Lithuania's 2018 figure.
- Any mindset measure for vocational pupils, university students, or adults (F1, F2, F4).

## What this changes in the plan

- **F3 (mathematics) moves first.** The belief gap is specific to mathematics, the
  ministry names it, and the exam gives a yearly, school-level measure to set beside it.
- **Unexcused absence joins F1** as a measured precursor of early leaving, with an
  Estonian comparison already in the national report.
- **Challenge avoidance is the sharper lever than general mindset.** A 19-point gap to
  the OECD is larger than any mindset gap, and stage 3 should look for causes of it.
- **Teachers report high confidence** in supporting such skills [S], which weakens a
  teacher-training product and favours one aimed at pupils. Verify at the source first.

## Sources

- OECD Table V.2, copy: https://www.edupedu.ro/wp-content/uploads/2024/11/tabel-2-pisa-vol-5.pdf
- Ministry summary of PISA 2022 Volume V (Latvian): https://www.izm.gov.lv/lv/media/25938/download
- Ministry release, April 8, 2021: https://lvportals.lv/dienaskartiba/326820-oecd-petijums-skoleni-latvija-vairak-tic-iespejai-attistit-savas-prasmes-2021
- National PISA 2018 report: https://ppdb.mk.gov.lv/wp-content/uploads/2023/09/OECD-Starptautiska-skolenu-novertesanas-programma-PISA-2018_PETIJUMS.pdf
- TALIS 2024 country note, Latvia: https://www.oecd.org/en/publications/results-from-talis-2024-country-notes_e127f9e2-en/latvia_f484f77f-en.html

---

# Stage 2 findings: the sweep for measured failures

Done 2026-11-24. Marks as in stage 1. **[P]** here means I extracted the official PDF
and read the figure in it. **[R]** covers press releases and news articles read through
a fetch agent; the news articles are secondary.

## Result

Mathematics (F3) is measured best and fails most where the plan did not look:
vocational schools and distance learning. Early leaving (F1) is measured but small by EU
standards, except for expulsion from vocational schools. University dropout (F2) has one
stale secondary figure. Abandonment of adult training (F4) is low and fails as framed.

| # | Failure | Measured? | Verdict |
|---|---|---|---|
| F3 | Failing the mathematics exam | Yes, yearly, by school | Advances. Strongest |
| F1 | Early leaving | Yes | Advances for vocational schools only |
| F2 | University dropout | One 2022 secondary figure | Holds until a primary source is read |
| F4 | Abandoning adult training | Yes, and the rate is low | Dropped as framed |

## F3. Mathematics

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Grade 9 exam, 2026: takers, mean, below the pass mark | 15,955 takers; mean 54.8%; 750 below 15% | Risk | Exam agency (VIAA) results, July 14, 2026 | [P] |
| Share of grade 9 takers below the pass mark, 2026 | 4.7% | Risk | 750 ÷ 15,955 | [C] |
| Pass mark | 10% from 2022/23; 15% from 2025/26; 20% in secondary | Risk | Same | [P] |
| Grade 9 exam, 2025 | 17,330 takers; mean 53.80%; 304 (1.8%) below 10% | Risk | VIAA analysis of the 2024/25 exam | [P] |
| Grade 9 pupils below 10%, earlier years | 654 in 2024; 826 in 2023 | Risk | LSM, July 8, 2024, citing the exam centre | [R] |
| Grade 9 exam, 2025: mean by part | Part one 60.92%; part two 32.93% | Risk | VIAA analysis | [P] |
| Secondary exam, optimal level, 2026 | Mean 42.4%; 2,591 below 20% | Risk | VIAA results, 2026 | [P] |
| Who the 2,591 are | 332 grade 12 pupils of general schools; 660 grade 12 in distance learning; 1,599 grade 11 pupils and vocational students | Risk | Same | [P] |
| Consequence | A secondary certificate requires the mathematics exam; a grade 9 pupil below the mark repeats the year | Risk | VIAA results [P]; LSM [R] | [P]/[R] |
| One vocational school, 2025 | 35 of 43 takers failed; mean under 11% | Risk | LSM, October 22, 2025 | [R] |
| One distance-learning school, grade 9, 2025 | 40 of 96 failed; mean 15% | Risk | Same | [R] |
| Mathematics lessons taught against plan | Up to 46% fewer over three years | Risk | State Audit Office release, February 18, 2026 | [R] |
| Variation the standard allows | ±25% of 1,501 lesson hours in grades 1 to 9, a gap of up to 751 hours | Risk | Same | [R] |

Causes the sources name, structural first: lessons untaught; a standard that lets
schools cut hours; no national diagnostic tests in grades 3 and 6 for three years; a
funding model blind to pupil need (a psychologist's time averages 14 to 18 minutes a
pupil a week); teacher shortage. The audit release mentions neither motivation nor
belief. A ministry official's statement that 600 to 700 pupils a year fail to finish
school because of mathematics [R] predates the higher pass mark.

Qualifiers: raising the mark from 10% to 15% explains most of the jump from 304 to 750;
my reading of the slide puts 314 of the 750 below 10%, level with 2025. The slide's
taker count for the secondary exam is ambiguous (between 14,449 and 15,765), which puts
the failure share at 16% to 18% [C].

## F1. Early leaving

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Early leavers aged 18 to 24, 2024 | Latvia 7.9%; EU 9.3% | Risk | Education and Training Monitor | [S] |
| Children aged 5 to 18 registered at no school | Over 15,000; just under 11,000 believed abroad; over 4,000 unaccounted for | Risk | LSM, September 26, 2025, citing the quality service (IKVD) | [R] |
| Students expelled from vocational programmes | 5,521 in 2022/23; 4,574 in 2023/24 | Risk | Ministry admissions review, 2024 | [P] |
| Same, 2024/25 | 4,207 | Risk | Sum of the reasons chart in the 2025 review | [C] |
| Expelled for insufficient or missing grades | 1,324; 1,017; 879 over the three years | Risk | Same two reviews | [P] |
| Expelled for non-attendance | 577; 362; 395 | Risk | Same | [P] |
| Expelled under "other" | 2,280; 1,867; 1,591 | Risk | Same | [P] |
| Expelled students who continue nowhere | 347 of 1,113 (31%), third quarter of 2024 | Risk | 2024 review | [P] |
| Vocational students, autumn 2025 | 28,795 | Size | 2025 review | [P] |
| Early-leaving project *PuMPuRS*, 2017 to 2022 | €39.81M, of which €33.8M EU | Money | Search summary of an IKVD document | [S] |
| Its successor *Skola – kopienā*, to August 2029 | €16M, just under €14M from the EU | Money | LSM, September 26, 2025 | [R] |

Causes named: emigration (counted); family, health, money, bullying, teacher attitude
(named, uncounted). The LSM investigation reports that unwillingness to study is one of
the rarer reasons. One municipality's closing report attributes 97% of risk factors to
learning difficulties [S].

Qualifiers: the national rate is already below the EU target, so the failure is small in
EU terms. The money is real, and it is EU project money, which is the second early
ending the plan names.

## F2. University dropout

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Bachelor students who finish on time | 48% | Risk | LSM, October 5, 2022, citing an unnamed OECD report | [R] |
| Non-completion by OECD method, against the ministry's target | About 50%; target 20% | Risk | Same, a ministry official quoted | [R] |
| Students, 2024/25; share on state-funded places | 74,790; 43% | Size | Ministry release, August 4, 2025 | [R] |

No first-year rate, no cause with a figure, and no cost per funded place turned up.
The ministry's concept paper on institutional funding is the next source to read, since
the 2022 article says funding would reward lower dropout.

## F4. Adult training

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Non-formal training, 2025: started, finished, expelled | 16,065; 14,424; 836 | Risk | Welfare ministry review of NVA training, 2025 | [P] |
| Reasons for those expulsions | Contract breach 37%; found work 19%; health 18%; other 26% | Risk | Same | [P] |
| Requalification, 2025: enrolled and expelled | 777; 72 (9.2%); 47% of them because they found work | Risk | Same | [P] |
| Online courses on *Coursera*, 2025 | 2,586 participations; 605 discontinued | Risk | Same | [P] |
| Share discontinued | 23% | Risk | 605 ÷ 2,586 | [C] |
| What NVA pays for them | €167,408.58 for 500 licences, July 2025 to June 2026 | Money | Same | [P] |
| Mean cost per person | €482 non-formal; €1,889 further education and upskilling | Money | Same | [P] |
| Completers with no employment effect, 2019 to mid-2022 | At least 44%; €12.7M over three years | Money | State Audit Office release, November 22, 2023 | [R] |
| Participants with low education | 28% | Risk | Same | [R] |

Abandonment is 5% in non-formal training [C], and nearly half of the requalification
exits are people who found work. The failure the audit measures is different: training
reaches the well educated and often changes nothing. Self-paced online study is the one
line where a quarter stop, and NVA pays per licence.

## What this changes

- **Reframe F3 around vocational and distance-learning students.** They are 2,259 of
  the 2,591 secondary failures, each school is a named payer, and vocational schools
  also expel about 900 students a year for failing grades. General-school grade 12
  pupils are 332.
- **The structural causes of F3 are large and measured; the belief cause is neither
  yet.** Stage 3 must find a measured belief cause among vocational students or the
  candidate goes to `scan.md` unlabelled. Untaught lessons alone may explain the result.
- **F1 survives only inside vocational schools**, where it merges with F3.
- **F4 is dropped.** Its online-course line joins F2 as a question about self-directed
  study, to revisit only if stage 3 finds a belief measure for adults.

## Gaps

- The audit's full report: the audit office server dropped the connection twice.
- Exam results by school, which VIAA publishes: the dataset for stage 3.
- A primary source for F2, and the national closing evaluation of *PuMPuRS*.
- The statistics office table of early leavers by sex and by town or country.

## Sources

- VIAA, 2025/26 exam results: https://www.viaa.gov.lv/lv/media/50817/download
- VIAA, analysis of the 2024/25 grade 9 mathematics exam: https://www.viaa.gov.lv/lv/media/48308/download
- State Audit Office release on basic education: https://lvportals.lv/dienaskartiba/386222-valsts-kontrole-latvija-nav-nodrosinata-vienlidz-kvalitativa-pamatizglitiba-2026
- LSM, full exam results, October 22, 2025: https://www.lsm.lv/raksts/zinas/latvija/22.10.2025-pilnie-centralizeto-eksamenu-rezultati-vadiba-valsts-gimnazijas-daudz-izkrituso-talmaciba.a619411/
- LSM, grade 9 failures, July 8, 2024: https://www.lsm.lv/raksts/zinas/latvija/08.07.2024-no-20252026-macibu-gada-9-klases-eksamenos-izkritusajiem-ipasa-programma-plano-macit-amatu-precizets.a560710/
- Ministry vocational admissions review, 2024: https://www.izm.gov.lv/lv/media/31373/download
- Ministry vocational admissions review, 2025: https://www.izm.gov.lv/lv/media/28206/download
- LSM, children outside school, September 26, 2025: https://www.lsm.lv/raksts/zinas/latvija/26.09.2025-arpus-izglitibas-sistemas-15-000-bernu-obligataja-skolas-vecuma-kapec-ta.a615603/
- LSM, OECD on completion, October 5, 2022: https://www.lsm.lv/raksts/zinas/latvija/oecd-studenti-latvija-biezi-nepabeidz-augstskolu.a476744/
- Ministry release on higher education statistics: https://lvportals.lv/dienaskartiba/379021-augstakas-izglitibas-latvija-statistika-2024-pieaug-studejoso-skaits-un-pieejams-vairak-valsts-budzeta-vietu-2025
- Welfare ministry, NVA training results 2025: https://www.lm.gov.lv/lv/media/35629/download
- State Audit Office release on adult education: https://lvportals.lv/dienaskartiba/357445-valsts-kontroles-zinojums-par-valsts-atbalstu-pieauguso-izglitiba-nodrosinats-parsvara-labi-izglitotiem-cilvekiem-2023

---

# Stage 3 findings: causes

Done 2026-11-24. Marks as before.

## Result

The gate passes for early leaving and fails for mathematics. Two ministry-commissioned
surveys measure lack of motivation as the leading reason young people give for leaving
school, vocational schools included. No source measures a belief about ability among
those who leave or fail, and the sources on mathematics failure name knowledge gaps and
untaught lessons. The evidence supports "motivation", a wider thing than mindset, and it
is ten years old.

| Failure | Measured belief or motivation cause? | Gate |
|---|---|---|
| F1 early leaving, mostly vocational | Yes: motivation, self-reported by leavers, 2015 | Passes, on motivation only |
| F3 mathematics failure | No. PISA shows the belief in the population, not among those who fail | Fails; to `scan.md` unlabelled unless stage 4 or a dataset changes this |
| F2 university dropout | No source read | On hold |

## Ledger

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Early leavers aged 15 to 20 who name lack of motivation among their reasons | 33%, the most frequent of nearly 20 reasons | Words (survey) | Ministry-commissioned survey of 318 early leavers, fieldwork September 15 to October 4, 2015 | [P] |
| Leavers who name it as the main reason | 15%, again the most frequent; then wish to start paid work 13%, pregnancy or marriage 12%, dislike of learning 12% | Words (survey) | Same | [P] |
| Leavers who say they disliked learning and found school boring | 27% | Words (survey) | Same | [P] |
| Lack of motivation, boys against girls | 39%; 25% | Words (survey) | Same | [P] |
| Lack of motivation among leavers aged 17 to 18 | 44% | Words (survey) | Same | [P] |
| Dislike of particular subjects, boys against girls | 25%; 16% | Words (survey) | Same | [P] |
| Leavers who rate their own grades as poor | 59 of 318 | Words (survey) | Same | [P] |
| School administrators' ranking of reasons for leavers' absences | Lack of motivation first, parental indifference second, in grades 7 to 9, grades 10 to 12, and vocational schools alike | Words (survey) | Ministry-commissioned survey of 382 schools on 2013/14, by the Baltic Institute of Social Sciences | [P] |
| Leavers those schools counted | 1,217, of whom 891 from vocational schools; 62% boys; 86% aged 16 to 19 | Risk | Same | [P] |
| Children helped by *PuMPuRS* in 2023 whose risk lay in schoolwork or the school | 80% | Risk | LSM, December 5, 2023, quoting the project's expert | [R] |
| Individual support plans written over the project | Nearly 86,000 | Size | Same | [R] |
| One distance-learning school, 2024/25 | 99 pupils failed the mathematics exam, half the previous year's count; 124 finished grade 12 without a certificate against 398 with one | Risk | The school's self-assessment, October 31, 2025 | [P] |

## What the sources say causes each failure

**Early leaving.** The leavers themselves name motivation first, then paid work, then
dislike of learning. The report's own conclusion is that no single factor dominates: the
top main reason holds 15%. Administrators agree on motivation and add parental
indifference. The 2023 project data put four in five supported children under
"schoolwork or the school", a category the source leaves undefined.

**Mathematics.** The distance-learning school blames incomplete foundations brought from
earlier schools and coursework marks far above exam marks (gaps of 18% to 50% between
the two in grade 12). Its remedy is a compulsory in-person diagnostic test and compulsory
consultations, and it reports half as many failures the next year. The audit office
blames untaught lessons. Neither names belief. PISA's finding that three in four
15-year-olds think mathematical ability is fixed describes the population, and nothing
links it to the 2,591 who fail.

## Qualifiers

- Motivation in these surveys covers "I saw no point" and "I wanted to earn" as well as
  "I could not do it". Mindset teaching addresses the last only. The surveys do not
  separate them.
- Both surveys predate the 2017 to 2022 prevention project and the curriculum reform.
- The administrators' survey reports opinions about pupils, and only 21 respondents
  answered for vocational schools. I could not match its chart values to categories.
- The 80% figure mixes bases: the article gives shares of children for one category and
  shares of cases for the others.

## Gaps

- The audit office's 2020 audit of vocational education, which may hold dropout causes:
  its server dropped the connection again.
- Any survey of leavers after 2015.
- Belief and score together for Latvia. The public PISA 2022 student file would give the
  score gap by belief, by family income, and by programme type, at the cost of a large
  download and a script.
- Why vocational students fail the exam: no source asked them.

## What this changes

- **The candidate is "vocational students leave without a qualification", and the
  measured lever is motivation.** Mathematics failure joins it as one measured route out
  (879 expelled for failing grades in 2024/25; most of the 1,599 exam failures).
- **The mindset label is unsupported so far.** A brief could honestly say "motivation is
  the most-named cause" and could not say "fixed beliefs about ability cause this".
  Edgar decides whether the idea widens to motivation or the hunt stops here; the plan's
  first early ending applies to mindset in the strict sense.
- **A cost per support plan is within reach for stage 4**: €39.81M [S] over nearly
  86,000 plans [R] is about €460 a plan [C], on two unverified inputs.

## Sources

- Survey of early leavers, 2015 (*Aptauju Centrs* and *Excolo Latvia*): https://www.izm.gov.lv/lv/media/3865/download
- Survey of schools, 2014 (Baltic Institute of Social Sciences): https://izm.gov.lv/lv/media/3868/download
- LSM, December 5, 2023: https://www.lsm.lv/raksts/dzive--stils/vecaki-un-berni/05.12.2023-latvija-macibas-priekslaicigi-pamet-7-bernu-valstij-risinajuma-nav.a532586/
- Rīga 1st Distance Secondary School, self-assessment 2025: https://www.r1tv.lv/uploads/files/dokumenti/Pasnovertejuma_zinojums_2025.pdf
- Kaniņa, I. (2024), early-leaving risk factors in schools, a survey of 195 teachers: https://journals.rta.lv/index.php/SIE/article/download/7906/6685/9779

---

# Stage 4 findings: money

Done 2026-11-24, after Edgar widened the idea from mindset to motivation. The candidate
is "vocational students leave without a qualification". Marks as before.

## Result

Money is tied to this problem, and nearly all of it is EU project money spent on school
staff time. The state's own money shows in three places: a funding formula that
penalises each expulsion, stipends conditional on attendance, and one emergency grant.
The plan's second early ending is close to firing: the buyer of prevention is a
five-year EU project that pays teachers by the hour, with one line open to outside
organisations. The closing evaluation of the previous project measured no effect, which
is the opening and the warning at once.

## Ledger

| Claim | Figure | Kind | Source | Mark |
|---|---|---|---|---|
| Previous project (*PuMPuRS*), eligible spending to its close | €36,131,036.62 | Money | Closing evaluation, 2023 (*Dynamic University*) | [P] |
| Pupils who received support under an individual plan | 42,375; peak 14,499 in 2021/22 | Size | Same | [P] |
| Spent by schools on individual support, 2018/19 to autumn 2022 | €20.5M of €31.9M planned | Money | Same | [P] |
| Mean cost of one individual support measure | €236.60; €183.27 in the last semester | Money | Same | [P] |
| Rate paid for teaching staff time | €12.74 an hour, a unit cost | Money | Same | [P] |
| Economic support: what it bought | Meals 78.7%; public transport 10.2% | Money | Same | [P] |
| Youth projects run by outside organisations | 474 completed | Money | Same | [P] |
| Ceiling per youth project | €4,600 | Money | Search summary of a municipal document | [S] |
| Did it work? | The evaluation made no effectiveness measurement, because no baseline or performance indicators were set before the project | Risk | Same evaluation | [P] |
| Expelled vocational students who continue nowhere | Fell from 4% to 3%; target met | Risk | Same | [P] |
| Parents naming lack of motivation as a leading risk, 2023 survey | 45%; dislike of particular subjects 43%; workload 33% | Words (survey) | Same | [P] |
| The evaluation's verdict on motivation | Impact "medium"; teachers report that low motivation also stops some pupils from taking up the consultations, and that the project failed to reach part of the group | Words | Same | [P] |
| Emergency state grant for extra consultations, autumn 2021 | €1.582M, of which €1.151M for individual consultations | Money | Same | [P] |
| Cost of that evaluation | €80,000 | Money | Same | [P] |
| Current project (*Skola – kopienā*), September 2024 to August 2029 | €15,951,890, of which €13,559,106 EU | Money | Exam agency (VIAA) slides, March 31, 2025 | [P] |
| Its budget for individual plans | €4,680,000 | Money | Same | [P] |
| Mentors for pupils at risk from age 13, February 2026 to May 2027 | €1,073,066.40 for a result of 696 | Money | Same | [P] |
| Per unit of that result | About €1,540 | Money | 1,073,066.40 ÷ 696; the slide leaves the unit unnamed | [C] |
| Consultations for pupils repeating grade 9 or admitted to vocational school without a certificate | €860,418.72 for a result of 596 | Money | Same slides | [P] |
| Initiative projects open to schools and community partners, to 2028 | 300 projects, €2,100,000 | Money | Same | [P] |
| Per initiative project | €7,000 | Money | 2,100,000 ÷ 300 | [C] |
| Partners' own share from 2026/27 | 15% co-financing | Money | Ministry release, August 18, 2026 | [R] |
| Base funding per vocational student per year | €502.46 times a field coefficient of 1.00 to 3.20, before teacher pay and stipend | Money | Cabinet Regulation 655, version of November 22, 2024 | [R] |
| Effect of an expulsion on a school's funded headcount | Each expelled student subtracts 0.6 of a student for the budget year | Money | Same, annex 1 formula | [R] |
| Base funding at stake across 2024/25 expulsions | At least €1.27M | Money | 4,207 × 0.6 × 502.46, at the lowest coefficient, teacher pay excluded | [C] |
| Stipend for vocational students | €15 a month minimum, up to €150; set twice a year from grades and conduct; unexcused absence costs the higher stipend | Money | Ombudsman's letter to the ministry, January 16, 2025 | [P] |

## Who pays, and for what

- **The EU project** pays for teacher consultations, support staff, mentors, and
  initiative projects. It is the only buyer of prevention at scale, and it is shrinking:
  €36.1M over six years became €16.0M over five.
- **The vocational school** loses funded headcount with each expulsion. The loss is
  real and small in base funding; the teacher-pay share, which the formula also scales
  by headcount, is the larger part and I could not price it.
- **The state** pays stipends that already work as a motivation payment. The ombudsman
  calls the higher stipend both a motivation and support that can decide whether a
  pupil stays.
- **Municipalities** will carry 15% of partner costs from 2026/27.

## What an outside seller could reach

- Initiative projects: €7,000 each, 300 of them, through schools and municipalities.
- Mentoring: delivered by adults trained on the project's own 36-hour course and
  selected with municipalities. The slides show no outside provider.
- Everything else is school staff paid by the hour.

## Qualifiers

- The mentor and consultation lines give a "result" count without naming its unit. If
  it counts pupils, mentoring costs about €1,540 a pupil; if it counts something else,
  the figure is meaningless.
- The fall from 4% to 3% happened during the project. The evaluation claims no causal
  link, and says it could not measure one.
- The regulation was read through a fetch agent from a cached page; later amendments
  are unchecked.

## Gaps

- The procurement run the plan called for. The e-tender file used on November 16 is no
  longer on disk, so I did not rerun the scripts for education and training services.
- The stipend budget in total, and teacher-pay funding per vocational student.
- Whether any vocational school has bought a motivation or mentoring programme with its
  own money.

## What this means for the next stage

- **The second early ending half-fires.** Prevention is bought with EU project money
  that ends in 2029. State money is tied to the failure (formula, stipends) but buys no
  programme.
- **The ceiling test now has prices to beat**: €236.60 a support measure, about €1,540
  a mentored pupil if the unit is pupils, €7,000 an initiative project.
- **The sharpest finding is the missing measurement.** €36M was spent with no measure
  of effect, and the evaluator says so. A product that measures whether support changes
  attendance or grades answers a named gap; a motivation course is one more unmeasured
  support.

## Sources

- Closing evaluation of *PuMPuRS*: https://ikvd.gov.lv/lv/media/4926/download
- VIAA slides on *Skola – kopienā*, March 31, 2025: https://izm.gov.lv/lv/media/27731/download
- Ministry release, August 18, 2026: https://lvportals.lv/dienaskartiba/393345-savlaicigs-atbalsts-berniem-un-papildu-iespejas-skolotajiem-projekta-skola-kopiena-2026
- EU funds page on the project: https://www.esfondi.lv/en/implemented-projects/inspirational-stories/school-within-the-community
- Cabinet Regulation 655: https://likumi.lv/ta/id/164266
- Ombudsman's letter on stipends: https://www.tiesibsargs.lv/wp-content/uploads/2026/03/par_stipendijam-1.pdf
