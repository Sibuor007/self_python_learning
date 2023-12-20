set_1 = {'wichlum', 'Otieno', 'Oele', 'Onyango'}
set_2 = {'Otieno', 'Oloo', 'Oburu', 'Onyango', 'Odhiambo'}
set_3 = {'Wichlum', 'Odongo', 'Usenge', 'Oele'}

print(set_1.isdisjoint(set_2))
print(set_1.isdisjoint(["Odongo", "Otieno"]))

print(set_1.issubset(['wichlum', 'Otieno', 'Oele', 'Onyango']))
print(set_1 <= set_2)

print(set_1.issuperset(set_2))
print(set_1 >= set_2)

# only deletes the items in the set and leaves an empty set
set_3.clear()
print(set_3)

# deletes everything including the set
del set_2
print(set_2)
