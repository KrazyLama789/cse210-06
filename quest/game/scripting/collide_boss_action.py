from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideBossAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service  
        self._is_boss_fight = False  
        
    def execute(self, cast, script, callback):
        if len(cast.get_actors(BOSS_GROUP)) != 0:
            adventurer = cast.get_first_actor(ADVENTURER_GROUP)
            body = adventurer.get_body()
            adventurer_position = body.get_position()
            adventurer_x = adventurer_position.get_x()
            boss = cast.get_first_actor(BOSS_GROUP)
            body = boss.get_body()
            boss_position = body.get_position()
            boss_x = boss_position.get_x()
            
            if adventurer_x in range(int(boss_x - 30), int(boss_x + 30)):
                callback.on_next(BOSS_FIGHT)