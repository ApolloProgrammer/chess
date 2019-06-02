#Developer: Marvin Fuchs, May 2019
import board as b
import engine as e

class B1koenig(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BK = 'H'
        self.position_y_BK = 5
        self.name_BK='B1koenig'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for BLACK KING!')
                e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_BK = destination[0]
                destination_y_BK = destination[1]

                if b.Board.giveStatusofField(self,destination_x_BK,destination_y_BK)[0]!='B':
                    print('Current position is: '+self.position_x_BK+' '+str(self.position_y_BK))


                    #logic
                    x_pos=b.Board.translateLettertoNumber(self,self.position_x_BK)
                    x_des=b.Board.translateLettertoNumber(self,destination_x_BK)

                    if ( abs(x_pos-x_des) <2 and abs(self.position_y_BK-destination_y_BK) < 2 ):
                        b.Board.changeAfield(self,self.position_x_BK,self.position_y_BK,'.......')
                        self.position_x_BK = destination_x_BK
                        self.position_y_BK = destination_y_BK
                        print('New position is: '+self.position_x_BK+' '+str(self.position_y_BK))
                        b.Board.changeAfield(self,self.position_x_BK,self.position_y_BK,self.name_BK)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BK,destination_y_BK))+'.')

class B1dame(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BD = 'H'
        self.position_y_BD = 4
        self.name_BD='B1dame'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_BD = destination[0]
                destination_y_BD = destination[1]

                if b.Board.giveStatusofField(self,destination_x_BD,destination_y_BD)[0]!='B':
                    print('Current position is: '+self.position_x_BD+' '+str(self.position_y_BD))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_BD)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_BD)
                    y_pos = self.position_y_BD
                    y_des = destination_y_BD
                    controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)
                    controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                    if controll_Diagonal == True or controll_Cross == True:
                        b.Board.changeAfield(self, self.position_x_BD, self.position_y_BD, '.......')
                        self.position_x_BD = destination_x_BD
                        self.position_y_BD = destination_y_BD
                        print('New position is: ' + self.position_x_BD + ' ' + str(self.position_y_BD))
                        b.Board.changeAfield(self, self.position_x_BD, self.position_y_BD, self.name_BD)
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
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BD,destination_y_BD))+'.')

class B1laeufer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BL1 = 'H'
        self.position_y_BL1 = 3
        self.name_BL1='B1laeufer'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for BLACK1 LAUFER!')
                e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_BL1 = destination[0]
                destination_y_BL1 = destination[1]

                if b.Board.giveStatusofField(self,destination_x_BL1,destination_y_BL1)[0]!='B':
                    print('Current position is: '+self.position_x_BL1+' '+str(self.position_y_BL1))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_BL1)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_BL1)
                    y_pos = self.position_y_BL1
                    y_des = destination_y_BL1
                    controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                    if controll == True:
                        b.Board.changeAfield(self, self.position_x_BL1, self.position_y_BL1, '.......')
                        self.position_x_BL1 = destination_x_BL1
                        self.position_y_BL1 = destination_y_BL1
                        print('New position is: ' + self.position_x_BL1 + ' ' + str(self.position_y_BL1))
                        b.Board.changeAfield(self, self.position_x_BL1, self.position_y_BL1, self.name_BL1)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        print('These are your options:')
                        print('Diagonal1')
                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                            print(element)
                        print('Diagonal2')
                        for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                            print(element)
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BL1,destination_y_BL1))+'.')

class B2laeufer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BL2 = 'H'
        self.position_y_BL2 = 6
        self.name_BL2 = 'B2laeufer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for BLACK2 LAUFER!')
            e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
            destination = e.Engine.__getattribute__(self, 'destination_choice')

            destination_x_BL2 = destination[0]
            destination_y_BL2 = destination[1]

            if b.Board.giveStatusofField(self, destination_x_BL2, destination_y_BL2)[0] != 'B':
                print('Current position is: ' + self.position_x_BL2 + ' ' + str(self.position_y_BL2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_BL2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_BL2)
                y_pos = self.position_y_BL2
                y_des = destination_y_BL2
                controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[0]  # checks whether move is allowed or not (either True or False)

                if controll == True:
                    b.Board.changeAfield(self, self.position_x_BL2, self.position_y_BL2, '.......')
                    self.position_x_BL2 = destination_x_BL2
                    self.position_y_BL2 = destination_y_BL2
                    print('New position is: ' + self.position_x_BL2 + ' ' + str(self.position_y_BL2))
                    b.Board.changeAfield(self, self.position_x_BL2, self.position_y_BL2, self.name_BL2)
                    return self.board
                    break

                else:
                    print('Your move is invalid, please choose cooridnates again!')
                    print('These are your options:')
                    print('Diagonal1')
                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[1]:
                        print(element)
                    print('Diagonal2')
                    for element in b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[2]:
                        print(element)
                    continue
            else:
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_BL2, destination_y_BL2)) + '.')

