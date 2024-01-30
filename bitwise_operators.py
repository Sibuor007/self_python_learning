# bitwise operators
# two variables taking values
a, b = 5, 4

# prints the value that results after the bitwise and operator
# 1 0 = 0
# 0 1 = 0
# 1 1 = 1
# 0 0 = 0
print(a & b)

# 1 0 = 1
# 0 1 = 1
# 1 1 = 1
# 0 0 = 0
print(a | b)

# 1 0 = 1
# 0 1 = 1
# 1 1 = 0
# 0 0 = 0
print(a ^ b)

# 1 = 0
# 0 = 1
print(~a)

# 1 = 0
# 0 = 1
print(~b)

# left shtifing bytes of a by two positions
print(a << 2)
# outcome = 20
# right shifting bytes of b by two positions
print(b >> 2)
# outcome = 3
