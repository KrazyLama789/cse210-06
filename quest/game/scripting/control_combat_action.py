from constants import *
from game.scripting.action import Action


class ControlCombatAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._turn_attack = 0
        self._attack = 0
        
    def execute(self, cast, script, callback):
        if self._turn_attack == 0:
            adventurer = cast.get_first_actor(ADVENTURER_GROUP)
            demon = cast.get_first_actor(DEMON_GROUP)
            is_player = True
            if self._keyboard_service.is_key_pressed("1"): 
                self._attack = adventurer.action_1(is_player)
                demon.lose_hp(self._attack)
                # sound = Sound(STAB_SOUND)
                # adventurer.audio_service.play_sound(sound)
                callback.on_next(ADVENTURER_ATTACK)
                self._turn_attack = 1
                print (self._attack)

            elif self._keyboard_service.is_key_pressed("2"): 
                self._attack = adventurer.action_2(is_player)
                demon.lose_hp(self._attack)
                callback.on_next(ADVENTURER_ATTACK)
                self._turn_attack = 1
                print (self._attack)

            elif self._keyboard_service.is_key_pressed("3"): 
                self._attack = adventurer.action_3(is_player)
                demon.lose_hp(self._attack)
                callback.on_next(ADVENTURER_ATTACK)
                self._turn_attack = 1
                print (self._attack)

            elif self._keyboard_service.is_key_pressed("r"): 
                self._attack = adventurer.action_r(is_player)
                demon.lose_hp(self._attack)
                callback.on_next(ADVENTURER_ATTACK)
                self._turn_attack = 1
                print (self._attack)
    
            elif self._keyboard_service.is_key_pressed("4"): 
                cast.clear_actors(DEMON_GROUP)
                callback.on_next(IN_PLAY)
                
            if demon.get_current_hp() <= 0:
                adventurer.reset_hp()
                cast.clear_actors(DEMON_GROUP)
                adventurer.add_xp(demon.get_level()+2)
                callback.on_next(IN_PLAY)

    def get_attack(self):
        message = ""
        if self._attack > 0:
            message = f"Adventurer attacked for {self._attack} damage."
        else:
            message = f"Your attack missed. {self._attack} damage."
        return message
    
    def reset_turn(self):
        self._turn_attack = 0