class B1pferd(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BP1 = 'H'
        self.position_y_BP1 = 2
        self.name_BP1='B1pferd'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for BLACK1 PFERD!')
                e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_BP1 = destination[0]
                destination_y_BP1 = destination[1]

                if b.Board.giveStatusofField(self,destination_x_BP1,destination_y_BP1)[0]!='B':
                    print('Current position is: '+self.position_x_BP1+' '+str(self.position_y_BP1))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_BP1)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_BP1)
                    y_pos = self.position_y_BP1
                    y_des = destination_y_BP1

                    if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (y_pos + 1 == y_des or y_pos - 1 == y_des) or
                            (x_pos + 1 == x_des or x_pos - 1 == x_des) and (y_pos + 2 == y_des or y_pos - 2 == y_des)):

                        b.Board.changeAfield(self,self.position_x_BP1,self.position_y_BP1,'.......')
                        self.position_x_BP1 = destination_x_BP1
                        self.position_y_BP1 = destination_y_BP1
                        print('New position is: '+self.position_x_BP1+' '+str(self.position_y_BP1))
                        b.Board.changeAfield(self,self.position_x_BP1,self.position_y_BP1,self.name_BP1)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BP1,destination_y_BP1))+'.')

class B2pferd(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BP2 = 'H'
        self.position_y_BP2 = 7
        self.name_BP2 = 'B2pferd'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for BLACK2 PFERD!')
            e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
            destination = e.Engine.__getattribute__(self, 'destination_choice')

            destination_x_BP2 = destination[0]
            destination_y_BP2 = destination[1]

            if b.Board.giveStatusofField(self, destination_x_BP2, destination_y_BP2)[0] != 'B':
                print('Current position is: ' + self.position_x_BP2 + ' ' + str(self.position_y_BP2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_BP2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_BP2)
                y_pos = self.position_y_BP2
                y_des = destination_y_BP2

                if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (y_pos + 1 == y_des or y_pos - 1 == y_des) or
                        (x_pos + 1 == x_des or x_pos - 1 == x_des) and (y_pos + 2 == y_des or y_pos - 2 == y_des)):

                    b.Board.changeAfield(self, self.position_x_BP2, self.position_y_BP2, '.......')
                    self.position_x_BP2 = destination_x_BP2
                    self.position_y_BP2 = destination_y_BP2
                    print('New position is: ' + self.position_x_BP2 + ' ' + str(self.position_y_BP2))
                    b.Board.changeAfield(self, self.position_x_BP2, self.position_y_BP2, self.name_BP2)
                    return self.board
                    break

                else:
                    print('Your move is invalid, please choose cooridnates again!')
                    continue
            else:
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_BP2, destination_y_BP2)) + '.')

class B1turm(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BT1 = 'H'
        self.position_y_BT1 = 1
        self.name_BT1='B1turm'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                destination = e.Engine.__getattribute__(self, 'destination_choice')

                destination_x_BT1 = destination[0]
                destination_y_BT1 = destination[1]

                if b.Board.giveStatusofField(self,destination_x_BT1,destination_y_BT1)[0]!='B':
                    print('Current position is: '+self.position_x_BT1+' '+str(self.position_y_BT1))

                    # logic
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_BT1)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_BT1)
                    y_pos = self.position_y_BT1
                    y_des = destination_y_BT1

                    controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                        0]  # checks whether move is allowed or not (either True or False)

                    if controll == True:
                        b.Board.changeAfield(self, self.position_x_BT1, self.position_y_BT1, '.......')
                        self.position_x_BT1 = destination_x_BT1
                        self.position_y_BT1 = destination_y_BT1
                        print('New position is: ' + self.position_x_BT1 + ' ' + str(self.position_y_BT1))
                        b.Board.changeAfield(self, self.position_x_BT1, self.position_y_BT1, self.name_BT1)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        print('These are your options:')
                        potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                        for element in potentialFields:
                            print(element)
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BT1,destination_y_BT1))+'.')

