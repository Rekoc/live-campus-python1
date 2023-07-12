import yaml
import os
import pathlib


# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
json_path = os.path.join(root_file, "yaml_files", "random.yml")
with open(json_path, "r") as json_file:
    content = yaml.load(json_file)
print(content)

# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
json_path = os.path.join(root_file, "yaml_files", "test.yml")

my_data = {"key1": 1, "key2": 2, "key3": 3}
with open(json_path, "w") as json_file:
    content = yaml.dump(my_data, json_file)