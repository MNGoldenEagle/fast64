import json, os

addon_path = os.path.dirname(os.path.realpath(os.path.join(__file__, '..')))

def readJsonFile(filename):
	with open(os.path.join(addon_path, filename)) as file:
		result = json.load(file)
	
	result = [tuple(arr) for arr in result]
	return result

ootEnumRoomShapeType = [
	# ("Custom", "Custom", "Custom"),
	("ROOM_SHAPE_TYPE_NORMAL", "Normal", "Normal (standard mesh)"),
	("ROOM_SHAPE_TYPE_IMAGE", "Image", "Image (JPEG backdrop, mesh used for masking obstructions)"),
	("ROOM_SHAPE_TYPE_CULLABLE", "Cullable", "Cullable (regions are autogenerated)"),
]

ootRoomShapeStructs = [
	"RoomShapeNormal",
	"RoomShapeImage",
	"RoomShapeCullable",
]

ootRoomShapeEntryStructs = [
	"RoomShapeDListsEntry",
	"RoomShapeDListsEntry",
	"RoomShapeCullableEntry",
]

ootEnumSceneMenu = [
	("General", "General", "General"),
	("Lighting", "Lighting", "Lighting"),
	("Cutscene", "Cutscene", "Cutscene"),
	("Exits", "Exits", "Exits"),
	("Alternate", "Alternate", "Alternate"),
]

ootEnumRenderScene = [
	("General", "General", "General"),
	("Alternate", "Alternate", "Alternate"),
]

ootEnumSceneMenuAlternate = [
	("General", "General", "General"),
	("Lighting", "Lighting", "Lighting"),
	("Cutscene", "Cutscene", "Cutscene"),
	("Exits", "Exits", "Exits"),
]

ootEnumRoomMenu = [
	("General", "General", "General"),
	("Objects", "Objects", "Objects"),
	("Alternate", "Alternate", "Alternate"),
]

ootEnumRoomMenuAlternate = [
	("General", "General", "General"),
	("Objects", "Objects", "Objects"),
]

ootEnumHeaderMenu = [
	("Child Night", "Child Night", "Child Night"),
	("Adult Day", "Adult Day", "Adult Day"),
	("Adult Night", "Adult Night", "Adult Night"),
	("Cutscene", "Cutscene", "Cutscene"),
]

ootEnumHeaderMenuComplete = [
	("Child Day", "Child Day", "Child Day"),
	("Child Night", "Child Night", "Child Night"),
	("Adult Day", "Adult Day", "Adult Day"),
	("Adult Night", "Adult Night", "Adult Night"),
	("Cutscene", "Cutscene", "Cutscene"),
]

ootEnumLightGroupMenu = [
	("Dawn", "Dawn", "Dawn"),
	("Day", "Day", "Day"),
	("Dusk", "Dusk", "Dusk"),
	("Night", "Night", "Night"),
]

ootEnumActorID = [
	("Custom", "Custom", "Custom"),
	("ACTOR_PLAYER", "Player", "PLAYER"),
	("ACTOR_EN_ITEM00", "Item00", "EN_ITEM00"),
	("ACTOR_EN_A_OBJ", "A Obj", "EN_A_OBJ")
] + readJsonFile('actors.json')

ootEnumTransitionActorID = [actor for actor in ootEnumActorID if 'door' in actor[1].lower() or 'holl' in actor[1].lower()]

ootEnumLinkIdle = [
	("Custom", "Custom", "Custom"),
	("0x00", "Default", "Default"),
	("0x01", "Sneezing", "Sneezing"),
	("0x02", "Wiping Forehead", "Wiping Forehead"),
	("0x04", "Yawning", "Yawning"),
	("0x07", "Gasping For Breath", "Gasping For Breath"),
	("0x09", "Brandish Sword", "Brandish Sword"),
	("0x0A", "Adjust Tunic", "Adjust Tunic"),
	("0xFF", "Hops On Epona", "Hops On Epona"),
]

# Make sure to add exceptions in utility.py - selectMeshChildrenOnly
ootEnumEmptyType = [
	("None", "None", "None"),
	("Scene", "Scene", "Scene"),
	("Room", "Room", "Room"),
	("Actor", "Actor", "Actor"),
	("Transition Actor", "Transition Actor", "Transition Actor"),
	("Entrance", "Entrance", "Entrance"),
	("Water Box", "Water Box", "Water Box"),
	("Cull Group", "Custom Cull Group", "Cull Group"),
	("LOD", "LOD Group", "LOD Group"),
	("Cutscene", "Cutscene", "Cutscene"),
	# ('Camera Volume', 'Camera Volume', 'Camera Volume'),
]

