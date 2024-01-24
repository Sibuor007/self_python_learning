def greet(name, dept="CS"):
    print(f"Hello, {name}")
    print(f"Are you from {dept} department")


# positional arguments
greet("Sibuor", "Computer Science")
# keyword arguments
# order is irrelevant here
greet(dept="Computer Science", name="Sibuor")
# positional arguments first, then keyword arguments
greet("Sibuor", dept="Computer Science")


# default arguments
# always include them after all non-default arguments

# arbitrary arguments

def add(res_=None, *nums_):
    for i in nums_:
        res_ += i
    print(f"The sum is : {res_}")


add(78, 90, 23, 2, 7)
