#!/usr/bin/env python3

# Sets and hashes

hero = "Harry"
friend = "Ron"
heroine = "Hermione"

print(hash(hero))
print(hash(friend))
print(hash(heroine))

# Can we create a set of strings?  YES
set1 = {friend, heroine, hero}
# Print order change
print(set1)


# Lists
l1 = [1,2]
l2 = [3,4]
l3 = [6,8]

# Try to make a set of lists:  FAILS
#set2 = {l1, l2, l3}
#print(set2)

# Create set of sets?  FAIL
set3 = { "hello",  "there"}
print(set3)

#s4 = {set1, set3}
#print(s4)
