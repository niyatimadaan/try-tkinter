from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Root Window")
# root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="public/icons/page_white_ruby.png"))
root.iconphoto(False, PhotoImage(file="public/icons/page_white_ruby.png"))

def open():
    global my_img
    top = Toplevel()
    top.title("Top Window")
    top.tk.call("wm", "iconphoto", top._w, PhotoImage(file="public/icons/box.png"))
    my_img = ImageTk.PhotoImage(Image.open("public/images/Screenshot 2024-07-03 230136.png"))
    my_label = Label(top, image=my_img).pack()
    button_quit = Button(top, text="Close Window", command=top.destroy).pack()


button_open = Button(root, text="Open Image", command=open, padx=10).pack(ipadx=10, ipady=10)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()