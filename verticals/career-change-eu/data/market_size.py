"""Size of paid career-advice markets, and a per-adult scaling to the Baltics.

Run: python -I market_size.py
Spend figures are those in candidates.md (marks there). Population is Eurostat
lfsa_pganws, ages 25 to 64, 2024, thousands. The Baltic line is an illustration of
scale under a stated assumption, not evidence of spending.
"""
import json
import urllib.request

API = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_pganws"
       "?lang=EN&time=2024&sex=T&age=Y25-64&wstatus=POP&citizen=TOTAL&unit=THS_PER&geo={}")


def adults(geo):
    with urllib.request.urlopen(API.format(geo)) as response:
        data = json.load(response)
    return next(iter(data["value"].values())) * 1000


# Yearly state spend on career assessment and counselling for adults, EUR.
FR_ASSESSMENTS = 0.06 * 1_391_000 * 1945   # CDC 2024: share, dossiers, average cost
FR_COUNSELLING = 90.96e6                    # France compétences 2024, employed adults only
DE_ACTIVATION = 874.6e6                     # IAB 2025: provider measures, joint job centres, 2024
DE_ENTRIES = 436_400

pop = {geo: adults(geo) for geo in ("FR", "DE", "EE", "LV", "LT")}
baltic = pop["EE"] + pop["LV"] + pop["LT"]

fr_total = FR_ASSESSMENTS + FR_COUNSELLING
fr_per_adult = fr_total / pop["FR"]
print(f"France, assessments + counselling for the employed: EUR {fr_total/1e6:.0f}M, "
      f"EUR {fr_per_adult:.2f} per adult aged 25-64")
print(f"Germany, provider-run activation in job centres: EUR {DE_ACTIVATION/1e6:.0f}M, "
      f"EUR {DE_ACTIVATION/DE_ENTRIES:,.0f} per entry (a ceiling: most of it is not career advice)")
for geo in ("EE", "LV", "LT"):
    print(f"{geo}: {pop[geo]/1e3:,.0f} thousand adults; at France's rate EUR {pop[geo]*fr_per_adult/1e6:.1f}M a year")
print(f"Baltics together: {baltic/1e6:.2f}M adults; at France's rate EUR {baltic*fr_per_adult/1e6:.1f}M a year")
