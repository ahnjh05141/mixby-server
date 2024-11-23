from collections import OrderedDict
import json

with open('./json_files/allProducts.json', 'r', encoding='UTF-8') as json_read :
    all_drinks = json.load(json_read, object_pairs_hook=OrderedDict)

def getalldrinks():
    return all_drinks

def search_byname(keyword):
    temp_list = []
    for j in all_drinks:
        if keyword in j["name"] and j not in temp_list: temp_list.append(j)
    temp_list.insert(0, "Total result found : {}".format(len(temp_list)))
    return temp_list

def search_bytype(keyword):
    temp_list = []
    for j in all_drinks:
        if keyword in j["type"] and j not in temp_list: temp_list.append(j)
    temp_list.insert(0, "Total result found : {}".format(len(temp_list)))
    return temp_list

def search_bycode(keyword):
    temp_list = []
    for j in all_drinks:
        if keyword == j["code"] and j not in temp_list: temp_list.append(j)
    temp_list.insert(0, "Total result found : {}".format(len(temp_list)))
    return temp_list
