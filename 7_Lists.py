#!/usr/bin/env python3

l = [-1, -2, 0]
print(l)
l.append(1)
l.append(2)
print(l," has a length of", len(l))

# Insert
l.insert(0,-100)
print(l)

# Concatenate lists
l1 = [1,2,3]
l2 = [4,5]
print(l1)
print(l2)
print(l1 + l2)

l3 = l1 + l2
print(l3)

print(l3[2:4])

