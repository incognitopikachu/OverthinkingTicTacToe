from Agent import Agent


def ai_take_turn_min_max(board, is_max):
    tup = findBestMove(board, is_max)
    board.take_turn(tup[0], tup[1], isX=is_max)


def findBestMove(board, is_max):
    best_dict = {}
    for i, j in board.get_possible_moves():
        board.take_turn(i, j, isX=is_max)
        best_dict[(i, j)] = minimax(board, is_max)
        board.clear(i, j)
    return min(best_dict, key=best_dict.get)  # returns tuple


def minimax(board, nextTurnX):
    if board.is_finished():
        return board.get_score()

    if not nextTurnX:
        bestVal = -1000
        for i, j in board.get_possible_moves():
            board.take_turn(i, j, not nextTurnX)
            val = minimax(board, not nextTurnX)
            bestVal = max(bestVal, val)
            board.clear(i, j)
        return bestVal
    else:
        bestVal = 1000
        for i, j in board.get_possible_moves():
            board.take_turn(i, j, not nextTurnX)
            val = minimax(board, not nextTurnX)
            bestVal = min(bestVal, val)
            board.clear(i, j)
        return bestVal


class MinimaxAgent(Agent):

    def take_turn(self, board):
        tup = findBestMove(board, self.isX)
        board.take_turn(tup[0], tup[1], isX=self.isX)
