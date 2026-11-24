import duckdb, sys
d = sys.argv[1]
con = duckdb.connect()
def q(title, sql):
    rows = con.execute(sql).fetchall()
    out = "\n== " + title + "\n" + "\n".join("  " + " | ".join(str(x)[:60] for x in r) for r in rows) + "\n"
    sys.stdout.buffer.write(out.encode("utf-8","replace"))
for y in (2024, 2025):
    con.execute(f"""CREATE TABLE a{y} AS SELECT Iepirkuma_ID id, coalesce(Iepirkuma_dalas_numurs,0) part, Pasutitaja_registracijas_numurs buyer,
        Pasutitaja_nosaukums buyer_name, CPV_kods_galvenais_prieksmets cpv, Proceduras_veids proc, Iepirkuma_prieksmeta_veids kind,
        coalesce(Dalas_planota_ligumcena, Planota_ligumcena) planned, coalesce(Pretendenta_registracijas_numurs, Pretendenta_nosaukums) bidder, Pretendenta_valsts country,
        Piedavajumu_atversanas_datums opened
        FROM read_csv('{d}/atv{y}.csv', sample_size=100000, ignore_errors=true)""").fetchall()
    con.execute(f"""CREATE TABLE lot{y} AS SELECT id, part, any_value(buyer) buyer, any_value(cpv) cpv, any_value(proc) proc, any_value(kind) kind,
        any_value(planned) planned, count(DISTINCT bidder) bidders, any_value(bidder) one_bidder FROM a{y} GROUP BY 1,2""").fetchall()
q("trend: year, lots, pct no bid, pct single (of all), median bidders",
  "SELECT 2024, count(*), round(avg((bidders=0)::int)*100,1), round(avg((bidders=1)::int)*100,1), median(bidders) FROM lot2024 UNION ALL SELECT 2025, count(*), round(avg((bidders=0)::int)*100,1), round(avg((bidders=1)::int)*100,1), median(bidders) FROM lot2025")
q("2025 by procedure: proc, lots, pct none, pct single",
  "SELECT proc, count(*), round(avg((bidders=0)::int)*100,1), round(avg((bidders=1)::int)*100,1) FROM lot2025 GROUP BY 1 ORDER BY 2 DESC LIMIT 8")
q("2025 no-bid lots by CPV division (top): div, lots total, no-bid lots, pct",
  "SELECT substr(cpv,1,2), count(*), sum((bidders=0)::int), round(avg((bidders=0)::int)*100,1) FROM lot2025 WHERE cpv IS NOT NULL GROUP BY 1 HAVING count(*)>=150 ORDER BY 4 DESC LIMIT 12")
# incumbency: single-bid lots 2025 where the sole bidder had bid to the same buyer in 2024
con.execute("CREATE TABLE pairs24 AS SELECT DISTINCT buyer, bidder FROM a2024 WHERE bidder IS NOT NULL").fetchall()
con.execute("CREATE TABLE pairs24cpv AS SELECT DISTINCT buyer, bidder, substr(cpv,1,2) div FROM a2024 WHERE bidder IS NOT NULL").fetchall()
q("2025 single-bid lots: n, pct sole bidder bid to same buyer in 2024, pct same buyer+division in 2024",
  """SELECT count(*), round(avg((p.bidder IS NOT NULL)::int)*100,1), round(avg((pc.bidder IS NOT NULL)::int)*100,1)
     FROM lot2025 l LEFT JOIN pairs24 p ON p.buyer=l.buyer AND p.bidder=l.one_bidder
     LEFT JOIN pairs24cpv pc ON pc.buyer=l.buyer AND pc.bidder=l.one_bidder AND pc.div=substr(l.cpv,1,2) WHERE l.bidders=1""")
q("same, by division (>=120 single-bid lots): div, single lots, pct known-to-buyer 2024, planned M",
  """SELECT substr(l.cpv,1,2) div, count(*), round(avg((p.bidder IS NOT NULL)::int)*100,1), round(sum(l.planned)/1e6,1)
     FROM lot2025 l LEFT JOIN pairs24 p ON p.buyer=l.buyer AND p.bidder=l.one_bidder WHERE l.bidders=1 AND l.cpv IS NOT NULL GROUP BY 1 HAVING count(*)>=120 ORDER BY 3""")
q("single-bid lots where sole bidder is NEW to buyer: n, planned M known, median planned",
  """SELECT count(*), round(sum(l.planned)/1e6,1), median(l.planned) FROM lot2025 l LEFT JOIN pairs24 p ON p.buyer=l.buyer AND p.bidder=l.one_bidder WHERE l.bidders=1 AND p.bidder IS NULL""")
q("supplier base 2025: distinct bidders, pct with exactly 1 bid, pct foreign bidders, bids by top 1% of bidders pct",
  """WITH b AS (SELECT bidder, count(*) n, any_value(country) c FROM a2025 WHERE bidder IS NOT NULL GROUP BY 1),
          r AS (SELECT *, row_number() OVER (ORDER BY n DESC) rn, count(*) OVER () tot, sum(n) OVER () allbids FROM b)
     SELECT max(tot), round(avg((n=1)::int)*100,1), round(avg((upper(c) NOT IN ('LATVIJA','LVA','LV'))::int)*100,1),
            round(sum(n) FILTER (WHERE rn<=tot/100)*100.0/max(allbids),1) FROM r""")
q("new bidders: distinct 2025 bidders not seen in 2024, pct", "SELECT count(*), round(avg((b24.bidder IS NULL)::int)*100,1) FROM (SELECT DISTINCT bidder FROM a2025 WHERE bidder IS NOT NULL) b25 LEFT JOIN (SELECT DISTINCT bidder FROM a2024) b24 USING (bidder)")
q("buyers: distinct buyers 2025, lots per buyer median, pct of buyers with >=50% single-or-none lots (min 10 lots)",
  """WITH x AS (SELECT buyer, count(*) n, avg((bidders<=1)::int) s FROM lot2025 GROUP BY 1) SELECT count(*), median(n), round(avg((s>=0.5)::int) FILTER (WHERE n>=10)*100,1), count(*) FILTER (WHERE n>=10) FROM x""")
