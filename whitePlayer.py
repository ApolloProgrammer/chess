#Developer: Marvin Fuchs, May 2019
import threading
import queue
import time
import board as b
import engine as e


class W1koenig(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WK = 'A'
        self.position_y_WK = 5
        self.name_WK='W1koenig'
        self.WK1_wrongDestination=0

    def move(self):
        while True:
                self.WK1_wrongDestination = 0
                print ('Give a x (letter) and y (number) coordinate for WHITE KING!')
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_WK = destination[0]
                destination_y_WK = destination[1]

                if b.Board.giveStatusofField(self,destination_x_WK,destination_y_WK)[0]!='W':
                    print('Current position is: '+self.position_x_WK+' '+str(self.position_y_WK))


                    #logic
                    x_pos=b.Board.translateLettertoNumber(self,self.position_x_WK)
                    x_des=b.Board.translateLettertoNumber(self,destination_x_WK)

                    if ( abs(x_pos-x_des) <2 and abs(self.position_y_WK-destination_y_WK) < 2 ):
                        b.Board.changeAfield(self,self.position_x_WK,self.position_y_WK,'.......')
                        self.position_x_WK = destination_x_WK
                        self.position_y_WK = destination_y_WK
                        print('New position is: '+self.position_x_WK+' '+str(self.position_y_WK))
                        b.Board.changeAfield(self,self.position_x_WK,self.position_y_WK,self.name_WK)
                        return self.board
                        break

                    else:
                        self.WK1_wrongDestination = 1
                        print('Your move is invalid, please choose cooridnates again!')
                        break
                else:
                    self.WK1_wrongDestination = 1
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WK,destination_y_WK))+'.')
                    break

class W1dame(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WD = 'A'
        self.position_y_WD = 4
        self.name_WD='W1dame'
        self.WD1_wrongDestination=0

    def move(self):
        while True:
                self.WD1_wrongDestination = 0
                print ('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_WD = destination[0]
                destination_y_WD = destination[1]

                if b.Board.giveStatusofField(self,destination_x_WD,destination_y_WD)[0]!='W':
                    print('Current position is: '+self.position_x_WD+' '+str(self.position_y_WD))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_WD)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_WD)
                    y_pos = self.position_y_WD
                    y_des = destination_y_WD
                    controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)
                    controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                    if controll_Diagonal == True or controll_Cross == True:
                        b.Board.changeAfield(self, self.position_x_WD, self.position_y_WD, '.......')
                        self.position_x_WD = destination_x_WD
                        self.position_y_WD = destination_y_WD
                        print('New position is: ' + self.position_x_WD + ' ' + str(self.position_y_WD))
                        b.Board.changeAfield(self, self.position_x_WD, self.position_y_WD, self.name_WD)
                        return self.board
                        break

                    else:
                        self.WD1_wrongDestination = 1
                        print('Your move is invalid, please choose cooridnates again!')
                        print('These are your options:')
                        if controll_Cross == False and controll_Diagonal == False:
                            print('Diagonal options:')

                            print('Diagonal1')
                            for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                print(element)
                            print('Diagonal2')
                            for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                print(element)

                            print('Cross options')
                            potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                            for element in potentialFields:
                                print(element)
                        elif controll_Diagonal==False or controll_Cross==False:
                            if controll_Cross == False:
                                potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                            else:
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                    print(element)
                        break
                else:
                    self.WD1_wrongDestination = 1
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WD,destination_y_WD))+'.')
                    break

class W1laeufer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WL1 = 'A'
        self.position_y_WL1 = 3
        self.name_WL1='W1laeufer'
        self.WL1_wrongDestination=0

    def move(self):
        while True:
                self.WL1_wrongDestination = 0
                print ('Give a x (letter) and y (number) coordinate for WHITE1 LAUFER!')
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_WL1 = destination[0]
                destination_y_WL1 = destination[1]

                if b.Board.giveStatusofField(self,destination_x_WL1,destination_y_WL1)[0]!='W':
                    print('Current position is: '+self.position_x_WL1+' '+str(self.position_y_WL1))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_WL1)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_WL1)
                    y_pos = self.position_y_WL1
                    y_des = destination_y_WL1
                    controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                    if controll == True:
                        b.Board.changeAfield(self, self.position_x_WL1, self.position_y_WL1, '.......')
                        self.position_x_WL1 = destination_x_WL1
                        self.position_y_WL1 = destination_y_WL1
                        print('New position is: ' + self.position_x_WL1 + ' ' + str(self.position_y_WL1))
                        b.Board.changeAfield(self, self.position_x_WL1, self.position_y_WL1, self.name_WL1)
                        return self.board
                        break

                    else:
                        self.WL1_wrongDestination = 1
                        print('Your move is invalid, please choose cooridnates again!')
                        print('These are your options:')
                        print('Diagonal1')
                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                            print(element)
                        print('Diagonal2')
                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                            print(element)
                        break
                else:
                    self.WL1_wrongDestination = 1
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WL1,destination_y_WL1))+'.')
                    break

