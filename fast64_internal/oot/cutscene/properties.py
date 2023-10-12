from bpy.types import PropertyGroup, Object, UILayout
from bpy.props import StringProperty, EnumProperty, IntProperty, BoolProperty, CollectionProperty, PointerProperty
from bpy.utils import register_class, unregister_class
from ...utility import PluginError, prop_split
from ..oot_utility import OOTCollectionAdd, drawCollectionOps, getEnumName
from ..oot_constants import ootEnumMusicSeq
from ..oot_upgrade import upgradeCutsceneSubProps, upgradeCSListProps, upgradeCutsceneProperty
from .operators import OOTCSTextAdd, OOT_SearchCSDestinationEnumOperator, drawCSListAddOp
from .constants import (
    ootEnumCSTextboxType,
    ootEnumCSListType,
    ootEnumCSTransitionType,
    ootEnumCSTextboxTypeIcons,
    ootEnumCSDestinationType,
    ootEnumCSMiscType,
    ootEnumTextType,
    ootCSSubPropToName,
    ootEnumOcarinaAction,
    ootEnumSeqPlayer,
)


class OOTCutsceneCommon:
    attrName = None
    subprops = ["startFrame", "endFrame"]
    expandTab: BoolProperty(default=True)
    startFrame: IntProperty(name="", default=0, min=0)
    endFrame: IntProperty(name="", default=1, min=0)

    def getName(self):
        pass

    def filterProp(self, name, listProp):
        return True

    def filterName(self, name, listProp):
        return name

    def draw_props(
        self,
        layout: UILayout,
        listProp: "OOTCSListProperty",
        listIndex: int,
        cmdIndex: int,
        objName: str,
        collectionType: str,
        tabName: str,
    ):
        # Draws list elements
        box = layout.box().column()

        box.prop(
            self,
            "expandTab",
            text=f"{tabName if tabName != 'Text' else self.getName()} No. {cmdIndex}",
            icon="TRIA_DOWN" if self.expandTab else "TRIA_RIGHT",
        )
        if not self.expandTab:
            return

        drawCollectionOps(box, cmdIndex, collectionType + "." + self.attrName, listIndex, objName)

        for p in self.subprops:
            if self.filterProp(p, listProp):
                name = self.filterName(p, listProp)
                displayName = ootCSSubPropToName[name]
                value = getattr(self, p)

                if name == "csSeqPlayer":
                    # change the property name to draw the other enum for fade seq command
                    p = name

                prop_split(box, self, p, displayName)

                customValues = [
                    "csMiscType",
                    "csTextType",
                    "ocarinaAction",
                    "csSeqID",
                    "csSeqPlayer",
                ]
                if name in customValues and value == "Custom":
                    prop_split(box, self, f"{name}Custom", f"{displayName} Custom")

                if name == "csTextType" and value != "CS_TEXT_CHOICE":
                    break


class OOTCSTextProperty(OOTCutsceneCommon, PropertyGroup):
    attrName = "textList"
    subprops = [
        "textID",
        "ocarinaAction",
        "startFrame",
        "endFrame",
        "csTextType",
        "topOptionTextID",
        "bottomOptionTextID",
        "ocarinaMessageId",
    ]
    textboxType: EnumProperty(items=ootEnumCSTextboxType)

    # subprops
    textID: StringProperty(name="", default="0x0000")
    ocarinaAction: EnumProperty(
        name="Ocarina Action", items=ootEnumOcarinaAction, default="OCARINA_ACTION_TEACH_MINUET"
    )
    ocarinaActionCustom: StringProperty(default="OCARINA_ACTION_CUSTOM")
    topOptionTextID: StringProperty(name="", default="0x0000")
    bottomOptionTextID: StringProperty(name="", default="0x0000")
    ocarinaMessageId: StringProperty(name="", default="0x0000")
    csTextType: EnumProperty(name="Text Type", items=ootEnumTextType, default="CS_TEXT_NORMAL")
    csTextTypeCustom: StringProperty(default="CS_TEXT_CUSTOM")

    def getName(self):
        return getEnumName(ootEnumCSTextboxType, self.textboxType)

    def filterProp(self, name, listProp):
        if self.textboxType == "Text":
            return name not in ["ocarinaAction", "ocarinaMessageId"]
        elif self.textboxType == "None":
            return name in ["startFrame", "endFrame"]
        elif self.textboxType == "OcarinaAction":
            return name in ["ocarinaAction", "startFrame", "endFrame", "ocarinaMessageId"]
        else:
            raise PluginError("Invalid property name for OOTCSTextProperty")


