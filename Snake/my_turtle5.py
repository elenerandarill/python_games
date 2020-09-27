import turtle
import random

my_wn = turtle.Screen()
my_pen = turtle.Turtle()
my_wn.tracer(False)
my_pen.speed(10)
my_wn.delay(0)

class Game():
	
	b_size = 20
	sx = 0
	sy = 0
	dx = 0
	dy = 10
	gx = random.randint(-b_size/2 +1, b_size/2 -1) * 10
	gy = random.randint(-b_size/2 +1, b_size/2 -1) * 10
		
	snake = [(0, 0)]

game = Game()

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
	
def border(size):
	
	bx = -10 * size/2
	by = -10 * size/2
	#rysuje do gory
	for i in range(0, size +1):
		my_square(bx, by, 10, "orange")
		by += 10
	#rysuje w prawo
	for i in range(0, size +1):
		my_square(bx, by, 10, "orange")
		bx += 10
	#rysuje w dol
	for i in range(0, size +1):
		my_square(bx, by, 10, "orange")
		by -= 10
	#rysuje w lewo
	for i in range(0, size +1):
		my_square(bx, by, 10, "orange")
		bx -= 10
	

def my_keypress_L():
	game.dx = -10
	game.dy = 0
	
	
def my_keypress_R():
	game.dx = 10
	game.dy = 0
	

def my_keypress_U():
	game.dy = 10
	game.dx = 0
	
def my_keypress_D():
	game.dy = -10
	game.dx = 0
	

def my_timer():
	
	#ruch
	game.snake.insert(0, (game.snake[0][0] + game.dx, game.snake[0][1] + game.dy))
	game.snake.pop() #ostatni element wylatuje :)
	game.sx += game.dx
	game.sy += game.dy
	
	#sprawdzenie, czy sie zjadam
	if len(game.snake) > 2:
		for e in range (1, len(game.snake)):
			if game.snake[0] == game.snake[e]:
				game_over()
				return 
				
	eat_apple()	
		
	my_pen.clear()
	
	border(game.b_size)
	
	#rysowanie snejka
	for j in range (0, len(game.snake)):
		my_square(game.snake[j][0], game.snake[j][1], 10, "blue")
	
	my_square(game.gx, game.gy, 10, "green") #jabco
		
	#sprawdzenie, czy uderza w border
	if game.snake[0][0] not in range (-5 * game.b_size +1, 5 * game.b_size +1):
		game_over()
		return
	if game.snake[0][1] not in range (-5 * game.b_size +1, 5 * game.b_size +1):
		game_over()
		return	
	
	my_wn.update()
	my_wn.ontimer(my_timer, 200)
	

def respawn_apple():
	game.gx = random.randint(-game.b_size/2 +1, game.b_size/2) * 10
	game.gy = random.randint(-game.b_size/2 +1, game.b_size/2) * 10
	my_square(game.gx, game.gy, 10, "green") #jabco
	#my_wn.ontimer(respawn_apple, 200) #cheat code!

def eat_apple():
	if game.sx == game.gx and game.sy == game.gy:
		respawn_apple()
		grow()
		
def grow():
	game.snake.append(game.snake[-1])

def game_over():
	my_square(game.snake[0][0], game.snake[0][1], 10, "red")
	my_pen.write("Game Over Man")

my_wn.onkeypress(my_keypress_L, "Left")
my_wn.onkeypress(my_keypress_R, "Right")
my_wn.onkeypress(my_keypress_U, "Up")
my_wn.onkeypress(my_keypress_D, "Down")
#my_wn.onkeypress(respawn_apple, "space") #cheat code!

my_wn.listen()

my_square(game.sx, game.sy, 10, "blue")

my_wn.ontimer(my_timer, 500)

turtle.done()
