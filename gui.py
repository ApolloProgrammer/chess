from tkinter import *
from tkinter.ttk import Frame, Label, Style

class Visual(Frame):

    def __init__(self):
        super().__init__()
        self.draw_Board()


    def draw_Board(self):
        self.master.title("FOXCHESS")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        factor=2
        size=factor*20
        x,y=factor*20,factor*20
        start,ende=x,y
        meta_Board=[]
        n=0
        for row in range(1,9):
            if row%2!=0:
                for col in range(1,9):
                    if col%2==0:
                        canvas.create_rectangle(x,y,x+size,y+size,fill='black')
                        meta_Board.append([n,x+size/2,y+size/2])
                    else:
                        canvas.create_rectangle(x, y, x + size, y + size, fill='white')
                        meta_Board.append([n,x+size/2,y+size/2])
                    x+=size
                    n+=1
            else:
                for col in range(1,9):
                    if col%2==0:
                        canvas.create_rectangle(x,y,x+size,y+size,fill='white')
                        meta_Board.append([n,x+size/2,y+size/2])
                    else:
                        canvas.create_rectangle(x, y, x + size, y + size, fill='black')
                        meta_Board.append([n,x+size/2,y+size/2])
                    x+=size
                    n+=1
            y+=size
            x=start


        #manipulating the list from 63 62 61 ... 56 to 56 57 58 ... 63
        #                           55 54 53 ... 48    48 49 50 ... 51
        #                           ...
        #                           7  6  5  ... 0     0  1  2  ... 7
        sol = []
        for i in range(8):
            if i == 0:
                temp = []
                for element in meta_Board[7::-1]:
                    temp.append(element)
            else:
                temp = []
                for element in meta_Board[8 * (i + 1) - 1:(8 * i) - 1:-1]:
                    temp.append(element)
            sol.extend(temp)
        sol.reverse()
        n = 0
        for element in sol:
            element[0] = n
            n += 1
        #conquer the chessboard by figures of both players
      
        canvas.pack(fill=BOTH, expand=1)
        return sol


root = Tk()
root.geometry("400x400")
board = Visual()
root.mainloop()


