import sqlite3
c=sqlite3.connect('Bootcamp.db')

c.execute("delete from participant where study='Btech'")
print(c.total_changes)
c.commit()
c.close()