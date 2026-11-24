"""L4: selected and spent shares by member state, and by intervention field for Latvia.
Inputs (cohesiondata.ec.europa.eu, dataset 3git-md5z, read 2026-11-16):
 1. $select=ms,tod_cycle,sum(total_amount) as planned,sum(total_eligiblecost_of_selectedoperations) as decided,
    sum(totalspendeligibleexpenditure_declared) as spent; $where dimension_type=Intervention Field and tod_cycle in
    (202512,202606,202608); $group=ms,tod_cycle
 2. same sums for ms=LV, tod_cycle=202608, grouped by category_code, category_short_title, fund
Run: python eu_funds_selected_spent.py ms_cycle.json lv_cat.json
"""
import json,sys
f=lambda v: float(v or 0)
d=json.load(open(sys.argv[1],encoding='utf-8'))
o=[]
cyc=sorted({x['tod_cycle'] for x in d})
o.append("cycles: "+str({c:sum(1 for x in d if x['tod_cycle']==c) for c in cyc}))
for c in cyc:
    rows=[x for x in d if x['tod_cycle']==c and f(x['planned'])>0]
    tp=sum(f(x['planned']) for x in rows); td=sum(f(x['decided']) for x in rows); ts=sum(f(x['spent']) for x in rows)
    o.append(f"== {c}: {len(rows)} MS; ALL planned {tp/1e9:.1f}bn decided {td/tp*100:.1f}% spent {ts/tp*100:.1f}%")
    rows.sort(key=lambda x:-f(x['spent'])/f(x['planned']))
    for i,x in enumerate(rows,1):
        if x['ms'] in ('LV','LT','EE') or i<=3 or i>len(rows)-2:
            o.append(f"  {i:2} {x['ms']} planned {f(x['planned'])/1e9:6.2f}bn decided {f(x['decided'])/f(x['planned'])*100:5.1f}% spent {f(x['spent'])/f(x['planned'])*100:5.1f}%")
l=json.load(open(sys.argv[2],encoding='utf-8'))
agg={}
for x in l:
    k=(x['category_code'],x['category_short_title']); a=agg.setdefault(k,[0,0,0]); a[0]+=f(x['planned']); a[1]+=f(x['decided']); a[2]+=f(x['spent'])
tp=sum(a[0] for a in agg.values()); o.append(f"== LV 202608 by intervention field, total planned {tp/1e9:.2f}bn decided {sum(a[1] for a in agg.values())/tp*100:.1f}% spent {sum(a[2] for a in agg.values())/tp*100:.1f}%")
for k,a in sorted(agg.items(), key=lambda kv:-kv[1][0])[:45]:
    o.append(f"  {k[1][:70]:70} plan {a[0]/1e6:7.1f}M dec {a[1]/a[0]*100 if a[0] else 0:5.1f}% spent {a[2]/a[0]*100 if a[0] else 0:5.1f}%")
sys.stdout.buffer.write("\n".join(o).encode('utf-8','replace'))
