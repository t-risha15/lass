import tkinter as tk

def greet():
    print("Hello!")

window = tk.Tk()

label = tk.Label(window, text="Welcome")
label.pack()

button = tk.Button(window, text="Click Me", command=greet)
button.pack()

entry = tk.Entry(window)
entry.pack()

check = tk.Checkbutton(window, text="I agree")
check.pack()

radio = tk.Radiobutton(window, text="Male")
radio.pack()

window.mainloop()