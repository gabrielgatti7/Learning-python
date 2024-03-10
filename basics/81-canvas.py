# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, width=500, height=500)
# canvas.create_line(0, 0, 500, 500, fill='blue', width=5)
# canvas.create_line(0, 500, 500, 0, fill='red', width=5)
# canvas.create_rectangle(100, 100, 400, 400, fill='pink', width=5)
# points = [250, 0, 500, 500, 0, 500]
# canvas.create_polygon(points, fill='light blue', width=5, outline="black")
# canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=45, extent=180)
canvas.create_arc(0, 0, 500, 500, fill='red', extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill='white', start=180, extent=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill='white', width=10)

canvas.pack()

window.mainloop()
