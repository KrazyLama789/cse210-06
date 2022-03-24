from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._hp = DEFAULT_HP
        self._xp = 0

    def add_life(self):
        """Adds one life."""
        self._hp += 3

    def add_points(self, points):
        """Adds the given points to the xp.
        
        Args:
            points: A number representing the points to add.
        """
        self._xp += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_hp(self):
        """Adds hit points.

        Returns:
            A number representing the amount of hit points.
        """
        return self._hp
  
    def get_xp(self):
        """Gets the xp.

        Returns:
            A number representing the xp.
        """
        return self._xp

    def lose_life(self):
        """Removes one life."""
        if self._hp > 0:
            self._hp -= 1
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._hp = DEFAULT_HP
        self._xp = 0