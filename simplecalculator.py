from tkinter import *

window =Tk()

window.title("simplecalculator")
window.geometry("300*250")

def add():
    result = int(num1.get()) + int(num2.get())
    answer.config(text="Answer:" + str(result))

    num1 =Entry(Window)
    num2.pack()

    button =Button(window,text="Add",command=add)
    button.pack()

    window.mainloop()