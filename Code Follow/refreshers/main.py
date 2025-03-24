# tuples have no methods, they are unchangeble. they are used to store multiple items in a single variable. Can I add multiple items to a tuple? No, you cannot add items to a tuple once it is created. Tuples are unchangeable.
my_tuple = ("apple", "banana", "cherry")

# Loops: several ways to loop through a list

# 1. Using a for loop
for x in my_tuple:
    print(x)

# 2. Using a while loop
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i = i + 1

# 3. Using list comprehension
[print(x) for x in my_tuple]

# 4. Using the iter() method
my_iter = iter(my_tuple)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
    
# 5. Using the enumerate() method
for i, x in enumerate(my_tuple):
    print(i, x)

#  6. Using the zip() method
my_tuple2 = ("red", "green", "blue")
for x, y in zip(my_tuple, my_tuple2):
    print(x, y)

# Dictionaries
user_dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Loops: several ways to loop through a dictionary


# 1. Keys
for x in user_dictionary:
    print(x)

# 2. Values
for x in user_dictionary:
    print(user_dictionary[x])

for x, y in user_dictionary.items():
    print(x, y)

# You can delete them
del user_dictionary["name"]

# If you want to clone, you can use the copy() method. You cannot assign a new to the old one because if you then modify the first one, the second one will also be modified.
user_dictionary2 = user_dictionary.copy()

# Standard library comes with Pythin
import random
types_of_drink = ["coffee", "tea", "water"]
print(random.choice(types_of_drink))