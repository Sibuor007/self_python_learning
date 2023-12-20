class Instructor:
    def __init__(self, inst_name, address):
        self.name = inst_name
        self.address = address
        self.followers = 0


instruct_0 = Instructor("Opol", "Uhanya")
print(instruct_0.name)
print(instruct_0.address)
