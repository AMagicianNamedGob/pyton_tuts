# tuples are like lists but they are immutable (cannot be changed), they use parentheses instead of square brackets
my_tuple = (1, 2, 3, 3, 2, 1)
print(my_tuple[0])  # access the first element
# my_tuple[0] = 10  # this will raise an error because tuples cannot be changed

# sets are unordered collections of unique elements, they use curly braces
my_set = {1, 2, 3}
print(my_set)
my_set.add(4)  # add an element to the set
print(my_set)
my_set.add(2)  # adding a duplicate element does nothing
print(my_set)
my_set.remove(3)  # remove an element from the set
print(my_set)

print("\nexercises\n")

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
numbers = (1, 2, 3, 4)
value = (1,)

# 3 - Given the following variable:

values = [10, 20, 30]

# Create a variable called static_values which is the result of the values variable converted to a tuple

static_values = tuple(values)
print(static_values)

# 4 - Given the following variable

stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)
print(unique_stuff)
