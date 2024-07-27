from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

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
    f_num = int(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    if math == "division":
        entry.insert(0, f_num / int(second_number))

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))