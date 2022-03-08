# Write a code to load a .json file and print JSON data. Display error if a file is empty or data is not in a json format


import json
class ErrorInJson(Exception):
    pass

data = {}
details = {"name":"John","age":31,"Salary":25000}
json_converted = json.dumps(details)

with open("Sample.json", "w") as s:
	json.dump(json_converted, s)

try:
    with open("Sample.json", "r") as read:
	    print(json.load(read))     
except:
    print("Error : Json is empty or it is not in json format")
    raise ErrorInJson