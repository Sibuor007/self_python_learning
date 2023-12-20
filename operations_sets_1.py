set_1 = {'wichlum', 'Otieno', 'Oele', 'Onyango'}
set_2 = {'Otieno', 'Oloo', 'Oburu', 'Onyango', 'Odhiambo'}
set_3 = {'Wichlum', 'Odongo', 'Usenge', 'Oele'}

# print(set_1.union(set_2, set_3))
# set_1.update(set_2)
# print(set_1)
# update set 1 with set 2
# set_1 |= set_2
# print(set_1 | set_2 | set_3)
# set_2.union(set_1)
print(set_1.intersection(set_2))
# & used to perform intersection- common items
print(set_1 & set_2)
set_1.intersection_update(set_3)
print(set_1)
