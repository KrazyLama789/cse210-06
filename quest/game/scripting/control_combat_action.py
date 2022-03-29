from constants import *
from game.scripting.action import Action


class ControlCombatAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        
       #This is for a "run away" action during combat. It is only partially working. 
        if self._keyboard_service.is_key_down("4"):
            callback.on_next(IN_PLAY)

        # Kosei, build combat controlls here.
        # if self._keyboard_service.is_key_down(): 
        #     adventurer.move_left()
        # elif self._keyboard_service.is_key_down(RIGHT): 
        #     adventurer.move_right()  
        # else: 
        #     adventurer.stop_moving()        