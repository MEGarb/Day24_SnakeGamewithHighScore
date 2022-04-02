from turtle import Screen
import time
from snake import Snake
import food
import scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


turt = Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()
screen.listen()
screen.onkey(turt.up, "Up")
screen.onkey(turt.down, "Down")
screen.onkey(turt.left, "Left")
screen.onkey(turt.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    turt.move()

    if turt.head.distance(food) < 15:
        scoreboard.increase_score()
        turt.add_segment()
        food.refresh()

    if turt.head.xcor() > 280 or turt.head.xcor() < -280 or turt.head.ycor() > 280 or turt.head.ycor() < -280:
        scoreboard.reset()
        turt.reset()

    for chunk in turt.turt[1:]:
        if turt.head.distance(chunk) < 10:
            scoreboard.reset()
            turt.reset()


screen.exitonclick()
