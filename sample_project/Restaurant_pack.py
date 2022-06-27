import Restaurants
from Restaurants import Book_cabins as bc
from Restaurants import registration as reg
from Restaurants import Bill as bb
from Restaurants.cabins import Types_of_cabins as tc
from Restaurants.Menu import menu as mu
from Restaurants.Menu import order as oo
print("____Registration____")
reg.register()
print("****WELCOME****")
cabin_type=int(input(''' 1. 6 members 
2. 4 members
3. 2 members
Enter the cabin type you want :'''))
bc.cabin(cabin_type)

print("Enter Time slot (only in hours)")
amorpm=int(input('''Enter 1 for AM :
Enter 2 for PM :'''))
if amorpm==1:
    tc.amslot(cabin_type,amorpm)
elif amorpm==2:
    tc.pmslot(cabin_type,amorpm)

print("*****MENU*****")
mu.menu_file()
oo.order_menu()
print("NAME : ")
reg.n()
print("PHONE NO. :")
reg.ph()
print("Cabin Charges : ")
if amorpm==1:
    tc.chargesam(amorpm)
elif amorpm==2:
    tc.chargespm(amorpm)

print("Dish Cost : ")
oo.totalcost()
'''print("TOTAL BILL : ")
if amorpm==1:
    bb.totbillam(amorpm)
elif amorpm==2:
    bb.totbillpm(amorpm)'''
