from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideDemonAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service  
        self._is_combat = False  
        
    def execute(self, cast, script, callback):
        if len(cast.get_actors(DEMON_GROUP)) > 0:
            adventurer = cast.get_first_actor(ADVENTURER_GROUP)
            body = adventurer.get_body()
            adventurer_position = body.get_position()
            adventurer_x = adventurer_position.get_x()
            demon = cast.get_first_actor(DEMON_GROUP)
            body = demon.get_body()
            demon_position = body.get_position()
            demon_x = demon_position.get_x()
            
            if adventurer_x in range(int(demon_x - 30), int(demon_x + DEMON_WIDTH)):
                callback.on_next(COMBAT)
