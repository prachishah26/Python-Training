# Create class Vehicle with properties name, engine, and price. Create vehicle object and convert it into JSON and vice-versa.
import json
class Vehicle:
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle_obj = Vehicle("prachi","engine","price") 
# print(vehicle_obj.name)

json_converted = json.dumps(vehicle_obj.__dict__)
print(json_converted)