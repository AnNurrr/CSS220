# Ainur
# 1/30/24
# CSS 220 In CLass Activity Module 3


# Problem 7 - Write a Python program to create if
# two given set have no elements in common
# Use sets x = {1, 2, 3, 4}, y = { 4, 5, 6, 7}, and z = {8}.

x = set([1, 2, 3, 4])
y = set([4 , 5, 6, 7])
z = set([8])
print(x)
print(y)
print(z)

# Check if sets are disjoint
print("Are x and y disjoint?")
print(x.isdisjoint(y))

print("Are x and z disjoint?")
print(x.isdisjoint(z))

print("Are y and z disjoint?")
print(y.isdisjoint(z))