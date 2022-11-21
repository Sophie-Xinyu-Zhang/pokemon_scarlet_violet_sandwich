from power_class import Power
from type_power_class import TypePower
import helper as h

SEPARATOR = "==========================================="

MENU_ITEMS = {
    "1": "Look up a power of a specific ingredient",
    "2": "Add up multiple ingredients and show the summary"
}

def main():

    raw_ing_list = h.get_all_ing_raw_list()
    all_ing = h.all_ing_obj_dic(raw_ing_list)

    # wait for user input and print out the power of the ingredient
    while True:
        print(SEPARATOR)
        print("Select from the menu below. Enter quit or q at anytime to quit.")
        # let the user select from the menu
        for key, value in MENU_ITEMS.items():
            print(f"{key}: {value}")
        print(SEPARATOR)

        if (user_input := input("Enter your choice: ")) == "1":
            while True:
                print(SEPARATOR)
                print("Select an ingredient to see its power. Enter back or b to go back to the main menu.")
                print(SEPARATOR)
                # print the list of ingredients with their id
                for key in all_ing.keys():
                    print(f"{key}: {all_ing[key]['name']}")

                # get user input
                print(SEPARATOR)
                user_input = input("Enter the id of the ingredient you want to know the power of: ")
                if user_input == "quit" or user_input == "q":
                    return
                elif user_input == "back" or user_input == "b":
                    break
                try:
                    user_input = int(user_input)
                    print(all_ing[user_input]['Power'])
                    print(SEPARATOR)
                    print(all_ing[user_input]['TypePower'])
                except:
                    print("Invalid input")

        elif user_input == "2":
            print(SEPARATOR)
            print("Enter the id of the ingredients you want to add up. Enter done or d when you are done.")
            print(SEPARATOR)
            # add the ingredients into a list
            ing_list = []
            while True:
                # print the list of ingredients with their id
                for key in all_ing.keys():
                    print(f"{key}: {all_ing[key]['name']}")

                # get user input
                print(SEPARATOR)
                print(f"Current list: {[ing['name'] for ing in ing_list]}")
                print(SEPARATOR)
                user_input = input("Enter the id of the ingredient you want to add up, or enter done/d to calculate: ")
                if user_input == "quit" or user_input == "q":
                    return
                
                elif user_input == "back" or user_input == "b":
                    break

                elif user_input == "done" or user_input == "d":
                    res = {}
                    # creat a dummy Power and TypePower object
                    dummy_power_obj = Power("DUMMY", {})
                    dummy_type_power_obj = TypePower("DUMMY", {})
                    for ing in ing_list:
                        dummy_power_obj += ing['Power']
                        dummy_type_power_obj += ing['TypePower']
                    
                    res['Ingredients added'] = [ing['name'] for ing in ing_list]
                    res['Power'] = dummy_power_obj
                    res['TypePower'] = dummy_type_power_obj

                    h.print_res(res, SEPARATOR)
                    ing_list = []
                    continue

                try:
                    user_input = int(user_input)
                    ing_list.append(all_ing[user_input])
                    print(f"Added {all_ing[user_input]['name']} to the list.")
                    
                except:
                    print("Invalid input")
        elif user_input == "quit" or user_input == "q":
            print("BYEEEEEEEEEEEEEEEEEEEEEEE")
            return

    
    

if __name__ == '__main__':
    main()