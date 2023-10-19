username = input("username :")
password = input("password :")

if username == "admin" and password == "123":
    print("------ Welcome ------")
    print("----- inno shop -----")
    print("1. Apple     10 THB")
    print("2. Banana    5 THB")
    print("3. Orange    15 THB")
    print("---------------------")
    userSelected = int(input("Choose the desired fruit :"))
    print("---------------------")
    if userSelected == 1:
        print("Promotion 10 Free 5")
        amount = int(input("How much do you want :"))
        print("---------------------")
        if amount == 10:
            price = 10
            item = 5 + amount
            totalAmount = amount * price
            print("Orange :", item, "item")
            print("Total amount : ", float(totalAmount), "THB")
            print("---------------------")
        elif amount <= 10:
            price = 10
            totalAmount = amount * price
            print("Orange :", amount, "item")
            print("Total amount : ", totalAmount, "THB")
            print("---------------------")
    elif userSelected == 2:
        print("Promotion Sell 50%")
        amount = int(input("How much do you want :"))
        print("---------------------")
        price = 5
        totalAmount = (amount * price)/2
        print("Banana :", amount, "item")
        print("Total amount : ", totalAmount, "THB")
        print("---------------------")
    elif userSelected == 3:
        print("Promotion Reduced price 5 THB")
        amount = int(input("How much do you want :"))
        print("---------------------")
        sell = 5
        price = 15 - 5
        totalAmount = amount * price
        print("Orange :", amount, "item")
        print("Total amount : ", float(totalAmount), "THB")
        print("---------------------")
    else:
        print("There are no items selected.")
else:
    print("Login Fail !")
