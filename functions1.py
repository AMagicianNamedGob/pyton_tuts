# def name_of_function():
from random import random


def say_hi():
    print("Hi")


say_hi()


def add_two_numbers(num1, num2):
    return num1 + num2


result = add_two_numbers(3, 5)
print(result)


def heads_or_tails():
    random_number = random()
    if random_number < 0.5:
        return "Heads"
    else:
        return "Tails"


result = heads_or_tails()
print(result)


# default parameters
def raise_to_power(base_num, pow_num=2):
    return base_num**pow_num


print(raise_to_power(3))
print(raise_to_power(3, 3))


def speak(animal="dog"):
    sounds = {"pig": "oink", "duck": "quack", "cat": "meow", "dog": "woof"}
    return sounds.get(animal, "?")


print(speak())
print(speak("pig"))
print(speak("giraffe"))


# keyword arguments
def raise_to_power(base_num, pow_num):
    return base_num**pow_num


print(raise_to_power(pow_num=3, base_num=3))

# global variables
total = 0


def increment():
    global total
    total += 1
    return total


print(increment())
print(increment())

# local variables
total = 0


def outer():
    total = 0

    def inner():
        nonlocal total
        total += 1
        return total

    return inner()


print(outer())


# docstrings
def say_hi():
    """This function prints 'Hi' to the console."""
    print("Hi")


print(say_hi.__doc__)

print(random.__doc__)