class B2turm(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BT2 = 'H'
        self.position_y_BT2 = 8
        self.name_BT2 = 'B2turm'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for BLACK2 TURM!')
            e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
            destination = e.Engine.__getattribute__(self, 'destination_choice')

            destination_x_BT2 = destination[0]
            destination_y_BT2 = destination[1]

            if b.Board.giveStatusofField(self, destination_x_BT2, destination_y_BT2)[0] != 'B':
                print('Current position is: ' + self.position_x_BT2+ ' ' + str(self.position_y_BT2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_BT2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_BT2)
                y_pos = self.position_y_BT2
                y_des = destination_y_BT2

                controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                    0]  # checks whether move is allowed or not (either True or False)

                if controll == True:
                    b.Board.changeAfield(self, self.position_x_BT2, self.position_y_BT2, '.......')
                    self.position_x_BT2 = destination_x_BT2
                    self.position_y_BT2 = destination_y_BT2
                    print('New position is: ' + self.position_x_BT2 + ' ' + str(self.position_y_BT2))
                    b.Board.changeAfield(self, self.position_x_BT2, self.position_y_BT2, self.name_BT2)
                    return self.board
                    break

                else:
                    print('Your move is invalid, please choose cooridnates again!')
                    print('These are your options:')
                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                    for element in potentialFields:
                        print(element)
                    continue
            else:
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_BT2, destination_y_BT2)) + '.')

class B1bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB1 = 'G'
        self.position_y_BB1 = 1
        self.name_BB1='B1bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK1 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB1 = destination[0]
                    destination_y_BB1 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB1,destination_y_BB1)[0]!='B':
                        print('Current position is: '+self.position_x_BB1+' '+str(self.position_y_BB1))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB1)
                        y_pos = self.position_y_BB1
                        y_des = destination_y_BB1

                        if True:
                        # if ((status[0] == '.' and x_pos == 7 and (
                        #         x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                        #         (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                        #         (status[0] == 'W' and x_pos - 1 == x_des and (
                        #                 y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB1,self.position_y_BB1,'.......')
                            self.position_x_BB1 = destination_x_BB1
                            self.position_y_BB1 = destination_y_BB1
                            print('New position is: '+self.position_x_BB1+' '+str(self.position_y_BB1))
                            b.Board.changeAfield(self,self.position_x_BB1,self.position_y_BB1,self.name_BB1)


                            #TRADE
                            if self.position_x_BB1 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB1 = 'BB1_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB1 = 'BB1_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB1 = 'BB1_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB1 = 'BB1_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB1,destination_y_BB1))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                        y_pos = self.position_y_BB1
                        b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB1 = destination[0]
                        destination_y_BB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB1)
                            y_pos = self.position_y_BB1
                            y_des = destination_y_BB1
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, '.......')
                                self.position_x_BB1 = destination_x_BB1
                                self.position_y_BB1 = destination_y_BB1
                                print('New position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
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
                                b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                        y_pos = self.position_y_BB1
                        b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB1 = destination[0]
                        destination_y_BB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB1)
                            y_pos = self.position_y_BB1
                            y_des = destination_y_BB1
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, '.......')
                                self.position_x_BB1 = destination_x_BB1
                                self.position_y_BB1 = destination_y_BB1
                                print('New position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
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
                                b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                        y_pos = self.position_y_BB1
                        b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB1 = destination[0]
                        destination_y_BB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB1)
                            y_pos = self.position_y_BB1
                            y_des = destination_y_BB1

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, '.......')
                                self.position_x_BB1 = destination_x_BB1
                                self.position_y_BB1 = destination_y_BB1
                                print('New position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                        y_pos = self.position_y_BB1
                        b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB1 = destination[0]
                        destination_y_BB1 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB1)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB1)
                            y_pos = self.position_y_BB1
                            y_des = destination_y_BB1

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, '.......')
                                self.position_x_BB1 = destination_x_BB1
                                self.position_y_BB1 = destination_y_BB1
                                print('New position is: ' + self.position_x_BB1 + ' ' + str(self.position_y_BB1))
                                b.Board.changeAfield(self, self.position_x_BB1, self.position_y_BB1, self.name_BB1)
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
                                b.Board.giveStatusofField(self, destination_x_BB1, destination_y_BB1)) + '.')

