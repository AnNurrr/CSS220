# Ainur
# 1/30/24
# CSS 220 In CLass Activity Module 3

# Write a Python program to check if a set is a subset of another set.
# Use sets x = {apple, mango}, y = {mango, orange}, and z = {mango}. This program should use the issubset() method.

x = set(["apple", "mango"])
y = (["mango", "orange"])
z = (["mango"])
print(x)
print(y)
print(z)

#Check for subsets
print("Is x subset of y?")
print(x.issubset(y))

print("Is y suset of x?")
print(x.issubset(z))

print("Is x subset of z?")
print(x.issubset(z))

print("Is z subset of x?")
print(z.issubset(x))

print("Is z subset of y?")
print(z.issubset(y))

print("Is y subset of z?")
print(y.issubset(x))

