height_ = input("Enter height sep = space: ")
height_l = height_.split()
print(height_l)
count = 0
for height in height_l:
    count = count + 1
print("count: ", count)
for i in range(0, count):
   height_l[i] = int(height_l[i])
print(height_l)

total_ = 0
for i in height_l:
    total_ = total_ + i
print(total_)
average_ = total_ / count
print(round(average_))

