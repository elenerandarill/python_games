import turtle
import random

my_wn = turtle.Screen()
my_pen = turtle.Turtle()	#my turtle
my_pen.speed(0)
my_wn.bgcolor("grey")
my_pen.color("white", "light blue")
my_wn.tracer(1, 10)


class Game():
	g1x = 50	#start pos
	g1y = 50
	g2x = -50	#start pos
	g2y = -50
	
	dx = 0	#wektor przesuniecia
	dy = 10
	
	speed = 200
	taken = []	#zajete miejsca

game = Game()



def teleport():		#leci na miejsce
	my_pen.up()
	my_pen.goto(game.g1x, game.g1y)
	my_pen.down()

def my_square(a):	#rysuje kwadrat
	teleport()
	my_pen.begin_fill()
	for i in range(4):
		my_pen.forward(10)
		my_pen.right(90)
	my_pen.end_fill()
	
	game.taken.append((game.g1x,game.g1y))	#dodanie ruchu do woreczka
	#print(game.taken)
	
def move_up():
	game.dy = 10
	game.dx = 0
	
	
def move_down():
	game.dy = -10
	game.dx = 0
	

def move_left():
	game.dx = -10
	game.dy = 0
	

def move_right():
	game.dx = 10
	game.dy = 0
	

def game_loop():
	game.g1x += game.dx
	game.g1y += game.dy
	my_square(10)

	
	my_wn.ontimer(game_loop, game.speed)


#gra
teleport()
my_square(10)
game_loop()

my_wn.listen()
my_wn.onkeypress(move_up, "Up")
my_wn.onkeypress(move_down, "Down")
my_wn.onkeypress(move_left, "Left")
my_wn.onkeypress(move_right, "Right")

my_wn.delay(0)


turtle.done()
# BIBLIOTEKI TURTLOWE
#def done():
#	while True:
#		if nacisnieto_klawisz():
#			uruchom_onkeypress_zarejestrowany();
#		if czas_minal():
#			uruchom_timery()