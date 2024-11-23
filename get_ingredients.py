from collections import OrderedDict
import json

with open('./json_files/allIngredients.json', 'r', encoding='UTF-8') as json_read :
    all_ingredients = json.load(json_read, object_pairs_hook=OrderedDict)


def getAllIngredients():
    return all_ingredients

def getCode(name):
    result = "None"
    for i in all_ingredients:
        if name == i["name"]:
            result = i["code"]
    return result