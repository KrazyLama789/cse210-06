from constants import *
from game.scripting.action import Action


class DrawDemonAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        if len(cast.get_actors(DEMON_GROUP)) != 0:
            demon = cast.get_first_actor(DEMON_GROUP)
            body = demon.get_body()

            if demon.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = demon.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)