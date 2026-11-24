# Worked example: building permit applications bounce for incompleteness

Brief 0, written 2026-11-16 to test the method. One session, about 25 searches and page
reads. Grade it: junk, plausible, or worth testing.

Verification marks: **[P]** means I read the primary source; **[S]** means I have only a
search summary or secondary report, and the claim needs a check before anyone relies on it.

## The problem

German architects file building permit applications that the authority sends back as
incomplete, and each round costs weeks. The failure is measured, recurring, and
acknowledged by both sides.

## Who has it

The architect who signs the application (the *bauvorlageberechtigter Entwurfsverfasser*)
has it first: German law requires one on almost every application. Germany had about
142,000 chamber-registered architects and planners in 2023, 54,000 of them self-employed
[S], and most offices are a single person [S]. The developer or owner waiting on the
permit carries the delay cost. The permit authority carries the handling cost.

## The workflow and where it breaks

An application is a package: forms, a building description, calculations, a site plan,
and drawings, with contents that vary by state (16 building codes), by procedure type,
and by the habits of the local authority. The architect assembles it by hand against
checklists. The authority checks completeness first and reviews substance only once the
package is complete.

- In Dortmund, 64% of applications arrive incomplete, completing them takes 50 days on
  average, and more than half of the incomplete ones end automatically because the
  applicant misses deadlines or repairs the package badly. The permit takes 233 days on
  average from receipt; substantive review takes 67 of them. The missing items are
  forms, building descriptions, calculations, site plans, and drawings. [P] (City of
  Dortmund, October 7, 2026)
- In a national survey of chamber members (15,659 respondents, 2023), requests for
  missing documents reached the architect 3 to 5 weeks after filing in 42% of cases and
  later than 5 weeks in 41%. Digital filing did not reduce those requests (3.6 on a scale
  where 5 means "does not apply at all"). About half of permit-authority staff named
  better application documents as a precondition for faster permits. [P]
  (Bundesarchitektenkammer, *Berufspolitische Befragung 2023*, part 8)
- England shows the same failure under a different regime: of 639 high-rise building
  control applications the Building Safety Regulator closed between December 2025 and
  February 2026, 273 were invalidations. [S]

## What it costs now

The evidence proves lost time and risk. It does not yet prove that anyone pays money to
avoid the problem, which is the gap in this brief.

| Kind | Evidence | Mark |
|---|---|---|
| Time | 50 days to complete a package; a first request for documents usually 3+ weeks after filing | [P] |
| Risk | More than half of incomplete Dortmund applications terminate; the applicant refiles and pays fees again | [P] |
| Volume | About 300,000 building applications a year in Germany, 130,000 filed digitally in 2025 | [S] |
| Money, public side | A federal pilot tests AI in the permit procedure; Bavaria wants AI-supported completeness and plausibility checks and notes that its portal lacks an upstream check | [S] |
| Money, private side | None found. A search for job postings and paid pre-check services returned nothing usable | gap |

## How they cope today

Architects use the authority's checklists, pre-application meetings (Dortmund is
expanding them), and experience with the local office. I found no paid tool or service
in Germany that checks a package before filing.

## Who already sells a fix

| Company | What it does | Why it leaves room | Mark |
|---|---|---|---|
| Struck (Amsterdam, €2M seed, November 2025) | Dutch building-rule lookup and permit-exemption checker for architects, developers, municipalities | Netherlands only; checks rules, not package completeness | [P] |
| Freeda (Paris, €3.4M) | AI review of construction plans | Plan content, not permit packages; German coverage unknown | [S] |
| Arkyv (Stockholm, €700k), Davis (€4.6M) | Code-aware design assistants | Design stage, not filing | [S] |
| State portals and federal pilot | May add completeness checks to the filing portal itself | A built-in check would remove the need for a product | [S] |

Investors fund the neighbourhood, and no one found sells this check in Germany.

## Why now

Digital filing puts the package in machine-readable form: Wiesbaden has accepted only
digital applications since December 1, 2025 [S]. Language models can read heterogeneous
PDFs and plans against a written checklist, which rule-based software could not do. Since
September 2026, authorities in the simplified procedure have one month to respond [P],
which raises the authority's own interest in complete packages.

