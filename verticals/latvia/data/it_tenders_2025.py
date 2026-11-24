"""L4: competition in IT-service tenders (CPV division 72), Latvia, bids opened in 2025.

Input: state e-procurement system open data on bid openings, 2025 (atv2025.csv).
Run: uv run --with duckdb python -I it_tenders_2025.py <path-to-atv2025.csv>

Notes. Bidder identity is coalesce(registration number, name), because the data blanks
the number for private individuals (the bug found in brief L-01). Purchases made through
the system's e-catalogues do not appear in this file, and those are the purchases the
2026 moratorium is about, so this shows the tendered part of state IT buying only.
"""
import sys
import duckdb

con = duckdb.connect()
con.execute(f"""CREATE TABLE a AS SELECT * FROM read_csv('{sys.argv[1]}',
    sample_size=200000, ignore_errors=true, all_varchar=true)""")
con.execute("""CREATE TABLE b AS SELECT Iepirkuma_ID AS pid, coalesce(Iepirkuma_dalas_numurs,'0') AS part,
    Pasutitaja_nosaukums AS buyer, left(CPV_kods_galvenais_prieksmets,2) AS div,
    left(CPV_kods_galvenais_prieksmets,60) AS cpv,
    try_cast(coalesce(Dalas_planota_ligumcena, Planota_ligumcena) AS double) AS planned,
    nullif(trim(coalesce(Pretendenta_registracijas_numurs, Pretendenta_nosaukums)),'') AS bidder,
    Pretendenta_nosaukums AS bname FROM a""")
con.execute("""CREATE TABLE lots AS SELECT pid, part, any_value(buyer) buyer, any_value(div) div,
    any_value(cpv) cpv, any_value(planned) planned, count(distinct bidder) n FROM b GROUP BY 1,2""")
out = []

def q(title, sql):
    out.append("== " + title)
    for r in con.execute(sql).fetchall():
        out.append("  " + " | ".join("" if v is None else str(v) for v in r))

q("IT lots (div 72) vs all: lots, no bid %, one bid %, median bidders, buyers",
  """SELECT CASE WHEN div='72' THEN 'IT 72' ELSE 'other' END, count(*),
     round(100.0*sum((n=0)::int)/count(*),1), round(100.0*sum((n=1)::int)/count(*),1),
     median(n), count(distinct buyer) FROM lots GROUP BY 1""")
q("IT lots by planned value band: lots, one bid %",
  """SELECT CASE WHEN planned IS NULL THEN 'unknown' WHEN planned<42000 THEN '<42k'
     WHEN planned<140000 THEN '42-140k' WHEN planned<1000000 THEN '140k-1M' ELSE '>=1M' END,
     count(*), round(100.0*sum((n=1)::int)/count(*),1) FROM lots WHERE div='72' GROUP BY 1 ORDER BY 2 DESC""")
q("IT lots by CPV code (top 12): lots, one bid %",
  "SELECT cpv, count(*), round(100.0*sum((n=1)::int)/count(*),1) FROM lots WHERE div='72' GROUP BY 1 ORDER BY 2 DESC LIMIT 12")
q("distinct bidders in IT lots; bidders seen in one IT lot only",
  """WITH x AS (SELECT bidder, count(distinct pid||'/'||part) k FROM b WHERE div='72' AND bidder IS NOT NULL GROUP BY 1)
     SELECT count(*), sum((k=1)::int) FROM x""")
q("top 15 bidders in IT lots: lots bid, of which as sole bidder",
  """WITH x AS (SELECT b.bidder, any_value(b.bname) nm, b.pid, b.part, l.n FROM b JOIN lots l USING (pid, part)
       WHERE b.div='72' AND b.bidder IS NOT NULL GROUP BY b.bidder, b.pid, b.part, l.n)
     SELECT any_value(nm), count(*), sum((n=1)::int) FROM x GROUP BY bidder ORDER BY 2 DESC LIMIT 15""")
q("top 12 buyers of IT lots: lots, one bid %",
  "SELECT buyer, count(*), round(100.0*sum((n=1)::int)/count(*),1) FROM lots WHERE div='72' GROUP BY 1 ORDER BY 2 DESC LIMIT 12")
sys.stdout.buffer.write("\n".join(out).encode("utf-8", "replace"))
