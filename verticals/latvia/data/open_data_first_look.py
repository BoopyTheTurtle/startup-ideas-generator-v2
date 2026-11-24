import duckdb, sys
d = sys.argv[1]
con = duckdb.connect()
def q(title, sql):
    rows = con.execute(sql).fetchall()
    out = "\n== " + title + "\n" + "\n".join("  " + " | ".join(str(x)[:75] for x in r) for r in rows) + "\n"
    sys.stdout.buffer.write(out.encode("utf-8","replace"))
con.execute(f"CREATE TABLE v AS SELECT * FROM read_csv('{d}/vak.csv', sample_size=50000, ignore_errors=true)").fetchall()
con.execute(f"CREATE TABLE b AS SELECT *, date_diff('day', Dokumenta_registresanas_datums, Saistita_darba_uzdevuma_pabeigsanas_datums) AS days FROM read_csv('{d}/bis_esrv.csv', sample_size=50000, ignore_errors=true)").fetchall()
con.execute(f"CREATE TABLE e AS SELECT * FROM read_csv('{d}/esf.csv', sample_size=50000, ignore_errors=true)").fetchall()
q("VAK by category", "SELECT Vakances_kategorija, count(*) n, round(median(Alga_no)) med_from FROM v GROUP BY 1 ORDER BY 2 DESC LIMIT 14")
q("VAK top titles", "SELECT upper(Vakances_nosaukums), count(*) n FROM v GROUP BY 1 ORDER BY 2 DESC LIMIT 22")
q("BIS rows by year", "SELECT year(Dokumenta_registresanas_datums) y, count(*) FROM b GROUP BY 1 ORDER BY 1 DESC LIMIT 8")
q("BIS doc types 2024-2026: n, share completed, median days, p90 days",
  """SELECT Dokumenta_veids, count(*) n, round(avg((days IS NOT NULL)::int)*100) pct_done, median(days) med, quantile_cont(days,0.9) p90
     FROM b WHERE year(Dokumenta_registresanas_datums)>=2024 GROUP BY 1 HAVING count(*)>800 ORDER BY 2 DESC LIMIT 25""")
q("BIS statuses 2024+", "SELECT Dokumentu_statusi, count(*) FROM b WHERE year(Dokumenta_registresanas_datums)>=2024 GROUP BY 1 ORDER BY 2 DESC LIMIT 10")
q("ESF by applicant type: n, total cost M, EU M", "SELECT ProjektaIesniedzejaTips, count(*), round(sum(ProjektaKopejasIzmaksas)/1e6), round(sum(ProjektamPieskirtaisESFonduLidzfinansejums)/1e6) FROM e GROUP BY 1 ORDER BY 3 DESC")
q("ESF top measures: n, total cost M", "SELECT PasakumaNumurs, PasakumaNosaukums, count(*), round(sum(ProjektaKopejasIzmaksas)/1e6) FROM e GROUP BY 1,2 ORDER BY 4 DESC LIMIT 22")
