# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("Huh?")


food = ['pizza', 'hamburger', 'hotdog']

window = Tk()

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],    # adds text to radio buttons
                               variable=x,      # groups radiobuttons together if they share the same var
                               value=i,         # assigns each radio button a different value
                               padx=25,
                               font=('Helvetica', 20),
                               command=order)   # set command of radiobutton to function
    radio_button.pack(anchor=W)
window.mainloop()