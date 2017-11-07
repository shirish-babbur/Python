"""
    This module contains class board and related methods
"""
class Board(object):

    def __init__(self, row, column):
        self.row = row
        self.col = column
        self.board=[]
        for i in range(self.row):
            self.board.append([])
            for j in range(self.col):
                self.board[i].append(-1)

    def update_board(self, r, c, sign):
        """
            This method will put the given sign at said position in board.
        """
        if self.board[r][c] == -1:
            self.board[r][c] = sign
        else:
            print("already occupied!")

    def isfull(self):
        """
            This method will let us know whether board is fully occupied or not
        """
        for i in range(self.row):
            for j in range(self.col):
                if(self.board[i][j] == -1):
                    return False

        return True

    def print_board(self):
        """
            This method will display the board.
        """
        for i in range(self.row):
            for j in range(self.col):
                print(self.board[i][j],"\t",end='')
            print()
