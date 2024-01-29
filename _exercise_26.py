# this is a class 
class Circle:
    # a public class attribute
    pi = 3.14
    # this is the constructor
    def __init__(self, radius):
        # _radius and _area use to access instance attributes
        # protected instance attributes
        self._radius = radius
        self._area = Circle.pi * radius * radius
    # this is a class method
    def circumference(self):
        return 2 * self.pi * self._radius

# creating an object, instance of the class
circle_1 = Circle(6)
# printing the circumference, which is returnd by the instance method
print(circle_1.circumference())

# creating another class, another instance of the class
# passing 91 as the actual parameter/argument
circle_2 = Circle(91)
# printing the return value of the instance method
print(circle_2.circumference())
# printing the _area attribute of the object
print(circle_1._area)
