"""L-02: software-service orders in the state e-catalogues (CI118P and CI126P), 2025-2026.

Input: state e-procurement system open data on e-catalogue orders, data.gov.lv dataset
"Pirkuma pasūtījumu datu grupa", files EIS_E_PASUT_APST_2025.csv and _2026.csv.
Run: uv run --with duckdb python -I it_catalogue_orders.py <2025.csv> <2026.csv>

Checks built in: totals are printed two ways (line sum, and line sum times quantity)
so they can be reconciled with the official totals on slide 7 of the Information
Society Council deck of July 27, 2026 (2025: EUR 56,662,213.59 from 197 buyers).
Suppliers are identified by coalesce(registration number, name).
"""
import sys
import duckdb

con = duckdb.connect()
con.execute(f"""CREATE TABLE r AS SELECT * FROM read_csv(['{sys.argv[1]}','{sys.argv[2]}'],
    sample_size=300000, ignore_errors=true, all_varchar=true, union_by_name=true)""")
con.execute("""CREATE TABLE o AS SELECT Kataloga_numurs cat, Kataloga_nosaukums catname, Pasutijuma_Nr ord,
    Pasutijuma_statuss status, Pasutitajs buyer, Augstak_stavosa_organizacija parent,
    coalesce(nullif(trim(Piegadataja_registracijas_numurs),''), Piegadatajs) sup, Piegadatajs supname,
    try_strptime(Pasutijuma_apstiprinasanas_datums, '%d.%m.%Y') d,
    try_cast(replace(Summa_bez_PVN, ',', '.') AS double) amt,
    try_cast(replace(Pasutitais_skaits, ',', '.') AS double) qty,
    Pasutitas_preces_nosaukums item
    FROM r WHERE Kataloga_numurs IN ('CI118P','CI126P')""")
out = []

def q(title, sql):
    out.append("== " + title)
    for r in con.execute(sql).fetchall():
        out.append("  " + " | ".join("" if v is None else str(v) for v in r))

q("all catalogues by year: lines, sum(amt) M", "SELECT right(Pasutijuma_apstiprinasanas_datums,4), count(*), round(sum(try_cast(replace(Summa_bez_PVN, ',', '.') AS double))/1e6,2) FROM r GROUP BY 1 ORDER BY 1")
q("software catalogues: name, lines", "SELECT cat, any_value(catname), count(*) FROM o GROUP BY 1")
q("status values: lines, sum M", "SELECT status, count(*), round(sum(amt)/1e6,2) FROM o GROUP BY 1 ORDER BY 2 DESC")
q("reconciliation by year: lines, orders, buyers, suppliers, sum(amt) M, sum(amt*qty) M, max line",
  "SELECT year(d), count(*), count(distinct ord), count(distinct buyer), count(distinct sup), round(sum(amt)/1e6,3), round(sum(amt*qty)/1e6,3), max(amt) FROM o GROUP BY 1 ORDER BY 1")
q("2026 through July 31: buyers, sum M", "SELECT count(distinct buyer), round(sum(amt)/1e6,3) FROM o WHERE d>='2026-01-01' AND d<'2026-08-01'")
q("monthly: month, orders, buyers, sum M, orders over 140k, their sum M",
  """WITH x AS (SELECT strftime(d,'%Y-%m') m, ord, any_value(buyer) b, sum(amt) s FROM o GROUP BY 1,2)
     SELECT m, count(*), count(distinct b), round(sum(s)/1e6,2), sum((s>140000)::int), round(sum(CASE WHEN s>140000 THEN s ELSE 0 END)/1e6,2) FROM x GROUP BY 1 ORDER BY 1""")
