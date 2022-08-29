import re
from .oot_actor import setAllActorsVisibility
import bpy
from .c_writer import OOTBootupSceneOptions
from ..panels import OOT_Panel
from bpy.utils import register_class, unregister_class
from .oot_level import oot_obj_panel_register, oot_obj_panel_unregister, oot_obj_register, oot_obj_unregister
from .oot_anim import oot_anim_panel_register, oot_anim_panel_unregister, oot_anim_register, oot_anim_unregister
from .oot_collision import oot_col_panel_register, oot_col_panel_unregister, oot_col_register, oot_col_unregister
from .oot_utility import oot_utility_register, oot_utility_unregister
from ..utility import prop_split
from . import oot_parse
from . import oot_constants
from ..render_settings import on_update_render_settings

from ..panels import OOT_Panel
from ..utility import prop_split, raisePluginError

from .oot_f3d_writer import (
    OOTDLExportSettings,
    OOTDLImportSettings,
    oot_dl_writer_panel_register,
    oot_dl_writer_panel_unregister,
    oot_dl_writer_register,
    oot_dl_writer_unregister,
)

from .oot_level_writer import (
    oot_level_panel_register,
    oot_level_panel_unregister,
    oot_level_register,
    oot_level_unregister,
)

from .oot_operators import (
    oot_operator_panel_register,
    oot_operator_panel_unregister,
    oot_operator_register,
    oot_operator_unregister,
)

from .oot_skeleton import (
    oot_skeleton_panel_register,
    oot_skeleton_panel_unregister,
    oot_skeleton_register,
    oot_skeleton_unregister,
)

from .oot_spline import (
    oot_spline_panel_register,
    oot_spline_panel_unregister,
    oot_spline_register,
    oot_spline_unregister,
)

from .oot_cutscene import (
    oot_cutscene_panel_register,
    oot_cutscene_panel_unregister,
    oot_cutscene_register,
    oot_cutscene_unregister,
)

import os
import os.path

