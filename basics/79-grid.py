from tkinter import *

# grid() = geometry manager that organizes widgets in a 2-dimensional table

window = Tk()

titleLabel = Label(window, text="Enter your info", font=("Arial", 25))
titleLabel.grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name: ", font=30, bg="pink", width=20)
firstNameLabel.grid(row=1, column=0)
firstNameEntry = Entry(window, font=30)
firstNameEntry.grid(row=1, column=1)

lastNameLabel = Label(window,text="Last Name: ", font=30, bg="light blue")
lastNameLabel.grid(row=2, column=0)
lastNameEntry = Entry(window,font=30)
lastNameEntry.grid(row=2, column=1)

emailLabel = Label(window,text="Email: ", font=30, bg="light green")
emailLabel.grid(row=3, column=0)
emailEntry = Entry(window,font=30)
emailEntry.grid(row=3, column=1)

submitButton = Button(window,text="Submit")
submitButton.grid(row=4, column=0, columnspan=2)

window.mainloop()
