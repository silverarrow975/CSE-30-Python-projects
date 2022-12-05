# assignment: PA 5 - 15 Puzzle
# author: Harshita Bhardwaj
# date: 12/4/22
# file: 
# input: 
# output: 

import numpy as np
from graph import Graph
from random import choice

class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4):
        # creates a numpy array from 1 to 15 with a 0 at the end
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.board = self.tiles.reshape(4, 4) # creates a 2d numpy array for the tiles
        self.size = size
        
        # still need to figure out how to create an adjacency list or a graph for the rest of __init__

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        print('+---+---+---+---+')
        for r in self.board:
            # for creating an individual row
            print('|', end="")
            for c in r:
                # if the tile is 0
                if c == 0:
                    print('   ', end='|')
                # if the tile is 2 digits
                elif len(str(c)) == 2:
                    print(f'{c} ', end="|")
                # if the tile is 1 digit
                else:
                    print(f' {c} ', end="|")
                    
            # create the divider for the next row
            print('\n+---+---+---+---+')
                

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self):
        s = ""
        for r in self.board:
            # for creating an individual row
            for c in r:
                # if the number is 0
                if c == 0:
                    s += '   '
                # if the number is 2 digits
                elif len(str(c)) == 2:
                    s += f'{c} '
                else:
                    s += f" {c} "
            s += '\n'
            
        return s

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):
        iRow, iCol = i[0], i[1]
        jRow, jCol = j[0], j[1]
        self.board[iRow][iCol], self.board[jRow][jCol] = self.board[jRow][jCol], self.board[iRow][iCol]
    
    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):  
        zeroIndex = self.index(0) # find where 0 is in the arr
        moveIndex = self.index(move)
        
        # the possible row or column the move can be in to be valid
        pRow = []
        pCol = []
        
        # checking which possible row the move can be in
        # if 0 is in the first row
        if zeroIndex[0] == 0:
            pRow.append(zeroIndex[0] + 1) # valid moves can be in the row below
        # if 0 is in the last row
        elif zeroIndex[0] == 3:
            pRow.append(zeroIndex[0] - 1) # valid moves can be in the row below
        # if 0 is in the middle rows
        else:
            pRow.append(zeroIndex[0] + 1)
            pRow.append(zeroIndex[0] - 1)
        # add the current row as a possible row
        pRow.append(zeroIndex[0])
        
        # checking which possible columns the move can be in
        # if 0 is in the left column
        if zeroIndex[1] == 0:
            pCol.append(zeroIndex[1] + 1)
        # if 0 is in the top right column
        elif zeroIndex[1] == 3:
            pCol.append(zeroIndex[1] - 1)
        # if 0 is in the middle columns
        else:
            pCol.append(zeroIndex[1] + 1)
            pCol.append(zeroIndex[1] - 1)
        # add the current col as a possible col
        pCol.append(zeroIndex[1])
            
        # check if the move is possible or not
        if moveIndex[0] in pRow and moveIndex[1] in pCol:
            return True
        else:
            return False

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move):
        if self.is_valid_move(move):
            vector = self.transpose(self.index(0), self.index(move))
    
    # looks for the index in a 2D numpy arr
    # can also be used for a normal arr
    def index(self, val):
        # holds an array for the index of the val
        # first element is the row index
        # second element is the column index
        i = [] 
        
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == val:
                    i.append(r) # add the row index
                    i.append(c) # add the col index
                    return i # return the index
                
        # if no index was found
        return -1
        
    # shuffle tiles
    def shuffle(self, moves = 30):
        if moves == 0:
            # once the number of moves is 0 then shuffle the board
            return
        else:
            self.shuffle(moves - 1)
            # create an arr of possible moves
            pMoves = []
            for r in self.board:
                for c in r:
                    if self.is_valid_move(c):
                        pMoves.append(c) # add c as a possible move if it is a valid move
            # choice a random move using choice from random
            randMove = choice(pMoves)
            
            # update the move on the board
            self.update(randMove)
    
    # verify if the puzzle is solved
    def is_solved(self):
        baseCheck = np.array([i for i in range(1,self.size**2)] + [0])
        normal = baseCheck.reshape(4, 4)
        zeroAtSt = np.array([i for i in range(0,self.size**2)]).reshape(4, 4)
        zeroAtEd = np.flip(zeroAtSt)
        flipped = np.flip(normal)
        
        if (self.board == normal).all() or (self.board == flipped).all() or (zeroAtSt == self.board).all() or (zeroAtEd == self.board).all():
            return True

        return False

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle (optional)
    def solve(self):
        pass
    
if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    