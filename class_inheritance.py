""" module to show aspects of OOP in Python"""
class Human:
    """ a class human with three public instance attributes"""
    # init function, the constructor that accepts heart as an arg
    def __init__(self, heart):
        # using the self parameter to initialize the attributes with their values
        self.my_eyes = 2
        self.my_nose =1
        self._heart = heart
    # this is an instance method
    def eat(self):
        print("I can eat")
    # this is an instance method
    def walk(self):
        print("I can walk")
    # this is an instance method
    def work(self):
        print("i can work")

class Male(Human):
    """ a  class that inherits from Human super class"""
    def __init__(self, name, heart):
        # init function that accepts two arguments
        super().__init__(heart)
        # super method used to intialize the attribute heart from the super class
        self._name = name
        # local attribute to the child class
    def flirt(self):
        # local class method
        print("I can flirt")

    def work(self):
        # super method used to intialize the method work from super class
        super().work()
        # print local to the instance method
        print("i can code")

    def display(self):
        # a local method that prints the two attributes
        print(f"Hello, I am {self._name} and i have {self._heart} heart")

# creating objects/instances from the super and sub classes
male_0 = Male("Jackie", 1)
# a class created from the child class
male_0.eat()
# invoking the eat method associated with male_0 obj
male_0.walk()
# invoking the walk method associated with male_0 obj
male_0.work()
# invoking the work method associated with male_0 obj
male_0.flirt()
# invoking the flirt method associated with male_0 obj
print(male_0.my_eyes)
# printing the attributes of obj
print(male_0.my_nose)
# printing the attributes of obj
print(male_0._name)
# printing the attributes of obj
print(male_0._heart)
# printing the attributes of obj
male_0.display()
# invoking the display method associated with male_0 obj