class B2bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB2 = 'G'
        self.position_y_BB2 = 2
        self.name_BB2='B2bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK2 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB2 = destination[0]
                    destination_y_BB2 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB2,destination_y_BB2)[0]!='B':
                        print('Current position is: '+self.position_x_BB2+' '+str(self.position_y_BB2))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB2)
                        y_pos = self.position_y_BB2
                        y_des = destination_y_BB2

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB2,self.position_y_BB2,'.......')
                            self.position_x_BB2 = destination_x_BB2
                            self.position_y_BB2 = destination_y_BB2
                            print('New position is: '+self.position_x_BB2+' '+str(self.position_y_BB2))
                            b.Board.changeAfield(self,self.position_x_BB2,self.position_y_BB2,self.name_BB2)


                            #TRADE
                            if self.position_x_BB2 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB2 = 'BB2_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB2 = 'BB2_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB2 = 'BB2_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB2 = 'BB2_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB2,destination_y_BB2))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                        y_pos = self.position_y_BB2
                        b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB2 = destination[0]
                        destination_y_BB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB2)
                            y_pos = self.position_y_BB2
                            y_des = destination_y_BB2
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, '.......')
                                self.position_x_BB2 = destination_x_BB2
                                self.position_y_BB2 = destination_y_BB2
                                print('New position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
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
                                b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                        y_pos = self.position_y_BB2
                        b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB2 = destination[0]
                        destination_y_BB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB2)
                            y_pos = self.position_y_BB2
                            y_des = destination_y_BB2
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, '.......')
                                self.position_x_BB2 = destination_x_BB2
                                self.position_y_BB2 = destination_y_BB2
                                print('New position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
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
                                b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                        y_pos = self.position_y_BB2
                        b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB2 = destination[0]
                        destination_y_BB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB2)
                            y_pos = self.position_y_BB2
                            y_des = destination_y_BB2

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, '.......')
                                self.position_x_BB2 = destination_x_BB2
                                self.position_y_BB2 = destination_y_BB2
                                print('New position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                        y_pos = self.position_y_BB2
                        b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB2 = destination[0]
                        destination_y_BB2 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB2)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB2)
                            y_pos = self.position_y_BB2
                            y_des = destination_y_BB2

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, '.......')
                                self.position_x_BB2 = destination_x_BB2
                                self.position_y_BB2 = destination_y_BB2
                                print('New position is: ' + self.position_x_BB2 + ' ' + str(self.position_y_BB2))
                                b.Board.changeAfield(self, self.position_x_BB2, self.position_y_BB2, self.name_BB2)
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
                                b.Board.giveStatusofField(self, destination_x_BB2, destination_y_BB2)) + '.')

class B3bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB3 = 'G'
        self.position_y_BB3 = 3
        self.name_BB3='B3bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK3 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB3 = destination[0]
                    destination_y_BB3 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB3,destination_y_BB3)[0]!='B':
                        print('Current position is: '+self.position_x_BB3+' '+str(self.position_y_BB3))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB3)
                        y_pos = self.position_y_BB3
                        y_des = destination_y_BB3

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB3,self.position_y_BB3,'.......')
                            self.position_x_BB3 = destination_x_BB3
                            self.position_y_BB3 = destination_y_BB3
                            print('New position is: '+self.position_x_BB3+' '+str(self.position_y_BB3))
                            b.Board.changeAfield(self,self.position_x_BB3,self.position_y_BB3,self.name_BB3)


                            #TRADE
                            if self.position_x_BB3 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB3 = 'BB3_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB3 = 'BB3_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB3 = 'BB3_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB3 = 'BB3_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB3,destination_y_BB3))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                        y_pos = self.position_y_BB3
                        b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB3 = destination[0]
                        destination_y_BB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB3)
                            y_pos = self.position_y_BB3
                            y_des = destination_y_BB3
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, '.......')
                                self.position_x_BB3 = destination_x_BB3
                                self.position_y_BB3 = destination_y_BB3
                                print('New position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
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
                                b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                        y_pos = self.position_y_BB3
                        b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB3 = destination[0]
                        destination_y_BB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB3)
                            y_pos = self.position_y_BB3
                            y_des = destination_y_BB3
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, '.......')
                                self.position_x_BB3 = destination_x_BB3
                                self.position_y_BB3 = destination_y_BB3
                                print('New position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
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
                                b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                        y_pos = self.position_y_BB3
                        b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB3 = destination[0]
                        destination_y_BB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB3)
                            y_pos = self.position_y_BB3
                            y_des = destination_y_BB3

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, '.......')
                                self.position_x_BB3 = destination_x_BB3
                                self.position_y_BB3 = destination_y_BB3
                                print('New position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                        y_pos = self.position_y_BB3
                        b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB3 = destination[0]
                        destination_y_BB3 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB3)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB3)
                            y_pos = self.position_y_BB3
                            y_des = destination_y_BB3

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, '.......')
                                self.position_x_BB3 = destination_x_BB3
                                self.position_y_BB3 = destination_y_BB3
                                print('New position is: ' + self.position_x_BB3 + ' ' + str(self.position_y_BB3))
                                b.Board.changeAfield(self, self.position_x_BB3, self.position_y_BB3, self.name_BB3)
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
                                b.Board.giveStatusofField(self, destination_x_BB3, destination_y_BB3)) + '.')

