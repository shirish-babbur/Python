"""
    This module contains engine which will let user play with CPU
"""
from board import Board
from Validator import Validator
class Engine(object):
    """
        This class will contain methods like play.
    """
    def play(self):
        """
            This method is the core of game which takes care of game's status
        """
        won = False
        who = -1;
        board = Board(3, 3)
        validator = Validator(3, 3)
        self.first = input("First player please input your Name:\n>> ")
        self.second = input("Second player please input your Name:\n>> ")
        while(won is not True):
            if board.isfull() is not True:
                r = int(input(f"{self.first}: give row number where you want to put cross\n>> "))
                c = int(input(f"{self.first}: give column number where you want to put cross\n>> "))
                board.update_board(r - 1, c - 1, 1)
                board.print_board()
                won = validator.check_if_won(board.board, 1)
                if(won is True):
                    who = 1
                    break
            else:
                print("Sorry No one won !")
                return
            if board.isfull() is not True:
                r = int(input(f"{self.second}: give row number where you want to put circle\n>> "))
                c = int(input(f"{self.second}: give column number where you want to put circle\n>> "))
                board.update_board(r - 1, c - 1, 0)
                board.print_board()
                won = validator.check_if_won(board.board, 0)
                if(won is True):
                    who = 2
                    break
            else:
                print("Sorry No one won !")
                return
        if(who == 1):
            print(f"Congrats {self.first} You won the game!")
        else:
            print("Congrats {self.second} You won the game!")

engine = Engine()
engine.play()
