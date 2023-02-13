# +
# -
# *
# /
# **
# %

# print(2 + 3)
# print(3 - 2)
# print(3 * 2)
# print(type(4 / 2))
# print(type(4 // 2))
# print(9 ** 3)
# print(4 % 3)
# print(4 * 6 / (1 + 3) - 9 ** 2)

# 4 * 6 / (1 + 3) - 9 ** 2
# 4 * 6 / 4 - 9 ** 2
# 4 * 6 / 4 - 81
# 24 / 4 - 81
# 6.0 - 81
# -75.0



# PEMDASLR
# PARENTHESES
# EXPONENTS
# MULTIPLICATION
# Division
# ADDITION
# SUBTRACTION



from turtle import *
bgcolor("grey")
fillcolor("yellow")
pensize(2)
begin_fill()
circle(100)
end_fill()
penup()
def draw_circle(x=-50, y=130):
    goto(x, y)
    dot(30, "red")
    goto(x, y+6)
    dot(15, "white")
draw_circle()
draw_circle(50)
goto(-50, 50)
pendown()
setheading(320)
fillcolor("red")
begin_fill()
circle(80, 80)
setheading(150)
circle(50, 62)
setheading(150)
circle(50, 62)
end_fill()
hideturtle()
exitonclick()























