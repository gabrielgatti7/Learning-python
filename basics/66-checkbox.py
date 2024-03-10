from tkinter import *


def display():
    if(x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree")


window = Tk()

writing_emoji = PhotoImage(file="writing.png")

x = IntVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           bg='white',
                           activebackground='white',
                           padx=25,
                           pady=10,
                           image=writing_emoji,
                           compound='left')
check_button.pack()

window.mainloop()