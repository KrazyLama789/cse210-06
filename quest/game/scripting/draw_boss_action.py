from constants import *
from game.scripting.action import Action


class DrawBossAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        boss = cast.get_first_actor(BOSS_GROUP)
        body = boss.get_body()

        if boss.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = boss.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)