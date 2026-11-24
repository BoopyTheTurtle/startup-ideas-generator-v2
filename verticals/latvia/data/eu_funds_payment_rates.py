"""L4: EU payment rate by member state, 2021-2027 cohesion funds.
Input: https://cohesiondata.ec.europa.eu/resource/ue97-5sq6.json?$limit=5000 saved as JSON (read 2026-11-16).
The field "fund" holds the country code. Run: python eu_funds_payment_rates.py pay_ms.json
"""
import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
rows=sorted(d,key=lambda x:-float(x['eu_payment_rate_actual_plan_eu_amt']))
o=[]
for i,x in enumerate(rows,1):
    o.append(f"{i:2} {x['fund']:5} plan {float(x['actual_plan_eu_amt_latest_adop'])/1e9:7.2f}bn  net paid {float(x['total_net_payments'])/1e9:6.2f}bn  interim {float(x['net_interim_payments'])/1e9:6.2f}bn rate {float(x['eu_payment_rate_actual_plan_eu_amt'])*100:5.1f}%  interim-only {float(x['net_interim_payments'])/float(x['actual_plan_eu_amt_latest_adop'])*100:5.1f}%")
print("\n".join(o))