class OOT_RefreshAssetEnums(bpy.types.Operator):
    # set bl_ properties
    bl_idname = 'scene.refresh_enums'
    bl_label = "Refresh Assets"
    bl_options = {'INTERNAL', 'BLOCKING'}

    # Only enable if the decomp path points to a real directory that matches the following criteria:
    # 1. Contains a .git folder
    # 2. Contains a build/include/tables folder
    # 3. Previous folder contains actor_table.h, object_table.h, scene_table.h
    @classmethod
    def poll(self, context):
        repoPath = context.scene.ootDecompPath

        if os.path.exists(repoPath):
            return os.path.exists(os.path.join(repoPath, '.git')) and \
                os.path.exists(os.path.join(repoPath, 'build', 'include', 'tables', 'actor_table.h')) and \
                os.path.exists(os.path.join(repoPath, 'build', 'include', 'tables', 'object_table.h')) and \
                os.path.exists(os.path.join(repoPath, 'build', 'include', 'tables', 'scene_table.h'))
        
        return False

    # Called on demand (i.e. button press, menu item)
    def execute(self, context):
        repoPath = context.scene.ootDecompPath
        tablesPath = os.path.join(repoPath, 'build', 'include', 'tables')
        includesPath = os.path.join(repoPath, 'include')

        try:
            with open(os.path.join(tablesPath, 'actor_table.h'), 'r') as actor_table:
                actors = [re.fullmatch('DEFINE_ACTOR\(([^,]+), ([^,]+), [^\)]+\)\n', line) for line in actor_table.readlines()]
                for i in range(len(actors)):
                    actor = actors[i]
                    if actor is None:
                        continue
                    actors[i] = (actor.group(2), actor.group(1), actor.group(1), i)
                actors.insert(0, ('Custom', 'Custom', 'Custom', -1))
                actors.insert(1, ("ACTOR_PLAYER", "Player", "Player", 0))
                actors.insert(2, ("ACTOR_EN_ITEM00", "En Item00", "En Item00", 1))
                actors.insert(3, ("ACTOR_EN_A_OBJ", "En A Obj", "En A Obj", 2))
                transitionActors = [actor for actor in actors if 'Door' in actor]
                print(actors)
                print(transitionActors)
            with open(os.path.join(tablesPath, 'object_table.h'), 'r') as object_table:
                objects = [re.fullmatch('DEFINE_OBJECT\(([^,]+), ([^\)]+)\)\n', line) for line in object_table.readlines()]
                for i in range(len(objects)):
                    obj = objects[i]
                    if obj is None:
                        continue
                    objects[i] = (obj.group(2), obj.group(1), obj.group(1), i)
                keeps = [obj for obj in objects if 'keep' in obj[1]]
                objects = [obj for obj in objects if obj not in keeps]
                objects.insert(0, ('Custom', 'Custom', 'Custom', -1))
                print(keeps)
                print(objects)
            with open(os.path.join(tablesPath, 'scene_table.h'), 'r') as scene_table:
                scenes = [re.fullmatch('DEFINE_SCENE\(([^,]+), [^,]+, ([^,]+), [^,]+, [^,]+, \d+, \d+\)\n', line) for line in scene_table.readlines()]
                for i in range(len(scenes)):
                    scene = scenes[i]
                    if scene is None:
                        continue
                    sceneName = scene.group(1).replace("_scene", "").replace("_", " ").title()
                    scenes[i] = (scene.group(2), sceneName, scene.group(1), i)
                scenes.insert(0, ('Custom', 'Custom', 'Custom', -1))
                print(scenes)
            with open(os.path.join(includesPath, "sequence.h"), 'r') as seq_h:
                data = seq_h.read()
                ambience = oot_parse.parseEnumFile(data, "NatureAmbienceId", "NATURE_ID", ignoreList=['MAX'], includeCustom=False)
                print(ambience)
            with open(os.path.join(tablesPath, 'sequence_table.h'), 'r') as seq_table:
                sequences = [re.fullmatch('([^,]+),\s*/?/?\s?(.*)\n', line) for line in seq_table.readlines()]
                for i in range(len(sequences)):
                    sequence = sequences[i]
                    if sequence is None:
                        continue
                    sequences[i] = (sequence.group(2), sequence.group(1), sequence.group(1), i)
                print(sequences)
            with open(os.path.join(includesPath, "z64transition.h"), 'r') as transition_h:
                data = transition_h.read()
                transitions = oot_parse.parseEnumFile(data, "TransitionType", "TRANS_TYPE", ignoreList=['MAX'], includeCustom=True)
                # Add the special circle types and variants, since there's no dedicated enums for them
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_BLACK, TCS_FAST)',     'Circle (Black, Fast)',      'Circle (Black, Fast)',       32))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_BLACK, TCS_SLOW)',     'Circle (Black, Slow)',      'Circle (Black, Slow)',       33))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_WHITE, TCS_FAST)',     'Circle (White, Fast)',      'Circle (White, Fast)',       34))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_WHITE, TCS_SLOW)',     'Circle (White, Slow)',      'Circle (White, Slow)',       35))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_BLACK, TCS_FAST)',       'Wave (Black, Fast)',        'Wave (Black, Fast)',         36))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_BLACK, TCS_SLOW)',       'Wave (Black, Slow)',        'Wave (Black, Slow)',         37))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_WHITE, TCS_FAST)',       'Wave (White, Fast)',        'Wave (White, Fast)',         38))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_WHITE, TCS_SLOW)',       'Wave (White, Slow)',        'Wave (White, Slow)',         39))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_BLACK, TCS_FAST)',     'Ripple (Black, Fast)',      'Ripple (Black, Fast)',       40))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_BLACK, TCS_SLOW)',     'Ripple (Black, Slow)',      'Ripple (Black, Slow)',       41))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_WHITE, TCS_FAST)',     'Ripple (White, Fast)',      'Ripple (White, Fast)',       42))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_WHITE, TCS_SLOW)',     'Ripple (White, Slow)',      'Ripple (White, Slow)',       43))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_BLACK, TCS_SLOW)',  'Starburst (Black, Slow)',   'Starburst (Black, Slow)',    44))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_BLACK, TCS_FAST)',  'Starburst (Black, Fast)',   'Starburst (Black, Fast)',    45))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_WHITE, TCS_FAST)',  'Starburst (White, Fast)',   'Starburst (White, Fast)',    46))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_WHITE, TCS_SLOW)',  'Starburst (White, Slow)',   'Starburst (White, Slow)',    47))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_GRAY, TCS_FAST)',       'Circle (Gray, Fast)',       'Circle (Gray, Fast)',       48))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_GRAY, TCS_SLOW)',       'Circle (Gray, Slow)',       'Circle (Gray, Slow)',       49))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_GRAY, TCS_FAST)',         'Wave (Gray, Fast)',         'Wave (Gray, Fast)',         50))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_GRAY, TCS_SLOW)',         'Wave (Gray, Slow)',         'Wave (Gray, Slow)',         51))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_GRAY, TCS_FAST)',       'Ripple (Gray, Fast)',       'Ripple (Gray, Fast)',       52))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_GRAY, TCS_SLOW)',       'Ripple (Gray, Slow)',       'Ripple (Gray, Slow)',       53))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_GRAY, TCS_FAST)',    'Starburst (Gray, Fast)',    'Starburst (Gray, Fast)',    54))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_GRAY, TCS_SLOW)',    'Starburst (Gray, Slow)',    'Starburst (Gray, Slow)',    55))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_SPECIAL, TCS_FAST)',    'Circle (Special, Fast)',    'Circle (Special, Fast)',    56))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_NORMAL, TCC_SPECIAL, TCS_SLOW)',    'Circle (Special, Slow)',    'Circle (Special, Slow)',    57))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_SPECIAL, TCS_FAST)',      'Wave (Special, Fast)',      'Wave (Special, Fast)',      58))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_WAVE, TCC_SPECIAL, TCS_SLOW)',      'Wave (Special, Slow)',      'Wave (Special, Slow)',      59))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_SPECIAL, TCS_FAST)',    'Ripple (Special, Fast)',    'Ripple (Special, Fast)',    60))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_RIPPLE, TCC_SPECIAL, TCS_SLOW)',    'Ripple (Special, Slow)',    'Ripple (Special, Slow)',    61))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_SPECIAL, TCS_FAST)', 'Starburst (Special, Fast)', 'Starburst (Special, Fast)', 62))
                transitions.append(('TRANS_TYPE_CIRCLE(TCA_STARBURST, TCC_SPECIAL, TCS_SLOW)', 'Starburst (Special, Slow)', 'Starburst (Special, Slow)', 63))
                print(transitions)
            with open(os.path.join(includesPath, "z64scene.h"), 'r') as scene_h:
                data = scene_h.read()
                scene_draws = oot_parse.parseEnumFile(data, "SceneDrawConfig", "SDC", ignoreList=['MAX'], includeCustom=False)
                print(scene_draws)
            oot_constants.ootEnumActorID.clear()
            oot_constants.ootEnumActorID.extend(actors)
            oot_constants.ootEnumTransitionActorID.clear()
            oot_constants.ootDefaultEnumTransitionActorID.extend(transitionActors)
            oot_constants.ootEnumObjectID.clear()
            oot_constants.ootEnumObjectID.extend(objects)
            oot_constants.ootEnumGlobalObject.clear()
            oot_constants.ootEnumGlobalObject.extend(keeps)
            oot_constants.ootEnumSceneID.clear()
            oot_constants.ootEnumSceneID.extend(scenes)
            oot_constants.ootEnumMusicSeq.clear()
            oot_constants.ootEnumMusicSeq.extend(sequences)
            oot_constants.ootEnumNightSeq.clear()
            oot_constants.ootEnumNightSeq.extend(ambience)
            oot_constants.ootEnumTransitionAnims.clear()
            oot_constants.ootEnumTransitionAnims.extend(transitions)
            oot_constants.ootDrawConfigNames.clear()
            oot_constants.ootDrawConfigNames.extend(scene_draws)
            return {'FINISHED'}
        except Exception as e:
            raisePluginError(self, e)
            return {'CANCELLED'} # must return a set



