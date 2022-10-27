import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.new_car()
        self.new_car()
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle('square')
        new_car.hideturtle()
        new_car.penup()
        new_car.goto(280, random.randint(-250, 250))
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.showturtle()
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.setx(car.xcor() - self.speed)

    def restart(self):
        for car in self.cars:
            car.setx(-320)
        self.cars = []
        self.speed = self.speed + MOVE_INCREMENT

    def spawn(self):
        randomizer = random.randint(1, 6)
        if 1 == randomizer:
            self.new_car()

