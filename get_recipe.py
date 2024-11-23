from collections import OrderedDict
import json

with open('./json_files/allRecipes.json', 'r', encoding='UTF-8') as json_read :
    all_recipes = json.load(json_read, object_pairs_hook=OrderedDict)


def getallrecipes():
    return all_recipes

def search_byname(name):
    temp_list = []
    for j in all_recipes:
        if name in j["name"] and j not in temp_list: temp_list.append(j)
    temp_list.insert(0, "Total result found : {}".format(len(temp_list)))
    return temp_list

def search_bycode(code):
    temp_list = []
    for j in all_recipes:
        if code == j["code"] and j not in temp_list: temp_list.append(j)
    temp_list.insert(0, "Total result found : {}".format(len(temp_list)))
    return temp_list

def search_byings(codes):
    code_list = list(map(''.join, zip(*[iter(codes)]*2)))
    temp_list = []
    for input_code in code_list:
        for j in all_recipes:
            recipe_code = j["code"][2:]
            if input_code in recipe_code:
                cnt = 0
                for c in code_list:
                    if c in recipe_code: cnt+=1
                j["have"] = "{}/{}".format(cnt, int(len(j["code"])/2))
                temp_list.append(j)
    
    return temp_list