import turtle
import random
   
# drawing snail sheel
"""   
my_wn = turtle.Screen()
my_wn.bgcolor("black")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.color("blue")
def my_sqrfunc(size):
   for i in range(4):
      my_pen.fd(size)
      my_pen.left(90)
      size = size - 5
	  
	
a = 200
for i in range(10):
	my_sqrfunc(a)
	a -= 20
"""

my_pen = turtle.Turtle()
my_pen.speed(1)

def my_dwg(x, y, a, color: str):
	my_pen.color("black", color)
	my_pen.up() 
	my_pen.setpos(x,y)
	my_pen.down()
	my_pen.begin_fill()
	for i in range(4):
	   my_pen.forward(a)           
	   my_pen.right(90)
	my_pen.end_fill()

for i in range(50):
	if i %5 == 0:
		my_pen.clear()
	x = random.randint(-150, 151)
	y = random.randint(-150, 151)
	a = random.randint(10, 101)
	color_lst = ['purple', 'pink', 'green', 'blue', 'orange', 'brown']
	color_id = random.randint(0, len(color_lst)-1)
	color = color_lst[color_id]
	print(f"x: {x}, y: {y}, a: {a}")
	my_dwg(x, y, a, color)
	   
turtle.done()

#drawing circle flower
"""
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_pen = turtle.Turtle() #to jest zolw!
my_pen.color("blue")
#my_wn.tracer(False)
my_pen.speed(1)
for i in range (20):
	my_pen.forward(10 + i)
	my_pen.circle(3*i)
	my_pen.circle(-5*i)
	my_pen.left(i)

my_wn.update()
my_wn.exitonclick()
"""