inputRound = int(input("Enter Number : "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("x" + str(x) + " : "))
    sum = inputNumber+sum
print("Sum : ",sum)