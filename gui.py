import Tkinter

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="white", height=600, width=600)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(coord)
C.pack()
top.mainloop()
