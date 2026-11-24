import duckdb
con = duckdb.connect()
con.execute("CREATE TABLE t AS SELECT * FROM 'decp_subset.parquet'")
con.execute("""
CREATE TABLE c AS
WITH base AS (
  SELECT uid,
         any_value(type) type, any_value(codeCPV) cpv,
         min(dateNotification) FILTER (WHERE modification_id=0) d0,
         max(montant) FILTER (WHERE modification_id=0) m0,
         max(modification_id) nmod,
         arg_max(montant, modification_id) mN,
         max(offresRecues) FILTER (WHERE modification_id=0) offres,
         bool_or(montant_anomalie IS NOT NULL) anom,
         bool_or(coalesce(techniques,'') ILIKE '%accord%') ac
  FROM t GROUP BY uid)
SELECT *, mN/m0-1 AS r,
  CASE WHEN type='Travaux' AND (cpv LIKE '4521%' OR cpv LIKE '4526%' OR cpv LIKE '453%' OR cpv LIKE '454%' OR cpv LIKE '4542%' OR cpv LIKE '4500%') THEN 'batiment'
       WHEN type='Travaux' THEN 'autres travaux' ELSE 'moe_712' END seg
FROM base WHERE m0 IS NOT NULL AND m0 BETWEEN 10000 AND 100000000 AND NOT anom AND NOT ac
""")
q = lambda s: con.execute(s).fetchall()
print("N by seg, notified 2019-2023:")
for row in q("""
SELECT seg, count(*) n, round(avg((nmod>0)::int)*100,1) pct_any_mod,
       round(avg((nmod>0 AND abs(r)>0.001)::int)*100,1) pct_amount_changed,
       round(avg((r>0.05)::int)*100,1) pct_up5, round(avg((r>0.15)::int)*100,1) pct_up15, round(avg((r>0.5)::int)*100,1) pct_up50,
       round(avg((r<-0.5)::int)*100,1) pct_down50,
       round(sum(m0)/1e9,2) sum_m0_bn
FROM c WHERE year(d0) BETWEEN 2019 AND 2023 GROUP BY 1 ORDER BY 1"""): print(row)
print("Among contracts with a plausible increase (0.1% < r <= 100%), 2019-2023:")
for row in q("""
SELECT seg, count(*) n, round(median(r)*100,1) med_pct, round(quantile_cont(r,0.75)*100,1) p75_pct, round(quantile_cont(r,0.9)*100,1) p90_pct,
       round(median(mN-m0)) med_eur, round(sum(mN-m0)/1e9,3) sum_added_bn, round(sum(m0)/1e9,2) base_bn
FROM c WHERE year(d0) BETWEEN 2019 AND 2023 AND r>0.001 AND r<=1 GROUP BY 1 ORDER BY 1"""): print(row)
print("Batiment by year: n, pct with increase>0.1%..100%, median increase among those")
for row in q("""
SELECT year(d0) y, count(*) n, round(avg((r>0.001 AND r<=1)::int)*100,1) pct_inc,
       round(median(r) FILTER (WHERE r>0.001 AND r<=1)*100,1) med
FROM c WHERE seg='batiment' AND year(d0) BETWEEN 2019 AND 2025 GROUP BY 1 ORDER BY 1"""): print(row)
print("Batiment by size band (2019-2023): band, n, pct_inc, median inc, sum added bn")
for row in q("""
SELECT CASE WHEN m0<90000 THEN '1 <90k' WHEN m0<500000 THEN '2 90k-500k' WHEN m0<5000000 THEN '3 500k-5M' ELSE '4 >5M' END b,
       count(*) n, round(avg((r>0.001 AND r<=1)::int)*100,1) pct_inc,
       round(median(r) FILTER (WHERE r>0.001 AND r<=1)*100,1) med, round(sum(mN-m0) FILTER (WHERE r>0.001 AND r<=1)/1e9,3) added_bn
FROM c WHERE seg='batiment' AND year(d0) BETWEEN 2019 AND 2023 GROUP BY 1 ORDER BY 1"""): print(row)
print("Offers received, MOE 712 (2022-2025): n, median, p25, p75, pct with >=5, pct with 1")
for row in q("""
SELECT count(*) n, median(offres), quantile_cont(offres,0.25), quantile_cont(offres,0.75),
       round(avg((offres>=5)::int)*100,1), round(avg((offres=1)::int)*100,1), round(avg(offres),1)
FROM c WHERE seg='moe_712' AND offres IS NOT NULL AND offres>0 AND offres<200 AND year(d0) BETWEEN 2022 AND 2025"""): print(row)
print("Offers received, batiment works (2022-2025):")
for row in q("""
SELECT count(*) n, median(offres), round(avg((offres=1)::int)*100,1) pct_single, round(avg((offres<=2)::int)*100,1) pct_le2
FROM c WHERE seg='batiment' AND offres IS NOT NULL AND offres>0 AND offres<200 AND year(d0) BETWEEN 2022 AND 2025"""): print(row)
print("top CPV in moe_712:", q("SELECT cpv, count(*) FROM c WHERE seg='moe_712' GROUP BY 1 ORDER BY 2 DESC LIMIT 8"))
