# author: Harshita Bhardwaj
# date: Oct 19, 2022
# file: board.py is a file that creates and sets up functionality for the tic tac toe board
# input: depends on the method being called
# output: depends on the method being called
# the file by itself does not ask for any input nor does it provide any output
# this class must be used with the tictac.py file to play a tic tac toe game

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = []
            # create a 2d array for the board
            for _ in range(self.size):
                  self.board.append(list(self.sign * self.size))
            # the winner's sign O or X
            self.winner = "" # reset the winner
      def get_size(self): 
             # optional, return the board size (an instance size)
            return len(self.board)* len(self.board[0])
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
            return self.winner

      # change the cell str to an index for the board 2d arr
      def convertCell(self, cell):
            alpha = cell[0].lower()

            # getting the column index
            match alpha:
                  case 'a':
                        col = 0
                  case 'b':
                        col = 1
                  case 'c':
                        col = 2
            row = int(cell[1]) - 1 # row index

            return (row, col)

      # mark the cell on the board with the sign X or O
      def set(self, cell, sign):
            # convert A1, B1, …, C3 cells into index values
            cellTupl = self.convertCell(cell)

            # update that index in the board to the sign
            self.board[cellTupl[0]][cellTupl[1]] = sign
            # print("done?", done)
                              
      def isempty(self, cell):
            # if the cell is invalid return false
            if(self.invalidIndex(cell)):
                  return False

            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            cellTupple = self.convertCell(cell)
            # return True if the cell is empty (not marked with X or O)
            if(self.board[cellTupple[0]][cellTupple[1]] == " "):
                  return True
            return False

      def invalidIndex (self, cell):
            # check if the alphabet part of the cell is not A, B, or C
            # or if the number part of the cell is greater than 3
            if(ord(cell[0].upper()) - 65 > 2 or int(cell[1]) > 3):
                  return True
            
            return False
      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # checking rows
            for row in self.board:
                  if(row[0] == row[1] == row[2] and row[0] != " "):
                        done = True # set done to be true
                        self.winner = row[0] # update the winning sign
                        break # break out of the rows loop
            
            # checking columns
            if not done:
                  for col in range(len(self.board)):
                        if(self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col]  != " "):
                              done = True # set done to be true
                              self.winner = self.board[0][col] # update the winning sign
                              break # break out of the cols loop

            # checking diagonals
            # coordinates of the 2 combs for there to be a diagonal win
            # diagonal = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1,1), (2, 0)]] Just for reference
            if(not done):
                  # if the signs in the diagonals are the same and are not empty
                  if(self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " "):
                        done = True
                        self.winner = self.board[0][0]
                  elif(self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " "):
                        done = True
                        self.winner = self.board[0][0]

            # depending on conditions assign the instance var winner to O or X
            return done

      # draw the board
      def show(self):
            print('   A   B   C ')
            print(' +---+---+---+')
            for i in range(len(self.board)):
                  print(f'{i + 1}|', end="") # print the number corresponsing to each row
                  for j in self.board[i]:
                        print(f' {j} |', end="") # print the signs of each spot in the board

                  print('\n +---+---+---+')


