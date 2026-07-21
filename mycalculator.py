import tkinter as tk

window = tk.Tk()
window.title("my calculator")
window.geometry("300*250")

num1 = tk.Entry(window)
num1.pack()

num2 = tk.Entry(window)
num2.pack()
def add():
    answer.config(text="Answer: " = str(int(num1.get))) + int(num2.get(()))

button = tk.Button(window, text="Add", command="Add")
button.pack()

answer = tk.Label(window text="Answer:")
answer.pack()

window.mainloop