username = input("username : ")
password = input("password : ")

while username != "admin" or password != "123":
    print("Login Fail")
    username = input("username : ")
    password = input("password : ")
print("Login Success")