class OOTCSLightSettingsProperty(OOTCutsceneCommon, PropertyGroup):
    attrName = "lightSettingsList"
    subprops = ["lightSettingsIndex", "startFrame"]
    lightSettingsIndex: IntProperty(name="", default=1, min=1)


class OOTCSTimeProperty(OOTCutsceneCommon, PropertyGroup):
    attrName = "timeList"
    subprops = ["startFrame", "hour", "minute"]
    hour: IntProperty(name="", default=23, min=0, max=23)
    minute: IntProperty(name="", default=59, min=0, max=59)


class OOTCSSeqProperty(OOTCutsceneCommon, PropertyGroup):
    attrName = "seqList"
    subprops = ["csSeqID", "startFrame", "endFrame"]
    csSeqID: EnumProperty(name="Seq ID", items=ootEnumMusicSeq, default="NA_BGM_SOUND_EFFECTS")
    csSeqIDCustom: StringProperty(default="NA_BGM_CUSTOM")
    csSeqPlayer: EnumProperty(name="Seq Player", items=ootEnumSeqPlayer, default="CS_FADE_OUT_BGM_MAIN")
    csSeqPlayerCustom: StringProperty(default="CS_FADE_OUT_CUSTOM")

    def filterProp(self, name, listProp):
        return name != "endFrame" or listProp.listType == "FadeOutSeqList"

    def filterName(self, name, listProp):
        if name == "csSeqID" and listProp.listType == "FadeOutSeqList":
            return "csSeqPlayer"
        return name


class OOTCSMiscProperty(OOTCutsceneCommon, PropertyGroup):
    attrName = "miscList"
    subprops = ["csMiscType", "startFrame", "endFrame"]
    csMiscType: EnumProperty(name="Type", items=ootEnumCSMiscType, default="CS_MISC_SET_LOCKED_VIEWPOINT")
    csMiscTypeCustom: StringProperty(default="CS_MISC_CUSTOM")


class OOTCSRumbleProperty(OOTCutsceneCommon, PropertyGroup):
    attrName = "rumbleList"
    subprops = ["startFrame", "rumbleSourceStrength", "rumbleDuration", "rumbleDecreaseRate"]

    # those variables are unsigned chars in decomp
    # see https://github.com/zeldaret/oot/blob/542012efa68d110d6b631f9d149f6e5f4e68cc8e/src/code/z_rumble.c#L58-L77
    rumbleSourceStrength: IntProperty(name="", default=0, min=0, max=255)
    rumbleDuration: IntProperty(name="", default=0, min=0, max=255)
    rumbleDecreaseRate: IntProperty(name="", default=0, min=0, max=255)


class OOTCSListProperty(PropertyGroup):
    expandTab: BoolProperty(default=True)

    listType: EnumProperty(items=ootEnumCSListType)
    textList: CollectionProperty(type=OOTCSTextProperty)
    lightSettingsList: CollectionProperty(type=OOTCSLightSettingsProperty)
    timeList: CollectionProperty(type=OOTCSTimeProperty)
    seqList: CollectionProperty(type=OOTCSSeqProperty)
    miscList: CollectionProperty(type=OOTCSMiscProperty)
    rumbleList: CollectionProperty(type=OOTCSRumbleProperty)

    transitionType: EnumProperty(items=ootEnumCSTransitionType)
    transitionTypeCustom: StringProperty(default="CS_TRANS_CUSTOM")
    transitionStartFrame: IntProperty(name="", default=0, min=0)
    transitionEndFrame: IntProperty(name="", default=1, min=0)

    def draw_props(self, layout: UILayout, listIndex: int, objName: str, collectionType: str):
        box = layout.box().column()
        enumName = getEnumName(ootEnumCSListType, self.listType)

        # Draw current command tab
        box.prop(
            self,
            "expandTab",
            text=enumName,
            icon="TRIA_DOWN" if self.expandTab else "TRIA_RIGHT",
        )

        if not self.expandTab:
            return

        drawCollectionOps(box, listIndex, collectionType, None, objName, False)

        # Draw current command content
        if self.listType == "TextList":
            attrName = "textList"
        elif self.listType == "Transition":
            prop_split(box, self, "transitionType", "Transition Type")
            if self.transitionType == "Custom":
                prop_split(box, self, "transitionTypeCustom", "Transition Type Custom")

            prop_split(box, self, "transitionStartFrame", "Start Frame")
            prop_split(box, self, "transitionEndFrame", "End Frame")
            return
        elif self.listType == "LightSettingsList":
            attrName = "lightSettingsList"
        elif self.listType == "TimeList":
            attrName = "timeList"
        elif self.listType in ["StartSeqList", "StopSeqList", "FadeOutSeqList"]:
            attrName = "seqList"
        elif self.listType == "MiscList":
            attrName = "miscList"
        elif self.listType == "RumbleList":
            attrName = "rumbleList"
        else:
            raise PluginError("Internal error: invalid listType " + self.listType)

        dat = getattr(self, attrName)

        if self.listType == "TextList":
            subBox = box.box()
            subBox.label(text="TextBox Commands")
            row = subBox.row(align=True)

            for l in range(3):
                addOp = row.operator(
                    OOTCSTextAdd.bl_idname,
                    text="Add " + ootEnumCSTextboxType[l][1],
                    icon=ootEnumCSTextboxTypeIcons[l],
                )

                addOp.collectionType = collectionType + ".textList"
                addOp.textboxType = ootEnumCSTextboxType[l][0]
                addOp.listIndex = listIndex
                addOp.objName = objName
        else:
            addOp = box.operator(
                OOTCollectionAdd.bl_idname, text="Add item to " + getEnumName(ootEnumCSListType, self.listType)
            )
            addOp.option = len(dat)
            addOp.collectionType = collectionType + "." + attrName
            addOp.subIndex = listIndex
            addOp.objName = objName

        for i, p in enumerate(dat):
            # ``p`` type:
            # OOTCSTextProperty | OOTCSLightSettingsProperty | OOTCSTimeProperty |
            # OOTCSSeqProperty | OOTCSMiscProperty | OOTCSRumbleProperty
            p.draw_props(box, self, listIndex, i, objName, collectionType, enumName.removesuffix(" List"))

        if len(dat) == 0:
            box.label(text="No items in " + getEnumName(ootEnumCSListType, self.listType))


