"""L4: who holds direct EU cohesion-fund project contracts in Latvia, 2021-2027.

Input: CFLA open data on 2021-2027 projects (data.gov.lv), downloaded as esf.csv.
Run: uv run --with duckdb python -I eu_funds_direct_contracts.py <path-to-esf.csv>

Caveat found by checking how the data encodes absence: IesniedzejaRegNo is blank for
most rows (508 distinct numbers against 1,324 distinct names), so beneficiaries are
identified by name. Firms helped through LIAA or ALTUM schemes are final recipients of
those bodies' projects and do not appear here as contract holders.
"""
import sys
import duckdb

con = duckdb.connect()
con.execute(f"""CREATE TABLE e AS SELECT * FROM read_csv('{sys.argv[1]}',
    sample_size=200000, ignore_errors=true, all_varchar=true)""")
out = []

def q(title, sql):
    out.append("== " + title)
    for r in con.execute(sql).fetchall():
        out.append("  " + " | ".join("" if v is None else str(v) for v in r))

EU = "sum(try_cast(ProjektamPieskirtaisESFonduLidzfinansejums as double))"
q("rows, distinct names, blank reg numbers, EU M",
  f"SELECT count(*), count(distinct IesniedzejaNosaukums), sum(case when IesniedzejaRegNo is null or trim(IesniedzejaRegNo)='' then 1 else 0 end), round({EU}/1e6) FROM e")
q("by applicant type: contracts, distinct holders, EU M, share of EU %",
  f"SELECT ProjektaIesniedzejaTips, count(*), count(distinct IesniedzejaNosaukums), round({EU}/1e6,1), round(100*{EU}/(SELECT {EU} FROM e),1) FROM e GROUP BY 1 ORDER BY 4 DESC")
q("state-budget institution flag: contracts, EU M",
  f"SELECT IrValstsBudzetaFinansetaInstitucija, count(*), round({EU}/1e6) FROM e GROUP BY 1")
q("selection type: contracts, EU M",
  f"SELECT AtlasesVeids, count(*), round({EU}/1e6) FROM e GROUP BY 1")
q("company-type holders (SIA, AS): top 25 by EU M",
  f"SELECT IesniedzejaNosaukums, ProjektaIesniedzejaTips, count(*), round({EU}/1e6,1) FROM e WHERE ProjektaIesniedzejaTips ILIKE '%sabiedrība%' GROUP BY 1,2 ORDER BY 4 DESC LIMIT 25")
q("company-type holders: measures by contracts",
  f"SELECT PasakumaNumurs, any_value(PasakumaNosaukums), count(*), count(distinct IesniedzejaNosaukums), round({EU}/1e6,1) FROM e WHERE ProjektaIesniedzejaTips ILIKE '%sabiedrība%' GROUP BY 1 ORDER BY 3 DESC LIMIT 20")
q("twenty raw rows, company-type holders (sample)",
  "SELECT IesniedzejaNosaukums, PasakumaNumurs, left(ProjektaNosaukums,70), ProjektamPieskirtaisESFonduLidzfinansejums FROM e WHERE ProjektaIesniedzejaTips ILIKE '%sabiedrība%' USING SAMPLE 20 ROWS (reservoir, 42)")
sys.stdout.buffer.write("\n".join(out).encode("utf-8", "replace"))
