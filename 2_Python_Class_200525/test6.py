import cx_Oracle
import os

os.putenv("NLS_LANG", ".UTF8")
connection = cx_Oracle.connect("system", "1234", "localhost/xe")
c = connection.cursor()
c.execute("select * from help")

d = []
for row in c:
    print(row[0], '-', row[1])