# # class called Greeter
# class Greeter:
#     # method say_hello
#     def say_hello(self, name):
#         print(f"Hello, {name}!")

# # Creating an instance of the Greeter class
# greeter = Greeter()
# # Calling the say_hello method
# greeter.say_hello("Savija") # Output: Hello!

#_______________________________________________________________
# class Cal:
#     def add(self, a, b):
#         c=6
#         return a+b

# cal = Cal()
# result = cal.add(5, 3)
# print(result)

#_______________________________________________________________
# global_var = "I am global"
# class Cal:
#     def add(self, a, b):
#         c=global_var
#         print(c)
#         return a+b

# cal = Cal()
# result = cal.add(5, 3)
# print(result)
# print(c)

#_______________________________________________________________
counter = 0
class Counter:
    def increment(self):
        global counter
        counter +=1

c = Counter()
c.increment()
print(counter)