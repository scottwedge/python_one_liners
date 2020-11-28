#!/usr/bin/env python3

# Test break action in a loop

n = 1
while True:
    print("hello", n)
    if n > 1000:
        break
    else:
        n = n + 100
    n = n + 1
