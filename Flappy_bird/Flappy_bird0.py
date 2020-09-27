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
	
	t = time.time_ns()
	#print(t)
	fps = 60
	speed = 0
	


def teleport(x,y):
	my_pen.up()
	my_pen.goto(x,y)
	my_pen.down()

def my_bird():
	my_pen.color("red","orange")
	my_pen.begin_fill()
	my_pen.circle(10)
	my_pen.end_fill()
	
def speed_up():
	game.speed = 150
	#print("speed up")

	
def speed_down():
	game.speed = -30
	#print("speed down")

	
def game_loop():
	
	now_t = time.time_ns()
	dif_t = now_t - game.t
	game.t = now_t
	dif_ts = dif_t / 1000000000
	#print(f"diff: {dif_ts} sec")
	
	delta_speed = 9.8 * dif_ts *20
	game.speed -= delta_speed
	print(f"game.speed: {game.speed}")
	
	dist = game.speed * dif_ts #przesuniecie pionowe ptaszka
	
	my_pen.clear()
	game.bird_y += dist
	teleport(game.bird_x, game.bird_y)
	my_bird()
	
	
	my_wn.ontimer(game_loop, int(1000 / game.fps))		
	
	
""""""
game = Game()

my_pen.up()
my_pen.goto(game.bird_x, game.bird_y)
my_pen.down()
my_bird()

my_wn.ontimer(game_loop, 100)



my_wn.listen()
my_wn.onkeypress(speed_up, "Up")
my_wn.onkeypress(speed_down, "Down")


my_wn.delay(0) 
turtle.done()