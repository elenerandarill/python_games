import turtle
import random

my_wn = turtle.Screen()
my_pen = turtle.Turtle()
my_pen.speed(1)

def teleport(x,y):
	my_pen.up() 
	my_pen.setpos(x,y)
	my_pen.down()

def my_square(x, y, a, color: str):
	my_pen.color("black", color)
	teleport(x,y)
	my_pen.begin_fill()
	for i in range(4):
	   my_pen.forward(a)           
	   my_pen.right(90)
	my_pen.end_fill()

def my_circle(x, y, r, color: str):
	my_pen.color("black", color)
	teleport(x,y)
	my_pen.begin_fill()
	my_pen.circle(r)
	my_pen.end_fill()

def rand_dwg(x, y):
	a = random.randint(10, 101)
	color_lst = ['purple', 'pink', 'green', 'blue', 'orange', 'brown']
	color_id = random.randint(0, len(color_lst)-1)
	color = color_lst[color_id]
	print(f"x: {x}, y: {y}, a: {a}")
	#losowanko
	i = random.randint(0,100)
	if i > 50:
		my_square(x, y, a, color)
	else:
		my_circle(x, y, a, color)
	

def my_onclick(x, y):
	rand_dwg(x, y)

def my_keypress_L():
	x = random.randint(-200, 0)
	y = random.randint(-200, 200)
	rand_dwg(x, y)
	
def my_keypress_R():
	x = random.randint(0, 200)
	y = random.randint(-200, 200)
	rand_dwg(x, y)

def my_keypress_U():
	x = random.randint(-200, 200)
	y = random.randint(0, 200)
	rand_dwg(x, y)
	
def my_keypress_D():
	x = random.randint(-200, 200)
	y = random.randint(-200, 0)
	rand_dwg(x, y)

my_wn.listen()
my_wn.onkey(my_keypress_L, "Left")
my_wn.onkey(my_keypress_R, "Right")
my_wn.onkey(my_keypress_U, "Up")
my_wn.onkey(my_keypress_D, "Down")
my_wn.listen()
my_wn.onclick(my_onclick)

turtle.done()