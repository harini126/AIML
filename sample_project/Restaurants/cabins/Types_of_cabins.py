

def chargesam(amorpm):
    print(amslot.var)
def chargespm(amorpm):
    print(pmslot.var1)







def amslot(cabin_type,amorpm):
    initial = int(input("From :"))
    final = int(input("To :"))
    c = initial - final
    t = abs(c)

    if cabin_type==1:
        charge=t*150
        print("Charges for 6 member cabin is ",charge)
    elif cabin_type==2:
        charge = t * 100
        print("Charges for 4 member cabin is ",charge)
    elif cabin_type==3:
        charge = t * 50
        print("Charges for 2 member cabin is ",charge)
    amslot.var=charge
def pmslot(cabin_type,amorpm):

    initial = int(input("From :"))
    final = int(input("To :"))

    c=initial-final
    t=abs(c)

    if cabin_type==1:
        charge = t * 150
        print("Charges for 6 member cabin is ",charge)
    elif cabin_type==2:
        charge = t * 100
        print("Charges for 4 member cabin is ",charge)
    elif cabin_type==3:
        charge = t * 50
        print("Charges for 2 member cabin is ",charge)
    pmslot.var1 = charge
