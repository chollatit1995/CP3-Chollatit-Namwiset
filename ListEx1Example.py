menuList = []
priceList = []
def showBill():
    print("------- My Food -------")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total = total + int(priceList[number])
    print("total price : ",total)

while True:
    menuName = input("Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()