class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')

            # if the user chose a cell that is not empty promt them to choose another cell
            # print a message that the input is wrong and rewrite the prompt
            while(not board.isempty(cell)):
                  print("You did not choose correctly.")
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')

            # if the user enters a valid string and the cell on the board is empty, update the board
            board.set(cell, self.sign)
            # use the methods board.isempty(cell), and board.set(cell, sign)

from random import randint
class AI (Player):
      def __init__(self, name, sign, board):
            ## this part is in parent class 
            # why are we passing in board????
            self.board = board
            super().__init__(name, sign)
      
      # having the AI randomly choose a spot on the board
      def choose(self, board):
            # choose a random cell
            row = randint(1, board.get_size()[0])
            col = randint(1, board.get_size()[1])

            cell = self.cellToStr(row, col) # convert to a cell str
            # while the cell is not empty continue to choose another cell
            while(not board.isempty(cell)):
                  # choose a random cell
                  row = randint(1, board.get_size()[0])
                  col = randint(1, board.get_size()[1])
                  # convert to a cell str
                  cell = self.cellToStr(row, col)

            # showing the user which cell the AI picked
            print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n{cell}')
            # choose a cell on the board
            board.set(cell, self.sign)

      
      def cellToStr(self, row, col):
            # convert the row index to a cell letter
            match row:
                  case 1:
                        c = "A"
                  case 2:
                        c = "B"
                  case 3:
                        c = "C"

            return c + str(col)
