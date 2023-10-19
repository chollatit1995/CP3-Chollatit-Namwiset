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
            vat = 7
            result = totalAmount * vat / 100
            print("Apple :", item, "item")
            print("Vat 7 % :", result, "THB")
            print("Total amount : ", totalAmount+result, "THB")
            # print("---------------------")
        elif amount <= 10:
            price = 10
            totalAmount = amount * price
            vat = 7
            result = totalAmount * vat / 100
            print("Apple :", amount, "item")
            print("Vat 7 % :", result, "THB")
            print("Total amount : ", totalAmount+result, "THB")
            # print("---------------------")
    elif userSelected == 2:
        print("Promotion Sell 50%")
        amount = int(input("How much do you want :"))
        # print("---------------------")
        price = 5
        totalAmount = (amount * price)/2
        vat = 7
        result = totalAmount * vat / 100
        print("Banana :", amount, "item")
        print("Vat 7 % :", result, "THB")
        print("Total amount : ", totalAmount+result, "THB")
        # print("---------------------")
    elif userSelected == 3:
        print("Promotion Reduced price 5 THB")
        amount = int(input("How much do you want :"))
        sell = 5
        price = 15 - sell
        totalAmount = amount * price
        vat = 7
        result = totalAmount * vat / 100
        print("Orange :", amount, "item")
        print("Vat 7 % :", result, "THB")
        print("Total amount : ", totalAmount+result, "THB")
    else:
        print("There are no items selected.")
    print("---------------------")
    print("----- THANK YOU -----")
    print("---------------------")
else:
    print("Login Fail !")
