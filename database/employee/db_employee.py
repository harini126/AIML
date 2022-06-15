import sqlite3
c=sqlite3.connect('Bootcamp2.db')
q1='''
    create table emp(e_id int primary key,name text not null,salary real not null)
'''
q2='''
alter table emp add column age int not null
'''
c.execute(q1)
c.execute(q2)
c.execute("insert into emp values(101,'aaa',30000,32)")
c.execute("insert into emp values(102,'bbb',20000,30)")
c.execute("insert into emp values(103,'ccc',10000,27)")
c.execute("insert into emp values(104,'ddd',50000,29)")
r=c.execute("select * from emp")
for i in r:
    print(i)

c.commit()
c.close()