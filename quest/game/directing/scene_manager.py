import csv
from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.adventurer import Adventurer
from game.casting.demon import Demon
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.control_combat_action import ControlCombatAction
from game.scripting.collide_demon_action import CollideDemonAction
from game.scripting.control_adventurer_action import ControlAdventurerAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_adventurer_action import DrawAdventurerAction
from game.scripting.draw_demon_action import DrawDemonAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.npc_combat_action import NpcCombatAction
from game.scripting.move_adventurer_action import MoveAdventurerAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    
    CONTROL_ADVENTURER_ACTION = ControlAdventurerAction(KEYBOARD_SERVICE)
    CONTROL_COMBAT_ACTION = ControlCombatAction(KEYBOARD_SERVICE)
    COLLIDE_DEMON_ACTION = CollideDemonAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_ADVENTURER_ACTION = DrawAdventurerAction(VIDEO_SERVICE)
    DRAW_DEMON_ACTION = DrawDemonAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    NPC_COMBAT_ACTION = NpcCombatAction()
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_ADVENTURER_ACTION = MoveAdventurerAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == NEW_SCREEN:
            self._prepare_new_screen(cast, script)
        elif scene == COMBAT:
            self._prepare_combat(cast, script)
        elif scene == ADVENTURER_COMBAT:
            self._prepare_adventurer_combat(cast, script)
        elif scene == ADVENTURER_ATTACK:
            self._prepare_adventurer_attack(cast, script)
        elif scene == NPC_COMBAT:
            self._prepare_npc_combat(cast, script)
        elif scene == NPC_ATTACK:
            self._prepare_npc_attack(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
        # elif scene == TRY_AGAIN:
        #     self._prepare_try_again(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_adventurer(cast)
        self._add_dialog(cast, WELCOME)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 4))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
        
    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_ADVENTURER_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)
        
    def _prepare_new_screen(self, cast, script):
        cast.clear_actors(DEMON_GROUP)
        self._add_demon(cast)
        
    def _prepare_combat(self, cast, script):
        self._get_adventurer(cast)
        self._get_demon(cast)
        self._add_dialog(cast, ENTERING_COMBAT)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(ADVENTURER_COMBAT, 2))
        self._add_output_script(script)
        self.CONTROL_COMBAT_ACTION.reset_turn()
        
    def _prepare_adventurer_combat(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        self._add_dialog(cast, "Adventurer: \n To Attack Press: \n 1 - Stab \n 2 - Slash \n 3 - Quick Attack", CENTER_X, CENTER_Y - 225)
        self._get_adventurer(cast)
        self._get_demon

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_COMBAT_ACTION)
        self._add_output_script(script)
        self.NPC_COMBAT_ACTION.reset_turn()
        print("Adventurer's turn:")
        
    def _prepare_adventurer_attack(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        self._add_dialog(cast, self.CONTROL_COMBAT_ACTION.get_attack())
        script.add_action(INPUT, TimedChangeSceneAction(NPC_COMBAT, 2))
        
    def _prepare_npc_combat(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        self._add_dialog(cast,"Demons Turn")
        self._get_adventurer(cast)
        self._get_demon(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.NPC_COMBAT_ACTION)
        script.add_action(INPUT, TimedChangeSceneAction(NPC_ATTACK, 2))
        self._add_output_script(script)
        self.CONTROL_COMBAT_ACTION.reset_turn()
        print("Demon's turn")
        
    def _prepare_npc_attack(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        self._add_dialog(cast, self.NPC_COMBAT_ACTION.get_attack())
        script.add_action(INPUT, TimedChangeSceneAction(ADVENTURER_COMBAT, 2))
 
    def _prepare_game_over(self, cast, script):
        print ("game over")
        self._add_dialog(cast, GAME_OVER)
        cast.clear_actors(ADVENTURER_GROUP)
        cast.clear_actors(DEMON_GROUP)

        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)
        self._add_output_script(script)
       
    # def _prepare_try_again(self, cast, script):
    #     self._add_adventurer(cast)
    #     self._add_dialog(cast, PREP_TO_LAUNCH)

    #     script.clear_actions(INPUT)
    #     script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
    #     self._add_update_script(script)
    #     self._add_output_script(script)
    
    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_dialog(self, cast, message, x = CENTER_X, y = CENTER_Y - 50):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(x, y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_adventurer(self, cast):
        cast.clear_actors(ADVENTURER_GROUP)
        x = CENTER_X - ADVENTURER_WIDTH / 2
        y = SCREEN_HEIGHT - 250 #ADVENTURER_HEIGHT
        position = Point(x, y)
        size = Point(ADVENTURER_WIDTH, ADVENTURER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(ADVENTURER_IMAGES, ADVENTURER_RATE)
        adventurer = Adventurer(body, animation)
        cast.add_actor(ADVENTURER_GROUP, adventurer)
        
    def _get_adventurer(self, cast):
        adventurer = cast.get_first_actor(ADVENTURER_GROUP)
        adventurer.reset_position()
        return cast.get_first_actor(ADVENTURER_GROUP)
        
    def _add_demon(self, cast, direction = "right"):
        cast.clear_actors(DEMON_GROUP)
        if direction == "left":
            x = LEFT_CENTER_X - DEMON_WIDTH / 2
        else:    
            x = RIGHT_CENTER_X - DEMON_WIDTH / 2
        x = RIGHT_CENTER_X - DEMON_WIDTH / 2
        y = SCREEN_HEIGHT - 320 #DEMON_HEIGHT
        position = Point(x, y)
        size = Point(DEMON_WIDTH, DEMON_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(DEMON_IMAGES, DEMON_RATE)
        demon = Demon(body, animation, cast.get_first_actor(ADVENTURER_GROUP).get_level())
        cast.add_actor(DEMON_GROUP, demon)
        
    def _get_demon(self, cast):
        return cast.get_first_actor(DEMON_GROUP)
        

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_ADVENTURER_ACTION)
        script.add_action(OUTPUT, self.DRAW_DEMON_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_ADVENTURER_ACTION)
        script.add_action(UPDATE, self.COLLIDE_DEMON_ACTION)
        script.add_action(UPDATE, self.MOVE_ADVENTURER_ACTION)