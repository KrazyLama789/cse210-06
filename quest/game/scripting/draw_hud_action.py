from constants import *
from game.scripting.action import Action
from game.casting.text import Text


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        self._text = Text
        
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        self._draw_label(cast, PLAYER_POSITION, PLAYER_FORMAT, "Adventurer")
        self._draw_label(cast, LEVEL_POSITION, LEVEL_FORMAT, adventurer.get_level())
        self._draw_label(cast, HP_POSITION, HP_FORMAT, adventurer.get_current_hp(), adventurer.get_max_hp())
        self._draw_label(cast, XP_POSITION, XP_FORMAT, adventurer.get_xp())
        
        if len(cast.get_actors(DEMON_GROUP)) > 0:
            demon = cast.get_first_actor(DEMON_GROUP)
            self._draw_label(cast, RIGHT_PLAYER_POSITION, RIGHT_PLAYER_FORMAT, "Demon")
            self._draw_label(cast, RIGHT_LEVEL_POSITION, RIGHT_LEVEL_FORMAT, demon.get_level())
            self._draw_label(cast, RIGHT_HP_POSITION, RIGHT_HP_FORMAT, demon.get_current_hp(), demon.get_max_hp())  
     
    def _draw_label(self, cast, position, format_str, data1, data2 = ""):
        stats = format_str.format(data1, data2)
        displayed_stats = self._text(stats, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = position
        self._video_service.draw_text(displayed_stats, position)