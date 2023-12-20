class Instructor:
    followers = 0  # class object variable

    def __init__(self, name, address):
        self._name = name
        self._address = address

    def update_followers(self, followers_update):
        self.followers += 1

    def display(self, subject_name):
        print(f"Hello {self._name}, can you teach me {subject_name}")

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address


ins_1 = Instructor('Opol', 'wichlum')
print(ins_1.name)
print(ins_1.address)
ins_1.display("Python")
ins_1.update_followers("Jenny")
print(ins_1.followers)

ins_2 = Instructor('Jemmy', "Kisii")
ins_2.update_followers("Opol")
print(ins_2.followers)