class B4bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB4 = 'G'
        self.position_y_BB4 = 4
        self.name_BB4='B4bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK4 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB4 = destination[0]
                    destination_y_BB4 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB4,destination_y_BB4)[0]!='B':
                        print('Current position is: '+self.position_x_BB4+' '+str(self.position_y_BB4))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB4)
                        y_pos = self.position_y_BB4
                        y_des = destination_y_BB4

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB4,self.position_y_BB4,'.......')
                            self.position_x_BB4 = destination_x_BB4
                            self.position_y_BB4 = destination_y_BB4
                            print('New position is: '+self.position_x_BB4+' '+str(self.position_y_BB4))
                            b.Board.changeAfield(self,self.position_x_BB4,self.position_y_BB4,self.name_BB4)


                            #TRADE
                            if self.position_x_BB4 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB4 = 'BB4_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB4 = 'BB4_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB4 = 'BB4_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB4 = 'BB4_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB4,destination_y_BB4))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                        y_pos = self.position_y_BB4
                        b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB4 = destination[0]
                        destination_y_BB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB4)
                            y_pos = self.position_y_BB4
                            y_des = destination_y_BB4
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, '.......')
                                self.position_x_BB4 = destination_x_BB4
                                self.position_y_BB4 = destination_y_BB4
                                print('New position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
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
                                b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                        y_pos = self.position_y_BB4
                        b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB4 = destination[0]
                        destination_y_BB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB4)
                            y_pos = self.position_y_BB4
                            y_des = destination_y_BB4
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, '.......')
                                self.position_x_BB4 = destination_x_BB4
                                self.position_y_BB4 = destination_y_BB4
                                print('New position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
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
                                b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                        y_pos = self.position_y_BB4
                        b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB4 = destination[0]
                        destination_y_BB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB4)
                            y_pos = self.position_y_BB4
                            y_des = destination_y_BB4

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, '.......')
                                self.position_x_BB4 = destination_x_BB4
                                self.position_y_BB4 = destination_y_BB4
                                print('New position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                        y_pos = self.position_y_BB4
                        b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB4 = destination[0]
                        destination_y_BB4 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB4)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB4)
                            y_pos = self.position_y_BB4
                            y_des = destination_y_BB4

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, '.......')
                                self.position_x_BB4 = destination_x_BB4
                                self.position_y_BB4 = destination_y_BB4
                                print('New position is: ' + self.position_x_BB4 + ' ' + str(self.position_y_BB4))
                                b.Board.changeAfield(self, self.position_x_BB4, self.position_y_BB4, self.name_BB4)
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
                                b.Board.giveStatusofField(self, destination_x_BB4, destination_y_BB4)) + '.')

