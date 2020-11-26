#!/usr/bin/env python3

x = input("Enter value: ")
print(x)
print(type(x))
x=int(x)
print(type(x))

if x > 3:
    print(">3")
elif x == 3:
    print("=3")
else:
    print("<3")
