

def order_menu():
    me = int(input('''\nSelect 
    1.Starters   2.Biryanis   3.Desserts  :'''))
    if me == 1:
        str = int(input("Select a starter :"))
        if str == 1:
            n = int(input("Enter no. of plates : "))
            cost = n * 250
            print("Cost of {}".format(n) + " plate Chilli Chicken - {} ".format(cost))
        elif str == 2:
            n = int(input("Enter no. of plates : "))
            cost = n * 250
            print("Cost of {}".format(n) + " plate Chicken 65 - {} ".format(cost))
        elif str == 3:
            n = int(input("Enter no. of plates : "))
            cost = n * 190
            print("Cost of {}".format(n) + " plate Paneer - {} ".format(cost))
        elif str == 4:
            n = int(input("Enter no. of plates : "))
            cost = n * 160
            print("Cost of {}".format(n) + " plate Veg Manchurian - {} ".format(cost))
        else:
            print("Enter again")
    elif me==2:
        str = int(input("Select a Biryani :"))
        if str == 1:
            n = int(input("Enter no. of plates : "))
            cost = n * 230
            print("Cost of {}".format(n) + " plate Chicken Biryani - {} ".format(cost))
        elif str == 3:
            n = int(input("Enter no. of plates : "))
            cost = n * 580
            print("Cost of {}".format(n) + " plate Chicken Family pack - {} ".format(cost))
        elif str == 4:
            n = int(input("Enter no. of plates : "))
            cost = n * 300
            print("Cost of {}".format(n) + " plate Chicken Dum Biryani - {} ".format(cost))
        elif str == 5:
            n = int(input("Enter no. of plates : "))
            cost = n * 350
            print("Cost of {}".format(n) + " plate Mutton Biryani - {} ".format(cost))
        elif str == 6:
            n = int(input("Enter no. of plates : "))
            cost = n * 600
            print("Cost of {}".format(n) + " plate Mutton Family pack - {} ".format(cost))
        elif str == 7:
            n = int(input("Enter no. of plates : "))
            cost = n * 170
            print("Cost of {}".format(n) + " plate Veg. Biryani - {} ".format(cost))
        elif str == 8:
            n = int(input("Enter no. of plates : "))
            cost = n * 370
            print("Cost of {}".format(n) + " plate Veg. Family pack - {} ".format(cost))
        else:
            print("Enter again")
    elif me==3:
        str = int(input("Select a Dessert :"))
        if str == 1:
            n = int(input("Enter no. Desserts : "))
            cost = n * 70
            print("Cost of {}".format(n) + " Butter Scotch - {} ".format(cost))
        elif str == 2:
            n = int(input("Enter no. Desserts : "))
            cost = n * 55
            print("Cost of {}".format(n) + " Vanilla - {} ".format(cost))
        elif str == 3:
            n = int(input("Enter no. Desserts : "))
            cost = n * 80
            print("Cost of {}".format(n) + " Strawberry - {} ".format(cost))
        elif str == 4:
            n = int(input("Enter no. Desserts : "))
            cost = n * 100
            print("Cost of {}".format(n) + " Chocolate - {} ".format(cost))
        elif str == 5:
            n = int(input("Enter no. Desserts : "))
            cost = n * 160
            print("Cost of {}".format(n) + " Black Forest - {} ".format(cost))
        elif str == 6:
            n = int(input("Enter no. Desserts : "))
            cost = n * 200
            print("Cost of {}".format(n) + " Red velvet - {} ".format(cost))
        else:
            print("Enter again")
    else:
        print("Enter again")
    order_menu.var= cost
def totalcost():

    print(order_menu.var)




