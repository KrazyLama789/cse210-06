from game.casting.color import Color
from game.casting.point import Point

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Quest"
FRAME_RATE = 120

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = int(SCREEN_WIDTH / 2)
CENTER_Y = int(SCREEN_HEIGHT / 2)
LEFT_CENTER_X = int(SCREEN_WIDTH / 3)
RIGHT_CENTER_X = int(LEFT_CENTER_X * 2)

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "quest/assets/fonts/DungeonFont.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "quest/assets/sounds/boing.wav"
WELCOME_SOUND = "quest/assets/sounds/start.wav"
OVER_SOUND = "quest/assets/sounds/over.wav"
COMBAT_SOUNDTRACK = "quest/assets/sounds/juhani-junkala-epic-boss-battle.mp3"


# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
IN_PLAY = 1
NEW_SCREEN = 2
COMBAT = 3
GAME_OVER = 4
TRY_AGAIN = 5

# LEVELS
LEVEL_FILE = "quest/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_HP = 10

# HUD
HUD_MARGIN = 15
LEVEL_POSITION = Point(HUD_MARGIN, HUD_MARGIN)
HP_POSITION = Point(HUD_MARGIN, HUD_MARGIN + FONT_SMALL)
XP_POSITION = Point(HUD_MARGIN, HUD_MARGIN + FONT_SMALL * 2)
LEVEL_FORMAT = "LEVEL: {}"
HP_FORMAT = "HP: {}/{}"
XP_FORMAT = "XP: {}"

# ADVENTURER
ADVENTURER_GROUP = "adventurers"
ADVENTURER_IMAGES = [f"quest/assets/images/{n:03}.png" for n in range(101, 113)]
ADVENTURER_WIDTH = 106
ADVENTURER_HEIGHT = 100 
"""I changed adventurer height to 250 to move it up on the screen, before I realized that it's starting position is set in scene_manager 
under add_adventurer"""
ADVENTURER_RATE = 6
ADVENTURER_VELOCITY = 1

# DEMON
DEMON_GROUP = "demon"
DEMON_IMAGES = [f"quest/assets/images/demon-idle{n:1}.png" for n in range(1, 6)]
DEMON_WIDTH = 106
DEMON_HEIGHT = 100
"""I changed Demon height to 325 to move it up on the screen, before I realized that it's starting position is set in scene_manager 
under add_adventurer"""
DEMON_RATE = 6
DEMON_VELOCITY = 1

#BACKGROUND
LAYER_1 = "quest/assets/images/redsky.png",
LAYER_2 = "quest/assets/images/redmountain.png",
LAYER_3 = "quest/assets/images/redtree.png",
LAYER_4 = "quest/assets/images/redtown.png",
LAYER_5 = "quest/assets/images/redcloud.png"

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
ENTERING_COMBAT = "ENTERING COMBAT"
WAS_GOOD_GAME = "GAME OVER"

DEMON_LINE_1 = "Fear the Dark"
DEMON_LINE_2 = "You Will Obey"
DEMON_LINE_3 = "I am your Master"
