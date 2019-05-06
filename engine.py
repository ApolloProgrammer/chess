#Developer: Marvin Fuchs, May 2019

import board as b
import whitePlayer as white
import blackPlayer as black

class Engine(white.W1koenig):
    def __init__(self):
        b.Board.__init__(self)
        #white
        white.W1turm.__init__(self)
        white.W1pferd.__init__(self)
        white.W1laeufer.__init__(self)
        white.W1dame.__init__(self)
        white.W1koenig.__init__(self)
        white.W2laeufer.__init__(self)
        white.W2pferd.__init__(self)
        white.W2turm.__init__(self)

        white.W1bauer.__init__(self)
        white.W2bauer.__init__(self)
        white.W3bauer.__init__(self)
        white.W4bauer.__init__(self)
        white.W5bauer.__init__(self)
        white.W6bauer.__init__(self)
        white.W7bauer.__init__(self)
        white.W8bauer.__init__(self)
        #black
        black.B1bauer.__init__(self)
        black.B2bauer.__init__(self)
        black.B3bauer.__init__(self)
        black.B4bauer.__init__(self)
        black.B5bauer.__init__(self)
        black.B6bauer.__init__(self)
        black.B7bauer.__init__(self)
        black.B8bauer.__init__(self)

        black.B1turm.__init__(self)
        black.B1pferd.__init__(self)
        black.B1laeufer.__init__(self)
        black.B1dame.__init__(self)
        black.B1koenig.__init__(self)
        black.B2laeufer.__init__(self)
        black.B2pferd.__init__(self)
        black.B2turm.__init__(self)


    def play(self):
        b.Board.showDataofBoard(self)

        counter = 0
        while True:
            if counter%2==0:
                print("Its the turn of Player 1! (White)")
                print('Please write what figure you choose to move: W1koenig, etc...')
                choice=input()
                if  choice == 'W1koenig':
                    white.W1koenig.move(self)
                    b.Board.showDataofBoard(self)
                    counter+=1
                    print(counter)
                elif  choice == 'W1dame':
                    white.W1dame.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W1laeufer':
                    white.W1laeufer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W2laeufer':
                    white.W2laeufer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W1pferd':
                    white.W1pferd.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W2pferd':
                    white.W2pferd.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W1turm':
                    white.W1turm.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W2turm':
                    white.W2turm.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W1bauer':
                    white.W1bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W2bauer':
                    white.W2bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W3bauer':
                    white.W3bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W4bauer':
                    white.W4bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W5bauer':
                    white.W5bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W6bauer':
                    white.W6bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W7bauer':
                    white.W7bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'W8bauer':
                    white.W8bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                else:
                    print ('please choose again')
            #turn of Player2(black)
            else:
                print("Its the turn of Player 2! (Black)")
                print('Please write what figure you choose to move: B1koenig, etc...')
                choice = input()
                if choice == 'B1koenig':
                    black.B1koenig.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B1dame':
                    black.B1dame.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B1laeufer':
                    black.B1laeufer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B2laeufer':
                    black.B2laeufer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B1pferd':
                    black.B1pferd.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B2pferd':
                    black.B2pferd.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B1turm':
                    black.B1turm.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B2turm':
                    black.B2turm.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B1bauer':
                    black.B1bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B2bauer':
                    black.B2bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B3bauer':
                    black.B3bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B4bauer':
                    black.B4bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B5bauer':
                    black.B5bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B6bauer':
                    black.B6bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B7bauer':
                    black.B7bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                elif  choice == 'B8bauer':
                    black.B8bauer.move(self)
                    b.Board.showDataofBoard(self)
                    counter += 1
                else:
                    print('please choose again')
