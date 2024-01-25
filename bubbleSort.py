# Ainur
# 2/20/2024
# CSS 220 Module 6

# Bubble Search

numberList = [5, 99, 30, 15, 29, 63, 7]
nlength = len(numberList)

def bubbleSort(numberList, nlength):
    for i in range(nlength):
        for j in range(0, nlength-i-1):

            if numberList[j] > numberList[j+1]:
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]

print("Pre Sort: ", numberList)
bubbleSort(numberList, nlength)
print("Bubble Sort: ", numberList)
