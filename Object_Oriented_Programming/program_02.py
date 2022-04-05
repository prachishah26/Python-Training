# 2. Create classes according to the following class map:
# ->  Animal => Wild => Leopard, Tiger
# 	=> Pet => Dog
# 	=> Canine => Fox
# -> Each class contains two methods to get dog name and info. Get the name returns the name of that animal and get the info returns hierarchy.
# For example,
# print(dog.get_name())  ⇒ My name is Tommy
# print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal


class Animal():
    def __init__(self,name):
        self.name = name
    def get_name(self):
        # self.name = name
        return "My name is " + self.name
    def get_info(self):
        return "I am Animal" 

class Wild(Animal):
    def get_name(self):
        return "My name is "+ self.name 
    def get_info(self):
        return f"I am Wild. {super().get_info()}" 

class Leopard(Wild):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Leopard. {super().get_info()}" 

class Tiger(Wild):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Tiger. {super().get_info()}"

class Pet(Animal):
    def get_name(self):
        # self.name = name
        return "My name is " + self.name
    def get_info(self):
        return f"I am Pet. {super().get_info()}"

class Dog(Pet):
    def get_name(self):
        # self.name = name
        return "My name is " + self.name
    def get_info(self):
        return f"I am Dog. {super().get_info()}" 

class Canine(Animal):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Canine. {super().get_info()}" 

class Fox(Canine):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Fox. {super().get_info()}" 


dog = Dog("n")
print(dog.get_name())


dog = Leopard("xyz")
print(dog.get_name())
print(dog.get_info())



























