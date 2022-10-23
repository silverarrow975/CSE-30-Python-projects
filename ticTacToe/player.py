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
            cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n')

            # if the user chose a cell that is not empty promt them to choose another cell
            # print a message that the input is wrong and rewrite the prompt
            while(not board.isempty(cell)):
                  print("You did not choose correctly.")
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n')

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

            #setting up the opponent's sign
            if(self.get_sign == "X"):
                  self.opp_sign = "O"
            else:
                  self.opp_sign = "X"
      
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

      def get_oppSign(self):
            return self.opp_sign

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

import math
class MiniMax(AI):
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True) # have minimax choose a cell
            print(cell)
            board.set(cell, self.sign)

      # self_player is a bool that lets you know whether it's minimax's turn
      # start is a bool
      def minimax(self, board, self_player, start):
            # check the base conditions
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == self.get_sign():
                        board.reset_winner()
                        return 1
                  # is a tie
                  elif board.get_winner() == " ":
                        board.reset_winner()
                        return 0
                  # self is a looser (opponent is a winner)
                  else:
                        board.reset_winner()
                        return -1
            
            # make a move (choose a cell) recursively
            move = "" # choosing a move
            
            # set the min and max score to infinity
            minScore = math.inf 
            maxScore = -math.inf     

            # iterate through all avalible cells
            # check if the cell is empty
            for col in range(board.get_size()[0]):
                  for row in range(board.get_size()[1]):
                        cell = super().cellToStr(row+1, col+1) # convert the row and cell index to a cell str because that's what isempty accepts
                        # print(cell)
                        
                        if(board.isempty(cell)):
                              if(self_player): # if it is the AI's turn mark with their sign
                                    board.set(cell, self.get_sign())
                                    score = self.minimax(board, False, False) # rescursive call
                                    board.set(cell, " ") # reset the cell
                                    # if the score is greater than the maxScore that is the best move
                                    if(score > maxScore):
                                          maxScore = score
                                          move = cell # best move
                              else: # mark with the other player's sign
                                    board.set(cell, super().get_oppSign())
                                    score = self.minimax(board, True, False)
                                    board.set(cell, " ") # reset the cell
                                    if(score < minScore):
                                          minScore = score
                                          move = cell

            if start:
                  return move # return to best move once you come back to the original call of the function
            elif self_player: # if it's minimax's turn return the maxScore
                  return maxScore
            else: # return the minScore if its the opponent's turn
                  return minScore

