import sqlite3
c=sqlite3.connect('Bootcamp.db')
r=c.execute("select * from participant")
for i in r:
    print(i)