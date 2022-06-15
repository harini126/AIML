import sqlite3
c=sqlite3.connect('Bootcamp.db')
#q=pragma table_info(participants)
str=c.execute("pragma table_info('participant')")
print(str)
for i in str:
    print(i)