class B5bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB5 = 'G'
        self.position_y_BB5 = 5
        self.name_BB5='B5bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK5 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB5 = destination[0]
                    destination_y_BB5 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB5,destination_y_BB5)[0]!='B':
                        print('Current position is: '+self.position_x_BB5+' '+str(self.position_y_BB5))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB5)
                        y_pos = self.position_y_BB5
                        y_des = destination_y_BB5

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB5,self.position_y_BB5,'.......')
                            self.position_x_BB5 = destination_x_BB5
                            self.position_y_BB5 = destination_y_BB5
                            print('New position is: '+self.position_x_BB5+' '+str(self.position_y_BB5))
                            b.Board.changeAfield(self,self.position_x_BB5,self.position_y_BB5,self.name_BB5)


                            #TRADE
                            if self.position_x_BB5 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB5 = 'BB5_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB5 = 'BB5_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB5 = 'BB5_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB5 = 'BB5_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB5,destination_y_BB5))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                        y_pos = self.position_y_BB5
                        b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB5 = destination[0]
                        destination_y_BB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB5)
                            y_pos = self.position_y_BB5
                            y_des = destination_y_BB5
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, '.......')
                                self.position_x_BB5 = destination_x_BB5
                                self.position_y_BB5 = destination_y_BB5
                                print('New position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
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
                                b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                        y_pos = self.position_y_BB5
                        b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB5 = destination[0]
                        destination_y_BB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB5)
                            y_pos = self.position_y_BB5
                            y_des = destination_y_BB5
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, '.......')
                                self.position_x_BB5 = destination_x_BB5
                                self.position_y_BB5 = destination_y_BB5
                                print('New position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
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
                                b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                        y_pos = self.position_y_BB5
                        b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB5 = destination[0]
                        destination_y_BB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB5)
                            y_pos = self.position_y_BB5
                            y_des = destination_y_BB5

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, '.......')
                                self.position_x_BB5 = destination_x_BB5
                                self.position_y_BB5 = destination_y_BB5
                                print('New position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                        y_pos = self.position_y_BB5
                        b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB5 = destination[0]
                        destination_y_BB5 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB5)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB5)
                            y_pos = self.position_y_BB5
                            y_des = destination_y_BB5

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, '.......')
                                self.position_x_BB5 = destination_x_BB5
                                self.position_y_BB5 = destination_y_BB5
                                print('New position is: ' + self.position_x_BB5 + ' ' + str(self.position_y_BB5))
                                b.Board.changeAfield(self, self.position_x_BB5, self.position_y_BB5, self.name_BB5)
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
                                b.Board.giveStatusofField(self, destination_x_BB5, destination_y_BB5)) + '.')

class B6bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB6 = 'G'
        self.position_y_BB6 = 6
        self.name_BB6='B6bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK6 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB6 = destination[0]
                    destination_y_BB6 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB6,destination_y_BB6)[0]!='B':
                        print('Current position is: '+self.position_x_BB6+' '+str(self.position_y_BB6))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB6)
                        y_pos = self.position_y_BB6
                        y_des = destination_y_BB6

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB6,self.position_y_BB6,'.......')
                            self.position_x_BB6 = destination_x_BB6
                            self.position_y_BB6 = destination_y_BB6
                            print('New position is: '+self.position_x_BB6+' '+str(self.position_y_BB6))
                            b.Board.changeAfield(self,self.position_x_BB6,self.position_y_BB6,self.name_BB6)


                            #TRADE
                            if self.position_x_BB6 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB6 = 'BB6_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB6 = 'BB6_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB6 = 'BB6_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB6 = 'BB6_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB6,destination_y_BB6))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                        y_pos = self.position_y_BB6
                        b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB6 = destination[0]
                        destination_y_BB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB6)
                            y_pos = self.position_y_BB6
                            y_des = destination_y_BB6
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, '.......')
                                self.position_x_BB6 = destination_x_BB6
                                self.position_y_BB6 = destination_y_BB6
                                print('New position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
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
                                b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                        y_pos = self.position_y_BB6
                        b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB6 = destination[0]
                        destination_y_BB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB6)
                            y_pos = self.position_y_BB6
                            y_des = destination_y_BB6
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, '.......')
                                self.position_x_BB6 = destination_x_BB6
                                self.position_y_BB6 = destination_y_BB6
                                print('New position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
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
                                b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                        y_pos = self.position_y_BB6
                        b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB6 = destination[0]
                        destination_y_BB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB6)
                            y_pos = self.position_y_BB6
                            y_des = destination_y_BB6

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, '.......')
                                self.position_x_BB6 = destination_x_BB6
                                self.position_y_BB6 = destination_y_BB6
                                print('New position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                        y_pos = self.position_y_BB6
                        b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB6 = destination[0]
                        destination_y_BB6 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB6)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB6)
                            y_pos = self.position_y_BB6
                            y_des = destination_y_BB6

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, '.......')
                                self.position_x_BB6 = destination_x_BB6
                                self.position_y_BB6 = destination_y_BB6
                                print('New position is: ' + self.position_x_BB6 + ' ' + str(self.position_y_BB6))
                                b.Board.changeAfield(self, self.position_x_BB6, self.position_y_BB6, self.name_BB6)
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
                                b.Board.giveStatusofField(self, destination_x_BB6, destination_y_BB6)) + '.')

