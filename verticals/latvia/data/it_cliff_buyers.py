"""L-02: have the buyers who hit the 2027 catalogue cap run open software tenders?

Inputs: e-catalogue orders 2025 (EIS_E_PASUT_APST_2025.csv) and bid openings 2025
(atv2025.csv), both from the state e-procurement system's open data on data.gov.lv.
Run: uv run --with duckdb python -I it_cliff_buyers.py <orders2025.csv> <atv2025.csv>

Buyers are matched by registration number. "Software lots" are lots whose main CPV code
starts with 722 (software programming and consultancy). A buyer with no 2025 software
lot may still have tendered in other years; this is one year only.
"""
import sys
import duckdb

con = duckdb.connect()
con.execute(f"CREATE TABLE r AS SELECT * FROM read_csv('{sys.argv[1]}', sample_size=300000, ignore_errors=true, all_varchar=true)")
con.execute(f"CREATE TABLE a AS SELECT * FROM read_csv('{sys.argv[2]}', sample_size=200000, ignore_errors=true, all_varchar=true)")
con.execute("""CREATE TABLE cb AS SELECT trim(Pasutitaja_registracijas_numurs) reg, any_value(Pasutitajs) buyer,
    sum(try_cast(replace(Summa_bez_PVN, ',', '.') AS double)) dev
    FROM r WHERE Kataloga_numurs IN ('CI118P','CI126P') AND Pasutitas_preces_nosaukums ILIKE '%izstrād%'
    GROUP BY 1 HAVING dev > 140000""")
con.execute("""CREATE TABLE tl AS SELECT trim(Pasutitaja_registracijas_numurs) reg, Iepirkuma_ID pid,
    coalesce(Iepirkuma_dalas_numurs,'0') part,
    count(distinct nullif(trim(coalesce(Pretendenta_registracijas_numurs, Pretendenta_nosaukums)),'')) n
    FROM a WHERE CPV_kods_galvenais_prieksmets LIKE '722%' GROUP BY 1,2,3""")
out = []
def q(title, sql):
    out.append("== " + title)
    for r in con.execute(sql).fetchall():
        out.append("  " + " | ".join("" if v is None else str(v) for v in r))
q("cap-hit buyers: count, blank reg numbers", "SELECT count(*), sum((reg IS NULL OR reg='')::int) FROM cb")
q("all software lots (CPV 722) in 2025: lots, buyers, one-bid %", "SELECT count(*), count(distinct reg), round(100.0*sum((n=1)::int)/count(*),1) FROM tl")
q("cap-hit buyers: with zero / 1-2 / 3+ software lots in 2025",
  """WITH x AS (SELECT cb.reg, count(tl.pid) k FROM cb LEFT JOIN tl USING (reg) GROUP BY 1)
     SELECT sum((k=0)::int), sum((k BETWEEN 1 AND 2)::int), sum((k>=3)::int), sum(k) FROM x""")
q("per cap-hit buyer: catalogue development spend M, software lots tendered, of which one bid",
  """SELECT cb.buyer, round(cb.dev/1e6,2), count(tl.pid), coalesce(sum((tl.n=1)::int),0) FROM cb LEFT JOIN tl USING (reg) GROUP BY 1,2 ORDER BY 2 DESC""")
sys.stdout.buffer.write("\n".join(out).encode("utf-8", "replace"))
