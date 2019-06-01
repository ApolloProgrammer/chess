#Developer: Marvin Fuchs, May 2019
from tkinter import *
from tkinter.ttk import Frame
import board as b


class Visual(Frame):

    def __init__(self):
        super().__init__()
        #start drawing
        self.canvas = Canvas(self)
        physical_brett=self.draw_Board()#setup the board. physical_brett is the list with information about the location in pixel of every single field of the physical (GUI) board

        self.showtheUpdate(physical_brett)#setup the figures
        self.canvas.pack(fill=BOTH, expand=1) #end drawing

    def givePixelLocation(self, player, sol): #looks for the current location of a figure and returns its coordinates
        physical_brett = b.Board.createBoard(self)
        n = 0
        for element in physical_brett:
            if element[2] == player:
                break
            n += 1
        physicalBoard = sol
        element = physicalBoard[n]
        x, y = element[1], element[2]
        return x, y

    def draw_Board(self):
        self.master.title("FOXCHESS")
        self.pack(fill=BOTH, expand=1)

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
                        self.canvas.create_rectangle(x,y,x+size,y+size,fill='brown')
                        meta_Board.append([n,x+size/2,y+size/2])
                    else:
                        self.canvas.create_rectangle(x, y, x + size, y + size, fill='white')
                        meta_Board.append([n,x+size/2,y+size/2])
                    x+=size
                    n+=1
            else:
                for col in range(1,9):
                    if col%2==0:
                        self.canvas.create_rectangle(x,y,x+size,y+size,fill='white')
                        meta_Board.append([n,x+size/2,y+size/2])
                    else:
                        self.canvas.create_rectangle(x, y, x + size, y + size, fill='brown')
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
        return sol



    #Visualizing and Updating, conquering the chessboard by figures of both players
    def showtheUpdate(self,sol): #sol is the list with information about the location in pixel of every single field of the physical (GUI) board

        # Visualization Classes
        class Visual_Koenig():
            def visualize(self, x, y, size, team):
                if team == 0:
                    color = 'orange'
                else:
                    color = 'black'
                self.canvas.create_polygon(x - size * 2 / 10, y - size * 2 / 10, x - size * 2 / 10, y - size * 2 / 10,
                                          x - size * 8 / 10, y - size * 2 / 10, x - size * 8 / 10, y + size * 2 / 10,
                                          x - size * 2 / 10, y + size * 2 / 10, x - size * 2 / 10, y + size * 8 / 10,
                                          x + size * 2 / 10, y + size * 8 / 10, x + size * 2 / 10, y + size * 2 / 10,
                                          x + size * 8 / 10, y + size * 2 / 10, x + size * 8 / 10, y - size * 2 / 10,
                                          x + size * 2 / 10, y - size * 2 / 10, x + size * 2 / 10, y - size * 8 / 10,
                                          x - size * 2 / 10, y - size * 8 / 10, fill=color)
        class Visual_Dame():
            def visualize(self, x, y, size, team):
                if team == 0:
                    color = 'orange'
                else:
                    color = 'black'
                self.canvas.create_oval(x - size * 9 / 10, y - size * 9 / 10, x + size * 9 / 10, y + size * 9 / 10,
                                   fill=color)
        class Visual_Turm():
            def visualize(self, x, y, size, team):
                if team == 0:
                    color = 'orange'
                else:
                    color = 'black'
                self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,
                                        fill=color)
        class Visual_Laeufer():
            def visualize(self, x, y, size, team):
                if team == 0:
                    color = 'orange'
                    self.canvas.create_polygon(x, y - size * 3 / 4, x - size / 3, y + size * 3 / 4, x + size / 3,
                                          y + size * 3 / 4, x, y - size * 3 / 4, fill=color)
                else:
                    color = 'black'
                    self.canvas.create_polygon(x, y + size * 3 / 4, x - size / 3, y - size * 3 / 4, x + size / 3,
                                          y - size * 3 / 4, x, y + size * 3 / 4, fill=color)
        class Visual_Pferd():
            def visualize(self, x, y, size, team):
                if team == 0:
                    color = 'orange'
                    self.canvas.create_polygon(x, y - size * 8 / 10, x - size * 3 / 5, y - size * 2 / 5, x,
                                          y + size * 9 / 10, x + size * 3 / 5, y - size * 2 / 5, x, y - size * 8 / 10,
                                          fill=color)
                else:
                    color = 'black'
                    self.canvas.create_polygon(x, y + size * 9 / 10, x - size * 3 / 5, y + size * 2 / 5, x,
                                          y - size * 8 / 10, x + size * 3 / 5, y + size * 2 / 5, x, y + size * 9 / 10,
                                          fill=color)
        class Visual_Bauer():
            def visualize(self, x, y, size, team):
                if team == 0:
                    color = 'orange'
                else:
                    color = 'black'
                self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill=color)

        #white
        coordinates_W1koenig = self.givePixelLocation('W1koenig',sol)
        Visual_Koenig.visualize(self, coordinates_W1koenig[0], coordinates_W1koenig[1], 20, 0)
        coordinates_W1dame=self.givePixelLocation('W1dame',sol)
        Visual_Dame.visualize(self,coordinates_W1dame[0],coordinates_W1dame[1], 20,0)
        coordinates_W1turm = self.givePixelLocation('W1turm',sol)
        Visual_Turm.visualize(self, coordinates_W1turm[0], coordinates_W1turm[1], 20, 0)
        coordinates_W2turm = self.givePixelLocation('W2turm',sol)
        Visual_Turm.visualize(self, coordinates_W2turm[0], coordinates_W2turm[1], 20, 0)
        coordinates_W1laeufer = self.givePixelLocation('W1laeufer',sol)
        Visual_Laeufer.visualize(self, coordinates_W1laeufer[0], coordinates_W1laeufer[1], 20, 0)
        coordinates_W2laeufer = self.givePixelLocation('W2laeufer',sol)
        Visual_Laeufer.visualize(self, coordinates_W2laeufer[0], coordinates_W2laeufer[1], 20, 0)
        coordinates_W1pferd = self.givePixelLocation('W1pferd',sol)
        Visual_Pferd.visualize(self, coordinates_W1pferd[0], coordinates_W1pferd[1], 20, 0)
        coordinates_W2pferd = self.givePixelLocation('W2pferd',sol)
        Visual_Pferd.visualize(self, coordinates_W2pferd[0], coordinates_W2pferd[1], 20, 0)
        coordinates_W1bauer = self.givePixelLocation('W1bauer',sol)
        coordinates_W2bauer = self.givePixelLocation('W2bauer',sol)
        coordinates_W3bauer = self.givePixelLocation('W3bauer',sol)
        coordinates_W4bauer = self.givePixelLocation('W4bauer',sol)
        coordinates_W5bauer = self.givePixelLocation('W5bauer',sol)
        coordinates_W6bauer = self.givePixelLocation('W6bauer',sol)
        coordinates_W7bauer = self.givePixelLocation('W7bauer',sol)
        coordinates_W8bauer = self.givePixelLocation('W8bauer',sol)
        Visual_Bauer.visualize(self, coordinates_W1bauer[0], coordinates_W1bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W2bauer[0], coordinates_W2bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W3bauer[0], coordinates_W3bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W4bauer[0], coordinates_W4bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W5bauer[0], coordinates_W5bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W6bauer[0], coordinates_W6bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W7bauer[0], coordinates_W7bauer[1], 20,0)
        Visual_Bauer.visualize(self, coordinates_W8bauer[0], coordinates_W8bauer[1], 20,0)
        #black
        coordinates_B1koenig = self.givePixelLocation('B1koenig',sol)
        Visual_Koenig.visualize(self, coordinates_B1koenig[0], coordinates_B1koenig[1], 20, 1)
        coordinates_B1dame = self.givePixelLocation('B1dame',sol)
        Visual_Dame.visualize(self, coordinates_B1dame[0], coordinates_B1dame[1], 20, 1)
        coordinates_B1turm = self.givePixelLocation('B1turm',sol)
        Visual_Turm.visualize(self, coordinates_B1turm[0], coordinates_B1turm[1], 20, 1)
        coordinates_B2turm = self.givePixelLocation('B2turm',sol)
        Visual_Turm.visualize(self, coordinates_B2turm[0], coordinates_B2turm[1], 20, 1)
        coordinates_B1laeufer = self.givePixelLocation('B1laeufer',sol)
        Visual_Laeufer.visualize(self, coordinates_B1laeufer[0], coordinates_B1laeufer[1], 20, 1)
        coordinates_B2laeufer = self.givePixelLocation('B2laeufer',sol)
        Visual_Laeufer.visualize(self, coordinates_B2laeufer[0], coordinates_B2laeufer[1], 20, 1)
        coordinates_B1pferd = self.givePixelLocation('B1pferd',sol)
        Visual_Pferd.visualize(self, coordinates_B1pferd[0], coordinates_B1pferd[1], 20, 1)
        coordinates_B2pferd = self.givePixelLocation('B2pferd',sol)
        Visual_Pferd.visualize(self, coordinates_B2pferd[0], coordinates_B2pferd[1], 20, 1)
        coordinates_B1bauer = self.givePixelLocation('B1bauer',sol)
        coordinates_B2bauer = self.givePixelLocation('B2bauer',sol)
        coordinates_B3bauer = self.givePixelLocation('B3bauer',sol)
        coordinates_B4bauer = self.givePixelLocation('B4bauer',sol)
        coordinates_B5bauer = self.givePixelLocation('B5bauer',sol)
        coordinates_B6bauer = self.givePixelLocation('B6bauer',sol)
        coordinates_B7bauer = self.givePixelLocation('B7bauer',sol)
        coordinates_B8bauer = self.givePixelLocation('B8bauer',sol)
        Visual_Bauer.visualize(self, coordinates_B1bauer[0], coordinates_B1bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B2bauer[0], coordinates_B2bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B3bauer[0], coordinates_B3bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B4bauer[0], coordinates_B4bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B5bauer[0], coordinates_B5bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B6bauer[0], coordinates_B6bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B7bauer[0], coordinates_B7bauer[1], 20, 1)
        Visual_Bauer.visualize(self, coordinates_B8bauer[0], coordinates_B8bauer[1], 20, 1)




root = Tk()
root.geometry("400x400")
board = Visual()
root.mainloop()