class W2laeufer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WL2 = 'A'
        self.position_y_WL2 = 6
        self.name_WL2 = 'W2laeufer'
        self.WL2_wrongDestination=0


    def move(self):
        while True:
            self.WL2_wrongDestination = 0
            print('Give a x (letter) and y (number) coordinate for WHITE2 LAUFER!')
            destination = e.Engine.__getattribute__(self, 'destination_choice')

            destination_x_WL2 = destination[0]
            destination_y_WL2 = destination[1]

            if b.Board.giveStatusofField(self, destination_x_WL2, destination_y_WL2)[0] != 'W':
                print('Current position is: ' + self.position_x_WL2 + ' ' + str(self.position_y_WL2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WL2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WL2)
                y_pos = self.position_y_WL2
                y_des = destination_y_WL2
                controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                if controll == True:
                    b.Board.changeAfield(self, self.position_x_WL2, self.position_y_WL2, '.......')
                    self.position_x_WL2 = destination_x_WL2
                    self.position_y_WL2 = destination_y_WL2
                    print('New position is: ' + self.position_x_WL2 + ' ' + str(self.position_y_WL2))
                    b.Board.changeAfield(self, self.position_x_WL2, self.position_y_WL2, self.name_WL2)
                    return self.board
                    break

                else:
                    self.WL2_wrongDestination = 1
                    print('Your move is invalid, please choose cooridnates again!')
                    print('These are your options:')
                    print('Diagonal1')
                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                        print(element)
                    print('Diagonal2')
                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                        print(element)
                    break
            else:
                self.WL2_wrongDestination = 1
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_WL2, destination_y_WL2)) + '.')
                break

class W1pferd(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WP1 = 'A'
        self.position_y_WP1 = 2
        self.name_WP1='W1pferd'
        self.WP1_wrongDestination=0

    def move(self):
        while True:
                self.WP1_wrongDestination = 0
                print ('Give a x (letter) and y (number) coordinate for WHITE1 PFERD!')
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_WP1 = destination[0]
                destination_y_WP1 = destination[1]

                if b.Board.giveStatusofField(self,destination_x_WP1,destination_y_WP1)[0]!='W':
                    print('Current position is: '+self.position_x_WP1+' '+str(self.position_y_WP1))

                    #logic
                    x_pos=b.Board.translateLettertoNumber(self,self.position_x_WP1)
                    x_des=b.Board.translateLettertoNumber(self,destination_x_WP1)
                    y_pos=self.position_y_WP1
                    y_des=destination_y_WP1

                    if ( (x_pos + 2 == x_des or x_pos - 2 == x_des) and (y_pos + 1 == y_des or y_pos - 1 == y_des) or
                         (x_pos + 1 == x_des or x_pos - 1 == x_des) and (y_pos + 2 == y_des or y_pos - 2 == y_des)):

                        b.Board.changeAfield(self,self.position_x_WP1,self.position_y_WP1,'.......')
                        self.position_x_WP1 = destination_x_WP1
                        self.position_y_WP1 = destination_y_WP1
                        print('New position is: '+self.position_x_WP1+' '+str(self.position_y_WP1))
                        b.Board.changeAfield(self,self.position_x_WP1,self.position_y_WP1,self.name_WP1)
                        return self.board
                        break

                    else:
                        self.WP1_wrongDestination = 1
                        print('Your move is invalid, please choose cooridnates again!')
                        break
                else:
                    self.WP1_wrongDestination = 1
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WP1,destination_y_WP1))+'.')
                    break

