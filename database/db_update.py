import sqlite3
c=sqlite3.connect('Bootcamp.db')
q='''
    update participant set name='Harini Anenka' where gid=1
'''
c.execute(q)
c.commit()
c.close()