class B7bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB7 = 'G'
        self.position_y_BB7 = 7
        self.name_BB7='B7bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK7 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB7 = destination[0]
                    destination_y_BB7 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB7,destination_y_BB7)[0]!='B':
                        print('Current position is: '+self.position_x_BB7+' '+str(self.position_y_BB7))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB7)
                        y_pos = self.position_y_BB7
                        y_des = destination_y_BB7

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB7,self.position_y_BB7,'.......')
                            self.position_x_BB7 = destination_x_BB7
                            self.position_y_BB7 = destination_y_BB7
                            print('New position is: '+self.position_x_BB7+' '+str(self.position_y_BB7))
                            b.Board.changeAfield(self,self.position_x_BB7,self.position_y_BB7,self.name_BB7)


                            #TRADE
                            if self.position_x_BB7 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB7 = 'BB7_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB7 = 'BB7_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB7 = 'BB7_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB7 = 'BB7_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB7,destination_y_BB7))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                        y_pos = self.position_y_BB7
                        b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB7 = destination[0]
                        destination_y_BB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB7)
                            y_pos = self.position_y_BB7
                            y_des = destination_y_BB7
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, '.......')
                                self.position_x_BB7 = destination_x_BB7
                                self.position_y_BB7 = destination_y_BB7
                                print('New position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
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
                                b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                        y_pos = self.position_y_BB7
                        b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB7 = destination[0]
                        destination_y_BB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB7)
                            y_pos = self.position_y_BB7
                            y_des = destination_y_BB7
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, '.......')
                                self.position_x_BB7 = destination_x_BB7
                                self.position_y_BB7 = destination_y_BB7
                                print('New position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
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
                                b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                        y_pos = self.position_y_BB7
                        b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB7 = destination[0]
                        destination_y_BB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB7)
                            y_pos = self.position_y_BB7
                            y_des = destination_y_BB7

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, '.......')
                                self.position_x_BB7 = destination_x_BB7
                                self.position_y_BB7 = destination_y_BB7
                                print('New position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                        y_pos = self.position_y_BB7
                        b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB7 = destination[0]
                        destination_y_BB7 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB7)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB7)
                            y_pos = self.position_y_BB7
                            y_des = destination_y_BB7

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, '.......')
                                self.position_x_BB7 = destination_x_BB7
                                self.position_y_BB7 = destination_y_BB7
                                print('New position is: ' + self.position_x_BB7 + ' ' + str(self.position_y_BB7))
                                b.Board.changeAfield(self, self.position_x_BB7, self.position_y_BB7, self.name_BB7)
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
                                b.Board.giveStatusofField(self, destination_x_BB7, destination_y_BB7)) + '.')

