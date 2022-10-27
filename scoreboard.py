from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write('Level : ' + str(self.score), align='center', font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write('Game over!', align='center', font=FONT)
