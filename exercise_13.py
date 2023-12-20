row_1 = ['🤤', '🤤', '🤤']
row_2 = ['🤤', '🤤', '🤤']
row_3 = ['🤤', '🤤', '🤤']

matrix = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

_pos = input("Enter position to store money: ")
row_num = int(_pos[0])
column_num = int(_pos[1])

row_select = matrix[row_num - 1]
row_select[column_num - 1] = 'X'
print(f"{row_1}\n{row_2}\n{row_3}")

