from tkinter import *

def openfile():
    print("File has been opened!")
def savefile():
    print("File has been saved!")

def cut():
    print("You cut some text!")

def copy():
    print("You copied some text!")

def paste():
    print("You pasted some text!")


window = Tk()

# open_image = PhotoImage(file='')

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)   # , image=open_image, compound='left')
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

window.mainloop()