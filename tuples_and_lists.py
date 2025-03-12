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