ootEnumCloudiness = [
	("Custom", "Custom", "Custom"),
	("0x00", "Sunny", "Sunny"),
	("0x01", "Cloudy", "Cloudy"),
]

ootEnumCameraMode = [
	("Custom", "Custom", "Custom"),
	("0x00", "Default", "Default"),
	("0x10", "Two Views, No C-Up", "Two Views, No C-Up"),
	("0x20", "Rotating Background, Bird's Eye C-Up", "Rotating Background, Bird's Eye C-Up"),
	("0x30", "Fixed Background, No C-Up", "Fixed Background, No C-Up"),
	("0x40", "Rotating Background, No C-Up", "Rotating Background, No C-Up"),
	("0x50", "Shooting Gallery", "Shooting Gallery"),
]

ootEnumMapLocation = [
	("Custom", "Custom", "Custom"),
	("0x00", "Hyrule Field", "Hyrule Field"),
	("0x01", "Kakariko Village", "Kakariko Village"),
	("0x02", "Graveyard", "Graveyard"),
	("0x03", "Zora's River", "Zora's River"),
	("0x04", "Kokiri Forest", "Kokiri Forest"),
	("0x05", "Sacred Forest Meadow", "Sacred Forest Meadow"),
	("0x06", "Lake Hylia", "Lake Hylia"),
	("0x07", "Zora's Domain", "Zora's Domain"),
	("0x08", "Zora's Fountain", "Zora's Fountain"),
	("0x09", "Gerudo Valley", "Gerudo Valley"),
	("0x0A", "Lost Woods", "Lost Woods"),
	("0x0B", "Desert Colossus", "Desert Colossus"),
	("0x0C", "Gerudo's Fortress", "Gerudo's Fortress"),
	("0x0D", "Haunted Wasteland", "Haunted Wasteland"),
	("0x0E", "Market", "Market"),
	("0x0F", "Hyrule Castle", "Hyrule Castle"),
	("0x10", "Death Mountain Trail", "Death Mountain Trail"),
	("0x11", "Death Mountain Crater", "Death Mountain Crater"),
	("0x12", "Goron City", "Goron City"),
	("0x13", "Lon Lon Ranch", "Lon Lon Ranch"),
	("0x14", "Dampe's Grave & Windmill", "Dampe's Grave & Windmill"),
	("0x15", "Ganon's Castle", "Ganon's Castle"),
	("0x16", "Grottos & Fairy Fountains", "Grottos & Fairy Fountains"),
]

ootEnumSkybox = [
	("Custom", "Custom", "Custom"),
	("0x00", "None", "None"),
	("0x01", "Standard Sky", "Standard Sky"),
	("0x02", "Hylian Bazaar", "Hylian Bazaar"),
	("0x03", "Brown Cloudy Sky", "Brown Cloudy Sky"),
	("0x04", "Market Ruins", "Market Ruins"),
	("0x05", "Black Cloudy Night", "Black Cloudy Night"),
	("0x07", "Link's House", "Link's House"),
	("0x09", "Market (Main Square, Day)", "Market (Main Square, Day)"),
	("0x0A", "Market (Main Square, Night)", "Market (Main Square, Night)"),
	("0x0B", "Happy Mask Shop", "Happy Mask Shop"),
	("0x0C", "Know-It-All Brothers' House", "Know-It-All Brothers' House"),
	("0x0E", "Kokiri Twins' House", "Kokiri Twins' House"),
	("0x0F", "Stable", "Stable"),
	("0x10", "Stew Lady's House", "Stew Lady's House"),
	("0x11", "Kokiri Shop", "Kokiri Shop"),
	("0x13", "Goron Shop", "Goron Shop"),
	("0x14", "Zora Shop", "Zora Shop"),
	("0x16", "Kakariko Potions Shop", "Kakariko Potions Shop"),
	("0x17", "Hylian Potions Shop", "Hylian Potions Shop"),
	("0x18", "Bomb Shop", "Bomb Shop"),
	("0x1A", "Dog Lady's House", "Dog Lady's House"),
	("0x1B", "Impa's House", "Impa's House"),
	("0x1C", "Gerudo Tent", "Gerudo Tent"),
	("0x1D", "Environment Color", "Environment Color"),
	("0x20", "Mido's House", "Mido's House"),
	("0x21", "Saria's House", "Saria's House"),
	("0x22", "Dog Guy's House", "Dog Guy's House"),
]

