from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.restart()
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.setpos(STARTING_POSITION)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.restart()
            return True