class W2pferd(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WP2 = 'A'
        self.position_y_WP2 = 7
        self.name_WP2= 'W2pferd'
        self.WP2_wrongDestination = 0

    def move(self):
        while True:
            self.WP2_wrongDestination = 0
            print('Give a x (letter) and y (number) coordinate for WHITE2 PFERD!')
            
            destination = e.Engine.__getattribute__(self, 'destination_choice')

            destination_x_WP2 = destination[0]
            destination_y_WP2 = destination[1]

            if b.Board.giveStatusofField(self, destination_x_WP2, destination_y_WP2)[0] != 'W':
                print('Current position is: ' + self.position_x_WP2 + ' ' + str(self.position_y_WP2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WP2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WP2)
                y_pos = self.position_y_WP2
                y_des = destination_y_WP2

                if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (y_pos + 1 == y_des or y_pos - 1 == y_des) or
                        (x_pos + 1 == x_des or x_pos - 1 == x_des) and (y_pos + 2 == y_des or y_pos - 2 == y_des)):

                    b.Board.changeAfield(self, self.position_x_WP2, self.position_y_WP2, '.......')
                    self.position_x_WP2 = destination_x_WP2
                    self.position_y_WP2 = destination_y_WP2
                    print('New position is: ' + self.position_x_WP2+ ' ' + str(self.position_y_WP2))
                    b.Board.changeAfield(self, self.position_x_WP2, self.position_y_WP2, self.name_WP2)
                    return self.board
                    break

                else:
                    self.WP2_wrongDestination = 1
                    print('Your move is invalid, please choose cooridnates again!')
                    break
            else:
                self.WP2_wrongDestination = 1
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_WP2, destination_y_WP2)) + '.')
                break

class W1turm(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WT1 = 'A'
        self.position_y_WT1 = 1
        self.name_WT1='W1turm'
        self.WT1_wrongDestination = 0

    def move(self):
        while True:
                self.WT1_wrongDestination = 0
                print ('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_WT1 = destination[0]
                destination_y_WT1 = destination[1]
                if b.Board.giveStatusofField(self, destination_x_WT1, destination_y_WT1)[0] != 'W':
                    print('Current position is: ' + self.position_x_WT1 + ' ' + str(self.position_y_WT1))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_WT1)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_WT1)
                    y_pos = self.position_y_WT1
                    y_des = destination_y_WT1

                    controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                        0]  # checks whether move is allowed or not (either True or False)

                    if controll == True:
                        b.Board.changeAfield(self, self.position_x_WT1, self.position_y_WT1, '.......')
                        self.position_x_WT1 = destination_x_WT1
                        self.position_y_WT1 = destination_y_WT1
                        print('New position is: ' + self.position_x_WT1 + ' ' + str(self.position_y_WT1))
                        b.Board.changeAfield(self, self.position_x_WT1, self.position_y_WT1, self.name_WT1)
                        return self.board
                        break

                    else:
                        self.WT1_wrongDestination = 1
                        print('Your move is invalid, please choose cooridnates again!')
                        print('These are your options:')
                        potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                        for element in potentialFields:
                            print(element)
                        break
                else:
                    self.WT1_wrongDestination = 1
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WT1,destination_y_WT1))+'.')
                    break

class W2turm(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WT2 = 'A'
        self.position_y_WT2 = 8
        self.name_WT2 = 'W2turm'
        self.WT2_wrongDestination = 0


    def move(self):
        while True:
            self.WT2_wrongDestination = 0
            print('Give a x (letter) and y (number) coordinate for WHITE2 TURM!')
            
            destination = e.Engine.__getattribute__(self, 'destination_choice')

            destination_x_WT2 = destination[0]
            destination_y_WT2 = destination[1]

            if b.Board.giveStatusofField(self, destination_x_WT2, destination_y_WT2)[0] != 'W':
                print('Current position is: ' + self.position_x_WT2 + ' ' + str(self.position_y_WT2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WT2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WT2)
                y_pos = self.position_y_WT2
                y_des = destination_y_WT2

                controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                if controll == True:
                    b.Board.changeAfield(self, self.position_x_WT2, self.position_y_WT2, '.......')
                    self.position_x_WT2 = destination_x_WT2
                    self.position_y_WT2 = destination_y_WT2
                    print('New position is: ' + self.position_x_WT2 + ' ' + str(self.position_y_WT2))
                    b.Board.changeAfield(self, self.position_x_WT2, self.position_y_WT2, self.name_WT2)
                    return self.board
                    break

                else:
                    self.WT2_wrongDestination = 1
                    print('Your move is invalid, please choose cooridnates again!')
                    print('These are your options:')
                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                    for element in potentialFields:
                        print(element)
                    break
            else:
                self.WT2_wrongDestination = 1
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_WT2, destination_y_WT2)) + '.')
                break

