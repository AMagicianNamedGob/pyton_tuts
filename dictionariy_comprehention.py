# {_ : _ for _ in _ }
# {key: value for key, value in iterable}

# example 1
numbers = dict(first=1, second=2, third=3)
squared = {key: value**2 for key, value in numbers.items()}
print(squared)

# example 2
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(min(len(str1), len(str2)))}
print(combo)

# example 3
num_list = [
    1,
    2,
    3,
    4,
]

answer = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(answer)


# exercises
# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. Save it to a variable called answer.
print("\nexercise 1\n")

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i]: list2[i] for i in range(len(list1))}
print(answer)

# using zip
answer = dict(zip(list1, list2))
print(answer)

print("\nexercise 2\n")

# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
print(answer)

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this

print("\nexercise 3\n")
vowels = "aeiou"
answer = {vowel: 0 for vowel in vowels}
print(answer)

# very character has an ASCII code (basically, a number that represents it).  Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code. Your task is to create dictionary that maps ASCII keys to their corresponding letters.  Use a dictionary comprehension and chr() . Save the result to the answer variable. You only need to care about capital letters (65-90 in ASCII).

print("\nexercise 4\n")
answer = {i: chr(i) for i in range(65, 91)}
print(answer)
