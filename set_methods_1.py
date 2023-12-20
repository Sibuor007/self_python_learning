set_1 = {'wichlum', 'Otieno', 'Oele', 'Onyango'}
set_2 = {'Otieno', 'Oloo', 'Oburu', 'Onyango', 'Odhiambo'}
set_3 = {'Wichlum', 'Odongo', 'Usenge', 'Oele'}

print(set_1.difference(set_2))
print(set_1.difference_update(set_2))
print(set_1 - set_2)
print(set_1.difference(('diablo', 'plomo', 'plata')))
print(set_1.difference(set_2, set_3))
print(set_1.difference_update(set_2, set_3))
# return elements in both sets, except the ones in both
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2 ^ set_3)
# update set
set_2.symmetric_difference_update(('Oyugi', 'Ndege'))
print(set_2)
