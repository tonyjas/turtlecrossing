import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


def level_up():
    player.reset()
    car_manager.level_up()
    scoreboard.increment()


screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.update()
    screen.update()
    if car_manager.collision(player):
        game_is_on = False

    if player.ycor() > 280:
        level_up()

scoreboard.game_over()

screen.exitonclick()