ootEnumSkyboxLighting = [
	("Custom", "Custom", "Custom"),
	("false", "Time Of Day", "Time Of Day"),
	("true", "Indoor", "Indoor"),
]

ootEnumAudioSessionPreset = [
	("Custom", "Custom", "Custom"),
	("0x00", "Default", "Default"),
]

ootEnumMusicSeq = [
	("Custom", "Custom", "Custom")
] + readJsonFile('music.json')

ootEnumNightSeq = [
	("Custom", "Custom", "Custom")
] + readJsonFile('night_sounds.json')

ootEnumObjectID = [
	("Custom", "Custom", "Custom")
] + readJsonFile('objects.json')

ootEnumGlobalObject = [obj for obj in ootEnumObjectID if 'keep' in obj[1].lower() and obj[0] != 'OBJECT_GAMEPLAY_KEEP']

ootEnumObjectID = [obj for obj in ootEnumObjectID if obj not in ootEnumGlobalObject]

ootEnumNaviHints = [
	("Custom", "Custom", "Custom"),
	("0x00", "None", "None"),
	("0x01", "Overworld", "elf_message_field"),
	("0x02", "Dungeon", "elf_message_ydan"),
]

ootEnumTransitionAnims = [
	("Custom", "Custom", "Custom")
] + readJsonFile('transitions.json')

# The order of this list matters (normal OoT scene order as defined by ``scene_table.h``)
ootEnumSceneID = [
	("Custom", "Custom", "Custom")
] + readJsonFile('scenes.json') + [
	("SCENE_SPC_RETURN", "Return from Grotto", "Return from Grotto")
]

