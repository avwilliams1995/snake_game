from turtle import Turtle, Screen
import turtle
from snake import Snake
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
score = 0
snake = Snake()
first = snake.first


game_on = True
while game_on:
    screen.update() 
    time.sleep(.1)
    snake.move()
    
    

    
        
        

    
















screen.exitonclick()

