try:
    in1 = int(input("in1 :"))
    in2 = int(input("in2 :"))
    print(in1/in2)
except ValueError:
    print("Error ! Please Re-Enter Number")
except ZeroDivisionError:
    print("Error ! You Can't Enter 0")
except:
    print("Error")