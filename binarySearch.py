# Ainur
# 2/20/2024
# CSS 220 Module 6

# Binary Search

numberList=[1, 4, 6, 9, 20, 40, 60]
number = 20
l =0
nlength = len(numberList)

def bSearch(numberList, number, nlength, l):
    while l<=nlength:
        mid = l+(nlength -l) //2;

        if numberList[mid] == number:
            return mid
        elif numberList[mid] < number:
            l = mid+1
        else:
            nlength = mid-1

i=bSearch(numberList, number, nlength, l)
print("The number is at index: ", i)