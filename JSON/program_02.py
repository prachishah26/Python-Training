# Write a code to load a .json file and print JSON data. Display error if a file is empty or data is not in a json format


# ----------------code is not completed yet



import json

details = {"name":"John","age":31,"Salary":25000}
json_converted = json.dumps(details)
print(type(json_converted))

with open("Sample.json", "w") as s:
	json.dump(json_converted, s)

with open("Sample.json", "r") as read:
	data = json.load(read)

# type(data)
if len(data) != 0:
    print(data)
else:
    print("Please enter a valid data")