def login():
    username = input("username :")
    password = input("password :")
    if username == "admin" and password == "123":
        return True
    else:
        return False
def showMenu():
    print("----- inno shop -----")
    print("1. Vat Cacilator")
    print("2. Price Cacilator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

def shop():
    if login():
        showMenu()
        select = menuSelect()
        if select == 1:
            vatPrice = int(input("Price  :"))
            print("Price", vatCalculate(vatPrice))
        elif select == 2:
            print("Price :",priceCalculate())
    else:
        print("Login Fail")

print(shop())