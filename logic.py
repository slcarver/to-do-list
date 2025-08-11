import json


#Prio Logic to make a selection of 1-4
def prio_logic():  
    while True:
        task_priority = input(str("Please type in a priority. (1 - 4 with 1 being the highest\n"))
        if task_priority == "1":
            task_priority = "1 - Critical"
            return task_priority
        elif task_priority == "2":
            task_priority = "2 - High"
            return task_priority
        elif task_priority == "3":
            task_priority = "3 - Moderate"
            return task_priority
        elif task_priority == "4":
            task_priority = "4 - Low"
            return task_priority
        else:
            print("That is not a valid priority...please try again")


#soon to be dictionary logic to append json dict
def json_dict_updater(existing_data, task_to_do_list):
    print(f"task_to_do_list from function: {task_to_do_list}")
    print(type(task_to_do_list))
    print(f"existing_data from function: {existing_data}")
    print(type(existing_data))