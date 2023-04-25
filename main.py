from turtle import Screen
from snake import Snake
import time
from Food_Snake import Food
from scoreboard import Score

score = 0

snake = Snake()

s = Screen()
food = Food()
sc = Score()

s.setup(600, 600)
s.bgcolor('black')
s.title("My Snake Game")
s.tracer(0)

s.listen()
s.onkey(snake.up, key="Up")
s.onkey(snake.down, key="Down")
s.onkey(snake.right, key="Right")
s.onkey(snake.left, key="Left")

game_is_on = True
while game_is_on:
    snake.move()
    s.update()
    time.sleep(0.1)
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        sc.increase()
        snake.extend()
    if snake.segments[0].xcor() >= 280 or snake.segments[0].xcor() <= -280 or snake.segments[0].ycor() >= 280 or \
            snake.segments[0].ycor() <= -280:
        game_is_on = False
        sc.gameover()

    for seg in snake.segments:
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10:
            game_is_on = False
            sc.gameover()

s.exitonclick()
