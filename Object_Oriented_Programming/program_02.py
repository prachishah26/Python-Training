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
        return f"I am Wild. {Animal.get_info(self)}" 

class Leopard(Wild):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Leopard. {Wild.get_info(self)}" 

class Tiger(Wild):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return "I am Tiger. {Wild.get_info(self)}"

class Pet(Animal):
    def get_name(self):
        # self.name = name
        return "My name is " + self.name
    def get_info(self):
        return f"I am Pet. {Animal.get_info(self)}"

class Dog(Pet):
    def get_name(self):
        # self.name = name
        return "My name is " + self.name
    def get_info(self):
        return f"I am Dog. {Pet.get_info(self)}" 

class Canine(Animal):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Canine. {Animal.get_info(self)}" 

class Fox(Canine):
    def get_name(self):
        return "My name is " + self.name
    def get_info(self):
        return f"I am Fox. {Canine.get_info(self)}" 


dog = Dog("n")
print(dog.get_name())


dog = Leopard("xyz")
print(dog.get_name())
print(dog.get_info())






























#         class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def speak(self):
#         print("I am", self.name, "and I am", self.age, "years old")


# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.type = "dog"

# tim = Dog("Tim", 5)
# tim.speak() # This will print "I am Tim and I am 5 years old" 
