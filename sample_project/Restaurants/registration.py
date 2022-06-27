def register():
    import re
    name = input("NAME : ")

    mail = input("Gmail : ")
    s = r'[A-Za-z0-9._-]+@[A-za-z0-9.-]+[A-Z|a-z]{2,}'
    re.search(s, mail).group()
    p = input("PHONE NO. :")
    re.search(r'\d{10}', p).group()
    print("--Registration Successfull--")
    register.var=name
    register.var1 = p
def n():
    print(register.var)

def ph():
    print(register.var1)