class OOTCutsceneProperty(PropertyGroup):
    csEndFrame: IntProperty(name="End Frame", min=0, default=100)
    csUseDestination: BoolProperty(name="Cutscene Destination (Scene Change)")
    csDestination: EnumProperty(
        name="Destination", items=ootEnumCSDestinationType, default="CS_DEST_CUTSCENE_MAP_GANON_HORSE"
    )
    csDestinationCustom: StringProperty(default="CS_DEST_CUSTOM")
    csDestinationStartFrame: IntProperty(name="Start Frame", min=0, default=99)
    csLists: CollectionProperty(type=OOTCSListProperty, name="Cutscene Lists")

    @staticmethod
    def upgrade_object(obj):
        print(f"Processing '{obj.name}'...")

        # using the new names since the old ones will be deleted before this is used
        csListsNames = ["textList", "lightSettingsList", "timeList", "seqList", "miscList", "rumbleList"]

        csProp: "OOTCutsceneProperty" = obj.ootCutsceneProperty
        upgradeCutsceneProperty(csProp)

        for csListProp in csProp.csLists:
            upgradeCSListProps(csListProp)

            for listName in csListsNames:
                for csListSubProp in getattr(csListProp, listName):
                    upgradeCutsceneSubProps(csListSubProp)

    def draw_props(self, layout: UILayout, obj: Object):
        layout.prop(self, "csEndFrame")

        csDestLayout = layout.box()
        csDestLayout.prop(self, "csUseDestination")
        if self.csUseDestination:
            r = csDestLayout.row()

            searchBox = r.box()
            boxRow = searchBox.row()
            searchOp = boxRow.operator(OOT_SearchCSDestinationEnumOperator.bl_idname, icon="VIEWZOOM", text="")
            searchOp.objName = obj.name
            boxRow.label(text=getEnumName(ootEnumCSDestinationType, self.csDestination))
            if self.csDestination == "Custom":
                prop_split(searchBox.column(), self, "csDestinationCustom", "Cutscene Destination Custom")

            r = csDestLayout.row()
            r.prop(self, "csDestinationStartFrame")

        drawCSListAddOp(layout, obj.name, "Cutscene")

        for i, csListProp in enumerate(self.csLists):
            # ``csListProp`` type: OOTCSListProperty
            csListProp.draw_props(layout, i, obj.name, "Cutscene")


classes = (
    OOTCSTextProperty,
    OOTCSLightSettingsProperty,
    OOTCSTimeProperty,
    OOTCSSeqProperty,
    OOTCSMiscProperty,
    OOTCSRumbleProperty,
    OOTCSListProperty,
    OOTCutsceneProperty,
)


def cutscene_props_register():
    for cls in classes:
        register_class(cls)

    Object.ootCutsceneProperty = PointerProperty(type=OOTCutsceneProperty)


def cutscene_props_unregister():
    del Object.ootCutsceneProperty

    for cls in reversed(classes):
        unregister_class(cls)
