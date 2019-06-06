#Developer: Marvin Fuchs, May-June 2019

import board as b
import whitePlayer as white
import blackPlayer as black


class Engine(white.W1koenig):
    def __init__(self):
        super().__init__()
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
        #important variables
        self.choice=0
        self.destination_choice=[]
        self.end = False
        self.counter = 0
        self.check_againstBlack = 0 # if 0, then no check; elif 1, then check; elif 2, then checkMate (end)
        self.check_againstWhite = 0


    def turn_of_White(self):
        if self.choice == 'W1koenig':
            white.W1koenig.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self,'board')
        elif self.choice == 'W1dame':
            white.W1dame.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'W1laeufer':
            white.W1laeufer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'W2laeufer':
            white.W2laeufer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'W1pferd':
            white.W1pferd.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'W2pferd':
            white.W2pferd.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'W1turm':
            white.W1turm.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'W2turm':
            white.W2turm.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W1bauer.__getattribute__(self, 'name_WB1'):
            white.W1bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
            return b.Board.__getattribute__(self,'board')
        elif self.choice == white.W2bauer.__getattribute__(self, 'name_WB2'):
            white.W2bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W3bauer.__getattribute__(self, 'name_WB3'):
            white.W3bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W4bauer.__getattribute__(self, 'name_WB4'):
            white.W4bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W5bauer.__getattribute__(self, 'name_WB5'):
            white.W5bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W6bauer.__getattribute__(self, 'name_WB6'):
            white.W6bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W7bauer.__getattribute__(self, 'name_WB7'):
            white.W7bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == white.W8bauer.__getattribute__(self, 'name_WB8'):
            white.W8bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'Rochade':
            print('Which Rochade? Left or Right?')
            Rochade_choice = str(input())
            if Rochade_choice == 'Left':
                if (white.W1koenig.__getattribute__(self, 'position_x_WK') == 'A' and white.W1koenig.__getattribute__(
                        self, 'position_y_WK') == 5) and (
                        white.W1turm.__getattribute__(self, 'position_x_WT1') == 'A' and white.W1turm.__getattribute__(
                    self, 'position_y_WT1') == 1) and b.Board.giveStatusofField(self, 'A',
                                                                                2) == '.......' and b.Board.giveStatusofField(
                    self, 'A', 3) == '.......' and b.Board.giveStatusofField(self, 'A', 4) == '.......':
                    b.Board.changeAfield(self, white.W1koenig.__getattribute__(self, 'position_x_WK'),
                                         white.W1koenig.__getattribute__(self, 'position_y_WK'), '.......')
                    white.W1koenig.__setattr__(self, 'position_y_WK', 3)
                    b.Board.changeAfield(self, white.W1turm.__getattribute__(self, 'position_x_WT1'),
                                         white.W1turm.__getattribute__(self, 'position_y_WT1'), '.......')
                    white.W1koenig.__setattr__(self, 'position_y_WT1', 4)
                    b.Board.changeAfield(self, 'A', 3, 'W1koenig')
                    b.Board.changeAfield(self, 'A', 4, 'W1turm')
                    b.Board.showDataofBoard(self)
                    self.counter += 1
                    self.choice = ''
                    return b.Board.__getattribute__(self, 'board')
                else:
                    print('Move is not allowed!')

            elif Rochade_choice == 'Right':
                if (white.W1koenig.__getattribute__(self, 'position_x_WK') == 'A' and white.W1koenig.__getattribute__(
                        self, 'position_y_WK') == 5) and (
                        white.W2turm.__getattribute__(self, 'position_x_WT2') == 'A' and white.W2turm.__getattribute__(
                    self, 'position_y_WT2') == 8) and b.Board.giveStatusofField(self, 'A',
                                                                                6) == '.......' and b.Board.giveStatusofField(
                    self, 'A', 7) == '.......':
                    print('Move approved!')
                    b.Board.changeAfield(self, white.W1koenig.__getattribute__(self, 'position_x_WK'),
                                         white.W1koenig.__getattribute__(self, 'position_y_WK'), '.......')
                    white.W1koenig.__setattr__(self, 'position_y_WK', 7)
                    b.Board.changeAfield(self, white.W2turm.__getattribute__(self, 'position_x_WT2'),
                                         white.W2turm.__getattribute__(self, 'position_y_WT2'), '.......')
                    white.W2turm.__setattr__(self, 'position_y_WT2', 6)
                    b.Board.changeAfield(self, 'A', 7, 'W1koenig')
                    b.Board.changeAfield(self, 'A', 6, 'W2turm')
                    b.Board.showDataofBoard(self)
                    self.counter += 1
                    self.choice = ''
                else:
                    print('Move is not allowed!')

        else:
            print('please choose again')

        # white->black
        # CKECKING WHETHER CHECK OR NOT
        # all possible killing destinations of each white player are stored in big list
        # if the position of the black king is in that list, white creates a CHECK situation for black

        wkoenig = b.Board.givepotentialKingDestination(self, b.Board.translateLettertoNumber(self,
                                                                                             white.W1koenig.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_WK')),
                                                       white.W1koenig.__getattribute__(self,
                                                                                       'position_y_WK'))

        wdame1 = b.Board.givepotentialLauferDestination(self,
                                                        b.Board.translateLettertoNumber(self,
                                                                                        white.W1dame.__getattribute__(
                                                                                            self,
                                                                                            'position_x_WD')),
                                                        white.W1dame.__getattribute__(self, 'position_y_WD'),
                                                        1, 1)[1]
        wdame2 = b.Board.givepotentialLauferDestination(self,
                                                        b.Board.translateLettertoNumber(self,
                                                                                        white.W1dame.__getattribute__(
                                                                                            self,
                                                                                            'position_x_WD')),
                                                        white.W1dame.__getattribute__(self, 'position_y_WD'),
                                                        1, 1)[2]
        wdame3 = b.Board.givepotentialTurmDestination(self,
                                                      b.Board.translateLettertoNumber(self,
                                                                                      white.W1dame.__getattribute__(
                                                                                          self,
                                                                                          'position_x_WD')),
                                                      white.W1dame.__getattribute__(self, 'position_y_WD'),
                                                      1, 1)[1]
        wdame = wdame1 + wdame2 + wdame3

        wlaeufer1_1 = b.Board.givepotentialLauferDestination(self,
                                                             b.Board.translateLettertoNumber(self,
                                                                                             white.W1laeufer.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_WL1')),
                                                             white.W1laeufer.__getattribute__(self,
                                                                                              'position_y_WL1'),
                                                             1, 1)[1]
        wlaeufer1_2 = b.Board.givepotentialLauferDestination(self,
                                                             b.Board.translateLettertoNumber(self,
                                                                                             white.W1laeufer.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_WL1')),
                                                             white.W1laeufer.__getattribute__(self,
                                                                                              'position_y_WL1'),
                                                             1, 1)[2]
        wlaeufer1 = wlaeufer1_1 + wlaeufer1_2

        wlaeufer2_1 = b.Board.givepotentialLauferDestination(self,
                                                             b.Board.translateLettertoNumber(self,
                                                                                             white.W2laeufer.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_WL2')),
                                                             white.W2laeufer.__getattribute__(self,
                                                                                              'position_y_WL2'),
                                                             1, 1)[1]
        wlaeufer2_2 = b.Board.givepotentialLauferDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                   white.W2laeufer.__getattribute__(
                                                                                                       self,
                                                                                                       'position_x_WL2')),
                                                             white.W2laeufer.__getattribute__(self,
                                                                                              'position_y_WL2'),
                                                             1, 1)[2]
        wlaeufer2 = wlaeufer2_1 + wlaeufer2_2

        wpferd1 = b.Board.givepotentialSpringerDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                 white.W1pferd.__getattribute__(
                                                                                                     self,
                                                                                                     'position_x_WP1')),
                                                           white.W1pferd.__getattribute__(self,
                                                                                          'position_y_WP1'))
        wpferd2 = b.Board.givepotentialSpringerDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                 white.W2pferd.__getattribute__(
                                                                                                     self,
                                                                                                     'position_x_WP2')),
                                                           white.W2pferd.__getattribute__(self,
                                                                                          'position_y_WP2'))

        wturm1 = b.Board.givepotentialTurmDestination(self, b.Board.translateLettertoNumber(self,
                                                                                            white.W1turm.__getattribute__(
                                                                                                self,
                                                                                                'position_x_WT1')),
                                                      white.W1turm.__getattribute__(self, 'position_y_WT1'),
                                                      1, 1)[1]
        wturm2 = b.Board.givepotentialTurmDestination(self, b.Board.translateLettertoNumber(self,
                                                                                            white.W2turm.__getattribute__(
                                                                                                self,
                                                                                                'position_x_WT2')),
                                                      white.W2turm.__getattribute__(self, 'position_y_WT2'),
                                                      1, 1)[1]

        wbauer1 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W1bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB1')),
                                                            white.W1bauer.__getattribute__(self,
                                                                                           'position_y_WB1'))
        wbauer2 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W2bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB2')),
                                                            white.W2bauer.__getattribute__(self,
                                                                                           'position_y_WB2'))
        wbauer3 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W3bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB3')),
                                                            white.W3bauer.__getattribute__(self,
                                                                                           'position_y_WB3'))
        wbauer4 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W4bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB4')),
                                                            white.W4bauer.__getattribute__(self,
                                                                                           'position_y_WB4'))
        wbauer5 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W5bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB5')),
                                                            white.W5bauer.__getattribute__(self,
                                                                                           'position_y_WB5'))
        wbauer6 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W6bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB6')),
                                                            white.W6bauer.__getattribute__(self,
                                                                                           'position_y_WB6'))
        wbauer7 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W7bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB7')),
                                                            white.W7bauer.__getattribute__(self,
                                                                                           'position_y_WB7'))
        wbauer8 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  white.W8bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_WB8')),
                                                            white.W8bauer.__getattribute__(self,
                                                                                           'position_y_WB8'))
        # possible Killing Destinations
        potentialKillingFields_WHITE = wkoenig + wdame + wlaeufer1 + wlaeufer2 + wpferd1 + wpferd2 + wturm1 + wturm2 + wbauer1 + wbauer2 + wbauer3 + wbauer4 + wbauer5 + wbauer6 + wbauer7 + wbauer8

        # condition for check
        if self.check_againstBlack == 0:
            for element in potentialKillingFields_WHITE:
                if black.B1koenig.__getattribute__(self, 'position_x_BK') == element[
                    0] and black.B1koenig.__getattribute__(self, 'position_y_BK') == element[1]:
                    self.check_againstBlack = 1
                    print('Check! (black)')
                    break

        # black->white
        # checking if checkMate is appropiate (when check and the king has no )
        if self.check_againstWhite == 1:
            for element in potentialKillingFields_BLACK:
                if white.W1koenig.__getattribute__(self, 'position_x_WK') == element[
                    0] and white.W1koenig.__getattribute__(self, 'position_y_WK') == element[
                    1]:  # if already check and player black could not handle the chack and is still in check position, then he lost due to checkMate
                    print('WHITE IS CHECK MATE!')
                    print('BLACK WINS! CONGRATULATIONS!!!')
                    self.end = True
                    break
                else:  # player black could defend himself. no check anymore. right now not in check/danger for checkMate
                    self.check_againstWhite = 0

    def turn_of_Black(self):
        if self.choice == 'B1koenig':
            black.B1koenig.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B1dame':
            black.B1dame.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B1laeufer':
            black.B1laeufer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B2laeufer':
            black.B2laeufer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B1pferd':
            black.B1pferd.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B2pferd':
            black.B2pferd.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B1turm':
            black.B1turm.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'B2turm':
            black.B2turm.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B1bauer.__getattribute__(self, 'name_BB1'):
            black.B1bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B2bauer.__getattribute__(self, 'name_BB2'):
            black.B2bauer.move(self)
            self.b.Board.showDataofBoard(self)
            counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B3bauer.__getattribute__(self, 'name_BB3'):
            black.B3bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B4bauer.__getattribute__(self, 'name_BB4'):
            black.B4bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B5bauer.__getattribute__(self, 'name_BB5'):
            black.B5bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B6bauer.__getattribute__(self, 'name_BB6'):
            black.B6bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B7bauer.__getattribute__(self, 'name_BB7'):
            black.B7bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == black.B8bauer.__getattribute__(self, 'name_BB8'):
            black.B8bauer.move(self)
            b.Board.showDataofBoard(self)
            self.counter += 1
            self.choice = ''
            return b.Board.__getattribute__(self, 'board')
        elif self.choice == 'Rochade':
            print('Which Rochade? Left or Right? (Perspective from top onto the field)')
            Rochade_choice = str(input())
            if Rochade_choice == 'Left':
                if (black.B1koenig.__getattribute__(self, 'position_x_BK') == 'H' and black.B1koenig.__getattribute__(
                        self, 'position_y_BK') == 5) and (
                        black.B1turm.__getattribute__(self, 'position_x_BT1') == 'H' and black.B1turm.__getattribute__(
                    self, 'position_y_BT1') == 1) and b.Board.giveStatusofField(self, 'H',
                                                                                2) == '.......' and b.Board.giveStatusofField(
                    self, 'H', 3) == '.......' and b.Board.giveStatusofField(self, 'H', 4) == '.......':
                    b.Board.changeAfield(self, black.B1koenig.__getattribute__(self, 'position_x_BK'),
                                         black.B1koenig.__getattribute__(self, 'position_y_BK'), '.......')
                    black.B1koenig.__setattr__(self, 'position_y_BK', 3)
                    b.Board.changeAfield(self, black.B1turm.__getattribute__(self, 'position_x_BT1'),
                                         black.B1turm.__getattribute__(self, 'position_y_BT1'), '.......')
                    black.B1koenig.__setattr__(self, 'position_y_BT1', 4)
                    b.Board.changeAfield(self, 'H', 3, 'B1koenig')
                    b.Board.changeAfield(self, 'H', 4, 'B1turm')
                    b.Board.showDataofBoard(self)
                    self.counter += 1
                    self.choice = ''
                    return b.Board.__getattribute__(self, 'board')
                else:
                    print('Move is not allowed!')

            elif Rochade_choice == 'Right':
                if (black.B1koenig.__getattribute__(self, 'position_x_BK') == 'H' and black.B1koenig.__getattribute__(
                        self, 'position_y_BK') == 5) and (
                        black.B2turm.__getattribute__(self, 'position_x_BT2') == 'H' and black.B2turm.__getattribute__(
                    self, 'position_y_BT2') == 8) and b.Board.giveStatusofField(self, 'H',
                                                                                6) == '.......' and b.Board.giveStatusofField(
                    self, 'H', 7) == '.......':
                    print('Move approved!')
                    b.Board.changeAfield(self, black.B1koenig.__getattribute__(self, 'position_x_BK'),
                                         black.B1koenig.__getattribute__(self, 'position_y_BK'), '.......')
                    black.B1koenig.__setattr__(self, 'position_y_BK', 7)
                    b.Board.changeAfield(self, black.B2turm.__getattribute__(self, 'position_x_BT2'),
                                         black.B2turm.__getattribute__(self, 'position_y_BT2'), '.......')
                    black.B2turm.__setattr__(self, 'position_y_BT2', 6)
                    b.Board.changeAfield(self, 'H', 7, 'B1koenig')
                    b.Board.changeAfield(self, 'H', 6, 'B2turm')
                    b.Board.showDataofBoard(self)
                    self.counter += 1
                    self.choice = ''
                    return b.Board.__getattribute__(self, 'board')
                else:
                    print('Move is not allowed!')

        else:
            print('please choose again')

        # black->white
        # CKECKING WHETHER CHECK OR NOT
        # all possible killing destinations of each black player are stored in big list
        # if the position of the white king is in that list, white creates a CHECK situation for white

        bkoenig = b.Board.givepotentialKingDestination(self, b.Board.translateLettertoNumber(self,
                                                                                             black.B1koenig.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_BK')),
                                                       black.B1koenig.__getattribute__(self,
                                                                                       'position_y_BK'))

        bdame1 = b.Board.givepotentialLauferDestination(self,
                                                        b.Board.translateLettertoNumber(self,
                                                                                        black.B1dame.__getattribute__(
                                                                                            self,
                                                                                            'position_x_BD')),
                                                        black.B1dame.__getattribute__(self, 'position_y_BD'),
                                                        1, 1)[1]
        bdame2 = b.Board.givepotentialLauferDestination(self,
                                                        b.Board.translateLettertoNumber(self,
                                                                                        black.B1dame.__getattribute__(
                                                                                            self,
                                                                                            'position_x_BD')),
                                                        black.B1dame.__getattribute__(self, 'position_y_BD'),
                                                        1, 1)[2]
        bdame3 = b.Board.givepotentialTurmDestination(self,
                                                      b.Board.translateLettertoNumber(self,
                                                                                      black.B1dame.__getattribute__(
                                                                                          self,
                                                                                          'position_x_BD')),
                                                      black.B1dame.__getattribute__(self, 'position_y_BD'),
                                                      1, 1)[1]
        bdame = bdame1 + bdame2 + bdame3

        blaeufer1_1 = b.Board.givepotentialLauferDestination(self,
                                                             b.Board.translateLettertoNumber(self,
                                                                                             black.B1laeufer.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_BL1')),
                                                             black.B1laeufer.__getattribute__(self,
                                                                                              'position_y_BL1'),
                                                             1, 1)[1]
        blaeufer1_2 = b.Board.givepotentialLauferDestination(self,
                                                             b.Board.translateLettertoNumber(self,
                                                                                             black.B1laeufer.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_BL1')),
                                                             black.B1laeufer.__getattribute__(self,
                                                                                              'position_y_BL1'),
                                                             1, 1)[2]
        blaeufer1 = blaeufer1_1 + blaeufer1_2

        blaeufer2_1 = b.Board.givepotentialLauferDestination(self,
                                                             b.Board.translateLettertoNumber(self,
                                                                                             black.B2laeufer.__getattribute__(
                                                                                                 self,
                                                                                                 'position_x_BL2')),
                                                             black.B2laeufer.__getattribute__(self,
                                                                                              'position_y_BL2'),
                                                             1, 1)[1]
        blaeufer2_2 = b.Board.givepotentialLauferDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                   black.B2laeufer.__getattribute__(
                                                                                                       self,
                                                                                                       'position_x_BL2')),
                                                             black.B2laeufer.__getattribute__(self,
                                                                                              'position_y_BL2'),
                                                             1, 1)[2]
        blaeufer2 = blaeufer2_1 + blaeufer2_2

        bpferd1 = b.Board.givepotentialSpringerDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                 black.B1pferd.__getattribute__(
                                                                                                     self,
                                                                                                     'position_x_BP1')),
                                                           black.B1pferd.__getattribute__(self,
                                                                                          'position_y_BP1'))
        bpferd2 = b.Board.givepotentialSpringerDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                 black.B2pferd.__getattribute__(
                                                                                                     self,
                                                                                                     'position_x_BP2')),
                                                           black.B2pferd.__getattribute__(self,
                                                                                          'position_y_BP2'))

        bturm1 = b.Board.givepotentialTurmDestination(self, b.Board.translateLettertoNumber(self,
                                                                                            black.B1turm.__getattribute__(
                                                                                                self,
                                                                                                'position_x_BT1')),
                                                      black.B1turm.__getattribute__(self, 'position_y_BT1'),
                                                      1, 1)[1]
        bturm2 = b.Board.givepotentialTurmDestination(self, b.Board.translateLettertoNumber(self,
                                                                                            black.B2turm.__getattribute__(
                                                                                                self,
                                                                                                'position_x_BT2')),
                                                      black.B2turm.__getattribute__(self, 'position_y_BT2'),
                                                      1, 1)[1]

        bbauer1 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B1bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB1')),
                                                            black.B1bauer.__getattribute__(self,
                                                                                           'position_y_BB1'))
        bbauer2 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B2bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB2')),
                                                            black.B2bauer.__getattribute__(self,
                                                                                           'position_y_BB2'))
        bbauer3 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B3bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB3')),
                                                            black.B3bauer.__getattribute__(self,
                                                                                           'position_y_BB3'))
        bbauer4 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B4bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB4')),
                                                            black.B4bauer.__getattribute__(self,
                                                                                           'position_y_BB4'))
        bbauer5 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B5bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB5')),
                                                            black.B5bauer.__getattribute__(self,
                                                                                           'position_y_BB5'))
        bbauer6 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B6bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB6')),
                                                            black.B6bauer.__getattribute__(self,
                                                                                           'position_y_BB6'))
        bbauer7 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B7bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB7')),
                                                            black.B7bauer.__getattribute__(self,
                                                                                           'position_y_BB7'))
        bbauer8 = b.Board.givepotentialBauerKillDestination(self, b.Board.translateLettertoNumber(self,
                                                                                                  black.B8bauer.__getattribute__(
                                                                                                      self,
                                                                                                      'position_x_BB8')),
                                                            black.B8bauer.__getattribute__(self,
                                                                                           'position_y_BB8'))
        # possible Killing Destinations
        potentialKillingFields_BLACK = bkoenig + bdame + blaeufer1 + blaeufer2 + bpferd1 + bpferd2 + bturm1 + bturm2 + bbauer1 + bbauer2 + bbauer3 + bbauer4 + bbauer5 + bbauer6 + bbauer7 + bbauer8

        # condition for check
        if self.check_againstWhite == 0:
            for element in potentialKillingFields_BLACK:
                if white.W1koenig.__getattribute__(self, 'position_x_WK') == element[
                    0] and white.W1koenig.__getattribute__(self, 'position_y_WK') == element[1]:
                    self.check_againstWhite = 1
                    print('Check! (black->white)')
                    break

        # white->black
        # checking if checkMate is appropiate (when check and the king has no )
        if self.check_againstBlack == 1:
            for element in potentialKillingFields_WHITE:
                if black.B1koenig.__getattribute__(self, 'position_x_BK') == element[
                    0] and black.B1koenig.__getattribute__(self, 'position_y_BK') == element[
                    1]:  # if already check and player black could not handle the chack and is still in check position, then he lost due to checkMate
                    print('BLACK IS CHECK MATE!')
                    print('WHITE WINS! CONGRATULATIONS!!!')
                    self.end = True
                    break
                else:  # player black could defend himself. no check anymore. right now not in check/danger for checkMate
                    self.check_againstBlack = 0


