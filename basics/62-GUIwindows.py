# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()       # instantiate an instance of a window
window.geometry("420x420")
window.title("Window title")

# icon = PhotoImage(file='logo.png')
# window.iconphoto(True, icon)
window.config(background="black")

window.mainloop()   # place window on computer screen, listen for events