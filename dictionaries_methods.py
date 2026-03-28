d = {'a': 1, 'b': 2, 'c': 3}
cloned = d.copy()

# clear - obviously clears the dictionary
(print(d.clear())) # None, {}

# copy - creates a copy of the dictionary
print(cloned) # {'a': 1, 'b': 2, 'c': 3}

# fromkeys - creates a new dictionary with keys from an iterable and values set to a value
new_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print(new_dict) # {'a': 0, 'b': 0, 'c': 0}

# get - returns the value for a key if it exists in the dictionary, otherwise returns a default value
print(d.get('a')) # 1
print(d.get('d', 'default')) # default

# pop - removes a key from the dictionary and returns its value
print(cloned.pop('c')) # 3
print(cloned) # {'a': 1, 'b': 2}

# popitem - removes the last inserted key-value pair from the dictionary and returns it as a tuple
print(cloned.popitem()) # ('c', 3)
print(cloned) # {'a': 1, 'b': 2}

# items - returns a view object that displays a list of dictionary's key-value tuple pairs
print(cloned.items()) # dict_items([('a', 1), ('b', 2)])

# update - updates the dictionary with the key-value pairs from another dictionary or from an iterable of
d2 = {'d': 4, 'e': 5}
cloned.update(d2)
print(cloned) # {'a': 1, 'b': 2, 'd': 4, 'e': 5}
