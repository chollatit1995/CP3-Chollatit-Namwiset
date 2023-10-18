# เป็นตัวเลขอยู่แล้วใส่ int() เลย
price = int(input("keypoint"))
vat = 7
# result = int(price) + (int(price)*vat/100)
result = price + (price*vat/100)
print(result)