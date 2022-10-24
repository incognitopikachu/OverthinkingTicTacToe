from Agent import Agent


class HumanAgent(Agent):

    def take_turn(self, board):
        while not board.is_finished():
            # b.display()
            try:
                i = int(input("Enter row: "))
                j = int(input("Enter col: "))
            except ValueError:
                print("Invalid input: please enter 2 integers 0, 1 or 2")
                continue

            isValid = board.take_turn(i, j, self.isX)
            if not isValid:
                print("Invalid input: Space not free")
                continue
            else:
                break
