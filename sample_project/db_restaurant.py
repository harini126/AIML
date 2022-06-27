import sqlite3

import Restaurants
from Restaurants import Book_cabins as bc
from Restaurants import registration as reg
from Restaurants.cabins import Types_of_cabins as tc
from Restaurants.Menu import menu as mu
from Restaurants.Menu import order as oo
c.execute("insert into Restaurant_Bill values(reg.register.name,reg.register.p,,'CSE','Btech')")
c.commit()
c.close()