#!/usr/bin/env python3

# Test break action in a loop

n = 1
while True:
    n = n + 200
    if n < 1000:
        continue
    print("hello", n)
    if n > 2000:
        break
