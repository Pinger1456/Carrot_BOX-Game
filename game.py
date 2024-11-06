"""Main file.
Contains the Game class that manages game logic
(e.g., carrot location, box swapping)"""

import random


class Player:
    """Class to manage player details."""
    def __init__(self, name):
        self.name = name


class Game:
    """Class to manage game logic."""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.carrot_in_first_box = random.randint(1, 2) == 1

    def reveal_carrot_location(self):
        """Reveals whether the carrot is in the first or second box."""
        return self.carrot_in_first_box

    def swap_boxes(self):
        """Swaps carrot location between boxes."""
        self.carrot_in_first_box = not self.carrot_in_first_box

    def get_winner(self):
        """Returns the player who won based on carrot's location."""
        return self.player1 if self.carrot_in_first_box else self.player2
