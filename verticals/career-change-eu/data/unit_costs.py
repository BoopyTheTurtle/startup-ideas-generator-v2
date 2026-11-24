"""Unit costs of state-funded career counselling, computed from figures in candidates.md.

Run: python -I unit_costs.py
Each input is a figure read in the cited source; see the ledger for marks.
"""
ROWS = [
    # label, amount, count, currency
    ("FR counselling for employed adults, 2024 (France compétences)", 90.96e6, 190_488, "EUR"),
    ("FR counselling for employed adults, 2023 (France compétences)", 72.99e6, 176_288, "EUR"),
    ("UK National Careers Service, 2023-24 (FE Week figures, secondary)", 55e6, 328_998, "GBP"),
]
for label, amount, count, currency in ROWS:
    print(f"{label}: {amount / count:,.0f} {currency} per entry")

# Netherlands: 68,000 development-advice tracks at a fixed EUR 700 subsidy (SEO, 2024).
print(f"NL development advice, total subsidy: EUR {68_000 * 700 / 1e6:.1f}M")
# France: assessments are 6% of 1.391M dossiers at EUR 1,945 average (CDC and France compétences).
dossiers = 0.06 * 1_391_000
print(f"FR assessments, 2024: about {dossiers:,.0f} dossiers, EUR {dossiers * 1945 / 1e6:.0f}M (share rounded to 6%, so +/- 8%)")
