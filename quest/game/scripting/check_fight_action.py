from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CheckFightAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        if self._is_boss_fight:
            adventurer = cast.get_first_actor(ADVENTURER_GROUP)
            boss = cast.get_first_actor(BOSS_GROUP)
            if boss.get_is_boss_fight == True:
                callback.on_next(BOSS_FIGHT)