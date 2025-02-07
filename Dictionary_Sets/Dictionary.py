# Dictionary In Python 

# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.
# The keys are unique and the values can be repeated.

my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

print(type(my_dict))
print(my_dict['key2']) 
print(my_dict['key3']) 
 
my_dict['key4'] = 'value4'

print(my_dict)
print(my_dict['key4'])
print(len(my_dict))
my_dict.clear()
print(my_dict)