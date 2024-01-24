phone_numbers = {'Sibuor': 1234,
                 'Jenny': 5678,
                 'Khatri': '91011'
                 }
phone_numbers_0 = dict([('otieno', 9087), ('denis', 5627), ('otonglo', 9028)])
# copy method to make a copy of a dictionary
phone_numbers_1 = phone_numbers_0.copy()
# you can also use the dict method to create a dictionary
print(phone_numbers_0)
print(phone_numbers['Jenny'])  # pass the key to obtain value
# it is case-sensitive
# duplicates are not allowed
print(phone_numbers)
# values can be of any data types
# all the keys should be immutable
# dictionary can contain list and another dictionary

# you can change the values in the dict
phone_numbers['Sibuor'] = 9990
phone_numbers_0['denis'] = 1232
phone_numbers['Ratego'] = {7821, 9000, 6272}
phone_numbers_0['otieno'] = {'Otieno_home': 7666, 'Otieno_work': 11222}

print(phone_numbers_0)
print(phone_numbers)
# accessing a value in a nested dictionary
print(phone_numbers_0['otieno']['Otieno_work'])
# we can also use get method to access value of a key
# in case of mismatch, None will be displayed instead of error
print(phone_numbers.get('Sibuor'))
# integers can also be used as keys
data = {1: 'Opol',
        2: 'Otieno',
        0: 'Ondiek'
        }
print(data[0])
# deletion using del keyword
del phone_numbers['Jenny']
# deletion using pop
deleted = phone_numbers_0.pop('denis')
print(f"Number deleted: {deleted}")
# using pop item to delete the last item
phone_numbers_0.popitem()
# using clear method do delete all items
print(phone_numbers.clear())
print(phone_numbers)
# keys method to get the keys from the dictionary
print(phone_numbers_0.keys())
# values method to get the values from the dictionary
print(phone_numbers_0.values())
# items method will return a list of all items in a tuple
print(phone_numbers_0.items())
print(phone_numbers_1)
# len to get length of a dictionary
print(len(phone_numbers_1))
