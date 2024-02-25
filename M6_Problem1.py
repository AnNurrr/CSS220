# Ainur
# 2/25/24

# CSS 220 Homework activity

# Find the smallest and largest numbers in the following unsorted list

unsortedList = [4, 2, 7, 3, 8, 5]
length = len(unsortedList)
smallest = unsortedList[0]
largest = unsortedList[0]


for number in unsortedList:
    if number < smallest:
        smallest = number
    elif number > largest:
        largest = number

print("The smallest number is: ", smallest)
print("The largest number is: ", largest)







