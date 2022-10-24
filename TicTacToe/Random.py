import random
from Agent import Agent


def find_space(board):
    pos_row = []
    pos_col = []
    for row, col in board.get_possible_moves():
        pos_row.append(row)
        pos_col.append(col)
    i = random.randint(0, len(pos_row) - 1)
    return pos_row[i], pos_col[i]


class RandomAgent(Agent):
    #
    # def __init__(self, isX=False):
    #     self.isX = isX

    def take_turn(self, board):
        row, col = find_space(board)
        board.take_turn(row, col, self.isX)
