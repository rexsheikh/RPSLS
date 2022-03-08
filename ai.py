from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.ai_gesture = random.randint(0,4)
        return self.ai_gesture