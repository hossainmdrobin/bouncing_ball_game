import turtle
import random
import winsound


wn = turtle.Screen()
wn.title("bouncing ball game by @jardary")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
tiles1 = []
tiles2 = []
tiles3 = []

player = turtle.Turtle()
player.speed(0)
player.color("gray")
player.penup()
player.shape("square")
player.goto(0, -260)
player.shapesize(stretch_wid=1, stretch_len=5)

ball = turtle.Turtle()
ball.speed(0)
ball.color("yellow")
ball.penup()
ball.shape("circle")
ball.goto(0, -240)
ball.dx = 0.4
ball.dy = 0.4

tilesholder = [tiles1, tiles2, tiles3]

for tiles in tilesholder:
    for i in range(10):
        tiles.append(turtle.Turtle())

posx = -16
posy = 150
for tiles in tilesholder:
    posx = -16
    for tile in tiles:
        tile.speed(0)
        tile.color("red")
        tile.penup()
        tile.shape("square")
        tile.setpos(posx * 10, posy)
        posx += 3
    posy += 50
        
def player_right():
    player.setx(player.xcor() + 30)

def player_left():
    player.setx(player.xcor() - 30)

def ball_go():
    ball.goto(0, -240)
  
    

wn.listen()
wn.onkey(player_right, "Right")
wn.onkey(player_left, "Left")
wn.onkey(ball_go, "space")
     
  
        
        


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
     
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx = ball.dx * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball. xcor() < -390:
        ball.setx(-390)
        ball.dx = ball.dx * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.goto(0, -240)

        
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < player.xcor() + 60 and ball.xcor() > player.xcor() - 60):
        ball.sety(-240)
        ball.dy = ball.dy * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    
        
    
        
    for tiles in tilesholder:
        for tile in tiles:
            if tile.isvisible():
                if (ball.xcor() > tile.xcor() - 20 and ball.xcor() < tile.xcor() + 20) and (ball.ycor() < tile.ycor() + 20 and ball.ycor() > tile.ycor() - 20):
                    tile.hideturtle()
                    ball.dx = ball.dx * -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    
