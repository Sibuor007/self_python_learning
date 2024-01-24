class Human:
    def __init__(self, heart):
        self.my_eyes = 2
        self.my_nose =1
        self._heart = heart
    def eat(self):
        print("I can eat")

    def walk(self):
        print("I can walk")

    def work(self):
        print("i can work")

class Male(Human):
    def __init__(self, name, heart):
        super().__init__(heart)
        self._name = name
    def flirt(self):
        print("I can flirt")

    def work(self):
        super().work()
        print("i can code")

    def display(self):
        print(f"Hello, I am {self._name} and i have {self._heart} heart")

male_0 = Male("Jackie", 1)
male_0.eat()
male_0.walk()
male_0.work()
male_0.flirt()
print(male_0.my_eyes)
print(male_0.my_nose)
print(male_0._name)
print(male_0._heart)
male_0.display()
