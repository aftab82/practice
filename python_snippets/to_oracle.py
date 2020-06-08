import cx_Oracle

dsn_tns = cx_Oracle.makedsn('localhost', '8000', sid='tiger')
conn = cx_Oracle.connect(user='scott', password='tiger', dsn=dsn_tns)
c = conn.cursor()
c.execute("""select * from dept 
              where dname = :dname""",
          dname='Finance')
for row in c:
    print(row[0], '-', row[1])
