from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="Info message box", message="You clicked me!")
    # messagebox.showwarning(title="WARNING!", message="You have a virus!!!")
    # messagebox.showerror(title="ERROR!", message="Something went wrong :/")

    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?"):
    #     print("You did a thing!")
    # else:
    #     print("You canceled a thing!")

    # messagebox.askyesno()
    # messagebox.askretrycancel()

    # answer = messagebox.askquestion(title="ask question", message="Do you like pie?")
    # if answer == "yes":
    #     print("I like pie too")
    # else:
    #     print("Why don't you like pie?")

    answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like do code?")
    if answer == True:
        print("You like to code :)")
    elif answer == False:
        print("Why not?")
    else:
        print("You have dodged the question")


window = Tk()

button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()