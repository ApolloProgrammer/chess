#Developer: Marvin Fuchs, May-June 2019
from tkinter import *
from tkinter.ttk import Frame
from tkinter import ttk
import threading
import queue
import time
import engine as e
import board as b

##threading class start
class ThreadedClient(threading.Thread):
    def __init__(self, queue, queue_choice,queue_destination):
        threading.Thread.__init__(self)
        self.queue = queue
        self.queue_choice = queue_choice
        self.queue_destination = queue_destination
        self.meta=[]
    def run(self):
        game=e.Engine()
        self.meta = b.Board.createBoard(self)


        while game.end == False:
            if game.counter % 2 == 0:
                print("Its the turn of Player 1! (White)")
                print('Please write what figure you choose to move: W1koenig, W1dame, ..., W8bauer, Rochade')
                game.choice = game.giveBoard()[self.queue_choice.get()][2]
                self.queue.put([self.meta])
                print("Thats your choice: "+str(game.choice))
                game.destination_choice=self.queue_destination.get()
                self.meta=game.turn_of_White()
                self.queue.get()
                self.queue.put([self.meta])
            # turn of Player2(black)
            else:
                print("Its the turn of Player 2! (Black)")
                print('Please write what figure you choose to move: B1koenig, B1dame, ..., B8bauer, Rochade')
                game.choice = game.giveBoard()[self.queue_choice.get()][2]
                self.queue.put([self.meta])
                print("Thats your choice: " + str(game.choice))
                game.destination_choice=self.queue_destination.get()
                self.meta=game.turn_of_Black()
                self.queue.get()
                self.queue.put([self.meta])


##threading class end

###beginning of Visual_Pieces classes
class Visual_W1Koenig():
    def visualize(self, x, y, size):
        self.shape_W1koenig=self.canvas.create_polygon(x - size * 2 / 10, y - size * 2 / 10, x - size * 2 / 10, y - size * 2 / 10,
                                          x - size * 8 / 10, y - size * 2 / 10, x - size * 8 / 10, y + size * 2 / 10,
                                          x - size * 2 / 10, y + size * 2 / 10, x - size * 2 / 10, y + size * 8 / 10,
                                          x + size * 2 / 10, y + size * 8 / 10, x + size * 2 / 10, y + size * 2 / 10,
                                          x + size * 8 / 10, y + size * 2 / 10, x + size * 8 / 10, y - size * 2 / 10,
                                          x + size * 2 / 10, y - size * 2 / 10, x + size * 2 / 10, y - size * 8 / 10,
                                          x - size * 2 / 10, y - size * 8 / 10, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W1koenig)
        self.shape_W1koenig=self.canvas.create_polygon(x - size * 2 / 10, y - size * 2 / 10, x - size * 2 / 10, y - size * 2 / 10,
                                          x - size * 8 / 10, y - size * 2 / 10, x - size * 8 / 10, y + size * 2 / 10,
                                          x - size * 2 / 10, y + size * 2 / 10, x - size * 2 / 10, y + size * 8 / 10,
                                          x + size * 2 / 10, y + size * 8 / 10, x + size * 2 / 10, y + size * 2 / 10,
                                          x + size * 8 / 10, y + size * 2 / 10, x + size * 8 / 10, y - size * 2 / 10,
                                          x + size * 2 / 10, y - size * 2 / 10, x + size * 2 / 10, y - size * 8 / 10,
                                          x - size * 2 / 10, y - size * 8 / 10, fill='orange')