class OOT_FileSettingsPanel(OOT_Panel):
    bl_idname = "OOT_PT_file_settings"
    bl_label = "OOT File Settings"
    bl_options = set()  # default to being open

    # called every frame
    def draw(self, context):
        col = self.layout.column()
        col.scale_y = 1.1  # extra padding, makes it easier to see these main settings
        prop_split(col, context.scene, "ootBlenderScale", "OOT Scene Scale")

        prop_split(col, context.scene, "ootDecompPath", "Repo Path")
        col.operator(OOT_RefreshAssetEnums.bl_idname, text="Refresh")
        col.prop(context.scene.fast64.oot, "headerTabAffectsVisibility")
        col.prop(context.scene.fast64.oot, "hackerFeaturesEnabled")


class OOT_Properties(bpy.types.PropertyGroup):
    """Global OOT Scene Properties found under scene.fast64.oot"""

    version: bpy.props.IntProperty(name="OOT_Properties Version", default=0)
    hackerFeaturesEnabled: bpy.props.BoolProperty(name="Enable HackerOOT Features")
    headerTabAffectsVisibility: bpy.props.BoolProperty(
        default=False, name="Header Sets Actor Visibility", update=setAllActorsVisibility
    )
    bootupSceneOptions: bpy.props.PointerProperty(type=OOTBootupSceneOptions)
    DLExportSettings: bpy.props.PointerProperty(type=OOTDLExportSettings)
    DLImportSettings: bpy.props.PointerProperty(type=OOTDLImportSettings)
    skeletonExportSettings: bpy.props.PointerProperty(type=oot_skeleton.OOTSkeletonExportSettings)
    skeletonImportSettings: bpy.props.PointerProperty(type=oot_skeleton.OOTSkeletonImportSettings)
    animExportSettings: bpy.props.PointerProperty(type=oot_anim.OOTAnimExportSettingsProperty)
    animImportSettings: bpy.props.PointerProperty(type=oot_anim.OOTAnimImportSettingsProperty)


