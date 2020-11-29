#!/usr/bin/env python3

# Use break, continue and pass statements

j = 1
while j < 100:
    while j < 30:
        print(j, "<30")
        j = j + 2
        continue
    while j < 60:
        print("..",j, "< 60")
        j = j + 5
        pass
    while j < 100:
        print(j, "<100")
        j = j + 10
        break
