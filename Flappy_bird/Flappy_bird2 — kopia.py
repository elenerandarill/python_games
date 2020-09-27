import turtle
import random
import time

my_wn = turtle.Screen()
my_pen = turtle.Turtle()	#my turtle
my_pen.speed(0)
my_wn.bgcolor("light blue")
my_wn.tracer(0, 10)

class Game():
	bird_x = -200
	bird_y = 0
	
	#'x' dla pozycji rur
	"""px = -350
	py = 400
	ph = 350"""
	pos_lst = [-400, 400]
	pipes_all = []
	
		
	t = time.time_ns()
	#print(t)
	fps = 60
	speed = 0
	px_delta = 3
	
class Pipe():
	x: int
	y: int
	h: int

	def __init__(self, x, y, h):
		self.x = x
		self.y = y
		self.h = h


def draw_pipe(x,y,h):	#rysuje rure	
	teleport(x,y)
	my_pen.color("green", "lime")
	my_pen.begin_fill()
	for i in range (0, 2):
		if y < 0:
			my_pen.forward(50)
			my_pen.left(90)
			my_pen.forward(h)
			my_pen.left(90)
		else:
			my_pen.forward(50)
			my_pen.right(90)
			my_pen.forward(h)
			my_pen.right(90)
	my_pen.end_fill()
	

def teleport(x,y):
	my_pen.up()
	my_pen.goto(x,y)
	my_pen.down()

def my_bird():
	my_pen.pensize(5)
	my_pen.color("orange", "yellow")
	my_pen.begin_fill()
	my_pen.circle(20)
	my_pen.end_fill()

	my_pen.color("blue")
	#my_pen.circle(30)

	
def speed_up():
	game.speed = 150
	#print("speed up")

	
def speed_down():
	game.speed = -30
	#print("speed down")

def game_over():
	teleport(0, 0)
	my_pen.color("red")
	my_pen.write("Game Over", align = "center", font = ("Arial", 12, "bold"))

"""tworzy Rure"""
def create_pipe():
	x = 350
	y = random.choice(game.pos_lst)
	h = random.randint(50, 350)
	pipe = Pipe(x, y, h)
	game.pipes_all.append(pipe)	#dodaje rure do listy
	my_wn.ontimer(create_pipe, 500)

	
def game_loop():
		
	now_t = time.time_ns()
	dif_t = now_t - game.t
	game.t = now_t
	dif_ts = dif_t / 1000000000
	if dif_ts > 1:
		dif_ts = 1
	#print(f"diff: {dif_ts} sec")
	
	delta_speed = 9.8 * dif_ts *20
	game.speed -= delta_speed
	#print(f"game.speed: {game.speed}")
	
	dist = game.speed * dif_ts #przesuniecie pionowe ptaszka
	
	my_pen.clear()
	
	"""rury"""
	for pipe in game.pipes_all:
		draw_pipe(pipe.x, pipe.y, pipe.h)	#rysuje rure
		pipe.x -= game.px_delta	#zmieniam 'x' dla rury
	
	'''bird'''
	game.bird_y += dist
	teleport(game.bird_x, game.bird_y)
	my_bird()
	if game.bird_y > 360 or game.bird_y < -400:
		game_over()
		return

	for pipe in game.pipes_all:
		if pipe.x < -400:
			game.pipes_all.remove(pipe)
	
	
	my_wn.ontimer(game_loop, int(1000 / game.fps))		
	
	
""""""
game = Game()


my_wn.ontimer(create_pipe, 300)
teleport(game.bird_x, game.bird_y)
my_bird()


my_wn.ontimer(game_loop, 100)



my_wn.listen()
my_wn.onkeypress(speed_up, "Up")
my_wn.onkeypress(speed_down, "Down")


my_wn.delay(0) 
turtle.done()