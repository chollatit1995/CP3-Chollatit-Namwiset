number = int(input("Key Number : "))
area = number
for i in range(number):
    print(((area)*" ")+((2*(i+1)-1)*"*"))
    area = area - 1