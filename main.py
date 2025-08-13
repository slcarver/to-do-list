import json
import os
import pprint
from collections import defaultdict
from logic import *




if not os.path.exists("to-do-list.json") or os.path.getsize("to-do-list.json") == 0:
    data = []
else: 
    with open("to-do-list.json", "r") as file:
        data = json.load(file)
        if isinstance(data, dict):
            data = [data]

print(data)
print("This is a to do list to manage your work related tasks ")
task = str(input("Please type in a task that needs to be completed: \n"))
priority = prio_logic()

print(f"task: {task}")
#logic to read key and update json data
for item in data:
    if priority in item:
        item[priority].append(task)
        break

else:
    data.append({priority: [task]})
   
print(data)   

with open ("to-do-list.json", "w") as file:
    json.dump(data, file, indent = 4)