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