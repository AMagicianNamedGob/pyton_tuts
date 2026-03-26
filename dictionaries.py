# dicts are essentially JSON objects, but they can also be used to store data in a more structured way.

my_first_dict = {
    "name": "Jared Truscott",
    "age": 48,
    "hobbies": ["coding", "gaming", "cooking"],
    "is_cool": True
}

print(f'{my_first_dict}\n')

my_first_dict["name"] = "Jared Leto"
my_first_dict["is_cool"] = False

print(f'{my_first_dict}\n')

alt_method = dict(name="Jared Truscott", age=48, hobbies=["coding", "gaming", "cooking"], is_cool=True)
print(f'{alt_method}\n')

#accessing values in a dict by iteration
for key in my_first_dict.keys():
    print(key)
print("\n")

for value in my_first_dict.values():
    print(value)
print("\n")

for key, value in my_first_dict.items():
    print(f"key={key} value={value}")
print("\n")

# rl example
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

total_donations = 0
for donation in donations.values():
    total_donations += donation
print(total_donations)

# one line solution
total_donations = sum(donations.values())
print(total_donations)

# check if a key is in the dict
print("sam" in donations) # True
print("cat" in donations) # False

print("\n")

#check if a value is in the dict
print(25.0 in donations.values()) # True
print(100.0 in donations.values()) # False