## EU angle

Permit rules are national or regional everywhere, so the product is built country by
country and competitors from elsewhere arrive slowly. Germany is the largest market in
the EU for it. Whether the failure rate is as high in other member states is unknown; I
checked only Germany and England.

## Solution directions

1. **Pre-filing check for architects.** Upload the package, pick state and procedure,
   get a list of missing and defective items before the authority sees it.
2. **Check as a service.** A fixed fee per application, done by a person with model
   support. It needs no product and tests willingness to pay within weeks.
3. **Intake triage for authorities.** The same check sold to the permit office. Public
   budgets exist, sales are slow, and state portals compete.
4. **Reply assistant.** Turns the authority's request for documents into a task list and
   a corrected package, attacking the 50 days rather than the 64%.
5. **Permit-risk tracker for developers.** Sold to the party that pays for delay.

## The weakest points

1. **Architects may file incomplete on purpose.** Filing early secures a place in the
   queue, and the request for documents then serves as a free checklist. If so, the 64%
   measures a tactic, not a failure, and no architect buys a fix. Ten conversations
   settle this.
2. **The portal may absorb the product.** Bavaria has said it wants the check in its own
   portal. A state that ships it removes that state's market.
3. **The payer is unclear.** The architect loses unbilled hours; the developer loses
   months. Neither has been shown to pay for prevention.
4. **Local variation is the work.** Sixteen codes and hundreds of authority habits make
   the rule base expensive to build and maintain.
5. **One city carries the headline number.** Dortmund publishes its figures; others may
   differ. The national survey supports the pattern, not the 64%.

## Kill criteria

Drop the brief if any of these holds:

- Six of ten architects say they file incomplete deliberately or see no cost in it.
- Two of the four largest states have a completeness check live in their filing portal,
  or funded and scheduled for 2027.
- No architect or developer among ten names a price above €100 per application.

## My own grade

Plausible, one step short of worth testing. The time and risk evidence is strong and
primary. The private-money evidence is missing, and weak point 1 could kill the brief in
a week of conversations. That check is the next step, and it costs nothing.

## Sources

- City of Dortmund, "Neue Konzepte, mehr Service: So wird Bauen in Dortmund schneller," October 7, 2026: https://www.dortmund.de/newsroom/nachrichten-dortmund.de/neue-konzepte-mehr-service-so-wird-bauen-in-dortmund-schneller.html
- Bundesarchitektenkammer, *Berufspolitische Befragung 2023*, part 8: https://bak.de/wp-content/uploads/2023/10/2023_BAK_Berufspolitische-Befragung_Bericht-08_Erfahrungen-mit-Baugenehmigungsbehoerden_FINAL.pdf
- Federal government, interim report on modernisation, June 26, 2026: https://www.bundesregierung.de/resource/blob/2196306/2445316/7924b375c665208836fc6487aed5d922/2026-06-26-zwischenbericht-modernisierung-data.pdf
- Bavarian Landtag, Drucksache on AI in permit procedures: https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Basisdrucksachen/0000009500/0000009599.pdf
- Building Safety Regulator, building control approval application data: https://www.gov.uk/government/publications/building-safety-regulator-building-control-approval-application-data-january-to-march-2026/building-safety-regulator-building-control-approval-application-data-january-to-march-2026
- tech.eu on Struck, November 6, 2025: https://tech.eu/2025/11/06/struck-raises-eur2-million-to-simplify-building-compliance-with-ai/
- Vestbee on Freeda: https://vestbee.com/blog/articles/freeda-raises-3-4-m
- Chamber statistics as of January 1, 2023: https://www.AKSachsen.org/fileadmin/Image_Archive/Berufspolitik/Statistik_und_Umfragen/Bundeskammerstatistik_zum_01.01.2023_gesamt_bearb_sch.pdf
- Wiesbaden building authority, digital filing: https://www.wiesbaden.de/leben-in-wiesbaden/wohnen-bauen/bauaufsicht/bauberatung/antragsannahme
