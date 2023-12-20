class Circle:
    pi = 3.14

    def __init__(self, radius):
        self._radius = radius
        self._area = Circle.pi * radius * radius

    def circumference(self):
        return 2 * self.pi * self._radius


circle_1 = Circle(6)
print(circle_1.circumference())

circle_2 = Circle(91)
print(circle_2.circumference())
print(circle_1._area)
