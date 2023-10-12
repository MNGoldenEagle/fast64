from dataclasses import dataclass
from os import path
from ...utility import PluginError
from .oot_getters import getXMLRoot
from .oot_data import OoT_BaseElement

# Note: "object" in this context refers to an OoT Object file (like ``gameplay_keep``)

@dataclass
class OoT_ObjectElement(OoT_BaseElement):
    pass

deletedEntry = ("None", "(Deleted from the XML)", "None")

class OoT_ObjectData:
    """Everything related to OoT objects"""

    def __init__(self):
        # general object list
        self.objectList: list[OoT_ObjectElement] = []

        # Path to the ``ObjectList.xml`` file
        objectXML = path.dirname(path.abspath(__file__)) + "/../../../objects.xml"
        objectRoot = getXMLRoot(objectXML)

        for obj in objectRoot.iterfind("Object"):
            objName = f"{obj.attrib['Name'].title()} - {obj.attrib['ID'].removeprefix('OBJECT_')}"
            self.objectList.append(
                OoT_ObjectElement(obj.attrib["ID"], obj.attrib["Key"], objName, int(obj.attrib["Index"]))
            )

        ootEnumGlobalObject = [obj for obj in self.objectList if 'keep' in obj.id.lower() and obj.id != 'OBJECT_GAMEPLAY_KEEP']
        self.objectList = [obj for obj in self.objectList if not obj.id.lower().endswith('keep')]

        self.objectsByID = {obj.id: obj for obj in self.objectList}
        self.objectsByKey = {obj.key: obj for obj in self.objectList}

        # list of tuples used by Blender's enum properties
        self.ootEnumObjectKey = self.getObjectIDList(self.objectList, False)

        self.globalObjects = ootEnumGlobalObject
        self.globalObjectsKey = self.getObjectIDList(self.globalObjects, False)

        # create the legacy object list for old blends
        self.ootEnumObjectIDLegacy = self.getObjectIDList(self.objectList, True)

        # validate the legacy list, if there's any None element then something's wrong
        if deletedEntry in self.ootEnumObjectIDLegacy:
            raise PluginError("ERROR: Legacy Object List doesn't match!")

    def getObjectIDList(self, list: list, isLegacy: bool):
        """Generates and returns the object list in the right order"""
        objList = []
        objList.append(("Custom", "Custom Object", "Custom"))
        for obj in list:
            identifier = obj.id if isLegacy else obj.key
            objList.append((identifier, obj.name, obj.id))
        return objList
