class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        pass

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
        pass

    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self): 
        pass

    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j): 
        pass

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):  
        pass

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move): 
        pass
    
    # shuffle tiles
    def shuffle(self, moves = 100):
        pass
    
    # verify if the puzzle is solved
    def is_solved(self):
        pass

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle (optional)
    def solve(self):
        pass