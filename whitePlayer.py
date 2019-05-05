#Developer: Marvin Fuchs, May 2019
import board as b

class W1koenig(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WK = 'A'
        self.position_y_WK = 5
        self.name_WK='W1koenig'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for WHITE KING!')
                destination_x_WK = str(input())
                destination_y_WK = int(input())

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
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WK,destination_y_WK))+'.')

class W1dame(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WD = 'A'
        self.position_y_WD = 4
        self.name_WD='W1dame'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for WHITE DAME!')
                destination_x_WD = str(input())
                destination_y_WD = int(input())

                if b.Board.giveStatusofField(self,destination_x_WD,destination_y_WD)[0]!='W':
                    print('Current position is: '+self.position_x_WD+' '+str(self.position_y_WD))


                    #logic
                    x_pos=b.Board.translateLettertoNumber(self,self.position_x_WD)
                    x_des=b.Board.translateLettertoNumber(self,destination_x_WD)

                    if ( abs(x_pos-x_des) <2 and abs(self.position_y_WD-destination_y_WD) < 2 ):
                        b.Board.changeAfield(self,self.position_x_WD,self.position_y_WD,'.......')
                        self.position_x_WD = destination_x_WD
                        self.position_y_WD = destination_y_WD
                        print('New position is: '+self.position_x_WD+' '+str(self.position_y_WD))
                        b.Board.changeAfield(self,self.position_x_WD,self.position_y_WD,self.name_WD)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WD,destination_y_WD))+'.')

class W1laeufer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WL1 = 'A'
        self.position_y_WL1 = 3
        self.name_WL1='W1laeufer'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for WHITE1 LAUFER!')
                destination_x_WL1 = str(input())
                destination_y_WL1 = int(input())

                if b.Board.giveStatusofField(self,destination_x_WL1,destination_y_WL1)[0]!='W':
                    print('Current position is: '+self.position_x_WL1+' '+str(self.position_y_WL1))


                    #logic
                    x_pos=b.Board.translateLettertoNumber(self,self.position_x_WL1)
                    x_des=b.Board.translateLettertoNumber(self,destination_x_WL1)

                    if ( abs(x_pos-x_des) <2 and abs(self.position_y_WL1-destination_y_WL1) < 2 ):
                        b.Board.changeAfield(self,self.position_x_WL1,self.position_y_WL1,'.......')
                        self.position_x_WL1 = destination_x_WL1
                        self.position_y_WL1 = destination_y_WL1
                        print('New position is: '+self.position_x_WL1+' '+str(self.position_y_WL1))
                        b.Board.changeAfield(self,self.position_x_WL1,self.position_y_WL1,self.name_WL1)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WL1,destination_y_WL1))+'.')

class W2laeufer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WL2 = 'A'
        self.position_y_WL2 = 6
        self.name_WK2 = 'W2laeufer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE2 LAUFER!')
            destination_x_WL2 = str(input())
            destination_y_WL2 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WL2, destination_y_WL2)[0] != 'W':
                print('Current position is: ' + self.position_x_WL2 + ' ' + str(self.position_y_WL2))

                # logic
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WL2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WL2)

                if (abs(x_pos - x_des) < 2 and abs(self.position_y_WL2 - destination_y_WL2) < 2):
                    b.Board.changeAfield(self, self.position_x_WL2, self.position_y_WL2, '.......')
                    self.position_x_WL2 = destination_x_WL2
                    self.position_y_WL2 = destination_y_WL2
                    print('New position is: ' + self.position_x_WL2 + ' ' + str(self.position_y_WL2))
                    b.Board.changeAfield(self, self.position_x_WL2, self.position_y_WL2, self.name_WL2)
                    return self.board
                    break

                else:
                    print('Your move is invalid, please choose cooridnates again!')
                    continue
            else:
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_WL2, destination_y_WL2)) + '.')

class W1pferd(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WP1 = 'A'
        self.position_y_WP1 = 2
        self.name_WP1='W1pferd'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for WHITE1 PFERD!')
                destination_x_WP1 = str(input())
                destination_y_WP1 = int(input())

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
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WP1,destination_y_WP1))+'.')

class W2pferd(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WP2 = 'A'
        self.position_y_WP2 = 7
        self.name_WP2= 'W2pferd'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE2 PFERD!')
            destination_x_WP2 = str(input())
            destination_y_WP2 = int(input())

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
                    print('Your move is invalid, please choose cooridnates again!')
                    continue
            else:
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_WP2, destination_y_WP2)) + '.')

class W1turm(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WT1 = 'A'
        self.position_y_WT1 = 1
        self.name_WT1='W1turm'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for WHITE1 TURM!')
                destination_x_WT1 = str(input())
                destination_y_WT1 = int(input())

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
                        print('Your move is invalid, please choose cooridnates again!')
                        print('These are your options:')
                        potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                        for element in potentialFields:
                            print(element)
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WT1,destination_y_WT1))+'.')

