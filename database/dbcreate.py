# import module
# create db
#connect
# create table in db
#execute




import sqlite3
c=sqlite3.connect('Bootcamp.db')
q='''
    create table participant(gid int primary key,name text not null,branch text not null)
'''
c.execute(q)