menuList = []

def showBill():
    print("---- My Food----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total = total+int(menuList[number][1])
    print("Total Price : ", total, "THB")
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()