#!/usr/bin/env python3

# Dictionary stuff

calories = {"apple":51, "pear":72, "banana":45}
print(calories)

# start using key:value pairs
print(calories["apple"])

# logic comparison
print(calories["apple"] < 52)   # Should be True

# Change value
calories["apple"] = 99
print(calories)

for k,v in calories.items():
    print(k)

for k,v in calories.items():
    print(v)

for k,v in calories.items():
    print(k) if v > 70 else print("low")

# Keys
for k in calories.keys():
    print(k)

# Values
for v in calories.values():
    print(v) if v > 70 else print("not > 70")

# List of tuples
customers = [ ("Allan", 1000),
        ("Steve", 2000),
        ("Gerry", 2100)]


# Top earning customers
TOP = 2000
whales = [ x for x,y in customers if y > 2000 ]
print(whales)