class Visual_B1Koenig():
    def visualize(self, x, y, size):
        self.shape_B1koenig=self.canvas.create_polygon(x - size * 2 / 10, y - size * 2 / 10, x - size * 2 / 10, y - size * 2 / 10,
                                          x - size * 8 / 10, y - size * 2 / 10, x - size * 8 / 10, y + size * 2 / 10,
                                          x - size * 2 / 10, y + size * 2 / 10, x - size * 2 / 10, y + size * 8 / 10,
                                          x + size * 2 / 10, y + size * 8 / 10, x + size * 2 / 10, y + size * 2 / 10,
                                          x + size * 8 / 10, y + size * 2 / 10, x + size * 8 / 10, y - size * 2 / 10,
                                          x + size * 2 / 10, y - size * 2 / 10, x + size * 2 / 10, y - size * 8 / 10,
                                          x - size * 2 / 10, y - size * 8 / 10, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B1koenig)
        self.shape_B1koenig=self.canvas.create_polygon(x - size * 2 / 10, y - size * 2 / 10, x - size * 2 / 10, y - size * 2 / 10,
                                          x - size * 8 / 10, y - size * 2 / 10, x - size * 8 / 10, y + size * 2 / 10,
                                          x - size * 2 / 10, y + size * 2 / 10, x - size * 2 / 10, y + size * 8 / 10,
                                          x + size * 2 / 10, y + size * 8 / 10, x + size * 2 / 10, y + size * 2 / 10,
                                          x + size * 8 / 10, y + size * 2 / 10, x + size * 8 / 10, y - size * 2 / 10,
                                          x + size * 2 / 10, y - size * 2 / 10, x + size * 2 / 10, y - size * 8 / 10,
                                          x - size * 2 / 10, y - size * 8 / 10, fill='black')

class Visual_W1Dame():
    def visualize(self, x, y, size):
        self.shape_W1dame=self.canvas.create_oval(x - size * 9 / 10, y - size * 9 / 10, x + size * 9 / 10, y + size * 9 / 10,fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W1dame)
        self.shape_W1dame=self.canvas.create_oval(x - size * 9 / 10, y - size * 9 / 10, x + size * 9 / 10, y + size * 9 / 10,fill='orange')
class Visual_B1Dame():
    def visualize(self, x, y, size):
        self.shape_B1dame=self.canvas.create_oval(x - size * 9 / 10, y - size * 9 / 10, x + size * 9 / 10, y + size * 9 / 10,fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B1dame)
        self.shape_B1bdame=self.canvas.create_oval(x - size * 9 / 10, y - size * 9 / 10, x + size * 9 / 10, y + size * 9 / 10,fill='black')

class Visual_W1Turm():
    def visualize(self, x, y, size):
        self.shape_W1turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W1turm)
        self.shape_W1turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='orange')

class Visual_W2Turm():
    def visualize(self, x, y, size):
        self.shape_W2turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W2turm)
        self.shape_W2turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='orange')

class Visual_B1Turm():
    def visualize(self, x, y, size):
        self.shape_B1turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B1turm)
        self.shape_B1turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='black')

class Visual_B2Turm():
    def visualize(self, x, y, size):
        self.shape_B2turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B2turm)
        self.shape_B2turm=self.canvas.create_rectangle(x - size * 4 / 5, y - size * 4 / 5, x + size * 4 / 5, y + size * 4 / 5,fill='black')

class Visual_W1Laeufer():
    def visualize(self, x, y, size):
        self.shape_W1laeufer=self.canvas.create_polygon(x, y - size * 3 / 4, x - size / 3, y + size * 3 / 4, x + size / 3,
                                          y + size * 3 / 4, x, y - size * 3 / 4, fill='orange')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_W1laeufer)
        self.shape_W1laeufer=self.canvas.create_polygon(x, y - size * 3 / 4, x - size / 3, y + size * 3 / 4, x + size / 3,
                                          y + size * 3 / 4, x, y - size * 3 / 4, fill='orange')

class Visual_W2Laeufer():
    def visualize(self, x, y, size):
        self.shape_W2laeufer=self.canvas.create_polygon(x, y - size * 3 / 4, x - size / 3, y + size * 3 / 4, x + size / 3,
                                          y + size * 3 / 4, x, y - size * 3 / 4, fill='orange')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_W2laeufer)
        self.shape_W2laeufer = self.canvas.create_polygon(x, y - size * 3 / 4, x - size / 3, y + size * 3 / 4, x + size / 3,
                                          y + size * 3 / 4, x, y - size * 3 / 4, fill='orange')

class Visual_B1Laeufer():
    def visualize(self, x, y, size):
        self.shape_B1laeufer=self.canvas.create_polygon(x, y + size * 3 / 4, x - size / 3, y - size * 3 / 4, x + size / 3,
                                          y - size * 3 / 4, x, y + size * 3 / 4, fill='black')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_B1laeufer)
        self.shape_B1laeufer = self.canvas.create_polygon(x, y + size * 3 / 4, x - size / 3, y - size * 3 / 4, x + size / 3,
                                          y - size * 3 / 4, x, y + size * 3 / 4, fill='black')