ootSceneIDToName = {
	"SCENE_YDAN": "ydan",
	"SCENE_DDAN": "ddan",
	"SCENE_BDAN": "bdan",
	"SCENE_BMORI1": "Bmori1",
	"SCENE_HIDAN": "HIDAN",
	"SCENE_MIZUSIN": "MIZUsin",
	"SCENE_JYASINZOU": "jyasinzou",
	"SCENE_HAKADAN": "HAKAdan",
	"SCENE_HAKADANCH": "HAKAdanCH",
	"SCENE_ICE_DOUKUTO": "ice_doukutu",
	"SCENE_GANON": "ganon",
	"SCENE_MEN": "men",
	"SCENE_GERUDOWAY": "gerudoway",
	"SCENE_GANONTIKA": "ganontika",
	"SCENE_GANON_SONOGO": "ganon_sonogo",
	"SCENE_GANONTIKA_SONOGO": "ganontikasonogo",
	"SCENE_TAKARAYA": "takaraya",
	"SCENE_YDAN_BOSS": "ydan_boss",
	"SCENE_DDAN_BOSS": "ddan_boss",
	"SCENE_BDAN_BOSS": "bdan_boss",
	"SCENE_MORIBOSSROOM": "moribossroom",
	"SCENE_FIRE_BS": "FIRE_bs",
	"SCENE_MIZUSIN_BS": "MIZUsin_bs",
	"SCENE_JYASINBOSS": "jyasinboss",
	"SCENE_HAKADAN_BS": "HAKAdan_bs",
	"SCENE_GANON_BOSS": "ganon_boss",
	"SCENE_GANON_FINAL": "ganon_final",
	"SCENE_ENTRA": "entra",
	"SCENE_ENTRA_N": "entra_n",
	"SCENE_ENRUI": "enrui",
	"SCENE_MARKET_ALLEY": "market_alley",
	"SCENE_MARKET_ALLEY_N": "market_alley_n",
	"SCENE_MARKET_DAY": "market_day",
	"SCENE_MARKET_NIGHT": "market_night",
	"SCENE_MARKET_RUINS": "market_ruins",
	"SCENE_SHRINE": "shrine",
	"SCENE_SHRINE_N": "shrine_n",
	"SCENE_SHRINE_R": "shrine_r",
	"SCENE_KOKIRI_HOME": "kokiri_home",
	"SCENE_KOKIRI_HOME3": "kokiri_home3",
	"SCENE_KOKIRI_HOME4": "kokiri_home4",
	"SCENE_KOKIRI_HOME5": "kokiri_home5",
	"SCENE_KAKARIKO": "kakariko",
	"SCENE_KAKARIKO3": "kakariko3",
	"SCENE_SHOP1": "shop1",
	"SCENE_KOKIRI_SHOP": "kokiri_shop",
	"SCENE_GOLON": "golon",
	"SCENE_ZOORA": "zoora",
	"SCENE_DRAG": "drag",
	"SCENE_ALLEY_SHOP": "alley_shop",
	"SCENE_NIGHT_SHOP": "night_shop",
	"SCENE_FACE_SHOP": "face_shop",
	"SCENE_LINK_HOME": "link_home",
	"SCENE_IMPA": "impa",
	"SCENE_MALON_STABLE": "malon_stable",
	"SCENE_LABO": "labo",
	"SCENE_HYLIA_LABO": "hylia_labo",
	"SCENE_TENT": "tent",
	"SCENE_HUT": "hut",
	"SCENE_DAIYOUSEI_IZUMI": "daiyousei_izumi",
	"SCENE_YOUSEI_IZUMI_TATE": "yousei_izumi_tate",
	"SCENE_YOUSEI_IZUMI_YOKO": "yousei_izumi_yoko",
	"SCENE_KAKUSIANA": "kakusiana",
	"SCENE_HAKAANA": "hakaana",
	"SCENE_HAKAANA2": "hakaana2",
	"SCENE_HAKAANA_OUKE": "hakaana_ouke",
	"SCENE_SYATEKIJYOU": "syatekijyou",
	"SCENE_TOKINOMA": "tokinoma",
	"SCENE_KENJYANOMA": "kenjyanoma",
	"SCENE_HAIRAL_NIWA": "hairal_niwa",
	"SCENE_HAIRAL_NIWA_N": "hairal_niwa_n",
	"SCENE_HIRAL_DEMO": "hiral_demo",
	"SCENE_HAKASITARELAY": "hakasitarelay",
	"SCENE_TURIBORI": "turibori",
	"SCENE_NAKANIWA": "nakaniwa",
	"SCENE_BOWLING": "bowling",
	"SCENE_SOUKO": "souko",
	"SCENE_MIHARIGOYA": "miharigoya",
	"SCENE_MAHOUYA": "mahouya",
	"SCENE_GANON_DEMO": "ganon_demo",
	"SCENE_KINSUTA": "kinsuta",
	"SCENE_SPOT00": "spot00",
	"SCENE_SPOT01": "spot01",
	"SCENE_SPOT02": "spot02",
	"SCENE_SPOT03": "spot03",
	"SCENE_SPOT04": "spot04",
	"SCENE_SPOT05": "spot05",
	"SCENE_SPOT06": "spot06",
	"SCENE_SPOT07": "spot07",
	"SCENE_SPOT08": "spot08",
	"SCENE_SPOT09": "spot09",
	"SCENE_SPOT10": "spot10",
	"SCENE_SPOT11": "spot11",
	"SCENE_SPOT12": "spot12",
	"SCENE_SPOT13": "spot13",
	"SCENE_SPOT15": "spot15",
	"SCENE_SPOT16": "spot16",
	"SCENE_SPOT17": "spot17",
	"SCENE_SPOT18": "spot18",
	"SCENE_SPOT20": "spot20",
	"SCENE_GANON_TOU": "ganon_tou",
	"SCENE_TEST01": "test01",
	"SCENE_BESITU": "besitu",
	"SCENE_DEPTH_TEST": "depth_test",
	"SCENE_SYOTES": "syotes",
	"SCENE_SYOTES2": "syotes2",
	"SCENE_SUTARU": "sutaru",
	"SCENE_HAIRAL_NIWA2": "hairal_niwa2",
	"SCENE_SASATEST": "sasatest",
	"SCENE_TESTROOM": "testroom",
}

ootEnumCamTransition = [
	("Custom", "Custom", "Custom"),
	("0x00", "0x00", "0x00"),
	# ("0x0F", "0x0F", "0x0F"),
	# ("0xFF", "0xFF", "0xFF"),
]

# see curRoom.unk_03
ootEnumRoomBehaviour = [
	("Custom", "Custom", "Custom"),
	("0x00", "Default", "Default"),
	("0x01", "Dungeon Behavior (Z-Target, Sun's Song)", "Dungeon Behavior (Z-Target, Sun's Song)"),
	("0x02", "Disable Backflips/Sidehops", "Disable Backflips/Sidehops"),
	("0x03", "Disable Color Dither", "Disable Color Dither"),
	("0x04", "(?) Horse Camera Related", "(?) Horse Camera Related"),
	("0x05", "Disable Darker Screen Effect (NL/Spins)", "Disable Darker Screen Effect (NL/Spins)"),
]

