from constants import *
from game.scripting.action import Action


class ControlAdventurerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            adventurer.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            adventurer.move_right()  
        else: 
            adventurer.stop_moving()        