import json
import re

# Load the JSON data
with open("getInstance.json", "r") as file:
    data = json.load(file)

# Define a function to sort AWS instance names
def instance_sorter(item):
    instance_id = item["instance_id"]
    match = re.match(r"([a-z]+)([0-9]+)(\.[a-z]+)?", instance_id)
    if match:
        instance_prefix = match.group(1)
        instance_num = int(match.group(2))
        instance_suffix = match.group(3) if match.group(3) else ""
        return (instance_prefix, instance_num, instance_suffix)
    else:
        return instance_id

# Sort the data by instance_id
data.sort(key=instance_sorter)

# Convert sorted data to list of strings
instance_list = [item["instance_id"] for item in data]

# Write each instance_id to the file
with open("instances_list.ts", "w") as file:
    for instance_id in instance_list:
        file.write(f'|" {instance_id}"\n')
