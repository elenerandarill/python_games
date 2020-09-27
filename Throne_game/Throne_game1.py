import turtle
import random

my_wn = turtle.Screen()
my_pen = turtle.Turtle()	#my turtle
my_pen.speed(20)
my_wn.bgcolor("grey")
my_pen.color("white", "light blue")

class Game():
	g1x = 50	#start pos
	g1y = 50
	g2x = -50	#start pos
	g2y = -50
	
	dx = 0	#wektor przesuniecia
	dy = 0
	
	g1= []	#woreczek ruchow

game = Game()
my_wn.delay(1)

	

def teleport():		#leci na miejsce
	my_pen.up()
	my_pen.goto(game.g1x, game.g1y)
	my_pen.down()

def my_square(a):	#rysuje kwadrat
	teleport()
	if is_free() == "dead":
		game_over()
		return
	my_pen.begin_fill()
	for i in range(4):
		my_pen.forward(10)
		my_pen.right(90)
	my_pen.end_fill()
	game.g1.append((game.g1x,game.g1y))	#dodanie ruchu do woreczka
	print(game.g1)



def is_free():
	if len(game.g1) > 1:
		for i in range (0, len(game.g1)):
			if game.g1x == game.g1[i][0] and game.g1y == game.g1[i][1]:
				return "dead"


#petla gry
my_square(10)


def game_over():
	my_pen.up()
	my_pen.goto(0,200)
	my_pen.down()
	my_pen.write("Game Over", align = "center", font = ("Arial", 12, "bold"))

def move_up():
	game.g1y += 10
	my_square(10)
	
def move_down():
	game.g1y -= 10
	my_square(10)
	
def move_left():
	game.g1x -= 10
	my_square(10)

def move_right():
	game.g1x += 10
	my_square(10)



my_wn.onkeypress(move_up, "Up")
my_wn.onkeypress(move_down, "Down")
my_wn.onkeypress(move_left, "Left")
my_wn.onkeypress(move_right, "Right")

my_wn.listen()
turtle.done()