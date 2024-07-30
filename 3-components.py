from tkinter import *

root = Tk()

entry1 = Entry(root, width=50, borderwidth=5)
entry1.pack()
entry1.insert(0, "Enter text here")

def onClick():
    myLabel = Label(root, text="You entered : " + entry1.get())
    myLabel.pack()


button1 = Button(root, text="Click Me!", state=DISABLED)
button2 = Button(root, text="Enter Text", padx=50, pady=10, 
                 command=onClick, fg="blue", bg="#000000")

button2.pack()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    radioLabel = Label(root, text=value)
    radioLabel.pack()

# r = IntVar()
# r.set(1)
# Radiobutton(root, text="Option 1",variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2",variable=r, value=2, command=lambda: clicked(r.get())).pack()
# radioLabel = Label(root, text=r.get()).pack()

radioButton1 = Button(root, text="Click Me!", command=lambda: clicked(pizza.get())).pack()


root.mainloop()

