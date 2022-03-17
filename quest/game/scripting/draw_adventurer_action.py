from constants import *
from game.scripting.action import Action


class DrawAdventurerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        body = adventurer.get_body()

        if adventurer.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = adventurer.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)