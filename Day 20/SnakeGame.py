from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import score_board
from game_over import GameOver


screen = Screen()

def main():

    height_and_width = 600
    walls = height_and_width / 2

    screen.setup(width=height_and_width, height=height_and_width)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    speed = Snake()
    score = score_board()
    blue_food = Food()
    game_over = GameOver()
    # new_segment = Turtle(shape="square")
    # new_segment.penup()
    # new_segment.color("white")
    # new_segment.goto(segments[0].pos()[0] - (len(segments) * 20), 0)
    # segments.append(new_segment)


    screen.update()

    screen.listen()
    screen.onkey(speed.up, "Up")
    screen.onkey(speed.down, "Down")
    screen.onkey(speed.left, "Left")
    screen.onkey(speed.right, "Right")

    snake_head = speed.segments[0]



    game_is_on = True
    while game_is_on:
        speed.snake_head = 0
        screen.update()
        time.sleep(0.1)
        speed.move()
        if speed.segments[0].distance(blue_food) < 15:
            speed.extend()
            blue_food.food_eaten()
            score.increase_score()
        if speed.segments[0].xcor() > 280 or speed.segments[0].xcor() < -280 or speed.segments[0].ycor() > 280 or \
                speed.segments[0].ycor() < -280:
            game_is_on = False
            score.clear()
            game_over.game_over(score.score)
        for segment in speed.segments:
            if speed.segments[0] == segment:
                pass
            elif speed.segments[0].distance(segment) < 10:
                game_is_on = False
                score.clear()
                game_over.game_over(score.score)

play = screen.textinput(title="Play", prompt="Do you wanna play the game?").lower()

if play == "yes":
    main()
else:
    print("Okay")

screen.exitonclick()
