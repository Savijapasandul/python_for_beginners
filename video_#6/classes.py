# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         return f"{self.name} says woof!"

# my_dog = Dog("Buddy", 3)
# print(my_dog.bark()) # output: Buddy says woof!

#_____________________________________________________________________
# class Car:
#     wheels = 4 # Class varaible
#     def __init__(self, brand, model):
#         self.brand = brand # instance variables
#         self.model = model # instance variables

#_____________________________________________________________________
class Cla:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b

cal = Cla()
print(cal.add(7, 3)) # 10
print(cal.sub(10, 20)) # -10

