import sqlite3
c=sqlite3.connect('Bootcamp.db')
c.execute("insert into participant values(1,2216127,'Harini','CSE','Btech')")
c.commit()
c.close()