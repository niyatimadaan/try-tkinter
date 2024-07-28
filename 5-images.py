from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Image Viewer")
# root.iconbitmap("path/to/ico/icon.ico")
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="public/icons/page_white_ruby.png"))

img_number = 1
my_img1 = ImageTk.PhotoImage(Image.open("public/images/Screenshot 2024-07-03 230136.png"))
my_img2 = ImageTk.PhotoImage(Image.open("public/images/Screenshot 2024-07-23 181340.png"))
my_img3 = ImageTk.PhotoImage(Image.open("public/images/Screenshot 2024-07-03 230136.png"))
my_img4 = ImageTk.PhotoImage(Image.open("public/images/Screenshot 2024-07-23 181340.png"))
my_img5 = ImageTk.PhotoImage(Image.open("public/images/Screenshot 2024-07-03 230136.png"))
img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
img_label = Label(image=my_img1)
img_label.grid(row=0, column=0, columnspan=3)

def forward ():
    global img_number
    global img_label
    global img_list
    global button_forward
    global button_back
    img_number +=1
    print(img_number)
    img_label.grid_forget()
    img_label = Label(image=img_list[img_number-1])
    img_label.grid(row=0, column=0, columnspan=3)

    if img_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED).grid(row=1, column=2)

    if img_number > 1:
        button_back = Button(root, text="<<", command=back).grid(row=1, column=0)


def back():
    global img_number
    global img_label
    global img_list
    global my_img1
    global button_forward
    global button_back

    img_number -=1
    img_label.grid_forget()
    img_label = Label(image=img_list[img_number-1])
    img_label.grid(row=0, column=0, columnspan=3)

    if img_number == 1:
        button_back = Button(root, text="<<", state=DISABLED).grid(row=1, column=0)

    if img_number < 5:
        button_forward = Button(root, text=">>", command=lambda: forward()).grid(row=1, column=2)


button_back = Button(root, text="<<", state=DISABLED, command=back).grid(row=1, column=0)
button_exit = Button(root, text="Exit Program", command=root.quit).grid(row=1, column=1)
button_forward = Button(root, text=">>", command=forward()).grid(row=1, column=2)

root.mainloop()