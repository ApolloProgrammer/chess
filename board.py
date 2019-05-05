#Developer: Marvin Fuchs, May 2019
class Board:
    def __init__(self):
        self.board = self.createBoard()
    def createBoard(self):
        self.board=[]
        spalten='ABCDEFGH'
        for spalte in spalten:
            for i in range(1,9):
                # if i%2==0:
                self.board.append([spalte,i,'.......'])
                # else:
                    # self.board.append([spalte,i,'empty',1])
        #white
        self.board[0][2]='W1turm'
        self.board[1][2]='W1pferd'
        self.board[2][2]='W1laeufer'
        self.board[3][2]='W1dame'
        self.board[4][2]='W1koenig'
        self.board[5][2]='W2laeufer'
        self.board[6][2]='W2pferd'
        self.board[7][2]='W2turm'

        self.board[8][2]='W1bauer'
        self.board[9][2]='W2bauer'
        self.board[10][2]='W3bauer'
        self.board[11][2]='W4bauer'
        self.board[12][2]='W5bauer'
        self.board[13][2]='W6bauer'
        self.board[14][2]='W7bauer'
        self.board[15][2]='W8bauer'
        #black
        self.board[48][2]='B1bauer'
        self.board[49][2]='B2bauer'
        self.board[50][2]='B3bauer'
        self.board[51][2]='B4bauer'
        self.board[52][2]='B5bauer'
        self.board[53][2]='B6bauer'
        self.board[54][2]='B7bauer'
        self.board[55][2]='B8bauer'

        self.board[56][2]='B1turm'
        self.board[57][2]='B1pferd'
        self.board[58][2]='B1laeufer'
        self.board[59][2]='B1dame'
        self.board[60][2]='B1koenig'
        self.board[61][2]='B2laeufer'
        self.board[62][2]='B2pferds'
        self.board[63][2]='B2turm'

        return self.board

    def showDataofBoard(self): #1 8   9 16   17 25   26 32   33 39   40 46  47 55  56 64 in reverse
        for i in range(7,-1,-1):
            zeile=[]
            geschickteListe=range((8*i)+1,(8*(i+1)+1))
            for j in geschickteListe:
                newElement=self.board[j-1]
                zeile.append(newElement)
            print(zeile)
            zeile[:]=[]

    def giveStatusofField(self,x,y):
        pos=[x,y]
        status=''
        for field in self.board:
            if field[0]==pos[0] and field[1]==pos[1]:
                status=field[2]
                break
        return status

    def givePostionofFigure(self,figure):
        for field in self.board:
            pos=[]
            if field[2]==figure:
                pos.append(field[0])
                pos.append(field[1])
                break
        return pos

    def changeAfield(self,x,y,newStatus): #method changes a specific field(y,x) to a certain status f.i. 'W1koenig'->'.......'
        pos=[x,y]
        for field in self.board:
            if field[0]==pos[0] and field[1]==pos[1]:
                field[2]=newStatus
                break

    def translateLettertoNumber(self,letter):
        dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        return dic.get(letter)

    def translateNumbertoLetter(self,number):
        dic = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
        return dic.get(number)

    def givepotentialTurmDestination(self,x,y,x_des,y_des): #method checks wether the given move of a tower is legit or not. If not, then it shows approved moves.
        potentialFields=[]
        x_letter = Board.translateNumbertoLetter(self, x)
        x_des_letter = Board.translateNumbertoLetter(self, x_des)
        status_quo = Board.giveStatusofField(self, x_letter, y)

        ownTeam=''
        opponent=''
        if status_quo[0]=='W':
            ownTeam = 'W'
            opponent = 'B'
        else:
            ownTeam = 'B'
            opponent = 'W'


        for field in self.board:
            #adding all possible fields without jumping to the list
            if status_quo[0] == ownTeam:
                if (x_letter == field[0] and y != field[1]) or (x_letter != field[0] and y == field[1]): #positions governed by own players are no potential fields
                    potentialFields.append(field)

        #Prohibiting phenomenon of Jumping
        potentialZeile = []
        potentialSpalte = []
        for element in potentialFields:
            if element[0]==x_letter and element[1]!=y:
                potentialZeile.append(element)
            else:
                potentialSpalte.append(element)

        #Spalte
        Spalte = []
        for element in potentialSpalte[x-1:7:1]: #0 1 2 (3) 3 4 5 6
            if element[2][0]!=ownTeam:
                if element[2][0]=='.':
                    Spalte.append(element)
                elif element[2][0]==ownTeam:
                    Spalte.append(element)
                    break
            else:
                break

        if x>1:
            for element in potentialSpalte[x-2::-1]:
                if element[2][0]!=ownTeam:
                    if element[2][0]=='.':
                        Spalte.append(element)
                    elif element[2][0]==opponent:
                        Spalte.append(element)
                        break
                else:                               #W und B veraölgemeinernn!! damit das auch fur schwarz funktioniert!!!
                    break

        #Zeile
        Zeile = []
        for element in potentialZeile[y-1:7:1]: #0 1 2 (3) 3 4 5 6
            if element[2][0]!=ownTeam:
                if element[2][0]=='.':
                    Zeile.append(element)
                elif element[2][0]==opponent:
                    Zeile.append(element)
                    break
            else:
                break

        if y>1:
            for element in potentialZeile[y-2::-1]:
                if element[2][0]!=ownTeam:
                    if element[2][0]=='.':
                        Zeile.append(element)
                    elif element[2][0]==opponent:
                        Zeile.append(element)
                        break
                else:                               #W und B veraölgemeinernn!! damit das auch fur schwarz funktioniert!!!
                    break

        potentialFields=Zeile+Spalte
        for potentialField in potentialFields:
            if x_des_letter == potentialField[0] and y_des == potentialField[1]:
                return True,potentialFields
                break
        return False,potentialFields


