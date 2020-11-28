#!/usr/bin/env python3

# Test break action in a loop

n = 1
while True:
    print("hello", n)
    if n == 2:
        break
    n = n + 1