class B8bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_BB8 = 'G'
        self.position_y_BB8 = 8
        self.name_BB8='B8bauer'
        self.mode='Bauer'
        self.n=0 #when chanhging mode, it gives information of the status of changing. n==0,changing to other figure. n==1,already changed, can be used as other figure!
    def move(self):
        while True:
                if self.mode=='Bauer':
                    print('Give a x (letter) and y (number) coordinate for BLACK8 BAUER!')
                    e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                    destination = e.Engine.__getattribute__(self, 'destination_choice')

                    destination_x_BB8 = destination[0]
                    destination_y_BB8 = destination[1]
                    if b.Board.giveStatusofField(self,destination_x_BB8,destination_y_BB8)[0]!='B':
                        print('Current position is: '+self.position_x_BB8+' '+str(self.position_y_BB8))

                        #logic
                        status = b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                        x_des = b.Board.translateLettertoNumber(self, destination_x_BB8)
                        y_pos = self.position_y_BB8
                        y_des = destination_y_BB8

                        if ((status[0] == '.' and x_pos == 7 and (
                                x_pos - 1 == x_des or x_pos - 2 == x_des) and y_pos == y_des) or
                                (status[0] == '.' and x_pos != 7 and x_pos - 1 == x_des and y_pos == y_des) or
                                (status[0] == 'W' and x_pos - 1 == x_des and (
                                        y_pos + 1 == y_des or y_pos - 1 == y_des))):

                            b.Board.changeAfield(self,self.position_x_BB8,self.position_y_BB8,'.......')
                            self.position_x_BB8 = destination_x_BB8
                            self.position_y_BB8 = destination_y_BB8
                            print('New position is: '+self.position_x_BB8+' '+str(self.position_y_BB8))
                            b.Board.changeAfield(self,self.position_x_BB8,self.position_y_BB8,self.name_BB8)


                            #TRADE
                            if self.position_x_BB8 == 'A':
                                print('Your pawn reached the end. Which figure do you choose ?')
                                print('Your options are: Dame, Laeufer, Pferd, Turm!')
                                choice_figure = str(input())
                                if choice_figure == 'Dame':
                                    self.mode = 'Dame'
                                    self.name_BB8 = 'BB8_Dame'
                                elif choice_figure=='Laeufer':
                                    self.mode = 'Laeufer'
                                    self.name_BB8 = 'BB8_Laeufer'
                                elif choice_figure=='Pferd':
                                    self.mode = 'Pferd'
                                    self.name_BB8 = 'BB8_Pferd'
                                elif choice_figure=='Turm':
                                    self.mode = 'Turm'
                                    self.name_BB8 = 'BB8_Turm'

                            ###TRADE END
                            if self.mode == 'Bauer':
                                return self.board
                                break

                        else:
                            print('Your move is invalid, please choose cooridnates again!')
                            continue
                    else:
                        print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_BB8,destination_y_BB8))+'.')

                if self.mode == 'Dame':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                        y_pos = self.position_y_BB8
                        b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK DAME!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB8 = destination[0]
                        destination_y_BB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))
                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB8)
                            y_pos = self.position_y_BB8
                            y_des = destination_y_BB8
                            controll_Diagonal = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)
                            controll_Cross = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll_Diagonal == True or controll_Cross == True:
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, '.......')
                                self.position_x_BB8 = destination_x_BB8
                                self.position_y_BB8 = destination_y_BB8
                                print('New position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
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
                                b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)) + '.')

                if self.mode == 'Laeufer':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                        y_pos = self.position_y_BB8
                        b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK LAUFER!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB8 = destination[0]
                        destination_y_BB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB8)
                            y_pos = self.position_y_BB8
                            y_des = destination_y_BB8
                            controll = b.Board.givepotentialLauferDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, '.......')
                                self.position_x_BB8 = destination_x_BB8
                                self.position_y_BB8 = destination_y_BB8
                                print('New position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
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
                                b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)) + '.')

                if self.mode == 'Pferd':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                        y_pos = self.position_y_BB8
                        b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK PFERD!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB8 = destination[0]
                        destination_y_BB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB8)
                            y_pos = self.position_y_BB8
                            y_des = destination_y_BB8

                            if ((x_pos + 2 == x_des or x_pos - 2 == x_des) and (
                                    y_pos + 1 == y_des or y_pos - 1 == y_des) or
                                    (x_pos + 1 == x_des or x_pos - 1 == x_des) and (
                                            y_pos + 2 == y_des or y_pos - 2 == y_des)):

                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, '.......')
                                self.position_x_BB8 = destination_x_BB8
                                self.position_y_BB8 = destination_y_BB8
                                print('New position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
                                return self.board
                                break

                            else:
                                print('Your move is invalid, please choose cooridnates again!')
                                continue
                        else:
                            print('Does not work! This field is already governed by your ' + (
                                b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)) + '.')

                if self.mode == 'Turm':
                    if self.n==0:
                        #logic of changing to DAME
                        x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                        y_pos = self.position_y_BB8
                        b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
                        self.n=1
                        return self.board
                        break

                    if self.n==1:
                        print('Give a x (letter) and y (number) coordinate for BLACK1 TURM!')
                        e.Engine.visualize(self, b.Board.__getattribute__(self, 'board'), 1)
                        destination = e.Engine.__getattribute__(self, 'destination_choice')

                        destination_x_BB8 = destination[0]
                        destination_y_BB8 = destination[1]

                        if b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)[0] != 'B':
                            print('Current position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))

                            # logic
                            x_pos = b.Board.translateLettertoNumber(self, self.position_x_BB8)
                            x_des = b.Board.translateLettertoNumber(self, destination_x_BB8)
                            y_pos = self.position_y_BB8
                            y_des = destination_y_BB8

                            controll = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[
                                0]  # checks whether move is allowed or not (either True or False)

                            if controll == True:
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, '.......')
                                self.position_x_BB8 = destination_x_BB8
                                self.position_y_BB8 = destination_y_BB8
                                print('New position is: ' + self.position_x_BB8 + ' ' + str(self.position_y_BB8))
                                b.Board.changeAfield(self, self.position_x_BB8, self.position_y_BB8, self.name_BB8)
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
                                b.Board.giveStatusofField(self, destination_x_BB8, destination_y_BB8)) + '.')