# ตัวแรกของชื่อ class ต้องเป็นตัวใหญ่
class Customer:
    nickname = ""
    firstname = ""
    age = ""
    def addCart(self):
        print("Added to" , self.nickname, self.firstname, "><")

customer1 = Customer()
customer1.nickname = "Aof"
customer1.firstname = "Chollatit"
customer1.addCart()

customer2 = Customer()
customer2.nickname = "Mac"
customer2.firstname = "Jummumboy"
customer2.addCart()

customer3 = Customer()
customer3.nickname = "Aod"
customer3.firstname = "Naras"
customer3.addCart()