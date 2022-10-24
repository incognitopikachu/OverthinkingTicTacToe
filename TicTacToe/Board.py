import numpy as np


def play(board, agent1, agent2, drawBoard=False):
    """
    Main game loop
    """
    # Loop until the game ends
    while not board.is_finished():

        if drawBoard:
            board.display()

        # Player 1's turn
        agent1.take_turn(board)

        if drawBoard:
            board.display()
        if board.is_finished():
            break
        # Player 2's turn
        agent2.take_turn(board)
        if drawBoard:
            board.display()
    # When the game is over return the score
    return board.get_score()


class Board:
    """
    Representation of a noughts and crosses grid
    1 represents an X
    -1 represents a O
    """
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.score = None

    def display(self):
        """
        Print the current board state
        """
        for row in self.board:
            row_str = ""
            for i in range(len(row)):
                if row[i] == 1:
                    row_str += "X"
                elif row[i] == 0:
                    row_str += "-"
                elif row[i] == -1:
                    row_str += "O"
                if i == 0 or i == 1:
                    row_str += "|"
            print(row_str)
            print("-----")
            print(" ")

    def get_possible_moves(self):
        """
        Returns the coordinates of empty spaces
        Can be used in loop: 'for i,j in board.get_possible_moves()'
        """
        rows = []
        cols = []
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    rows.append(i)
                    cols.append(j)
        return zip(rows, cols)

    def is_empty(self, i, j):
        """
        Check if space on board is occupied
        """
        if self.board[i][j] == 0:
            return True
        return False

    def clear(self, i, j):
        """
        Reset a space on the board to be empty
        """
        self.board[i][j] = 0

    def take_turn(self, i, j, isX=True):
        """
        Insert a move on an empty space
        Returns false if the space is not empty
        """
        if self.board[i][j] != 0:
            return False  # invalid
        self.board[i][j] = 1 if isX else -1
        return True

    def get_score(self):
        """
        Get the score of a board after a game is complete
        1: X wins, -1: O wins, 0: stalemate
        """
        assert self.is_finished()
        assert self.score is not None
        return self.score

    def is_finished(self):
        """
        Returns true if the game is complete.
        Updates the score attribute if it is
        """
        # check rows
        for row in self.board:
            if abs(np.sum(row)) == 3:
                self.score = np.sum(row) / 3
                return True
        # check cols
        for col in np.transpose(self.board):
            if abs(np.sum(col)) == 3:
                self.score = np.sum(col) / 3
                return True
        # check diagonals
        if abs(np.sum(self.board.diagonal())) == 3:
            self.score = np.sum(self.board.diagonal()) / 3
            return True
        if abs(self.board[2][0] + self.board[1][1] + self.board[0][2]) == 3:
            self.score = (self.board[2][0] + self.board[1][1] + self.board[0][2]) / 3
            return True
        # check for stalemate
        if 0 in self.board:
            return False
        self.score = 0
        return True
