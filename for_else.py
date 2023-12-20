num_tuple = (23, 78, 90, 13, 38)

for i in num_tuple:
    # print(i)
    if i % 3 == 0:
        break
# its execution symbolizes absence of break statement
else:
    print("number is not divisible by six")
print("out of loop")
