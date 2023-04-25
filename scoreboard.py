from turtle import Turtle

score = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'Score {self.score}', move=False, align='left', font=('Arial', 12, 'normal'))

    def increase(self):
        self.score += 10
        self.clear()
        self.update()

    def gameover(self):
        self.goto(-40, 0)
        self.write(f'Game Over your score is: {self.score}', move=False, align='left', font=('Arial', 12, 'normal'))
