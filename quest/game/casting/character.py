from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Character(Actor):
    """Character."""
    
    def __init__(self, body, animation, debug = False):
        """Interface for player characters and non player characters.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._debug = debug
        self._level = self._set_level()
        self._max_hp = DEFAULT_HP
        self._current_hp = DEFAULT_HP

    def _set_level(self):
        self._level = 1
    
    def get_animation(self):
        """Gets character's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets character's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
    
    def move_next(self):
        """Moves the character using its velocity."""

        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        """Moves the character to the left."""
        velocity = Point(-ADVENTURER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        """Moves the character to the right."""
        velocity = Point(ADVENTURER_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the character from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
    
    def action_1(self, opponent_level):
        """What the character does when key 1 is pressed"""
        # hit = (rand.int(1, 6) * level)
        # if hit >= opponent_level:
    def action_2(self):
        """What the character does when key 2 is pressed"""
        
    def action_3(self):
        """What the character does when key 3 is pressed"""
            
    def action_4(self):
        """What the character does when key 4 is pressed"""
        
    def add_hp(self):
        """Adds to current hit xp."""
        if self._current_hp < self._max_hp:
            self._current_hp += 1

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
        """Get max hit points.

        Returns:
            A number representing the amount of hit points.
        """
        return self._max_hp

    def lose_hp(self):
        """Removes one life."""
        if self._hp > 0:
            self._hp -= 1