class W1bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB1 = 'B'
        self.position_y_WB1 = 1
        self.name_WB1='W1bauer'
        self.mode='Bauer'
        self.n=0 #when changing mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB1_wrongDestination=0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB1_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE1 BAUER!')

                    destination=e.Engine.__getattribute__(self,'destination_choice')

                    destination_x_WB1 = destination[0]
                    destination_y_WB1 = destination[1]

                    if b.Board.giveStatusofField(self,destination_x_WB1,destination_y_WB1)[0]!='W':
                        print('Current position is: '+self.position_x_WB1+' '+str(self.position_y_WB1))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB1)
                        y_pos = self.position_y_WB1
                        y_des = destination_y_WB1

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB1,self.position_y_WB1,'.......')
                            self.position_x_WB1 = destination_x_WB1
                            self.position_y_WB1 = destination_y_WB1
                            print('New position is: '+self.position_x_WB1+' '+str(self.position_y_WB1))
                            b.Board.changeAfield(self,self.position_x_WB1,self.position_y_WB1,self.name_WB1)


                            #TRADE
                            if self.position_x_WB1 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB1 = 'WB1_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB1 = 'WB1_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB1 = 'WB1_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB1 = 'WB1_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB1_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB1_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB1,destination_y_WB1))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                        y_pos = self.position_y_WB1
                        b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB1 = destination[0]
                        destination_y_WB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB1)
                            y_pos = self.position_y_WB1
                            y_des = destination_y_WB1
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, '.......')
                                self.position_x_WB1 = destination_x_WB1
                                self.position_y_WB1 = destination_y_WB1
                                print('New position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                        y_pos = self.position_y_WB1
                        b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB1 = destination[0]
                        destination_y_WB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB1)
                            y_pos = self.position_y_WB1
                            y_des = destination_y_WB1
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, '.......')
                                self.position_x_WB1 = destination_x_WB1
                                self.position_y_WB1 = destination_y_WB1
                                print('New position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                        y_pos = self.position_y_WB1
                        b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB1 = destination[0]
                        destination_y_WB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB1)
                            y_pos = self.position_y_WB1
                            y_des = destination_y_WB1

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, '.......')
                                self.position_x_WB1 = destination_x_WB1
                                self.position_y_WB1 = destination_y_WB1
                                print('New position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                        y_pos = self.position_y_WB1
                        b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB1 = destination[0]
                        destination_y_WB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB1)
                            y_pos = self.position_y_WB1
                            y_des = destination_y_WB1

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, '.......')
                                self.position_x_WB1 = destination_x_WB1
                                self.position_y_WB1 = destination_y_WB1
                                print('New position is: ' + self.position_x_WB1 + ' ' + str(self.position_y_WB1))
                                b.Board.changeAfield(self, self.position_x_WB1, self.position_y_WB1, self.name_WB1)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)) + '.')

class W2bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB2 = 'B'
        self.position_y_WB2 = 2
        self.name_WB2='W2bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB2_wrongDestination = 0
    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB2_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE2 BAUER!')
                    
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB2 = destination[0]
                    destination_y_WB2 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB2,destination_y_WB2)[0]!='W':
                        print('Current position is: '+self.position_x_WB2+' '+str(self.position_y_WB2))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB2)
                        y_pos = self.position_y_WB2
                        y_des = destination_y_WB2

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB2,self.position_y_WB2,'.......')
                            self.position_x_WB2 = destination_x_WB2
                            self.position_y_WB2 = destination_y_WB2
                            print('New position is: '+self.position_x_WB2+' '+str(self.position_y_WB2))
                            b.Board.changeAfield(self,self.position_x_WB2,self.position_y_WB2,self.name_WB2)


                            #TRADE
                            if self.position_x_WB2 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB2 = 'WB2_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB2 = 'WB2_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB2 = 'WB2_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB2 = 'WB2_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB2_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB2_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB2,destination_y_WB2))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                        y_pos = self.position_y_WB2
                        b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB2 = destination[0]
                        destination_y_WB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB2)
                            y_pos = self.position_y_WB2
                            y_des = destination_y_WB2
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, '.......')
                                self.position_x_WB2 = destination_x_WB2
                                self.position_y_WB2 = destination_y_WB2
                                print('New position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                        y_pos = self.position_y_WB2
                        b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB2 = destination[0]
                        destination_y_WB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB2)
                            y_pos = self.position_y_WB2
                            y_des = destination_y_WB2
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, '.......')
                                self.position_x_WB2 = destination_x_WB2
                                self.position_y_WB2 = destination_y_WB2
                                print('New position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                        y_pos = self.position_y_WB2
                        b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB2 = destination[0]
                        destination_y_WB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB2)
                            y_pos = self.position_y_WB2
                            y_des = destination_y_WB2

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, '.......')
                                self.position_x_WB2 = destination_x_WB2
                                self.position_y_WB2 = destination_y_WB2
                                print('New position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                        y_pos = self.position_y_WB2
                        b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB2 = destination[0]
                        destination_y_WB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB2)
                            y_pos = self.position_y_WB2
                            y_des = destination_y_WB2

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, '.......')
                                self.position_x_WB2 = destination_x_WB2
                                self.position_y_WB2 = destination_y_WB2
                                print('New position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))
                                b.Board.changeAfield(self, self.position_x_WB2, self.position_y_WB2, self.name_WB2)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)) + '.')

