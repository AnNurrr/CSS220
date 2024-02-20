# Ainur
# 2/6/2024


# Module 4 In-Class Activity
# Encodes a message using the Ceasar's cipher

message = "computer"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in range(len(LETTERS)):
    encoded =''
    for y in message:
        if y in LETTERS:
            n = LETTERS.find(y)
            n = (n + x) % len(LETTERS)
            if n<0:
                n = n+len(LETTERS)
            encoded = encoded+LETTERS[n]
        else:
            encoded = encoded+y
    print("Shift key ", x ," : ", encoded)

