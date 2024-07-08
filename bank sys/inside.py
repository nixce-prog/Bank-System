from tkinter import *
from PIL import Image, ImageTk

def main_menu():
    root1 = Tk()
    root1.geometry('1280x700+90+50')

    image = Image.open("bg_photo/main_menu_bg.png")
    bg_image = ImageTk.PhotoImage(image)
    background_label = Label(root1, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #-------------------------------
    my_card = Button(root1, text='My card', font=('italic', 15), bg='#1a7867', bd=0,activeforeground='white', activebackground='#1a7867').place(x=180,y=415)
    transaction = Button(root1, text='Transaction', font=('italic', 15), bg='#1a7867', bd=0,activeforeground='white', activebackground='#1a7867').place(x=580,y=395)
    create_card = Button(root1, text='Create bank card', font=('italic', 15), bg='#1a7867', bd=0,activeforeground='white', activebackground='#1a7867').place(x=940,y=415)
    Profile = Button(root1, text='Profile', font=('italic', 20), bg='#1494f1', bd=0,activeforeground='white', activebackground='#1494f1').place(x=590,y=550)
    location = Button(root1, text='We', font=('italic', 13), bg='#9c9c9c', bd=0,activeforeground='white', activebackground='#9c9c9c').place(x=453,y=650)
    support = Button(root1, text='Support', font=('italic', 15), bg='#bc3f3f', bd=0,activeforeground='white', activebackground='#bc3f3f').place(x=758,y=625)


    root1.mainloop()