class W3bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB3 = 'B'
        self.position_y_WB3 = 3
        self.name_WB3='W3bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB3_wrongDestination = 0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB3_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE3 BAUER!')
                    
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB3 = destination[0]
                    destination_y_WB3 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB3,destination_y_WB3)[0]!='W':
                        print('Current position is: '+self.position_x_WB3+' '+str(self.position_y_WB3))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB3)
                        y_pos = self.position_y_WB3
                        y_des = destination_y_WB3

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB3,self.position_y_WB3,'.......')
                            self.position_x_WB3 = destination_x_WB3
                            self.position_y_WB3 = destination_y_WB3
                            print('New position is: '+self.position_x_WB3+' '+str(self.position_y_WB3))
                            b.Board.changeAfield(self,self.position_x_WB3,self.position_y_WB3,self.name_WB3)


                            #TRADE
                            if self.position_x_WB3 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB3 = 'WB3_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB3 = 'WB3_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB3 = 'WB3_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB3 = 'WB3_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB3_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB3_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB3,destination_y_WB3))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                        y_pos = self.position_y_WB3
                        b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB3 = destination[0]
                        destination_y_WB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB3)
                            y_pos = self.position_y_WB3
                            y_des = destination_y_WB3
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, '.......')
                                self.position_x_WB3 = destination_x_WB3
                                self.position_y_WB3 = destination_y_WB3
                                print('New position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                        y_pos = self.position_y_WB3
                        b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB3 = destination[0]
                        destination_y_WB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB3)
                            y_pos = self.position_y_WB3
                            y_des = destination_y_WB3
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, '.......')
                                self.position_x_WB3 = destination_x_WB3
                                self.position_y_WB3 = destination_y_WB3
                                print('New position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                        y_pos = self.position_y_WB3
                        b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB3 = destination[0]
                        destination_y_WB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB3)
                            y_pos = self.position_y_WB3
                            y_des = destination_y_WB3

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, '.......')
                                self.position_x_WB3 = destination_x_WB3
                                self.position_y_WB3 = destination_y_WB3
                                print('New position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                        y_pos = self.position_y_WB3
                        b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB3 = destination[0]
                        destination_y_WB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB3)
                            y_pos = self.position_y_WB3
                            y_des = destination_y_WB3

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, '.......')
                                self.position_x_WB3 = destination_x_WB3
                                self.position_y_WB3 = destination_y_WB3
                                print('New position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))
                                b.Board.changeAfield(self, self.position_x_WB3, self.position_y_WB3, self.name_WB3)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)) + '.')

