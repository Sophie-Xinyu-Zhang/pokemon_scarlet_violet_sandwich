import csv
from power_class import Power
from type_power_class import TypePower

def data_clean(power_raw_string):
    # replace \n with colon
    power_raw_string = power_raw_string.replace('\n', ':')
    power_list = power_raw_string.split(':')

    # convert into dictionary
    power_dict = {}
    for i in range(0, len(power_list), 2):
        power_dict[power_list[i]] = int(power_list[i+1])
    
    return power_dict


def process_file(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            ing_dict = {}
            ing_dict['name'] = row[0]
            ing_dict['power_raw_string'] = row[2]
            ing_dict['type_raw_string'] = row[3]
            yield ing_dict
            
def get_all_ing_raw_list():
    ing_list = []
    for ing in process_file("ingredients.csv"):
        ing_list.append(ing)

    seasoning_list = []
    for seasoning in process_file("seasonings.csv"):
        seasoning_list.append(seasoning)
    
    # combine the two lists
    ing_list.extend(seasoning_list)

    # sort the list by name in alphabetical order
    ing_list.sort(key=lambda x: x['name'])

    return ing_list

def all_ing_obj_dic(raw_ing_list):
    all_ing = {}

    for idx, ing in enumerate(raw_ing_list):
        all_ing[idx + 1] = {
            "name": ing['name'], 
            "Power": Power(ing['name'], data_clean(ing['power_raw_string'])),
            "TypePower": TypePower(ing['name'], data_clean(ing['type_raw_string']))
        }
    return all_ing

def print_res(res, SEPARATOR):
    print(SEPARATOR)
    print("Result of these ingredients:")
    print(SEPARATOR)
    print(res['Ingredients added'])
    print(SEPARATOR)
    print("POWER")
    print(SEPARATOR)
    print(res['Power'])
    print(SEPARATOR)
    print("TYPE POWER")
    print(SEPARATOR)
    print(res['TypePower'])
    print(SEPARATOR)