from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._max_hp = DEFAULT_HP
        self._current_hp = DEFAULT_HP
        self._xp = 0

    def add_max_hp(self):
        """Increases maximum hit xp."""
        self._max_hp += 3
        self._current_hp = self._max_hp
        
    def add_hp(self):
        """Adds to current hit xp."""
        if self._current_hp < self._max_hp:
            self._current_hp += 1
        
    def add_xp(self, xp):
        """Adds the given xp to the total experience points.
        
        Args:
            xp: A number representing the experience to add.
        """
        self._xp += xp

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_current_hp(self):
        """Get current hit points.

        Returns:
            A number representing the amount of hit points.
        """
        return self._current_hp
    
    def get_max_hp(self):
        """Git max hit points.

        Returns:
            A number representing the amount of hit points.
        """
        return self._max_hp
  
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

# Uses if implementing new game functionality.
    # def reset(self):
    #         """Resets the stats back to their default values."""
    #         self._level = 1
    #         self._hp = DEFAULT_HP
    #         self._xp = 0