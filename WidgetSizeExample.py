from tkinter import *

def sayHi():
    print("Hi Baby")

mainWindows = Tk()
button = Button(mainWindows,text="Okay 1",command=sayHi).grid(row=0,column=1)
button2 = Button(mainWindows,text="Okay 2",command=sayHi).grid(row=1,column=1)
button3 = Button(mainWindows,text="Okay 2",command=sayHi).grid(row=0,column=2)
label = Label(mainWindows,text="Hello World",width=20,fg="red",bg="black",font=("Helvetica",38),anchor=E).grid(row=0,column=1)
mainWindows.mainloop()
