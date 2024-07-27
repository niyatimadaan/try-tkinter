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

root.mainloop()

