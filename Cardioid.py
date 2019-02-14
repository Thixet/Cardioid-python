from math import *
from turtle import *

setup(600, 600)
hideturtle()
tracer(0)
listen()

points = 10
factor = 2
r = (window_width() / 2) - 20


def draw():
	global points
	clear()
	penup(), setpos(0, -r), pendown()
	circle(r)
	for i in range(points + 1):
		penup()
		x = r * cos(i * 2 * pi / points)
		y = r * sin(i * 2 * pi / points)
		setpos(x, y), dot(5)

		setpos(x, y), pendown()
		a = i * factor % points
		x = r * cos(a * 2 * pi / points)
		y = r * sin(a * 2 * pi / points)
		setpos(x, y)
	points += 1


def factor_plus():
	global factor
	factor += 1
	draw()


def factor_moins():
	global factor
	factor -= 1
	draw()

draw()
onkeypress(draw, "space")
onkeypress(factor_plus, "Right")
onkeypress(factor_moins, "Left")
mainloop()
