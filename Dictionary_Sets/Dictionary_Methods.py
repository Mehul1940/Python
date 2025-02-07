# Dictionaty Methods In Python 

my_dict = {
    'key1': 'value1',
    'key': 'value',
    'key3': 'value3'
}

print(my_dict)

my_dict['key4'] = 'value4' # It inserts the key and value
print(my_dict)

my_dict.pop('key3') # It removes the key and value
print(my_dict)

my_dict.popitem() # It removes the last key and value
print(my_dict)

my_dict.update({'key': 'value2'}) # It updates the key and value
print(my_dict)

my_dict.setdefault('key4', 'value4') # It adds the key and value
print(my_dict)

d= my_dict.fromkeys(['key1', 'key2', 'key3'], 'value') # It adds the key and value
print(d)

di=my_dict.copy() # It copies the dictionary
print(di)

print(len(my_dict)) # It returns the length of the dictionary
print(my_dict.keys()) # It returns the keys of the dictionary
print(my_dict.values()) # It returns the values of the dictionary
print(my_dict.items()) # It returns the items of the dictionary
print(my_dict)