from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, X, Y):
        super().__init__()
        # Not to create object from Turtle class. Already inherited, not required below line.
        # self.paddle = Turtle("square")
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(X, Y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




