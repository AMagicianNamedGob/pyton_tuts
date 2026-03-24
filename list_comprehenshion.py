# [_ for _ in _ ]

name = 'Jared'
letters = [letter.upper() for letter in name]
print(''.join(letters))

# can also be used with conditionals
nums = list(range(1,11))
even_nums = [num for num in nums if num % 2 == 0]

# "better way" is [num * 10 for num in even_nums] this is just an example of using comprehension with a condition in the same line
multiplied  = [nums * 10 for nums in nums if nums % 2 == 0]

# the f-string is to keep the formatting of the list on a new line without having any extra spaces in the output
print(f"{even_nums}\nmultiplied\n{multiplied}")

numbers = list(range(1,11))
sample = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(sample)

names, nums =  ["Elie", "Tim", "Matt"],  [1,2,3,4,5,6]


answer = [name[0] for name in names]
answer2 = [num for num in nums if num % 2 == 0]

results = [answer, answer2]

print(*results, sep="\n")
