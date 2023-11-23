from tkinter import *
import math
def leftClickButton(event):
    BMI = round(float(textBoxWeight.get())/math.pow(float(textBoxHigth.get())/100,2))
    # lableResual.configure(text=(float(textBoxWeight.get())/math.pow(float(textBoxHigth.get())/100,2)))
    lableResual.configure(text=BMI)
    if BMI < 18.5:
        lableResual.configure(text="ผอมเกินไป BMI = " + str(BMI))
    elif BMI < 22.9:
        lableResual.configure(text="น้ำหนักปกติ เหมาะสม BMI = " + str(BMI))
    elif BMI < 24.9:
        lableResual.configure(text="น้ำหนักเกิน BMI = " + str(BMI))
    elif BMI < 29.9:
        lableResual.configure(text="อ้วน BMI = " + str(BMI))
    else:
        lableResual.configure(text="อ้วนมาก BMI = " + str(BMI))

mainWindows = Tk()
lableHigth = Label(mainWindows,text="ส่วนสูง (cm.)")
lableHigth.grid(row=0,column=0)
textBoxHigth = Entry(mainWindows)
textBoxHigth.grid(row=0,column=1)
lableCM = Label(mainWindows,text="เซนติเมตร")
lableCM.grid(row=0,column=2)

lableWeight = Label(mainWindows,text="น้ำหนัก (kg.)")
lableWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindows)
textBoxWeight.grid(row=1,column=1)
lableKG = Label(mainWindows,text="กิโลกรัม")
lableKG.grid(row=1,column=2)

calculateButton = Button(mainWindows,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
lableResual = Label(mainWindows,text="ผลลัพธ์")
lableResual.grid(row=2,column=1)
mainWindows.mainloop()