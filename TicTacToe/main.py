import sys
from Board import Board, play
from MCTS import MctsAgent
from Human import HumanAgent
from Random import RandomAgent
from Minimax import MinimaxAgent

# Entry point
if __name__ == '__main__':

    human = HumanAgent(isX=True)

    if "-minimax" in sys.argv:
        ai = MinimaxAgent()
    elif "-random" in sys.argv:
        ai = RandomAgent()
    elif "-MCTS" in sys.argv:
        ai = MctsAgent()
    else:
        print("Please specify your oponent:")
        print("-random      Uses random moves")
        print("-minimax      Uses minimax algorithm")
        print("-MCTS      Uses MCTS (monte carlo tree search) reinforcement learning")
        raise SystemExit

    b = Board()
    score = play(b, human, ai, drawBoard=True)

    print("Game Over")
    if score > 0:
        print("X won")
    elif score < 0:
        print("0 won")
    else:
        print("Stalemate")
