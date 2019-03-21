## Caibidil 9
# print
print('\n\n###\n\nCaibidil :\n\n')
print('Classes...')

class Dog(): 
    # a container to store data (=attributes) and actions (=methods)
    # attributes and methods
    def __init__(self, name, age):
        # initialises name and age attributes
        self.name = name
        self.age = age
    
    def sit(self): 
        # action or method
        return self.name + " is now sitting"

    def roll_over(self):
        # another method
        # let's say the dog can roll
        return self.name + " rolled over"
            


# call the action from the class
# the class is like a template
# an object is needed to me made or instantiated

my_dog = Dog('Tory', 8)  # this is the instance and is the object 
# needed the values name (Tory) and age(8)
# values can be anything... can have any name or any age 
# 
# Let's see if can get the dog to sit
# Instead of using the class name use the instant of the class which my_dog
# 
# sit
print(my_dog.sit())

# now roll over
print(my_dog.roll_over())


print('\n\nScroll to top to view all outputs!')