from turtle import Turtle
import random
colors = ["red", "yellow", "green", "pink", "orange", "brown", "white", "violet", "Lime", "Cyan", "Navy blue"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")

    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)
        self.color(random.choice(colors))

