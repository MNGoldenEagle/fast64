import os
from .data import OoT_Data


addon_path = os.path.dirname(os.path.realpath(os.path.join(__file__, '..', '..')))


ootData = OoT_Data()

ootEnumRoomShapeType = ootData.enumData.ootEnumRoomShapeType

ootEnumHeaderMenu = [
	("Child Night", "Child Night", "Child Night"),
	("Adult Day", "Adult Day", "Adult Day"),
	("Adult Night", "Adult Night", "Adult Night"),
	("Cutscene", "Cutscene", "Cutscene"),
]
ootEnumHeaderMenuComplete = [
    ("Child Day", "Child Day", "Child Day"),
] + ootEnumHeaderMenu

ootEnumLinkIdle = ootData.enumData.ootEnumLinkIdle

ootEnumCloudiness = [
	("Custom", "Custom", "Custom"),
	("0x00", "Sunny", "Sunny"),
	("0x01", "Cloudy", "Cloudy"),
]

ootEnumCameraMode = ootData.enumData.ootEnumCameraMode
ootEnumMapLocation = ootData.enumData.ootEnumMapLocation
ootEnumSkybox = ootData.enumData.ootEnumSkybox
ootEnumSkyboxLighting = ootData.enumData.ootEnumLightModes
ootEnumAudioSessionPreset = ootData.enumData.ootAudioPresets
ootEnumMusicSeq = ootData.enumData.ootEnumSeqId
ootEnumNightSeq = ootData.enumData.ootEnumNightSeq
ootEnumNaviHints = ootData.enumData.ootEnumNaviQuestHintType
ootEnumSceneID = ootData.enumData.ootEnumSceneID
ootEnumRoomBehaviour = ootData.enumData.ootEnumRoomBehavior
ootEnumDrawConfig = ootData.enumData.ootEnumDrawConfig

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
ootSceneNameToID = {val: key for key, val in ootSceneIDToName.items()}

ootEnumCamTransition = [
	("Custom", "Custom", "Custom"),
	("0x00", "0x00", "0x00"),
	# ("0x0F", "0x0F", "0x0F"),
	# ("0xFF", "0xFF", "0xFF"),
]


ootSceneNameToID = {val: key for key, val in ootSceneIDToName.items()}
