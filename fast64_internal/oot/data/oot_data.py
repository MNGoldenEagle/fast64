from dataclasses import dataclass
import os, json

addon_path = os.path.dirname(os.path.realpath(os.path.join(__file__, '..', '..', '..')))

def readJsonFile(filename):
	with open(os.path.join(addon_path, filename)) as file:
		result = json.load(file)
	
	result = [tuple(arr) for arr in result]
	return result

@dataclass
class OoT_BaseElement:
    id: str
    key: str
    name: str
    index: int


@dataclass
class OoT_Data:
    """Contains data related to OoT, like actors or objects"""

    def __init__(self):
        from .oot_enum_data import OoT_EnumData
        from .oot_object_data import OoT_ObjectData
        from .oot_actor_data import OoT_ActorData

        self.enumData = OoT_EnumData()
        self.objectData = OoT_ObjectData()
        self.actorData = OoT_ActorData()
