# Note, Python 3 has lowercase Tkinter.
import Tkinter

tk     = Tkinter.Tk()
canvas = Tkinter.Canvas(tk, width = 200, height = 200)
canvas.pack()

canvas.create_rectangle( 20, 20, 180, 180, fill="orange")

canvas.create_line(  10,  10,  190,  190, fill="blue")
canvas.create_line(  10, 190,  190,   10)

Tkinter.mainloop()