class W2turm(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WT2 = 'A'
        self.position_y_WT2 = 8
        self.name_WT2 = 'W2turm'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE2 TURM!')
            destination_x_WT2 = str(input())
            destination_y_WT2 = int(input())

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
                    print('Your move is invalid, please choose cooridnates again!')
                    print('These are your options:')
                    potentialFields = b.Board.givepotentialTurmDestination(self, x_pos, y_pos, x_des, y_des)[1]
                    for element in potentialFields:
                        print(element)
                    continue
            else:
                print('Does not work! This field is already governed by your ' + (
                    b.Board.giveStatusofField(self, destination_x_WT2, destination_y_WT2)) + '.')

class W1bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB1 = 'B'
        self.position_y_WB1 = 1
        self.name_WB1='W1bauer'
    def move(self):
        while True:
                print ('Give a x (letter) and y (number) coordinate for WHITE1 BAUER!')
                destination_x_WB1 = str(input())
                destination_y_WB1 = int(input())

                if b.Board.giveStatusofField(self,destination_x_WB1,destination_y_WB1)[0]!='W':
                    print('Current position is: '+self.position_x_WB1+' '+str(self.position_y_WB1))

                    #logic
                    status = b.Board.giveStatusofField(self, destination_x_WB1, destination_y_WB1)
                    x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB1)
                    x_des = b.Board.translateLettertoNumber(self, destination_x_WB1)
                    y_pos = self.position_y_WB1
                    y_des = destination_y_WB1
                    print(status)

                    if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                        (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                        (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

                        b.Board.changeAfield(self,self.position_x_WB1,self.position_y_WB1,'.......')
                        self.position_x_WB1 = destination_x_WB1
                        self.position_y_WB1 = destination_y_WB1
                        print('New position is: '+self.position_x_WB1+' '+str(self.position_y_WB1))
                        b.Board.changeAfield(self,self.position_x_WB1,self.position_y_WB1,self.name_WB1)
                        return self.board
                        break

                    else:
                        print('Your move is invalid, please choose cooridnates again!')
                        continue
                else:
                    print('Does not work! This field is already governed by your '+(b.Board.giveStatusofField(self,destination_x_WB1,destination_y_WB1))+'.')

class W2bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB2 = 'B'
        self.position_y_WB2 = 2
        self.name_WB2 = 'W2bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE2 BAUER!')
            destination_x_WB2 = str(input())
            destination_y_WB2 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)[0] != 'W':
                print('Current position is: ' + self.position_x_WB2 + ' ' + str(self.position_y_WB2))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB2, destination_y_WB2)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB2)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB2)
                y_pos = self.position_y_WB2
                y_des = destination_y_WB2

                if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                    (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                    (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

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

class W3bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB3 = 'B'
        self.position_y_WB3 = 3
        self.name_WB3 = 'W3bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE3 BAUER!')
            destination_x_WB3 = str(input())
            destination_y_WB3 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)[0] != 'W':
                print('Current position is: ' + self.position_x_WB3 + ' ' + str(self.position_y_WB3))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB3, destination_y_WB3)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB3)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB3)
                y_pos = self.position_y_WB3
                y_des = destination_y_WB3

                if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                    (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                    (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

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

class W4bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB4 = 'B'
        self.position_y_WB4 = 4
        self.name_WB4 = 'W4bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE4 BAUER!')
            destination_x_WB4 = str(input())
            destination_y_WB4 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)[0] != 'W':
                print('Current position is: ' + self.position_x_WB4 + ' ' + str(self.position_y_WB4))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB4, destination_y_WB4)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB4)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB4)
                y_pos = self.position_y_WB4
                y_des = destination_y_WB4

                if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                    (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                    (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

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

class W5bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB5 = 'B'
        self.position_y_WB5 = 5
        self.name_WB5 = 'W5bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE5 BAUER!')
            destination_x_WB5 = str(input())
            destination_y_WB5 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)[0] != 'W':
                print('Current position is: ' + self.position_x_WB5 + ' ' + str(self.position_y_WB5))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB5, destination_y_WB5)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB5)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB5)
                y_pos = self.position_y_WB5
                y_des = destination_y_WB5

                if ((status[0] == '.' and x_pos == 2 and (
                        x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                        (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                        (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):
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

class W6bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB6 = 'B'
        self.position_y_WB6 = 6
        self.name_WB6 = 'W6bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE6 BAUER!')
            destination_x_WB6 = str(input())
            destination_y_WB6 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)[0] != 'W':
                print('Current position is: ' + self.position_x_WB6 + ' ' + str(self.position_y_WB6))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB6, destination_y_WB6)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB6)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB6)
                y_pos = self.position_y_WB6
                y_des = destination_y_WB6

                if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                    (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                    (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

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

class W7bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB7 = 'B'
        self.position_y_WB7 = 7
        self.name_WB7 = 'W7bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE7 BAUER!')
            destination_x_WB7 = str(input())
            destination_y_WB7 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)[0] != 'W':
                print('Current position is: ' + self.position_x_WB7 + ' ' + str(self.position_y_WB7))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB7, destination_y_WB7)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB7)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB7)
                y_pos = self.position_y_WB7
                y_des = destination_y_WB7

                if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                    (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                    (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

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

class W8bauer(b.Board):
    def __init__(self):
        b.Board.__init__(self)
        self.position_x_WB8 = 'B'
        self.position_y_WB8 = 8
        self.name_WB8 = 'W8bauer'

    def move(self):
        while True:
            print('Give a x (letter) and y (number) coordinate for WHITE8 BAUER!')
            destination_x_WB8 = str(input())
            destination_y_WB8 = int(input())

            if b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)[0] != 'W':
                print('Current position is: ' + self.position_x_WB8 + ' ' + str(self.position_y_WB8))

                # logic
                status = b.Board.giveStatusofField(self, destination_x_WB8, destination_y_WB8)
                x_pos = b.Board.translateLettertoNumber(self, self.position_x_WB8)
                x_des = b.Board.translateLettertoNumber(self, destination_x_WB8)
                y_pos = self.position_y_WB8
                y_des = destination_y_WB8

                if ((status[0] == '.' and x_pos == 2 and (x_pos + 1 == x_des or x_pos + 2 == x_des) and y_pos == y_des) or
                    (status[0] == '.' and x_pos != 2 and x_pos + 1 == x_des and y_pos == y_des) or
                    (status[0] == 'B' and x_pos + 1 == x_des and (y_pos + 1 == y_des or y_pos - 1 == y_des))):

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