from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Adventurer(Actor):
    """A player who is represented as a Knight."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a player.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the player's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the player's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the player using its velocity."""

        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        """Moves the player to the left."""
        velocity = Point(-ADVENTURER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        """Moves the player to the right."""
        velocity = Point(ADVENTURER_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the player from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
    
    def attack_1(self):
        pass
        # boss health -= (rand.int(1, 6) * level)
        
    def attack_2(self):
        pass
        # boss health -= (rand.int(1, 6) * level)
        
    def attack_3(self):
        pass
        # boss health -= (rand.int(1, 6) * level)
            
    def run_away(self):
        pass
        # boss health -= (rand.int(1, 6) * level)