class W4bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB4 = 'B'
        self.position_y_WB4 = 4
        self.name_WB4='W4bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB4_wrongDestination = 0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB4_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE4 BAUER!')
                    
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB4 = destination[0]
                    destination_y_WB4 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB4,destination_y_WB4)[0]!='W':
                        print('Current position is: '+self.position_x_WB4+' '+str(self.position_y_WB4))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB4)
                        y_pos = self.position_y_WB4
                        y_des = destination_y_WB4

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB4,self.position_y_WB4,'.......')
                            self.position_x_WB4 = destination_x_WB4
                            self.position_y_WB4 = destination_y_WB4
                            print('New position is: '+self.position_x_WB4+' '+str(self.position_y_WB4))
                            b.Board.changeAfield(self,self.position_x_WB4,self.position_y_WB4,self.name_WB4)


                            #TRADE
                            if self.position_x_WB4 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB4 = 'WB4_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB4 = 'WB4_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB4 = 'WB4_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB4 = 'WB4_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB4_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB4_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB4,destination_y_WB4))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                        y_pos = self.position_y_WB4
                        b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB4 = destination[0]
                        destination_y_WB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB4)
                            y_pos = self.position_y_WB4
                            y_des = destination_y_WB4
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, '.......')
                                self.position_x_WB4 = destination_x_WB4
                                self.position_y_WB4 = destination_y_WB4
                                print('New position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                        y_pos = self.position_y_WB4
                        b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB4 = destination[0]
                        destination_y_WB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB4)
                            y_pos = self.position_y_WB4
                            y_des = destination_y_WB4
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, '.......')
                                self.position_x_WB4 = destination_x_WB4
                                self.position_y_WB4 = destination_y_WB4
                                print('New position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                        y_pos = self.position_y_WB4
                        b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB4 = destination[0]
                        destination_y_WB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB4)
                            y_pos = self.position_y_WB4
                            y_des = destination_y_WB4

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, '.......')
                                self.position_x_WB4 = destination_x_WB4
                                self.position_y_WB4 = destination_y_WB4
                                print('New position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                        y_pos = self.position_y_WB4
                        b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB4 = destination[0]
                        destination_y_WB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB4)
                            y_pos = self.position_y_WB4
                            y_des = destination_y_WB4

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, '.......')
                                self.position_x_WB4 = destination_x_WB4
                                self.position_y_WB4 = destination_y_WB4
                                print('New position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))
                                b.Board.changeAfield(self, self.position_x_WB4, self.position_y_WB4, self.name_WB4)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)) + '.')

class W5bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB5 = 'B'
        self.position_y_WB5 = 5
        self.name_WB5='W5bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB5_wrongDestination = 0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB5_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE5 BAUER!')
                    
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB5 = destination[0]
                    destination_y_WB5 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB5,destination_y_WB5)[0]!='W':
                        print('Current position is: '+self.position_x_WB5+' '+str(self.position_y_WB5))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB5)
                        y_pos = self.position_y_WB5
                        y_des = destination_y_WB5

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB5,self.position_y_WB5,'.......')
                            self.position_x_WB5 = destination_x_WB5
                            self.position_y_WB5 = destination_y_WB5
                            print('New position is: '+self.position_x_WB5+' '+str(self.position_y_WB5))
                            b.Board.changeAfield(self,self.position_x_WB5,self.position_y_WB5,self.name_WB5)


                            #TRADE
                            if self.position_x_WB5 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB5 = 'WB5_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB5 = 'WB5_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB5 = 'WB5_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB5 = 'WB5_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB5_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB5_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB5,destination_y_WB5))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                        y_pos = self.position_y_WB5
                        b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB5 = destination[0]
                        destination_y_WB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB5)
                            y_pos = self.position_y_WB5
                            y_des = destination_y_WB5
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, '.......')
                                self.position_x_WB5 = destination_x_WB5
                                self.position_y_WB5 = destination_y_WB5
                                print('New position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                        y_pos = self.position_y_WB5
                        b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB5 = destination[0]
                        destination_y_WB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB5)
                            y_pos = self.position_y_WB5
                            y_des = destination_y_WB5
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, '.......')
                                self.position_x_WB5 = destination_x_WB5
                                self.position_y_WB5 = destination_y_WB5
                                print('New position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                        y_pos = self.position_y_WB5
                        b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB5 = destination[0]
                        destination_y_WB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB5)
                            y_pos = self.position_y_WB5
                            y_des = destination_y_WB5

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, '.......')
                                self.position_x_WB5 = destination_x_WB5
                                self.position_y_WB5 = destination_y_WB5
                                print('New position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                        y_pos = self.position_y_WB5
                        b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB5 = destination[0]
                        destination_y_WB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB5)
                            y_pos = self.position_y_WB5
                            y_des = destination_y_WB5

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, '.......')
                                self.position_x_WB5 = destination_x_WB5
                                self.position_y_WB5 = destination_y_WB5
                                print('New position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))
                                b.Board.changeAfield(self, self.position_x_WB5, self.position_y_WB5, self.name_WB5)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)) + '.')

