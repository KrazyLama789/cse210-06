from constants import *
from game.scripting.action import Action


class ControlCombatAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        demon = cast.get_first_actor(DEMON_GROUP)

         # Kosei, build combat controlls here.
        if self._keyboard_service.is_key_pressed("1"): 
            demon.lose_hp(adventurer.action_1())
            callback.on_next(NPC_COMBAT)

        elif self._keyboard_service.is_key_pressed("2"): 
            demon.lose_hp(adventurer.action_2())
            callback.on_next(NPC_COMBAT)

        elif self._keyboard_service.is_key_pressed("3"): 
            demon.lose_hp(adventurer.action_3())
            callback.on_next(NPC_COMBAT)

        # This is for a "run away" action during combat. It is only partially working. 
        elif self._keyboard_service.is_key_pressed("4"): 
            cast.clear_actors(DEMON_GROUP)
            callback.on_next(IN_PLAY)

        else: 
            adventurer.stop_moving()

    #    if adventurer.get_current_hp() <= 0:
    #         callback.on_next(GAME_OVER)
