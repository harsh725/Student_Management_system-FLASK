import sqlite3

con=sqlite3.connect("student.db")
cur=con.cursor()
# cur.execute("""DROP trigger calculate""")
cur.execute("""DROP table performance""")
con.commit()
con.close()