"""
Core class representing a player
"""


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 10
        self.team = None

