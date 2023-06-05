from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# Animation turn off
screen.tracer(0)

# Centre of Paddle @350, in range (340,360)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Now while loop created to update screen after creating paddle.
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection of ball collision with wall. And bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # When ball goes out of bounds.
    # For r_paddle.
    if ball.xcor() > 380:
        # ball reset to (0,0)
        ball.out_bound()
        # ball move towards other player
        ball.bounce_x()
        scoreboard.r_point()


    # For l_paddle.
    if ball.xcor() < -380:
        # ball reset to (0,0)
        ball.out_bound()
        # ball move towards other player
        ball.bounce_x()
        scoreboard.l_point()




screen.exitonclick()