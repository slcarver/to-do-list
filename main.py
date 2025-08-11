import json
from logic import *
from file_handling import *


#global variables
task_to_do_list = []

print("This is a to do list to manage your work related tasks ")
task = input(str("Please type in a task that needs to be completed: \n"))

task_to_do_list.append(task)
task_priority = prio_logic()
json_dict_updater(existing_data, task_to_do_list)

existing_data[task_priority] = task_to_do_list




    