ootEnumExitIndex = [
	("Custom", "Custom", "Custom"),
	("Default", "Default", "Default"),
]

ootEnumSceneSetupPreset = [
	("Custom", "Custom", "Custom"),
	("All Scene Setups", "All Scene Setups", "All Scene Setups"),
	("All Non-Cutscene Scene Setups", "All Non-Cutscene Scene Setups", "All Non-Cutscene Scene Setups"),
]

ootEnumCSWriteType = [
	("Custom", "Custom", "Provide the name of a cutscene header variable"),
	("Embedded", "Embedded", "Cutscene data is within scene header (deprecated)"),
	("Object", "Object", "Reference to Blender object representing cutscene"),
]

ootEnumCSListType = [
	("Textbox", "Textbox", "Textbox"),
	("FX", "Scene Trans FX", "Scene Trans FX"),
	("Lighting", "Lighting", "Lighting"),
	("Time", "Time", "Time"),
	("PlayBGM", "Play BGM", "Play BGM"),
	("StopBGM", "Stop BGM", "Stop BGM"),
	("FadeBGM", "Fade BGM", "Fade BGM"),
	("Misc", "Misc", "Misc"),
	("0x09", "Cmd 09", "Cmd 09"),
	("Unk", "Unknown Data", "Unknown Data"),
]

ootEnumCSListTypeIcons = [
	"ALIGN_BOTTOM",
	"COLORSET_10_VEC",
	"LIGHT_SUN",
	"TIME",
	"PLAY",
	"SNAP_FACE",
	"IPO_EASE_IN_OUT",
	"OPTIONS",
	"EVENT_F9",
	"QUESTION",
]

ootEnumCSListTypeListC = {
	"Textbox": "CS_TEXT_LIST",
	"FX": "CS_SCENE_TRANS_FX",
	"Lighting": "CS_LIGHTING_LIST",
	"Time": "CS_TIME_LIST",
	"PlayBGM": "CS_PLAY_BGM_LIST",
	"StopBGM": "CS_STOP_BGM_LIST",
	"FadeBGM": "CS_FADE_BGM_LIST",
	"Misc": "CS_MISC_LIST",
	"0x09": "CS_CMD_09_LIST",
	"Unk": "CS_UNK_DATA_LIST",
}

ootEnumCSListTypeEntryC = {
	"Textbox": None,  # special case
	"FX": None,  # no list entries
	"Lighting": "CS_LIGHTING",
	"Time": "CS_TIME",
	"PlayBGM": "CS_PLAY_BGM",
	"StopBGM": "CS_STOP_BGM",
	"FadeBGM": "CS_FADE_BGM",
	"Misc": "CS_MISC",
	"0x09": "CS_CMD_09",
	"Unk": "CS_UNK_DATA",
}

ootEnumCSTextboxType = [("Text", "Text", "Text"), ("None", "None", "None"), ("LearnSong", "Learn Song", "Learn Song")]

ootEnumCSTextboxTypeIcons = ["FILE_TEXT", "HIDE_ON", "FILE_SOUND"]

ootEnumCSTextboxTypeEntryC = {
	"Text": "CS_TEXT_DISPLAY_TEXTBOX",
	"None": "CS_TEXT_NONE",
	"LearnSong": "CS_TEXT_LEARN_SONG",
}

ootEnumCSTransitionType = [
	("1", "To White +", "Also plays whiteout sound for certain scenes/entrances"),
	("2", "To Blue", "To Blue"),
	("3", "From Red", "From Red"),
	("4", "From Green", "From Green"),
	("5", "From White", "From White"),
	("6", "From Blue", "From Blue"),
	("7", "To Red", "To Red"),
	("8", "To Green", "To Green"),
	("9", "Set Unk", "gSaveContext.unk_1410 = 1, works with scene xn 11/17"),
	("10", "From Black", "From Black"),
	("11", "To Black", "To Black"),
	("12", "To Dim Unk", "Fade gSaveContext.unk_1410 255>100, works with scene xn 11/17"),
	("13", "From Dim", "Alpha 100>255"),
]

ootEnumDrawConfig = readJsonFile('draw_configs.json')
