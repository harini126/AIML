import sqlite3
c=sqlite3.connect('Bootcamp.db')
q='''
alter table participant add column study txt not null
'''

c.execute(q1)
c.commit()