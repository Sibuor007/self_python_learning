set_1 = {10, 34, -12, True, 'Jenny', 45, 76}
set_3 = set()
print(set_3)
"""
duplicates are not allowed
indexing is not possible
it contains items that are unordered
the items can be changed/mutable
items are not subscriptable
"""
set_1.add(90)
set_1.discard(76)
set_3.clear()
set_1.pop()
set_1.add((23, 456, 1, 6))
print(set_1.pop())
# set_2 = {}
# print(type(set_2))
print(type(set_1))
print(set_1)
print(len(set_1))
