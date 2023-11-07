point = 20
userPoint = 0
while userPoint != point:
    userPoint = int(input("Please guess a point :"))
    if userPoint > point:
        print("Point Large")
    elif userPoint < point:
        print("Point Small")
    elif userPoint == point:
        print("Point Success")