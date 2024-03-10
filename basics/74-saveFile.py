from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[('Text file', '.txt'),
                                               ('HTML file', '.html'),
                                               ('All Files', '.*')])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()


window = Tk()
button = Button(window, text='save', command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
