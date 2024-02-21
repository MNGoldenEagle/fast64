from dataclasses import dataclass, field
from .oot_getters import getXMLRoot
from .oot_data import OoT_BaseElement
from os import path

# Note: "enumData" in this context refers to an OoT Object file (like ``gameplay_keep``)


@dataclass
class OoT_ItemElement(OoT_BaseElement):
    parentKey: str


@dataclass
class OoT_EnumElement(OoT_BaseElement):
    items: list[OoT_ItemElement]
    itemByKey: dict[str, OoT_ItemElement] = field(default_factory=dict)
    itemByIndex: dict[int, OoT_ItemElement] = field(default_factory=dict)
    itemById: dict[int, OoT_ItemElement] = field(default_factory=dict)

    def __post_init__(self):
        self.itemByKey = {item.key: item for item in self.items}
        self.itemByIndex = {item.index: item for item in self.items}
        self.itemById = {item.id: item for item in self.items}


def readEnumFromXml(filename: str, item_type: str) -> OoT_EnumElement:
    file = getXMLRoot(path.join(path.dirname(path.abspath(__file__)), filename))
    result = []
    parent_key = file.attrib["Key"]
    for item in file.iterfind(item_type):
        result.append(
            OoT_ItemElement(
                item.attrib["ID"],
                item.attrib["Key"],
                item.attrib["Name"],
                int(item.attrib["Index"]),
                parent_key
            )
        )

    return OoT_EnumElement(
        file.attrib["ID"],
        parent_key,
        None,
        None,
        result
    )

def getOoTEnumData(enum: OoT_EnumElement):
    deletedEntry = ("None", "(Deleted from the XML)", "None")
    firstIndex = min(1, *(item.index for item in enum.items))
    lastIndex = max(1, *(item.index for item in enum.items)) + 1
    enumData = [deletedEntry] * lastIndex
    custom = ("Custom", "Custom", "Custom")

    for item in enum.items:
        if item.index < lastIndex:
            identifier = item.key
            enumData[item.index] = (identifier, item.name, item.id)

    if firstIndex > 0:
        enumData[0] = custom
    else:
        enumData.insert(0, custom)

    return enumData

class OoT_EnumData:
    """Enum data"""

    def __init__(self):
        # Load enums from the XML files

        audio_presets = readEnumFromXml('xml/audio_presets.xml', 'Preset')
        cs_cmd = readEnumFromXml('xml/cutscene_cmd.xml', 'Cmd')
        cs_dest = readEnumFromXml('xml/cutscene_dest.xml', 'Destination')
        cs_misc = readEnumFromXml('xml/cutscene_misc.xml', 'Misc')
        cs_seqp = readEnumFromXml('xml/cutscene_seqp.xml', 'SeqPlayer')
        cs_text = readEnumFromXml('xml/cutscene_text.xml', 'CsText')
        cs_tran = readEnumFromXml('xml/cutscene_tran.xml', 'Transition')
        light_modes = readEnumFromXml('xml/light_modes.xml', 'Mode')
        nature_sounds = readEnumFromXml('xml/nature_sounds.xml', 'Sound')
        navi_hints = readEnumFromXml('xml/navi_hints.xml', 'HintFile')
        oca_action = readEnumFromXml('xml/ocarina_actions.xml', 'Action')
        player_cues = readEnumFromXml('xml/player_cues.xml', 'Cue')
        player_idle = readEnumFromXml('xml/player_idle.xml', 'Idle')
        room_fx = readEnumFromXml('xml/room_effects.xml', 'Effect')
        room_types = readEnumFromXml('xml/room_types.xml', 'Type')
        scn_cams = readEnumFromXml('xml/scene_cams.xml', 'CamMode')
        scn_cfg = readEnumFromXml('xml/scene_config.xml', 'Config')
        scn_locale = readEnumFromXml('xml/scene_locale.xml', 'Location')
        scn_skybox = readEnumFromXml('xml/scene_skybox.xml', 'Skybox')
        scn_ids = readEnumFromXml('xml/scenes.xml', 'Scene')
        sequences = readEnumFromXml('xml/sequences.xml', 'Sequence')
        transitions = readEnumFromXml('xml/transitions.xml', 'Transition')

        # create list of tuples used by Blender's enum properties

        self.ootAudioPresets: list[tuple[str, str, str]] = getOoTEnumData(audio_presets)
        self.ootEnumCameraMode: list[tuple[str, str, str]] = getOoTEnumData(scn_cams)
        self.ootEnumCsCmd: list[tuple[str, str, str]] = getOoTEnumData(cs_cmd)
        self.ootEnumCsDestination: list[tuple[str, str, str]] = getOoTEnumData(cs_dest)
        self.ootEnumCsFadeOutSeqPlayer: list[tuple[str, str, str]] = getOoTEnumData(cs_seqp)
        self.ootEnumCsMiscType: list[tuple[str, str, str]] = getOoTEnumData(cs_misc)
        self.ootEnumCsPlayerCueId: list[tuple[str, str, str]] = getOoTEnumData(player_cues)
        self.ootEnumCsTextType: list[tuple[str, str, str]] = getOoTEnumData(cs_text)
        self.ootEnumCsTransitionType: list[tuple[str, str, str]] = getOoTEnumData(cs_tran)
        self.ootEnumDrawConfig: list[tuple[str, str, str]] = getOoTEnumData(scn_cfg)
        self.ootEnumLightModes: list[tuple[str, str, str]] = getOoTEnumData(light_modes)
        self.ootEnumLinkIdle: list[tuple[str, str, str]] = getOoTEnumData(player_idle)
        self.ootEnumMapLocation: list[tuple[str, str, str]] = getOoTEnumData(scn_locale)
        self.ootEnumNaviQuestHintType: list[tuple[str, str, str]] = getOoTEnumData(navi_hints)
        self.ootEnumNightSeq: list[tuple[str, str, str]] = getOoTEnumData(nature_sounds)
        self.ootEnumOcarinaSongActionId: list[tuple[str, str, str]] = getOoTEnumData(oca_action)
        self.ootEnumRoomBehavior: list[tuple[str, str, str]] = getOoTEnumData(room_fx)
        self.ootEnumRoomShapeType: list[tuple[str, str, str]] = getOoTEnumData(room_types)
        self.ootEnumSceneID: list[tuple[str, str, str]] = getOoTEnumData(scn_ids)
        self.ootEnumSeqId: list[tuple[str, str, str]] = getOoTEnumData(sequences)
        self.ootEnumSkybox: list[tuple[str, str, str]] = getOoTEnumData(scn_skybox)
        self.ootEnumTransitions: list[tuple[str, str, str]] = getOoTEnumData(transitions)

        # general enumData lists
        self.enumDataList: list[OoT_EnumElement] = [audio_presets, cs_cmd, cs_dest, cs_misc, cs_seqp, cs_text, cs_tran, light_modes, nature_sounds, navi_hints, oca_action, player_cues, player_idle, room_fx, room_types, scn_cams, scn_cfg, scn_locale, scn_skybox]

        self.enumByKey = {enum.key: enum for enum in self.enumDataList}