class Visual_B2Laeufer():
    def visualize(self, x, y, size):
        self.shape_B2laeufer=self.canvas.create_polygon(x, y + size * 3 / 4, x - size / 3, y - size * 3 / 4, x + size / 3,
                                          y - size * 3 / 4, x, y + size * 3 / 4, fill='black')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_B2laeufer)
        self.shape_B2laeufer = self.canvas.create_polygon(x, y + size * 3 / 4, x - size / 3, y - size * 3 / 4, x + size / 3,
                                          y - size * 3 / 4, x, y + size * 3 / 4, fill='black')

class Visual_W1Pferd():
    def visualize(self, x, y, size):
        self.shape_W1pferd=self.canvas.create_polygon(x, y - size * 8 / 10, x - size * 3 / 5, y - size * 2 / 5, x,
                                           y + size * 9 / 10, x + size * 3 / 5, y - size * 2 / 5, x, y - size * 8 / 10,
                                           fill='orange')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_W1pferd)
        self.shape_W1pferd=self.canvas.create_polygon(x, y - size * 8 / 10, x - size * 3 / 5, y - size * 2 / 5, x,
                                           y + size * 9 / 10, x + size * 3 / 5, y - size * 2 / 5, x, y - size * 8 / 10,
                                           fill='orange')

class Visual_W2Pferd():
    def visualize(self, x, y, size):
        self.shape_W2pferd=self.canvas.create_polygon(x, y - size * 8 / 10, x - size * 3 / 5, y - size * 2 / 5, x,
                                           y + size * 9 / 10, x + size * 3 / 5, y - size * 2 / 5, x, y - size * 8 / 10,
                                           fill='orange')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_W2pferd)
        self.shape_W2pferd=self.canvas.create_polygon(x, y - size * 8 / 10, x - size * 3 / 5, y - size * 2 / 5, x,
                                           y + size * 9 / 10, x + size * 3 / 5, y - size * 2 / 5, x, y - size * 8 / 10,
                                           fill='orange')

class Visual_B1Pferd():
    def visualize(self, x, y, size):
        self.shape_B1pferd=self.canvas.create_polygon(x, y + size * 9 / 10, x - size * 3 / 5, y + size * 2 / 5, x,
                                           y - size * 8 / 10, x + size * 3 / 5, y + size * 2 / 5, x, y + size * 9 / 10,
                                           fill='black')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_B1pferd)
        self.shape_B1pferd=self.canvas.create_polygon(x, y + size * 9 / 10, x - size * 3 / 5, y + size * 2 / 5, x,
                                           y - size * 8 / 10, x + size * 3 / 5, y + size * 2 / 5, x, y + size * 9 / 10,
                                           fill='black')

class Visual_B2Pferd():
    def visualize(self, x, y, size):
        self.shape_B2pferd=self.canvas.create_polygon(x, y + size * 9 / 10, x - size * 3 / 5, y + size * 2 / 5, x,
                                           y - size * 8 / 10, x + size * 3 / 5, y + size * 2 / 5, x, y + size * 9 / 10,
                                           fill='black')
    def move(self, x, y, size):
        self.canvas.delete(self.shape_B2pferd)
        self.shape_B2pferd=self.canvas.create_polygon(x, y + size * 9 / 10, x - size * 3 / 5, y + size * 2 / 5, x,
                                           y - size * 8 / 10, x + size * 3 / 5, y + size * 2 / 5, x, y + size * 9 / 10,
                                           fill='black')

class Visual_W1Bauer():
    def visualize(self, x, y, size):
        self.shape_W1bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W1bauer)
        self.shape_W1bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W2Bauer():
    def visualize(self, x, y, size):
        self.shape_W2bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W2bauer)
        self.shape_W2bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W3Bauer():
    def visualize(self, x, y, size):
        self.shape_W3bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W3bauer)
        self.shape_W3bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W4Bauer():
    def visualize(self, x, y, size):
        self.shape_W4bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W4bauer)
        self.shape_W4bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W5Bauer():
    def visualize(self, x, y, size):
        self.shape_W5bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W5bauer)
        self.shape_W5bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W6Bauer():
    def visualize(self, x, y, size):
        self.shape_W6bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W6bauer)
        self.shape_W6bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W7Bauer():
    def visualize(self, x, y, size):
        self.shape_W7bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W7bauer)
        self.shape_W7bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_W8Bauer():
    def visualize(self, x, y, size):
        self.shape_W8bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_W8bauer)
        self.shape_W8bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='orange')

