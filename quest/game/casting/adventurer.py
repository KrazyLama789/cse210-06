from constants import *
from game.casting.character import Character
from game.casting.point import Point


class Adventurer(Character):
    """A player who is represented as a Knight."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a player.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(body, animation, debug)
        self._xp = 0

    def add_xp(self, xp):
        """Adds the given xp to the total experience points.
        
        Args:
            xp: A number representing the experience to add.
        """
        self._xp += xp
      
    def get_xp(self):
        """Gets the xp.

        Returns:
            A number representing the xp.
        """
        return self._xp
    
    def level_up(self):
        """Adds one level."""
        self._level += 1
        self.add_max_hp()
        
    def add_max_hp(self):
        """Increases maximum hit hp."""
        self._max_hp += 3
        self._current_hp = self._max_hp
        
    def reset_position(self):
        body = self.get_body()
        position = body.get_position()
        current_y = position.get_y()
        body.set_position(Point(LEFT_CENTER_X, current_y))
        self.stop_moving()