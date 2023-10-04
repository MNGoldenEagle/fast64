import bpy
from bpy.types import Operator
from bpy.props import EnumProperty, StringProperty
from bpy.utils import register_class, unregister_class
from ...utility import PluginError
from ..oot_constants import ootData, ootEnumTransitionActorID, ootEnumActorID


class OOT_SearchActorIDEnumOperator(Operator):
    bl_idname = "object.oot_search_actor_id_enum_operator"
    bl_label = "Select Actor ID"
    bl_property = "actorID"
    bl_options = {"REGISTER", "UNDO"}

    def actorItems(self, _):
        return ootEnumTransitionActorID if self.actorUser == "Transition Actor" else ootEnumActorID

    actorUser: StringProperty(default="Actor")
    actorID: EnumProperty(items=actorItems)
    objName: StringProperty()

    def execute(self, context):
        obj = bpy.data.objects[self.objName]
        if self.actorUser == "Transition Actor":
            obj.ootTransitionActorProperty.actor.actorID = self.actorID
        elif self.actorUser == "Actor":
            obj.ootActorProperty.actorID = self.actorID
        elif self.actorUser == "Entrance":
            obj.ootEntranceProperty.actor.actorID = self.actorID
        else:
            raise PluginError(f"Invalid actor user for search: {self.actorUser}")

        context.region.tag_redraw()
        self.report({"INFO"}, f"Selected: {self.actorID}")
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {"RUNNING_MODAL"}


classes = (OOT_SearchActorIDEnumOperator,)


def actor_ops_register():
    for cls in classes:
        register_class(cls)


def actor_ops_unregister():
    for cls in reversed(classes):
        unregister_class(cls)
