import json
import time

time_format = "%Y-%m-%d %H:%M:%S"

def add_data(my_fridge):
    file_json = json.dumps(my_fridge)
    with open ("data/my_fridge.json", "w") as f:
        f.write(file_json)

def read_data():
    with open ("data/my_fridge.json", "r") as json_f:
        my_fridge = json.load(json_f)
        index = 1
        for item in my_fridge.items():
            print(str(index) + ". " + str(item))
            index += 1
        return my_fridge