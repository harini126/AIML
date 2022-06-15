import sqlite3
c=sqlite3.connect('Bootcamp.db')
c.execute("drop table participant")
c.commit()
c.close()