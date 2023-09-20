import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
is_game_on = True
score = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect if snake ate food
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.new_food()

    if (snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290
            or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290):
        is_game_on = False
        scoreboard.game_over()

    for seg in snake.snakes[1:]:
        if snake.snake_head.distance(seg) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
