import turtle
#import random

my_wn = turtle.Screen()
my_pen = turtle.Turtle()	#my turtle
my_pen.speed(0)
my_wn.bgcolor("grey")
#my_pen.color("white", "light blue")
my_wn.tracer(1, 10)


class Game():
	g1x = 50	#start pos
	g1y = 50
	g2x = -50	#start pos
	g2y = -50
	
	dx = 0	#wektor przesuniecia
	dy = 10
	d2x = 0
	d2y = -10
	
	speed = 200		#tyle milisekund mija miedzy jednym loopem gry a drugim
	taken = []	#zajete miejsca

game = Game()



def teleport(x,y):		#leci na miejsce
	my_pen.up()
	my_pen.goto(x, y)
	my_pen.down()

def is_free(x,y):
	if len(game.taken) > 2:
		for i in range(0, len(game.taken)):
			if x == game.taken[i][0] and y == game.taken[i][1]:
				return "dead"
		
		
def my_square(color):	#rysuje kwadrat
	my_pen.color("white", color)
	my_pen.begin_fill()
	for i in range(4):
		my_pen.forward(10)
		my_pen.right(90)
	my_pen.end_fill()
	
	
def game_over():
	my_square("red")
	teleport(0,200)
	my_pen.write("Game Over", align = "center", font = ("Arial", 12, "bold"))	

""""""
	
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
	
""""""	

def move2_up():
	game.d2y = 10
	game.d2x = 0
	
def move2_down():
	game.d2y = -10
	game.d2x = 0

def move2_left():
	game.d2x = -10
	game.d2y = 0

def move2_right():
	game.d2x = 10
	game.d2y = 0


def game_loop():
	teleport(game.g1x, game.g1y)
	if is_free(game.g1x, game.g1y) == "dead":
		game_over()
		return
	my_square("light blue")
	game.taken.append((game.g1x,game.g1y))	#dodanie ruchu do woreczka 'taken'
	#print(game.taken)
	game.g1x += game.dx
	game.g1y += game.dy
	
	teleport(game.g2x, game.g2y)
	if is_free(game.g2x, game.g2y) == "dead":
		game_over()
		return
	my_square("yellow")
	game.taken.append((game.g2x,game.g2y))	#dodanie ruchu do woreczka 'taken'
	#print(game.taken)
	game.g2x += game.d2x
	game.g2y += game.d2y
	
	my_wn.ontimer(game_loop, game.speed)#'on timer' zapewnia ponowne wywolanie game_loop za 200 milisekund


#gra
	
game_loop()

my_wn.listen()
my_wn.onkeypress(move_up, "Up")
my_wn.onkeypress(move_down, "Down")
my_wn.onkeypress(move_left, "Left")
my_wn.onkeypress(move_right, "Right")

my_wn.onkeypress(move2_up, "w")
my_wn.onkeypress(move2_down, "s")
my_wn.onkeypress(move2_left, "a")
my_wn.onkeypress(move2_right, "d")

my_wn.delay(0) #zobacz opis nizej vvvvv


turtle.done()
# BIBLIOTEKI TURTLOWE
#def done():
#	while True:
#		if nacisnieto_klawisz():
#			uruchom_onkeypress_zarejestrowany();
#		if czas_minal():
#			uruchom_timery()