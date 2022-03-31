from random import Random
from constants import *
from game.casting.character import Character
from game.casting.point import Point
import random


class Demon(Character):
    """Demon."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a demon.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(body, animation, debug)
        self._level = random.randint(1, 9) #If we make the level two-digits, we will need to fix spacing from side margin
        self._max_hp = self._level * 5
        self._current_hp = self._max_hp 

        print(f"level: {self._level}")
        print(f"current hp: {self._current_hp}")
        print(f"current hp: {self._max_hp}")
        
    
