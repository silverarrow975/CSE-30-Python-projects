from player import AI
class MiniMax(AI):
    def choose(self, board):
        print(f"\n{self.?}, {self.?}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == ?
                return 1
            # is a tie
            elif board.get_winner() == ?:
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
                
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
           ???