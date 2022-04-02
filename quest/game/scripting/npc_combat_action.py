
from constants import *
from game.scripting.action import Action
import random


class NpcCombatAction(Action):

    def __init__(self):
        self._turn_attack = 0
        self._attack = 0
    
    def execute(self, cast, script, callback):
        if self._turn_attack == 0:
            adventurer = cast.get_first_actor(ADVENTURER_GROUP)
            demon = cast.get_first_actor(DEMON_GROUP)
        
            attacks = [demon.action_1(), demon.action_2(), demon.action_3()]
            choose_attack = random.choice(attacks)
            self._attack = choose_attack
            adventurer.lose_hp(choose_attack) 
            print(f"Demon's attack: {choose_attack}")
            self._turn_attack = 1
        
            if adventurer.get_current_hp() <= 0:
                callback.on_next(GAME_OVER)
        return
 
        # if hit == 1:
        #     adventurer.lose_hp(demon.action_1())
        #     callback.on_next(ADVENTURER_COMBAT)
    
            
    def get_attack(self):
        message = ""
        if self._attack > 0:
            message = f"The Demon attacked for {self._attack} damage."
        else:
            message = f"The Demon attack missed. {self._attack} damage."
        return message 
    
    def reset_turn(self):
        self._turn_attack = 0
        
        

