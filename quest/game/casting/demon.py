from random import Random
from constants import *
from game.casting.character import Character
from game.casting.point import Point
import random


class Demon(Character):
    """Demon."""
    
    def __init__(self, body, animation, adventurer_level, debug = False):
        """Constructs a demon.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(body, animation, debug)
        self._level = adventurer_level + random.randint(0,3)
        self._max_hp = self._level + 5
        self._current_hp = self._max_hp 

        
    
