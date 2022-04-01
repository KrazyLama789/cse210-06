
from constants import *
from game.scripting.action import Action
import random


class NpcCombatAction(Action):

    def __init__(self):
        pass
    
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        demon = cast.get_first_actor(DEMON_GROUP)
    
        attacks = [demon.action_1(), demon.action_2(), demon.action_3()]
        choose_attack = random.choice(attacks)
        adventurer.lose_hp(choose_attack) 
        print(f"Demon's attack: {choose_attack}")
        callback.on_next(ADVENTURER_COMBAT)

        # if adventurer.get_current_hp() <= 0:
        #     callback.on_next(GAME_OVER)
         
        # if hit == 1:
        #     adventurer.lose_hp(demon.action_1())
        #     callback.on_next(ADVENTURER_COMBAT)

