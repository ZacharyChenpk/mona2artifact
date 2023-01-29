import json
import re
from mona2artifact_const import *

inputting = '../artifacts_mona.json'
outputting = '../artifacts_gene.json'

with open(inputting, 'r', encoding='utf-8') as f:
    mona = json.loads(f.read())

# print(mona)

def getval(tag):
    if tag["value"] < 1:
        return round(tag["value"] * 100, 2)
    return int(tag["value"])

objs = []
regex = re.compile("([a-z])([A-Z])")

for part in parts:
    for obj in mona[part]:
        if obj["star"] > 4 and obj["level"] > 15:
            new_obj = {
                "asKey": artifact_map[obj["setName"]] if obj["setName"] in artifact_map else regex.sub(r"\1_\2",obj["setName"]).lower(),
                "rarity": obj["star"],
                "slot": part2slot[part],
                "level": obj["level"],
                "mainStat": tagmap[obj["mainTag"]["name"]],
                "subStat1Type": tagmap[obj["normalTags"][0]["name"]],
                "subStat1Value": getval(obj["normalTags"][0]),
                "subStat2Type": tagmap[obj["normalTags"][1]["name"]],
                "subStat2Value": getval(obj["normalTags"][1]),
                "subStat3Type": tagmap[obj["normalTags"][2]["name"]],
                "subStat3Value": getval(obj["normalTags"][2]),
                "subStat4Type": 'critRate',
                "subStat4Value": 0.0
            }
            if len(obj["normalTags"]) > 3:
                new_obj["subStat4Type"] = tagmap[obj["normalTags"][3]["name"]]
                new_obj["subStat4Value"] = getval(obj["normalTags"][3])
            objs.append(new_obj)

with open(outputting, 'w') as f:
    f.write(json.dumps(objs))