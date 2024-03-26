from turtle import *

# Ainur
# 3/12/24
# CSS 220 Fractal tree Example ( T-tree)
# rearient the trunk of the tree to vertical

# increase drawing speed
speed('fastest')

rt(-90)
# branching angle for the base
angle = 30


# function for the Y-tree
# size = length of first line, depth = number of iterations
def yTree(size, depth):
    if depth >0:

        colormode(225)
        # add in color
        pencolor(0, 225 // depth, 0)
        #draw the base ( a vertical line)
        fd(size)
        rt(angle)

        # recursive call to build branches
        yTree(0.9*size, depth-1)
        # add in color
        pencolor(0, 225 // depth, 0)

        # rotates left 60 degrees
        lt(2*angle)

        # recursive call to build branches
        yTree(0.8 * size, depth - 1)

        # add in color
        pencolor(0, 225 // depth, 0)

        # reset position
        rt(angle)
        fd(-size)
yTree(80, 8)
Screen().exitonclick()
