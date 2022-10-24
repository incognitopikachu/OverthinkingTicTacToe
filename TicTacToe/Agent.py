from abc import ABC, abstractmethod


class Agent(ABC):
    """
    Abstract base class for concrete instances to inherit form
    """

    def __init__(self, isX=False):
        self.isX = isX

    @abstractmethod
    def take_turn(self, b):
        pass