oot_classes = (
    OOT_FileSettingsPanel,
    OOT_Properties,
    OOT_RefreshAssetEnums
)

decompPath = ""

def oot_set_repo_path(self, path):
    self["path"] = path
    if bpy.ops.scene.refresh_enums.poll():
        bpy.ops.scene.refresh_enums()

def oot_get_repo_path(self):
    return self.get("path", "")

def oot_panel_register():
    oot_operator_panel_register()
    oot_dl_writer_panel_register()
    oot_col_panel_register()
    oot_obj_panel_register()
    oot_level_panel_register()
    oot_spline_panel_register()
    oot_anim_panel_register()
    oot_skeleton_panel_register()
    oot_cutscene_panel_register()


def oot_panel_unregister():
    oot_operator_panel_unregister()
    oot_col_panel_unregister()
    oot_obj_panel_unregister()
    oot_level_panel_unregister()
    oot_spline_panel_unregister()
    oot_dl_writer_panel_unregister()
    oot_anim_panel_unregister()
    oot_skeleton_panel_unregister()
    oot_cutscene_panel_unregister()


def oot_register(registerPanels):
    oot_operator_register()
    oot_utility_register()
    oot_col_register()  # register first, so panel goes above mat panel
    oot_obj_register()
    oot_level_register()
    oot_spline_register()
    oot_dl_writer_register()
    oot_anim_register()
    oot_skeleton_register()
    oot_cutscene_register()

    for cls in oot_classes:
        register_class(cls)

    if registerPanels:
        oot_panel_register()

    bpy.types.Scene.ootBlenderScale = bpy.props.FloatProperty(
        name="Blender To OOT Scale", default=10, update=on_update_render_settings
    )
    bpy.types.Scene.ootDecompPath = bpy.props.StringProperty(name="Repo Folder", subtype="DIR_PATH", get=oot_get_repo_path, set=oot_set_repo_path)


def oot_unregister(unregisterPanels):
    for cls in reversed(oot_classes):
        unregister_class(cls)

    oot_operator_unregister()
    oot_utility_unregister()
    oot_col_unregister()  # register first, so panel goes above mat panel
    oot_obj_unregister()
    oot_level_unregister()
    oot_spline_unregister()
    oot_dl_writer_unregister()
    oot_anim_unregister()
    oot_skeleton_unregister()
    oot_cutscene_unregister()

    if unregisterPanels:
        oot_panel_unregister()

    del bpy.types.Scene.ootBlenderScale
    del bpy.types.Scene.ootDecompPath
