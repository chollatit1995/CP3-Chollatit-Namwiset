username = input("username :")
password = input("password :")

if username == "admin" and password == "123":
    print("Login Success")
    print("----- inno shop -----")
    print("1. Vat Cacilator")
    print("1. Price Cacilator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("price :"))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected ==2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("First Product Price : "))
        print(price1+price2)
else:
    print("Login Fail !")