class W6bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB6 = 'B'
        self.position_y_WB6 = 6
        self.name_WB6='W6bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB6_wrongDestination = 0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB6_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE6 BAUER!')
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB6 = destination[0]
                    destination_y_WB6 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB6,destination_y_WB6)[0]!='W':
                        print('Current position is: '+self.position_x_WB6+' '+str(self.position_y_WB6))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB6)
                        y_pos = self.position_y_WB6
                        y_des = destination_y_WB6

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB6,self.position_y_WB6,'.......')
                            self.position_x_WB6 = destination_x_WB6
                            self.position_y_WB6 = destination_y_WB6
                            print('New position is: '+self.position_x_WB6+' '+str(self.position_y_WB6))
                            b.Board.changeAfield(self,self.position_x_WB6,self.position_y_WB6,self.name_WB6)


                            #TRADE
                            if self.position_x_WB6 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB6 = 'WB6_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB6 = 'WB6_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB6 = 'WB6_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB6 = 'WB6_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB6_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB6_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB6,destination_y_WB6))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                        y_pos = self.position_y_WB6
                        b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB6 = destination[0]
                        destination_y_WB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB6)
                            y_pos = self.position_y_WB6
                            y_des = destination_y_WB6
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, '.......')
                                self.position_x_WB6 = destination_x_WB6
                                self.position_y_WB6 = destination_y_WB6
                                print('New position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                        y_pos = self.position_y_WB6
                        b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB6 = destination[0]
                        destination_y_WB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB6)
                            y_pos = self.position_y_WB6
                            y_des = destination_y_WB6
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, '.......')
                                self.position_x_WB6 = destination_x_WB6
                                self.position_y_WB6 = destination_y_WB6
                                print('New position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                        y_pos = self.position_y_WB6
                        b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB6 = destination[0]
                        destination_y_WB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB6)
                            y_pos = self.position_y_WB6
                            y_des = destination_y_WB6

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, '.......')
                                self.position_x_WB6 = destination_x_WB6
                                self.position_y_WB6 = destination_y_WB6
                                print('New position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                        y_pos = self.position_y_WB6
                        b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB6 = destination[0]
                        destination_y_WB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB6)
                            y_pos = self.position_y_WB6
                            y_des = destination_y_WB6

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, '.......')
                                self.position_x_WB6 = destination_x_WB6
                                self.position_y_WB6 = destination_y_WB6
                                print('New position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))
                                b.Board.changeAfield(self, self.position_x_WB6, self.position_y_WB6, self.name_WB6)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)) + '.')

class W7bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB7 = 'B'
        self.position_y_WB7 = 7
        self.name_WB7='W7bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB7_wrongDestination = 0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB7_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE7 BAUER!')
                    
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB7 = destination[0]
                    destination_y_WB7 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB7,destination_y_WB7)[0]!='W':
                        print('Current position is: '+self.position_x_WB7+' '+str(self.position_y_WB7))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB7)
                        y_pos = self.position_y_WB7
                        y_des = destination_y_WB7

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB7,self.position_y_WB7,'.......')
                            self.position_x_WB7 = destination_x_WB7
                            self.position_y_WB7 = destination_y_WB7
                            print('New position is: '+self.position_x_WB7+' '+str(self.position_y_WB7))
                            b.Board.changeAfield(self,self.position_x_WB7,self.position_y_WB7,self.name_WB7)


                            #TRADE
                            if self.position_x_WB7 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB7 = 'WB7_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB7 = 'WB7_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB7 = 'WB7_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB7 = 'WB7_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB7_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB7_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB7,destination_y_WB7))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                        y_pos = self.position_y_WB7
                        b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB7 = destination[0]
                        destination_y_WB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB7)
                            y_pos = self.position_y_WB7
                            y_des = destination_y_WB7
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, '.......')
                                self.position_x_WB7 = destination_x_WB7
                                self.position_y_WB7 = destination_y_WB7
                                print('New position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                        y_pos = self.position_y_WB7
                        b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB7 = destination[0]
                        destination_y_WB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB7)
                            y_pos = self.position_y_WB7
                            y_des = destination_y_WB7
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, '.......')
                                self.position_x_WB7 = destination_x_WB7
                                self.position_y_WB7 = destination_y_WB7
                                print('New position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                        y_pos = self.position_y_WB7
                        b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB7 = destination[0]
                        destination_y_WB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB7)
                            y_pos = self.position_y_WB7
                            y_des = destination_y_WB7

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, '.......')
                                self.position_x_WB7 = destination_x_WB7
                                self.position_y_WB7 = destination_y_WB7
                                print('New position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                        y_pos = self.position_y_WB7
                        b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB7 = destination[0]
                        destination_y_WB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB7)
                            y_pos = self.position_y_WB7
                            y_des = destination_y_WB7

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, '.......')
                                self.position_x_WB7 = destination_x_WB7
                                self.position_y_WB7 = destination_y_WB7
                                print('New position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))
                                b.Board.changeAfield(self, self.position_x_WB7, self.position_y_WB7, self.name_WB7)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)) + '.')

