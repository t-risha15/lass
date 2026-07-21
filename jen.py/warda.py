import tkinter as tk

def greet():
    print("how are you")

window = tk.Tk()

label = tk.label(window, text="welcome")
label.pack()

button = tk.Button(window,text="click me", command=greet)
button.pack()

entry =tk.entry(window)
entry.pack()

check = tk.checkbutton(window, text="i agree")
check.pack()

radio = tk.Checkbutton(window, text="male")
radio.pack()

window.mainloop()
