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