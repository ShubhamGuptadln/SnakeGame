from turtle import Turtle

MOVING_POINT = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []

        self.create()

    def create(self):
        for point in MOVING_POINT:
            self.add_segment(point)

    def add_segment(self, point):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(point)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
