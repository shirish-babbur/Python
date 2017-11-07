"""
    This module will have all the validation logic for game.
"""
class Validator(object):
    """
        This class will have all the methods related to the validation
    """
    def __init__(self, r, c):
        self.row = r
        self.col = c

    def check_if_won(self, board, sign):
        """
            This method checks if any player won or not
        """
        i = 0
        j = 0
        while i < self.row:
            j = 0
            while j < self.col:
                if (self.row_c(board, sign, i, j) or self.col_c(board, sign, i, j) or self.diagonal_c(board, sign, i, j)):
                    return True
                j += 1
            i += 1
        else:
            return False
    def row_c(self, board, sign, r, c):
        """
            This method will chcek by row
        """
        counter = 0
        coll = c
        colr = c + 1
        while(coll >= 0 ):
            if(board[r][coll] == sign):
                counter += 1
            coll -= 1
        while(colr < self.col):
            if(board[r][colr] == sign):
                counter += 1
            colr += 1
        if (counter == 3):
            return True
        else:
            return False

    def col_c(self, board, sign, r, c):
        """
            This method will check column wise
        """
        counter = 0
        rowu = r
        rowd = r + 1
        while(rowu >= 0):
            if(board[rowu][c] == sign):
                counter += 1
            rowu -= 1
        while(rowd < self.row):
            if(board[rowd][c] == sign):
                counter += 1
            rowd += 1
        if (counter == 3):
            return True
        else:
            return False

    def diagonal_c(self, board, sign, r, c):
        """
            This method will check by diagonals
        """
        counter = 0
        if (r == 1 and c == 1):
                return True
            if( board[r - 1][c - 1] == sign and board[r + 1][c + 1] == sign and board[r][c] == sign):
            elif( board[r + 1][c - 1] == sign and board[r - 1][c + 1] == sign and board[r][c] == sign):
                return True
            else:
                return False
        else:
            return False
