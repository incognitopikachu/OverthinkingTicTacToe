# OverthinkingTicTacToe
This project implements a simple game of noughts and crosses (tic tac toe) printing the board graphically
Players may input their moves inputing the (zero-indexed) coordinates of the chosen move: (row, column) 

A few CPU player stratagies are implemtned, inheriting from the Agent,py base class/interface:
- Random, this stratagy makes random (valid) moves
- Minimax, this uses the minimax algorithm to maximise/minimise the score. This will play optimally (assumming it's opponent is also playing optimally)
- MCTS (Monte Carlo Tree Search), this stratagy uses a monte carlo tree search to evaluate potential moves, given enough training this appears to perform close to optimally

# Running
- Python version 3.6+ (earlier versions of 3.x will probably also work)
- Only standard python libs are used so it shouldn't be necesary to install any packages with pip
- Run: "python main.py"
- Optional arguements can be used to specify the computer's stratagy: 
  - "-mcts"
  - "-random"
  - "-minimax"
