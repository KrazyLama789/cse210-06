from constants import *
from game.scripting.action import Action
from game.casting.text import Text


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        self._text = Text
        
    def execute(self, cast, script, callback):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        self._draw_label(cast, LEVEL_POSITION, LEVEL_FORMAT, adventurer.get_level())
        self._draw_label(cast, HP_POSITION, HP_FORMAT, adventurer.get_current_hp(), adventurer.get_max_hp())
        self._draw_label(cast, XP_POSITION, XP_FORMAT, adventurer.get_xp())

    def _draw_label(self, cast, position, format_str, data1, data2 = ""):
        stats = format_str.format(data1, data2)
        displayed_stats = self._text(stats, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = position
        self._video_service.draw_text(displayed_stats, position)