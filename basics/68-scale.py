from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + "ºC")


window = Tk()

# hotImage = PhotoImage(file='hot.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              font='Consolas 20',
              tickinterval=20,      # adds numeric indicator for value
              # resolution=5        # increment of the slider
              troughcolor="#69EAFF"
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # set default value of the slider
scale.pack()

# coldImage = PhotoImage(file='cold.png')
# coldLabel = Label(image=coldImage)
# coldLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()