from tkinter import *
from tkinter import filedialog


def openfile():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\gabri\\PycharmProjects\\variables",
                                           title="Select file",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = open(file_path, 'r')
    print(file.read())
    file.close()


window = Tk()
button = Button(window, text="Open", command=openfile)
button.pack()
window.mainloop()