for y in (2025, 2026):
    q(f"{y} top 15 suppliers: sum M, share %, cumulative %, buyers",
      f"""WITH x AS (SELECT sup, any_value(supname) nm, sum(amt) s, count(distinct buyer) nb FROM o WHERE year(d)={y} GROUP BY 1)
          SELECT nm, round(s/1e6,2), round(100*s/sum(s) OVER (),1), round(100*sum(s) OVER (ORDER BY s DESC)/sum(s) OVER (),1), nb FROM x ORDER BY s DESC LIMIT 15""")
    q(f"{y} top 12 buyers: sum M, share %, suppliers used, top supplier share of that buyer %",
      f"""WITH bs AS (SELECT buyer, sup, sum(amt) s FROM o WHERE year(d)={y} GROUP BY 1,2),
          b AS (SELECT buyer, sum(s) t, count(*) ns, max(s) mx FROM bs GROUP BY 1)
          SELECT buyer, round(t/1e6,2), round(100*t/sum(t) OVER (),1), ns, round(100*mx/t,1) FROM b ORDER BY t DESC LIMIT 12""")
q("2025 buyers by supplier count (buyers spending over 140k in the year): buyers with 1 supplier, 2-3, 4+; and share of their spend going to the top supplier (median)",
  """WITH bs AS (SELECT buyer, sup, sum(amt) s FROM o WHERE year(d)=2025 GROUP BY 1,2),
     b AS (SELECT buyer, sum(s) t, count(*) ns, max(s)/sum(s) topshare FROM bs GROUP BY 1 HAVING sum(s)>140000)
     SELECT count(*), sum((ns=1)::int), sum((ns BETWEEN 2 AND 3)::int), sum((ns>=4)::int), round(100*median(topshare),1), round(sum(t)/1e6,2) FROM b""")
q("2025 by item type (name contains 'izstrād' = development): lines, sum M",
  "SELECT CASE WHEN item ILIKE '%izstrād%' THEN 'development' ELSE 'other (product services, support, testing)' END, count(*), round(sum(amt)/1e6,2) FROM o WHERE year(d)=2025 GROUP BY 1")
q("2025 the cliff: buyers whose development spend exceeded 140k; their development spend M; the part above 140k each M",
  """WITH b AS (SELECT buyer, sum(amt) t FROM o WHERE year(d)=2025 AND item ILIKE '%izstrād%' GROUP BY 1)
     SELECT sum((t>140000)::int), round(sum(CASE WHEN t>140000 THEN t ELSE 0 END)/1e6,2), round(sum(greatest(t-140000,0))/1e6,2), count(*), round(sum(t)/1e6,2) FROM b""")
q("2025 same, all software-catalogue spend",
  """WITH b AS (SELECT buyer, sum(amt) t FROM o WHERE year(d)=2025 GROUP BY 1)
     SELECT sum((t>140000)::int), round(sum(CASE WHEN t>140000 THEN t ELSE 0 END)/1e6,2), round(sum(greatest(t-140000,0))/1e6,2) FROM b""")
q("2025 development lines: hours and implied hourly rate (amt/qty): median, p10, p90, total hours",
  "SELECT round(median(amt/qty),1), round(quantile_cont(amt/qty,0.1),1), round(quantile_cont(amt/qty,0.9),1), round(sum(qty)) FROM o WHERE year(d)=2025 AND item ILIKE '%izstrād%' AND qty>0")
q("freeze effect, June-October: year, orders, sum M, orders over 140k",
  """WITH x AS (SELECT year(d) y, ord, sum(amt) s FROM o WHERE month(d) BETWEEN 6 AND 10 GROUP BY 1,2)
     SELECT y, count(*), round(sum(s)/1e6,2), sum((s>140000)::int) FROM x GROUP BY 1 ORDER BY 1""")
q("orders over 140k since 2026-06-15: date, buyer, supplier, sum",
  """SELECT min(d)::date, any_value(buyer), any_value(supname), round(sum(amt)) FROM o WHERE d>='2026-06-15' GROUP BY ord HAVING sum(amt)>140000 ORDER BY 1""")
q("twenty sampled lines 2025: buyer, supplier, item, amt, qty",
  "SELECT left(buyer,35), left(supname,28), left(item,60), amt, qty FROM (SELECT * FROM o WHERE year(d)=2025 ORDER BY hash(ord||item) LIMIT 20)")
sys.stdout.buffer.write("\n".join(out).encode("utf-8", "replace"))
