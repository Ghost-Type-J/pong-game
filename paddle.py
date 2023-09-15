from turtle import Turtle

MOVE_DISTANCE = 30
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setposition(position)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)