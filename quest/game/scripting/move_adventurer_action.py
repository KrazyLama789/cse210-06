from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveAdventurerAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        body = adventurer.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(SCREEN_WIDTH, position.get_y())
        elif x > (SCREEN_WIDTH):
            position = Point(0, position.get_y())
            
        body.set_position(position)
        