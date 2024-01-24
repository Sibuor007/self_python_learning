# arbitrary positional arguments
def add_func(*args):  # the arguments are capture and put into a tuple
    # a tuple is immutable, hence the choice
    c = 0
    for i in args:
        c += i
    print(f"the sum is {c}")


add_func(8, 9, 2, 4, 5)


# arbitrary keyword arguments
def info_person(**kwargs):  # arguments will be passed in form of dict
    for key, value in kwargs.items():
        print(key, value)


# args precedes **kwargs by convention
# args => tuple
# kwargs => dictionary
info_person(name="Sibuor", age=28, dept="Software Engineering")
