import json
import os
import pathlib


# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
json_path = os.path.join(root_file, "json_files", "random.json")
with open(json_path, "r") as json_file:
    content = json.load(json_file)
print(content)


# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
json_path = os.path.join(root_file, "json_files", "test.json")

my_data = {"key1": 1, "key2": 2, "key3": 3}
with open(json_path, "w") as json_file:
    content = json.dump(my_data, json_file)

