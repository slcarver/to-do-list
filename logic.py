import json


#Prio Logic to make a selection of 1-4
def prio_logic():  
    while True:
        task_priority = input(str("Please type in a priority. (1 - 4 with 1 being the highest\n"))
        if task_priority == "1":
            return f"1 - Critical"
        elif task_priority == "2":
            return f"2 - High"
        elif task_priority == "3":
            return f"3 - Moderate"
        elif task_priority == "4":
            return f"4 - Low"
        else:
            print("That is not a valid priority...please try again")


#soon to be dictionary logic to append json dict
def json_dict_updater(existing_data, task_to_do_list):
    for key, values in existing_data.items():
        print(key)
        print(values)