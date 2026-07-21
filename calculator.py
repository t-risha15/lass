from tkinter import *

def add():
    result.config(text=int(e1.get()) + int(e2.get()))

root = Tk()

e1 = Entry(root)
e2 = Entry(root)

e1.pack()
e2.pack()

Button(root, text="Add", command=add).pack()

result = Label(root, text="")
result.pack()   

root.mainloop()