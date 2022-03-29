from constants import *
from game.scripting.action import Action


class ChangeSceneAction(Action):

    def __init__(self, next_scene):
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        callback.on_next(self._next_scene)