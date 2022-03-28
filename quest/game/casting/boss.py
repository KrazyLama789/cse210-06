from constants import *
from game.casting.character import Character
from game.casting.point import Point


class Boss(Character):
    """Boss."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a boss.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(body, animation, debug)