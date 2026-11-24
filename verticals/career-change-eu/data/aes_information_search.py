"""Eurostat Adult Education Survey: who looks for information on learning, and who fails to find it.

Run: python -I aes_information_search.py
Source: Eurostat dissemination API, tables trng_aes_182, trng_aes_186, trng_aes_188.
Scope: EU27 (2020 composition), both sexes, ages 25 to 64.
"""
import itertools
import json
import urllib.request

API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{}?geo=EU27_2020&lang=EN"


def rows(table):
    with urllib.request.urlopen(API.format(table)) as response:
        data = json.load(response)
    dims = data["id"]
    codes = {d: list(data["dimension"][d]["category"]["index"]) for d in dims}
    labels = {d: data["dimension"][d]["category"].get("label", {}) for d in dims}
    for position, combo in enumerate(itertools.product(*(codes[d] for d in dims))):
        value = data["value"].get(str(position))
        if value is None:
            continue
        row = dict(zip(dims, combo))
        if row.get("sex", "T") != "T" or row.get("age", "Y25-64") != "Y25-64":
            continue
        yield {d: labels[d].get(c, c) for d, c in row.items()}, value


def pick(table, key, wanted):
    return {(r[key], r["time"]): v for r, v in rows(table) if r[key] in wanted}


searched = pick("trng_aes_182", "training", {"Total"})
print("Searched for information on learning possibilities, % of adults:")
for (_, year), value in sorted(searched.items(), key=lambda kv: kv[0][1]):
    print(f"  {year}: {value}")

effect = pick("trng_aes_186", "effect", {"Looked for and found", "Looked for but did not find"})
print("Outcome of the search (table ends in 2011), % of adults:")
for year in ("2007", "2011"):
    found = effect[("Looked for and found", year)]
    missed = effect[("Looked for but did not find", year)]
    share = 100 * missed / (found + missed)
    print(f"  {year}: found {found}, did not find {missed}, failed share of searchers {share:.1f}%")

kinds = {
    "Non-formal education and training - job-related and sponsored by the employer",
    "Non-formal education and training - job-related and not sponsored by the employer",
    "Non-formal education and training - not job-related",
}
sponsor = pick("trng_aes_188", "training", kinds)
print("Non-formal learning activities by type, 2022, % of activities:")
for kind in sorted(kinds):
    print(f"  {kind}: {sponsor[(kind, '2022')]}")
