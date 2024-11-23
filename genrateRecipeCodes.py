from collections import OrderedDict
import json
import get_ingredients


with open('api_codes/json_files/recipes.json', 'r', encoding='UTF-8') as json_read :
    all_recipes = json.load(json_read, object_pairs_hook=OrderedDict)

allRecipesList =[]
cnt = 0
for recipe in all_recipes:
    tempDict = {}
    tempList = []
    code = str(recipe["code"])

    for i in recipe["ingredients"]:
        ingDict = {}
        c = get_ingredients.getCode(i["name"])
        ingDict["name"] = i["name"]
        ingDict["code"] = c
        ingDict["amount"] = i["amount"]
        ingDict["unit"] = i["unit"]
        code = code + c[:2]
        tempList.append(ingDict)

    tempDict["english_name"] = recipe["english_name"]
    tempDict["korean_name"] = recipe["korean_name"]
    tempDict["code"] = code
    tempDict["base"] = recipe["base"]
    tempDict["ingredients"] = tempList
    tempDict["instructions"] = recipe["instructions"]

    allRecipesList.append(tempDict)

with open('api_codes/json_files/allRecipes.json', 'w', encoding='utf-8') as f:
    json.dump(allRecipesList, f, ensure_ascii = False, indent=4)


print('\nfile successfully created!\n')