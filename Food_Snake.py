from turtle import Turtle
import random
''' This file is used to create the food and place at random positions after every time the sanke eats the food.
This process will be continued until the game is over'''

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.speed(0)
        self.color("blue")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