class Visual_B1Bauer():
    def visualize(self, x, y, size):
        self.shape_B1bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B1bauer)
        self.shape_B1bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B2Bauer():
    def visualize(self, x, y, size):
        self.shape_B2bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B2bauer)
        self.shape_B2bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B3Bauer():
    def visualize(self, x, y, size):
        self.shape_B3bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B3bauer)
        self.shape_B3bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B4Bauer():
    def visualize(self, x, y, size):
        self.shape_B4bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B4bauer)
        self.shape_B4bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B5Bauer():
    def visualize(self, x, y, size):
        self.shape_B5bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B5bauer)
        self.shape_B5bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B6Bauer():
    def visualize(self, x, y, size):
        self.shape_B6bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B6bauer)
        self.shape_B6bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B7Bauer():
    def visualize(self, x, y, size):
        self.shape_B7bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B7bauer)
        self.shape_B7bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')

class Visual_B8Bauer():
    def visualize(self, x, y, size):
        self.shape_B8bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
    def move(self,x,y,size):
        self.canvas.delete(self.shape_B8bauer)
        self.shape_B8bauer=self.canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2, fill='black')
###end of Visual_Pieces classes

class Visual(Frame):

    def __init__(self): #case wurde entfernt
        super().__init__()
        #threading
        self.queue = queue.Queue()
        self.queue_choice= queue.Queue()
        self.queue_destination = queue.Queue()
        #gui
        self.factor = 2
        self.size = self.factor * 20
        self.x, self.y = self.factor * 20, self.factor * 20
        self.player_choice=0
        self.destination_choice=[]
        self.marker_counter = 0
        self.white_dead = 0
        self.black_dead = 0
        #start drawing
        self.canvas = Canvas(self)
        self.physical_brett=self.draw_Board()#setup the board. physical_brett is the list with information about the location in pixel of every single field of the physical (GUI) board
        self.showtheUpdate(self.physical_brett, b.Board.createBoard(self), 0)

        self.button1 = Button(self.canvas, text="Start", command=self.spawnthread)
        self.button1.pack(padx=10, pady=10)

        self.canvas.pack(fill=BOTH, expand=1) #end drawing

    ###threading functions start
    def spawnthread(self):
        self.button1.config(state="disabled")
        self.thread = ThreadedClient(self.queue,self.queue_choice,self.queue_destination)
        self.thread.start()
        self.update()

    def update(self):
        def locate0(event):
            x, y = event.x, event.y
            self.chooseInhabitantofField(x,y,self.physical_brett,self.marker_counter)
            self.marker_counter=1
        def locate1(event):
            x, y = event.x, event.y
            meta = self.queue.get()
            self.queue.put([meta[0]])
            self.chooseField(x,y,self.physical_brett,self.marker_counter,meta[0])
            print(self.queue.qsize())
            self.marker_counter=1
        self.canvas.bind("<Button-1>", locate0)
        self.canvas.bind("<Button-2>", locate1)
        self.button2 = Button(self.canvas, text="Submit",command=lambda:self.showtheUpdate(self.physical_brett, self.queue.get()[0],1))

        self.button2.pack()

    ###threading functions end


    ###gui functions begin

    def chooseField(self,x,y,physical_brett,counter,meta): #only the coordinates f.i. D3 get selected
        for element in physical_brett:
            if (x <= element[1] + self.size * 1 / 2 and x >= element[1] - self.size * 1 / 2) and (
                    y <= element[2] + self.size * 1 / 2 and y >= element[2] - self.size * 1 / 2):
                n=element[0]
                break
        self.destination_choice=[meta[n][0],meta[n][1]]
        self.queue_destination.put(self.destination_choice)
        self.markaField(n,x,y,physical_brett,counter,'yellow')

    def chooseInhabitantofField(self,x,y,physical_brett,counter): #only the number(f.i. field 10 (indirectly W3bauer)) of the field gets selected
        for element in physical_brett:
            if (x <= element[1] + self.size * 1 / 2 and x >= element[1] - self.size * 1 / 2) and (
                    y <= element[2] + self.size * 1 / 2 and y >= element[2] - self.size * 1 / 2):
                n=element[0]
                break
        self.player_choice=n
        self.queue_choice.put(self.player_choice)
        self.markaField(n,x,y,physical_brett,counter,'blue')

    def markaField(self,n,x,y,physical_brett,counter,color):
        if counter==0:
            self.marker = self.canvas.create_rectangle(physical_brett[n][1]-self.size*1/2, physical_brett[n][2]-self.size*1/2, physical_brett[n][1] + self.size*1/2, physical_brett[n][2] + self.size*1/2, outline=color, width=3) #  PROJECT MARKING A FIELD THAT IS INHABITED
        elif counter!=0:
            self.canvas.delete(self.marker)  # Delete the rectangle
            self.marker = self.canvas.create_rectangle(physical_brett[n][1]-self.size*1/2, physical_brett[n][2]-self.size*1/2, physical_brett[n][1] + self.size*1/2, physical_brett[n][2] + self.size*1/2, outline=color, width=3) #  PROJECT MARKING A FIELD THAT IS INHABITED

    def givePixelLocation(self, player, sol, meta): #looks for the current location of a figure and returns its coordinates
        # physical_brett = b.Board.createBoard(self)
        physical_brett = meta
        life=True
        n = 0
        for element in physical_brett:
            if element[2] == player:
                break
            n += 1
        if n!=64:
            physicalBoard = sol
            element = physicalBoard[n]
            x, y = element[1], element[2]
            return x, y, life
        else:
            life=False
            if player[0]=='W':
                x,y=self.white_dead*self.size*2/3 +self.size, 20
                self.white_dead+=1
                return  x,y,life
            else:
                x, y = self.black_dead * self.size*2/3 + self.size, 380
                self.black_dead += 1
                return x,y,life

    def draw_Board(self):
        self.master.title("FOXCHESS")
        self.pack(fill=BOTH, expand=1)
        start,ende=self.x,self.y
        meta_Board=[]
        n=0
        for row in range(1,9):
            if row%2!=0:
                for col in range(1,9):
                    if col%2==0:
                        self.canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill='brown')
                        meta_Board.append([n,self.x+self.size/2,self.y+self.size/2])
                    else:
                        self.canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill='white')
                        meta_Board.append([n,self.x+self.size/2,self.y+self.size/2])
                    self.x+=self.size
                    n+=1
            else:
                for col in range(1,9):
                    if col%2==0:
                        self.canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,fill='white')
                        meta_Board.append([n,self.x+self.size/2,self.y+self.size/2])
                    else:
                        self.canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill='brown')
                        meta_Board.append([n,self.x+self.size/2,self.y+self.size/2])
                    self.x+=self.size
                    n+=1
            self.y+=self.size
            self.x=start


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
    def showtheUpdate(self,sol,meta,case): #sol is the list with information about the location in pixel of every single field of the physical (GUI) board
        print(meta)
        print('BEFORE VISUALIZING')
        print(self.queue.qsize())
        if case==0:

            #white
            coordinates_W1koenig = self.givePixelLocation('W1koenig',sol,meta)
            Visual_W1Koenig.visualize(self, coordinates_W1koenig[0], coordinates_W1koenig[1], self.size*1/2)
            coordinates_W1dame=self.givePixelLocation('W1dame',sol,meta)
            Visual_W1Dame.visualize(self,coordinates_W1dame[0],coordinates_W1dame[1], self.size*1/2)
            coordinates_W1turm = self.givePixelLocation('W1turm',sol,meta)
            Visual_W1Turm.visualize(self, coordinates_W1turm[0], coordinates_W1turm[1], self.size*1/2)
            coordinates_W2turm = self.givePixelLocation('W2turm',sol,meta)
            Visual_W2Turm.visualize(self, coordinates_W2turm[0], coordinates_W2turm[1], self.size*1/2)
            coordinates_W1laeufer = self.givePixelLocation('W1laeufer',sol,meta)
            Visual_W1Laeufer.visualize(self, coordinates_W1laeufer[0], coordinates_W1laeufer[1], self.size*1/2)
            coordinates_W2laeufer = self.givePixelLocation('W2laeufer',sol,meta)
            Visual_W2Laeufer.visualize(self, coordinates_W2laeufer[0], coordinates_W2laeufer[1], self.size*1/2)
            coordinates_W1pferd = self.givePixelLocation('W1pferd',sol,meta)
            Visual_W1Pferd.visualize(self, coordinates_W1pferd[0], coordinates_W1pferd[1], self.size*1/2)
            coordinates_W2pferd = self.givePixelLocation('W2pferd',sol,meta)
            Visual_W2Pferd.visualize(self, coordinates_W2pferd[0], coordinates_W2pferd[1], self.size*1/2)
            coordinates_W1bauer = self.givePixelLocation('W1bauer',sol,meta)
            coordinates_W2bauer = self.givePixelLocation('W2bauer',sol,meta)
            coordinates_W3bauer = self.givePixelLocation('W3bauer',sol,meta)
            coordinates_W4bauer = self.givePixelLocation('W4bauer',sol,meta)
            coordinates_W5bauer = self.givePixelLocation('W5bauer',sol,meta)
            coordinates_W6bauer = self.givePixelLocation('W6bauer',sol,meta)
            coordinates_W7bauer = self.givePixelLocation('W7bauer',sol,meta)
            coordinates_W8bauer = self.givePixelLocation('W8bauer',sol,meta)
            Visual_W1Bauer.visualize(self, coordinates_W1bauer[0], coordinates_W1bauer[1], self.size*1/2)
            Visual_W2Bauer.visualize(self, coordinates_W2bauer[0], coordinates_W2bauer[1], self.size*1/2)
            Visual_W3Bauer.visualize(self, coordinates_W3bauer[0], coordinates_W3bauer[1], self.size*1/2)
            Visual_W4Bauer.visualize(self, coordinates_W4bauer[0], coordinates_W4bauer[1], self.size*1/2)
            Visual_W5Bauer.visualize(self, coordinates_W5bauer[0], coordinates_W5bauer[1], self.size*1/2)
            Visual_W6Bauer.visualize(self, coordinates_W6bauer[0], coordinates_W6bauer[1], self.size*1/2)
            Visual_W7Bauer.visualize(self, coordinates_W7bauer[0], coordinates_W7bauer[1], self.size*1/2)
            Visual_W8Bauer.visualize(self, coordinates_W8bauer[0], coordinates_W8bauer[1], self.size*1/2)
            # #black
            coordinates_B1koenig = self.givePixelLocation('B1koenig',sol,meta)
            Visual_B1Koenig.visualize(self, coordinates_B1koenig[0], coordinates_B1koenig[1], self.size*1/2)
            coordinates_B1dame = self.givePixelLocation('B1dame',sol,meta)
            Visual_B1Dame.visualize(self, coordinates_B1dame[0], coordinates_B1dame[1], self.size*1/2)
            coordinates_B1turm = self.givePixelLocation('B1turm',sol,meta)
            Visual_B1Turm.visualize(self, coordinates_B1turm[0], coordinates_B1turm[1], self.size*1/2)
            coordinates_B2turm = self.givePixelLocation('B2turm',sol,meta)
            Visual_B2Turm.visualize(self, coordinates_B2turm[0], coordinates_B2turm[1], self.size*1/2)
            coordinates_B1laeufer = self.givePixelLocation('B1laeufer',sol,meta)
            Visual_B1Laeufer.visualize(self, coordinates_B1laeufer[0], coordinates_B1laeufer[1], self.size*1/2)
            coordinates_B2laeufer = self.givePixelLocation('B2laeufer',sol,meta)
            Visual_B2Laeufer.visualize(self, coordinates_B2laeufer[0], coordinates_B2laeufer[1], self.size*1/2)
            coordinates_B1pferd = self.givePixelLocation('B1pferd',sol,meta)
            Visual_B1Pferd.visualize(self, coordinates_B1pferd[0], coordinates_B1pferd[1], self.size*1/2)
            coordinates_B2pferd = self.givePixelLocation('B2pferd',sol,meta)
            Visual_B2Pferd.visualize(self, coordinates_B2pferd[0], coordinates_B2pferd[1], self.size*1/2)
            coordinates_B1bauer = self.givePixelLocation('B1bauer',sol,meta)
            coordinates_B2bauer = self.givePixelLocation('B2bauer',sol,meta)
            coordinates_B3bauer = self.givePixelLocation('B3bauer',sol,meta)
            coordinates_B4bauer = self.givePixelLocation('B4bauer',sol,meta)
            coordinates_B5bauer = self.givePixelLocation('B5bauer',sol,meta)
            coordinates_B6bauer = self.givePixelLocation('B6bauer',sol,meta)
            coordinates_B7bauer = self.givePixelLocation('B7bauer',sol,meta)
            coordinates_B8bauer = self.givePixelLocation('B8bauer',sol,meta)
            Visual_B1Bauer.visualize(self, coordinates_B1bauer[0], coordinates_B1bauer[1], self.size*1/2)
            Visual_B2Bauer.visualize(self, coordinates_B2bauer[0], coordinates_B2bauer[1], self.size*1/2)
            Visual_B3Bauer.visualize(self, coordinates_B3bauer[0], coordinates_B3bauer[1], self.size*1/2)
            Visual_B4Bauer.visualize(self, coordinates_B4bauer[0], coordinates_B4bauer[1], self.size*1/2)
            Visual_B5Bauer.visualize(self, coordinates_B5bauer[0], coordinates_B5bauer[1], self.size*1/2)
            Visual_B6Bauer.visualize(self, coordinates_B6bauer[0], coordinates_B6bauer[1], self.size*1/2)
            Visual_B7Bauer.visualize(self, coordinates_B7bauer[0], coordinates_B7bauer[1], self.size*1/2)
            Visual_B8Bauer.visualize(self, coordinates_B8bauer[0], coordinates_B8bauer[1], self.size*1/2)

        else:
            # white
            coordinates_W1koenig = self.givePixelLocation('W1koenig', sol, meta)
            Visual_W1Koenig.move(self, coordinates_W1koenig[0], coordinates_W1koenig[1], self.size * 1 / 2)
            coordinates_W1dame = self.givePixelLocation('W1dame', sol, meta)
            Visual_W1Dame.move(self, coordinates_W1dame[0], coordinates_W1dame[1], self.size * 1 / 2)
            coordinates_W1turm = self.givePixelLocation('W1turm', sol, meta)
            Visual_W1Turm.move(self, coordinates_W1turm[0], coordinates_W1turm[1], self.size * 1 / 2)
            coordinates_W2turm = self.givePixelLocation('W2turm', sol, meta)
            Visual_W2Turm.move(self, coordinates_W2turm[0], coordinates_W2turm[1], self.size * 1 / 2)
            coordinates_W1laeufer = self.givePixelLocation('W1laeufer', sol, meta)
            Visual_W1Laeufer.move(self, coordinates_W1laeufer[0], coordinates_W1laeufer[1], self.size * 1 / 2)
            coordinates_W2laeufer = self.givePixelLocation('W2laeufer', sol, meta)
            Visual_W2Laeufer.move(self, coordinates_W2laeufer[0], coordinates_W2laeufer[1], self.size * 1 / 2)
            coordinates_W1pferd = self.givePixelLocation('W1pferd', sol, meta)
            Visual_W1Pferd.move(self, coordinates_W1pferd[0], coordinates_W1pferd[1], self.size * 1 / 2)
            coordinates_W2pferd = self.givePixelLocation('W2pferd', sol, meta)
            Visual_W2Pferd.move(self, coordinates_W2pferd[0], coordinates_W2pferd[1], self.size * 1 / 2)
            coordinates_W1bauer = self.givePixelLocation('W1bauer', sol, meta)
            coordinates_W2bauer = self.givePixelLocation('W2bauer', sol, meta)
            coordinates_W3bauer = self.givePixelLocation('W3bauer', sol, meta)
            coordinates_W4bauer = self.givePixelLocation('W4bauer', sol, meta)
            coordinates_W5bauer = self.givePixelLocation('W5bauer', sol, meta)
            coordinates_W6bauer = self.givePixelLocation('W6bauer', sol, meta)
            coordinates_W7bauer = self.givePixelLocation('W7bauer', sol, meta)
            coordinates_W8bauer = self.givePixelLocation('W8bauer', sol, meta)
            Visual_W1Bauer.move(self, coordinates_W1bauer[0], coordinates_W1bauer[1], self.size * 1 / 2)
            Visual_W2Bauer.move(self, coordinates_W2bauer[0], coordinates_W2bauer[1], self.size * 1 / 2)
            Visual_W3Bauer.move(self, coordinates_W3bauer[0], coordinates_W3bauer[1], self.size * 1 / 2)
            Visual_W4Bauer.move(self, coordinates_W4bauer[0], coordinates_W4bauer[1], self.size * 1 / 2)
            Visual_W5Bauer.move(self, coordinates_W5bauer[0], coordinates_W5bauer[1], self.size * 1 / 2)
            Visual_W6Bauer.move(self, coordinates_W6bauer[0], coordinates_W6bauer[1], self.size * 1 / 2)
            Visual_W7Bauer.move(self, coordinates_W7bauer[0], coordinates_W7bauer[1], self.size * 1 / 2)
            Visual_W8Bauer.move(self, coordinates_W8bauer[0], coordinates_W8bauer[1], self.size * 1 / 2)
            # #black
            coordinates_B1koenig = self.givePixelLocation('B1koenig', sol, meta)
            Visual_B1Koenig.move(self, coordinates_B1koenig[0], coordinates_B1koenig[1], self.size * 1 / 2)
            coordinates_B1dame = self.givePixelLocation('B1dame', sol, meta)
            Visual_B1Dame.move(self, coordinates_B1dame[0], coordinates_B1dame[1], self.size * 1 / 2)
            coordinates_B1turm = self.givePixelLocation('B1turm', sol, meta)
            Visual_B1Turm.move(self, coordinates_B1turm[0], coordinates_B1turm[1], self.size * 1 / 2)
            coordinates_B2turm = self.givePixelLocation('B2turm', sol, meta)
            Visual_B2Turm.move(self, coordinates_B2turm[0], coordinates_B2turm[1], self.size * 1 / 2)
            coordinates_B1laeufer = self.givePixelLocation('B1laeufer', sol, meta)
            Visual_B1Laeufer.move(self, coordinates_B1laeufer[0], coordinates_B1laeufer[1], self.size * 1 / 2)
            coordinates_B2laeufer = self.givePixelLocation('B2laeufer', sol, meta)
            Visual_B2Laeufer.move(self, coordinates_B2laeufer[0], coordinates_B2laeufer[1], self.size * 1 / 2)
            coordinates_B1pferd = self.givePixelLocation('B1pferd', sol, meta)
            Visual_B1Pferd.move(self, coordinates_B1pferd[0], coordinates_B1pferd[1], self.size * 1 / 2)
            coordinates_B2pferd = self.givePixelLocation('B2pferd', sol, meta)
            Visual_B2Pferd.move(self, coordinates_B2pferd[0], coordinates_B2pferd[1], self.size * 1 / 2)
            coordinates_B1bauer = self.givePixelLocation('B1bauer', sol, meta)
            coordinates_B2bauer = self.givePixelLocation('B2bauer', sol, meta)
            coordinates_B3bauer = self.givePixelLocation('B3bauer', sol, meta)
            coordinates_B4bauer = self.givePixelLocation('B4bauer', sol, meta)
            coordinates_B5bauer = self.givePixelLocation('B5bauer', sol, meta)
            coordinates_B6bauer = self.givePixelLocation('B6bauer', sol, meta)
            coordinates_B7bauer = self.givePixelLocation('B7bauer', sol, meta)
            coordinates_B8bauer = self.givePixelLocation('B8bauer', sol, meta)
            Visual_B1Bauer.move(self, coordinates_B1bauer[0], coordinates_B1bauer[1], self.size * 1 / 2)
            Visual_B2Bauer.move(self, coordinates_B2bauer[0], coordinates_B2bauer[1], self.size * 1 / 2)
            Visual_B3Bauer.move(self, coordinates_B3bauer[0], coordinates_B3bauer[1], self.size * 1 / 2)
            Visual_B4Bauer.move(self, coordinates_B4bauer[0], coordinates_B4bauer[1], self.size * 1 / 2)
            Visual_B5Bauer.move(self, coordinates_B5bauer[0], coordinates_B5bauer[1], self.size * 1 / 2)
            Visual_B6Bauer.move(self, coordinates_B6bauer[0], coordinates_B6bauer[1], self.size * 1 / 2)
            Visual_B7Bauer.move(self, coordinates_B7bauer[0], coordinates_B7bauer[1], self.size * 1 / 2)
            Visual_B8Bauer.move(self, coordinates_B8bauer[0], coordinates_B8bauer[1], self.size * 1 / 2)
        print('AFTER VISUALIZING')
        print(self.queue.qsize())
def main():
    root = Tk()
    root.geometry("400x400")
    board = Visual()
    root.mainloop()

if __name__== "__main__":
  main()


