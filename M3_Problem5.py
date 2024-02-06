# Ainur
# 1/30/24
# CSS 220 In CLass Activity Module 3

# Write a program to create set difference.
# Use sets x = {apple, mango} and y={mango, orange}


# Creat sets x and y
x = set(["apple", "mango"])
y = set({"mango", "orange"})
print(x)
print(y)


# Checks for an intersection
a = x & y
print("Intersection =", a)


# Set difference of x and y
z = x-y
print("Difference = ", z)

b = y - x
print("Difference = ", b)

c = z | b
print("The difference = ", c)
