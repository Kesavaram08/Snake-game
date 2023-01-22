from turtle import Turtle
import random
DISTANCE = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
colors = ["blue", "red", "yellow", "green", "pink", "orange", "brown", "white", "violet", "Lime", "Cyan", "Navy blue"]


class Snake:

    def __init__(self):
        self.new_segment = []
        self.create_snake()
        self.head = self.new_segment[0]

    def create_snake(self):
        for position in DISTANCE:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape="circle")
        turtle.color(random.choice(colors))
        turtle.penup()
        turtle.goto(position)
        self.new_segment.append(turtle)

    def extend(self):
        self.add_segment(self.new_segment[-1].position())

    def reset(self):
        for seg in self.new_segment:
            seg.goto(1000, 1000)
        self.new_segment.clear()
        self.create_snake()
        self.head = self.new_segment[0]

    def move(self):
        for seg in range(len(self.new_segment) - 1, 0, -1):
            x = self.new_segment[seg - 1].xcor()
            y = self.new_segment[seg - 1].ycor()
            self.new_segment[seg].goto(x, y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
