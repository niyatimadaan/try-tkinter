from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    if math == "division":
        entry.insert(0, f_num / float(second_number))

for i in range(1, 10):
    button = Button(root, text=str(i), padx=40, pady=20, command=lambda i=i: button_click(i))
    button.grid(row=(4- int((i-1)/3)), column=(i-1)%3)

button0 = Button(root, text="0", padx=80, pady=20, command=lambda: button_click(0))
button0.grid(row=5, column=0, columnspan=2)
button_dot = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_dot.grid(row=5, column=2)

button_clear = Button(root, text="C", padx=40, pady=20, command=button_clear)
button_clear.grid(row=1, column=2)

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_add.grid(row=1, column=3)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_subtract.grid(row=2, column=3)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_multiply.grid(row=3, column=3)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)
button_divide.grid(row=4, column=3)

button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_equal.grid(row=5, column=3)


root.mainloop()