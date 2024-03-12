from turtle import *

# Ainur
# 3/12/24
# CSS 220 Fractal tree Example ( T-tree)
# rearient the trunk of the tree to vertical

rt(-90)
# branching angle for the base
angle = 30


# function for the Y-tree
# size = length of first line, depth = number of iterations
def yTree(size, depth):
    if depth >0:
        #draw the base ( a vertical line)
        fd(size)
        rt(angle)

yTree(100, 10)
Screen().exitonclick()