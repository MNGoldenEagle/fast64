import re
from ..utility import *

def createEnum(enumName, enumList):
	enumData = enumName + ' = [\n'
	for item in enumList:
		enumData += item.toC()
	enumData += ']'
	return enumData

def parseEnumFile(data, enumName, enumPrefix, ignoreList, includeCustom):
	if includeCustom:
		enumList = [("Custom", "Custom", "Custom", -1)]
	else:
		enumList = []

	checkResult = re.search('typedef enum \{([^\}]*)\} ' + enumName, data, re.DOTALL)
	if checkResult is None:
		raise ValueError("Cannot find enum by name: " + str(enumName))
	enumData = checkResult.group(1)

	i = 0
	for matchResult in re.finditer(rf'{enumPrefix}\_(\S*)[ \t]*=?[ \t]*(\d*),[ \t]*/?/?[ \t]*([^\n]*)', enumData, flags = re.UNICODE):
		if matchResult.group(2):
			i = int(matchResult.group(2))
		oldName = matchResult.group(1)
		if oldName[:5] == "UNSET" or oldName in ignoreList:
			continue
		spacedName = oldName.replace("_", " ")
		words = spacedName.split(" ")
		capitalizedWords = [word.capitalize() for word in words]
		newName = " ".join(capitalizedWords)
		desc = newName
		if matchResult.group(3):
			desc = matchResult.group(3).replace("//", "").strip()
		enumList.append((f"{enumPrefix}_{oldName}", newName, desc, i))
		i = i + 1

	return enumList

def parseObjectID():
	data = readFile("z64object.h")
	enumList = parseEnumFile(data, "ObjectID", "OBJECT", [
		'GAMEPLAY_KEEP',
		'GAMEPLAY_DANGEON_KEEP',
		'GAMEPLAY_FIELD_KEEP',
		'LINK_BOY',
		'LINK_CHILD',
	], True)
	pythonEnum = createEnum('ootEnumObjectID', enumList)
	writeFile("oot_obj_enum.py", pythonEnum)

def parseSceneID():
	data = readFile("z64scene.h")
	enumList = parseEnumFile(data, "SceneID", "SCENE", [], True)
	pythonEnum = createEnum('ootEnumSceneID', enumList)
	writeFile("oot_scene_enum.py", pythonEnum)