class W8bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB8 = 'B'
        self.position_y_WB8 = 8
        self.name_WB8='W8bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
        self.WB8_wrongDestination = 0

    def move(self):
        while True:
                if self.mode=='Bauer':
                    self.WB8_wrongDestination = 0
                    print('Give a x (letter) and y (number) coordinate for WHITE8 BAUER!')
                    
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_WB8 = destination[0]
                    destination_y_WB8 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_WB8,destination_y_WB8)[0]!='W':
                        print('Current position is: '+self.position_x_WB8+' '+str(self.position_y_WB8))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_WB8)
                        y_pos = self.position_y_WB8
                        y_des = destination_y_WB8

                        if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                            (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                            (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_WB8,self.position_y_WB8,'.......')
                            self.position_x_WB8 = destination_x_WB8
                            self.position_y_WB8 = destination_y_WB8
                            print('New position is: '+self.position_x_WB8+' '+str(self.position_y_WB8))
                            b.Board.changeAfield(self,self.position_x_WB8,self.position_y_WB8,self.name_WB8)


                            #TRADE
                            if self.position_x_WB8 == 'H':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_WB8 = 'WB8_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_WB8 = 'WB8_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_WB8 = 'WB8_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_WB8 = 'WB8_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            self.WB8_wrongDestination = 1
                            print('Your move is invalid, please choose cooridnates again!')
                            break
                    else:
                        self.WB8_wrongDestination = 1
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB8,destination_y_WB8))+'.')
                        break

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                        y_pos = self.position_y_WB8
                        b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB8 = destination[0]
                        destination_y_WB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB8)
                            y_pos = self.position_y_WB8
                            y_des = destination_y_WB8
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, '.......')
                                self.position_x_WB8 = destination_x_WB8
                                self.position_y_WB8 = destination_y_WB8
                                print('New position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                if controll_Cross == False and controll_Diagonal == False:
                                    print('Diagonal options:')

                                    print('Diagonal1')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                                        print(element)
                                    print('Diagonal2')
                                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                                        print(element)

                                    print('Cross options')
                                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                    for element in potentialFields:
                                        print(element)
                                elif controll_Diagonal == False or controll_Cross == False:
                                    if controll_Cross == False:
                                        potentialFields = \
                                        b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                        for element in potentialFields:
                                            print(element)
                                    else:
                                        print('Diagonal1')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            1]:
                                            print(element)
                                        print('Diagonal2')
                                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                            2]:
                                            print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                        y_pos = self.position_y_WB8
                        b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE LAUFER!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB8 = destination[0]
                        destination_y_WB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB8)
                            y_pos = self.position_y_WB8
                            y_des = destination_y_WB8
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, '.......')
                                self.position_x_WB8 = destination_x_WB8
                                self.position_y_WB8 = destination_y_WB8
                                print('New position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                print('Diagonal1')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    1]:
                                    print(element)
                                print('Diagonal2')
                                for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                    2]:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                        y_pos = self.position_y_WB8
                        b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE PFERD!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB8 = destination[0]
                        destination_y_WB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB8)
                            y_pos = self.position_y_WB8
                            y_des = destination_y_WB8

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, '.......')
                                self.position_x_WB8 = destination_x_WB8
                                self.position_y_WB8 = destination_y_WB8
                                print('New position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                        y_pos = self.position_y_WB8
                        b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                        
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_WB8 = destination[0]
                        destination_y_WB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)[0] != 'W':
                            print('Current position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_WB8)
                            y_pos = self.position_y_WB8
                            y_des = destination_y_WB8

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, '.......')
                                self.position_x_WB8 = destination_x_WB8
                                self.position_y_WB8 = destination_y_WB8
                                print('New position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))
                                b.Board.changeAfield(self, self.position_x_WB8, self.position_y_WB8, self.name_WB8)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                print('These are your options:')
                                potentialFields = \
                                b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                                for element in potentialFields:
                                    print(element)
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)) + '.')