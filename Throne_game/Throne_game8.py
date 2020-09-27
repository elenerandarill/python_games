import turtle
import random

my_wn = turtle.Screen()
my_pen = turtle.Turtle()	#my turtle
my_pen.speed(0)
my_wn.bgcolor("grey")
my_wn.tracer(0, 10)

ALL_MOVES = [(0, -10), (0, 10), (10, 0), (-10, 0)]

class Game():
	g1x = 50	#start pos
	g1y = 50
	g2x = -50	#start pos
	g2y = -50
	
	dx = 0	#wektor przesuniecia
	dy = 10
	#d2x = 0
	#d2y = -10
	
	last_mv = random.choice(ALL_MOVES)
	
	speed = 300		#tyle milisekund mija miedzy jednym loopem gry a drugim
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
				return "taken"
		
	
def the_wall(length):
	x = -length * 5
	y = -length * 5
	for i in range(0, length):	#w gore
		teleport(x,y)
		my_square("white")
		game.taken.append((x,y))
		y += 10
	for i in range(0, length):	#w prawo
		teleport(x,y)
		my_square("white")
		game.taken.append((x,y))
		x += 10
	for i in range(0, length):	#w dol
		teleport(x,y)
		my_square("white")
		game.taken.append((x,y))
		y -= 10
	for i in range(0, length):	#w lewo
		teleport(x,y)
		my_square("white")
		game.taken.append((x,y))
		x -= 10
	
	

	
def my_square(color):	#rysuje kwadrat
	my_pen.color("white", color)
	my_pen.begin_fill()
	for i in range(4):
		my_pen.forward(10)
		my_pen.right(90)
	my_pen.end_fill()
	
	
def game_over(who):
	my_square("red")
	teleport(0,200)
	if who == "win":
		my_pen.write("Game Over - you win!", align = "center", font = ("Arial", 12, "bold"))
	else:
		my_pen.write("Game Over - you lose...", align = "center", font = ("Arial", 12, "bold"))

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


def try_move(x, y):
	#print()
	#print(f"x:{x}, y:{y}")
	
	all_2moves = ALL_MOVES.copy()		#[(0, -10), (0, 10), (10, 0), (-10, 0)]
	#print()
	#print(all_2moves)
	#dodaje ten ruch jeszcze 8 razy, zeby byla najwieksza szansa na jego wypadniecie
	for i in range(1, 9):	
		all_2moves.append(game.last_mv)
	
	rem_moves = []
	for move in all_2moves:
		if is_free(x+move[0], y+move[1]) != "taken":
			rem_moves.append(move)
	
	"""strawdza, czy jest jeszcze jakis mozliwy ruch"""
	if len(rem_moves) == 0:
		return "taken"
	
	next_move = random.choice(rem_moves)
	
	game.g2x += next_move[0]
	game.g2y += next_move[1]
	teleport(game.g2x, game.g2y)
	my_square("yellow")
	game.last_mv = next_move		#zapisuje to jak ostatnio wykonany ruch
	
	
def game_loop():
	"""ruch gracza g1"""
	teleport(game.g1x, game.g1y)		
	if is_free(game.g1x, game.g1y) == "taken":
		game_over("lose")
		return
	my_square("light blue")
	game.taken.append((game.g1x,game.g1y))	#dodanie ruchu do woreczka 'taken'
	#print(game.taken)
	game.g1x += game.dx
	game.g1y += game.dy
	
	"""ruch gracza g2"""
	teleport(game.g2x, game.g2y)	
	game.taken.append((game.g2x,game.g2y))
	if try_move(game.g2x, game.g2y)	== "taken":
		game_over("win")
		return
	else:
		game.taken.append((game.g2x,game.g2y))	#dodanie ruchu do woreczka 'taken'
		#print(f"zajete pola: {game.taken}")	
	
	my_wn.ontimer(game_loop, game.speed)#'on timer' zapewnia ponowne wywolanie game_loop za 200 milisekund


"""GRA"""
the_wall(40)
game_loop()

my_wn.listen()
my_wn.onkeypress(move_up, "Up")
my_wn.onkeypress(move_down, "Down")
my_wn.onkeypress(move_left, "Left")
my_wn.onkeypress(move_right, "Right")

my_wn.delay(0) 

turtle.done()