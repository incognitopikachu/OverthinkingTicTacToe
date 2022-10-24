from Board import play
from Agent import Agent
from Random import RandomAgent
import copy
import math


class Node:

    def __init__(self, board, action, parent=None, isX_turn=True):
        self.children = []
        self.parent = parent
        self.board = board
        self.t = 0
        self.n = 0
        self.isX = isX_turn
        self.action = action

    def select(self):
        """
        Calc. ucb1 of children and return selected child node
        """
        selectedNode = (None, None)
        C = 1.5
        for child in self.children:
            if child.n == 0:
                return child
            x = 1 if self.isX else -1
            ucb = x * (child.t / child.n) + C * math.sqrt(math.log(self.n) / child.n)
            if selectedNode[0] is None or ucb > selectedNode[1]:
                selectedNode = (child, ucb)
        return selectedNode[0]

    def chooseSimNode(self):
        if self.board.is_finished():
            return self
        elif not self.children:
            self.expand()  # we only do one expansion per trial
            return self.select()
        else:
            chosenChild = self.select()
            return chosenChild.chooseSimNode()

    def expand(self):
        """
        Create child nodes
        """
        for i, j in self.board.get_possible_moves():
            b = copy.deepcopy(self.board)
            b.take_turn(i, j, isX=self.isX)
            child = Node(b, (i, j), self, isX_turn=not self.isX)
            self.children.append(child)

    def simulate(self):
        selectedNode = self.chooseSimNode()
        agentX = RandomAgent(isX=True)
        agentO = RandomAgent(isX=False)
        board = copy.deepcopy(selectedNode.board)
        if self.isX:
            score = play(board, agentX, agentO)
        else:
            score = play(board, agentO, agentX)
        selectedNode.backpropogate(score)

    def backpropogate(self, reward):
        self.n = self.n + 1
        self.t = self.t + reward
        if self.parent:
            self.parent.backpropogate(reward)


class MctsAgent(Agent):

    def train(self, node, n_iter=1000):
        for i in range(n_iter):
            node.simulate()

    def take_turn(self, board):
        rootNode = Node(board, None, isX_turn=self.isX)
        self.train(rootNode)
        max_node = max(rootNode.children, key=lambda node: node.n)
        i = max_node.action[0]
        j = max_node.action[1]
        isValid = board.take_turn(i, j, self.isX)
        assert isValid
