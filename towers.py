# Ainur
# 3/12/24
# CSS 220 Module 9 In Class Activity

def TowersofHanoi ( n, r1, r3, r2):
    if n==1:
        print("Move disk 1 from rod", r1, "to rod", r3)
        return
    else:
        TowersofHanoi(n-1, r1, r2, r3)
        print("Move disk", n, "from rod", r1, "to rod", r3)
        TowersofHanoi(n-1, r1, r3, r1)

TowersofHanoi(3, "A", "C", "B")