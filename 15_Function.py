#!/usr/bin/env python3

# Function format is 'def' '<NAME>' '(var1, var2):'

def power_of(x, power):
    return x ** power

def square(y):
    return y ** 2


def combo (a, b, c):
     return power_of(a,b)/square(c)

print(power_of(10,2))

print(square(9))

print(combo(8,9,100))
