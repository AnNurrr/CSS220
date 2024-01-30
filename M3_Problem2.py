# Ainur
# 1/30/24

# Problem 2 - Write a Python program to add members to a set.
# Start off with an emtpy set
# Add "Red" to the set
# Update the set with "Blue" and "Green"


# Create an empty set
colorSet = set()
print(colorSet)

# Add "Red" to the set. Example of single item.
colorSet.add('Red')
print("colorSet = ", colorSet)

# Update the set with "Blue" and "Green"
# colorSet.add("Blue", "Green") This didnt work too many times
colorSet.update(["Blue", "Green"])  # Allows you to add multiple items
print("colorSet = ", colorSet)