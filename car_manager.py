from turtle import Turtle
from player import Player
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    cars = []

    def __init__(self):
        for x in range(0, 25):
            car = Turtle()
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(random.randint(-340, 340), random.randint(-250, 250))
            self.cars.append(car)
            self.move_by = MOVE_INCREMENT

    def update(self):
        for car in self.cars:
            car.forward(self.move_by)
            if car.xcor() < -340:
                car.goto(340, random.randint(-260, 260))

    def collision(self, player):
        for car in self.cars:
            if car.distance(player) < 22 and 30 > (car.ycor() - player.ycor()) > -30:

                return True
        return False

    def level_up(self):
        self.move_by *= 1.2
