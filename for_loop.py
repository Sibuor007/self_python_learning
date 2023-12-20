name_ = ['Francis', 'Opol', 'Otieno']

for i in name_:
    print(i)
    if i == 'Opol':
        print('Hello Francis!')
        break

numbers_ = [4, 9, 8, 2, 10]
squares_l = []
for num in numbers_:
    sqr = num ** 2
    squares_l.append(sqr)
print("List sqr: ", squares_l)
