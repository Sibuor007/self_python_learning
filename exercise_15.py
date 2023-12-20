num_ = input("Enter list of numbers: ")
# 25 980 82 27 34 19
num_list = num_.split()
print(num_list)

count = 0
for i in num_list:
    count = count + 1
print(f"Length of list is {count}")

for i in range(count):
    num_list[i] = int(num_list[i])
print(num_list)

max_num =num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num
print(f"Maximum number is: {max_num}")