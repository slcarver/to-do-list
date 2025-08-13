import json



def open_file():
    try:
        with open ("to-do.json", "a") as file:
           existing_data = json.load(file)
           print(existing_data)

    # except FileNotFoundError:
    #     return type(dict(existing_data))
        
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from the file. Check if it's valid JSON.")
        


