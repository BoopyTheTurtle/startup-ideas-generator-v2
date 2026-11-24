import sys, duckdb
url = sys.argv[1]
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")
con.execute(f"""
CREATE TABLE t AS
SELECT DISTINCT uid, modification_id, montant_rationalise AS montant, type, codeCPV,
       dateNotification, offresRecues, montant_anomalie, techniques, acheteur_categorie
FROM read_parquet('{url}')
WHERE type = 'Travaux' OR codeCPV LIKE '712%'
""")
print("rows", con.execute("select count(*) from t").fetchone())
print(con.execute("select type, count(distinct uid) n, count(distinct case when modification_id>0 then uid end) n_mod from t group by 1").fetchall())
print("anomalie", con.execute("select montant_anomalie, count(*) from t group by 1").fetchall())
print("years", con.execute("select year(dateNotification) y, count(distinct uid) from t where modification_id=0 group by 1 order by 1 desc limit 12").fetchall())
con.execute("COPY t TO 'decp_subset.parquet' (FORMAT PARQUET)")
