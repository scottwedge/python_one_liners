#!/usr/bin/env python3
# one line way
lst =  [x**2 for x in range(10)]
print(lst)


# Long way
lst2 = []  # define list
for x in range(10):
  square = x * x
  lst2.append(square)

print(lst2)
