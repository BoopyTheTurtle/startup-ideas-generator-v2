import duckdb, sys
d = sys.argv[1]
con = duckdb.connect()
def q(title, sql):
    rows = con.execute(sql).fetchall()
    out = "\n== " + title + "\n" + "\n".join("  " + " | ".join(str(x)[:70] for x in r) for r in rows) + "\n"
    sys.stdout.buffer.write(out.encode("utf-8","replace"))
con.execute(f"CREATE TABLE a AS SELECT * FROM read_csv('{d}/atv2025.csv', sample_size=100000, ignore_errors=true)").fetchall()
con.execute("""
CREATE TABLE lot AS
SELECT Iepirkuma_ID id, coalesce(Iepirkuma_dalas_numurs,0) part,
       any_value(Iepirkuma_prieksmeta_veids) kind,
       any_value(CPV_kods_galvenais_prieksmets) cpv,
       any_value(Proceduras_veids) proc,
       any_value(coalesce(Iepirkuma_dalas_statuss, Iepirkuma_statuss)) status,
       any_value(Iepirkuma_statuss) pstatus,
       any_value(coalesce(Dalas_planota_ligumcena, Planota_ligumcena)) planned,
       any_value(Pasutitaja_nosaukums) buyer,
       min(Piedavajumu_atversanas_datums) opened,
       count(DISTINCT coalesce(Pretendenta_registracijas_numurs, Pretendenta_nosaukums)) bidders,
       count(*) FILTER (WHERE Pretendenta_nosaukums IS NULL) null_rows
FROM a GROUP BY 1,2""").fetchall()
q("lots, null-bidder rows, opened range", "SELECT count(*), sum((bidders=0)::int), min(opened), max(opened) FROM lot")
q("bidders distribution", "SELECT CASE WHEN bidders>=6 THEN 6 ELSE bidders END b, count(*) n, round(count(*)*100.0/sum(count(*)) over (),1) pct FROM lot GROUP BY 1 ORDER BY 1")
q("overall: lots, pct single, mean, median", "SELECT count(*), round(avg((bidders=1)::int)*100,1), round(avg(bidders),2), median(bidders) FROM lot WHERE bidders>0")
q("by kind", "SELECT kind, count(*), round(avg((bidders=1)::int)*100,1) pct1, round(avg(bidders),2), round(sum(planned)/1e6) planned_M FROM lot WHERE bidders>0 GROUP BY 1 ORDER BY 2 DESC")
q("status of procurement", "SELECT pstatus, count(*) FROM lot GROUP BY 1 ORDER BY 2 DESC LIMIT 8")
q("by CPV division (>=150 lots): div, lots, pct single, mean bidders, planned M EUR, single-bid planned M",
  """SELECT substr(cpv,1,2)||' '||substr(any_value(regexp_replace(cpv,'^[0-9-]+ ','')),1,45) div, count(*) n, round(avg((bidders=1)::int)*100,1) pct1, round(avg(bidders),2) mean_b,
            round(sum(planned)/1e6) planned_M, round(sum(planned) FILTER (WHERE bidders=1)/1e6) single_M
     FROM lot WHERE bidders>0 AND cpv IS NOT NULL GROUP BY substr(cpv,1,2) HAVING count(*)>=150 ORDER BY pct1 DESC""")
q("CPV group (5 digits) with >=60 lots, top single-bid",
  """SELECT substr(cpv,1,5) g, substr(any_value(regexp_replace(cpv,'^[0-9-]+ ','')),1,50), count(*) n, round(avg((bidders=1)::int)*100,1) pct1, round(sum(planned)/1e6,1) planned_M
     FROM lot WHERE bidders>0 AND cpv IS NOT NULL GROUP BY 1 HAVING count(*)>=60 ORDER BY pct1 DESC LIMIT 22""")
q("IT (72,48) detail by 5-digit", """SELECT substr(cpv,1,5) g, substr(any_value(regexp_replace(cpv,'^[0-9-]+ ','')),1,50), count(*) n, round(avg((bidders=1)::int)*100,1) pct1, round(sum(planned)/1e6,1)
     FROM lot WHERE bidders>0 AND (cpv LIKE '72%' OR cpv LIKE '48%') GROUP BY 1 HAVING count(*)>=15 ORDER BY n DESC LIMIT 12""")
q("single-bid share by planned size", """SELECT CASE WHEN planned<42000 THEN '1 <42k' WHEN planned<143000 THEN '2 42-143k' WHEN planned<1000000 THEN '3 143k-1M' WHEN planned>=1000000 THEN '4 >1M' ELSE '5 unknown' END b, count(*), round(avg((bidders=1)::int)*100,1) FROM lot WHERE bidders>0 GROUP BY 1 ORDER BY 1""")
