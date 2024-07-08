from tkinter import *
from PIL import Image, ImageTk
from wind import Window
from inside import main_menu



def next(window, nextw):
    window.destroy()
    nextw()

def show_hide(ent_pas, checkbox_var):
    if checkbox_var.get() == 1:
        ent_pas.config(show='')
    else:
        ent_pas.config(show='*')



def login():
    root = Window('Bank', '1280x700+50+50')

    image = Image.open("bg_photo/log_bg.png")
    bg_image = ImageTk.PhotoImage(image)
    background_label = Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    btn_next = Button(root, text='МенюРегистрации', command=lambda: next(root, register)).pack()

    ent_log = Entry(root, font=('Italic', 17), fg='white', bg='#315f89', width=29, bd=0, highlightthickness=0)
    ent_log.place(x=775, y=210)
    ent_pas = Entry(root, font=('Italic', 17), show='*', fg='white', bg='#315f89', width=29, bd=0, highlightthickness=0)
    ent_pas.place(x=775, y=335)

    btn_acc = Button(root, text='Accept', width=10, fg='white', bg='#214c8c', activebackground='#214c8c',
                     font=('Italic', 15), bd=0, highlightthickness=0, command=lambda: next(root, main_menu))
    btn_acc.place(x=1035, y=458)

    reg_btn = Button(root, text='Open register window', bg='#d9d9d9', activebackground='#d9d9d9', bd=0,command=lambda: next(root, register)).place(x=1015, y=388)

    checkbox_var = IntVar()
    chec = Checkbutton(root, text='Show password?', font=('italic', 14), bg='#d9d9d9', activebackground='#d9d9d9',
                       variable=checkbox_var, command=lambda: show_hide(ent_pas, checkbox_var))
    chec.place(x=775, y=385)

    root.mainloop()

def register():
    root = Window('Login', '1280x700+50+50')

    image = Image.open("bg_photo/reg_bg.png")
    bg_image = ImageTk.PhotoImage(image)
    background_label = Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    ent_log = Entry(root, font=('Italic', 17), fg='white', bg='#315f89', width=29, bd=0, highlightthickness=0)
    ent_log.place(x=100, y=210)
    ent_pas = Entry(root, font=('Italic', 17), show='*', fg='white', bg='#315f89', width=29, bd=0, highlightthickness=0)
    ent_pas.place(x=100, y=335)

    btn_acc = Button(root, text='Accept', width=10, fg='white', bg='#214c8c', activebackground='#214c8c',
                     font=('Italic', 15), bd=0, highlightthickness=0,command=lambda: next(root, main_menu))
    btn_acc.place(x=350, y=463)

    reg_btn = Button(root, text='Open login window', bg='#d9d9d9', activebackground='#d9d9d9', bd=0,command=lambda: next(root, login)).place(x=340, y=388)

    checkbox_var = IntVar()
    chec = Checkbutton(root, text='Show password?', font=('italic', 14), bg='#d9d9d9', activebackground='#d9d9d9',
                       variable=checkbox_var, command=lambda: show_hide(ent_pas, checkbox_var))
    chec.place(x=100, y=385)

    root.mainloop()
