from os import path
from dataclasses import dataclass
from .oot_getters import getXMLRoot
from .oot_data import OoT_BaseElement


@dataclass
class OoT_ActorElement(OoT_BaseElement):
    category: str
    tiedObjects: list[str]


class OoT_ActorData:
    """Everything related to OoT Actors"""

    def __init__(self):
        # Path to the ``ActorList.xml`` file
        actorXML = path.dirname(path.abspath(__file__)) + "/xml/actors.xml"
        actorRoot = getXMLRoot(actorXML)

        # general actor list
        self.actorList: list[OoT_ActorElement] = []

        for actor in actorRoot.iterfind("Actor"):
            tiedObjects = []
            objKey = actor.get("ObjectKey")
            actorName = f"{actor.attrib['Name']} - {actor.attrib['ID'].removeprefix('ACTOR_')}"
            if objKey is not None:  # actors don't always use an object
                tiedObjects = objKey.split(",")
            self.actorList.append(
                OoT_ActorElement(
                    actor.attrib["ID"],
                    actor.attrib["Key"],
                    actorName,
                    int(actor.attrib["Index"]),
                    actor.attrib["Category"],
                    tiedObjects,
                )
            )

        self.actorsByKey = {actor.key: actor for actor in self.actorList}
        self.actorsByID = {actor.id: actor for actor in self.actorList}

        ootEnumTransitionActorID = [actor for actor in self.actorList if actor.id.startswith('ACTOR_DOOR')]

        self.transitionActors = ootEnumTransitionActorID

        # list of tuples used by Blender's enum properties
        self.ootEnumActorID = []
        self.ootEnumActorID.insert(0, ("Custom", "Custom Actor", "Custom"))
        for actor in self.actorList:
            self.ootEnumActorID.append((actor.id, actor.name, actor.id))
