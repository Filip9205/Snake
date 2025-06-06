from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        scoreboard.reset()
        snake.reset()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
