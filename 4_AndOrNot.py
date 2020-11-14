#!/usr/bin/env python3

x,y = True, False
print("x,y = True, False")
print("x is : ",x, "not x is: ", not x)

print("x and y:", x and y)
print("x or y:", x or y)

print("not (x and y):", not ( x and y ))
print("not (x or y):", not ( x or y ))

print("Precedence is not, then and, then or")
print("so   not x and y or x:", not x and y or x)


