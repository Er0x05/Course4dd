#代码将画出三个红色线条，中间有间隙。可以看出，某些代码重复了。请更改代码，使这些代码行位于 for 循环里

#循环每次运行时，它都使用不同的颜色，例如使用红色，黄色，蓝色

#画出三个不同颜色的正方形，而不是三条线

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between
amy.color("red")

amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()

amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()

amy.forward(50)
amy.penup()
amy.forward(50)
amy.pendown()

