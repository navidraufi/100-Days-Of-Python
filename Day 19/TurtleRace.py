from turtle import Turtle, Screen
import random


def random_pace():
    pace = random.randint(1, 10)

    return pace


screen = Screen()

screen.setup(width=500, height=400)

ENDING_POSITION = 225


def line_drawer():
    draw_the_line = Turtle()
    draw_the_line.hideturtle()
    draw_the_line.color("black")
    draw_the_line.pensize(10)
    draw_the_line.penup()
    draw_the_line.goto(ENDING_POSITION + 10, -200)
    draw_the_line.pendown()
    draw_the_line.goto(ENDING_POSITION + 10, 200)


def create_turtle(name_turtle, color, y_axis):
    name_turtle = Turtle("square")
    name_turtle.color(color)
    name_turtle.penup()
    name_turtle.goto(-235, y_axis)

    return name_turtle


line_drawer()

red = create_turtle("red", "red", 0)
blue = create_turtle("blue", "blue", -25)
purple = create_turtle("purple", "purple", -50)
yellow = create_turtle("yellow", "yellow", -75)
black = create_turtle("black", "black", 25)
cyan = create_turtle("cyan", "cyan", 50)
teal = create_turtle("teal", "teal", 75)


def run_turtle(name):
    name.forward(random_pace())


def calculate_position(name_of_turtle):
    if name_of_turtle.pos()[0] >= ENDING_POSITION:
        return True
    else:
        return False


winner = ""
is_on = True
user_bet = screen.textinput(title="User bet.", prompt="Who do you bet on? colors only.").lower()

while is_on:
    run_turtle(blue)
    run_turtle(black)
    run_turtle(yellow)
    run_turtle(cyan)
    run_turtle(teal)
    run_turtle(purple)
    run_turtle(red)
    if calculate_position(red):
        winner = "red"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break
    elif calculate_position(blue):
        winner = "blue"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break
    elif calculate_position(cyan):
        winner = "cyan"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break
    elif calculate_position(teal):
        winner = "teal"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break
    elif calculate_position(black):
        winner = "black"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break
    elif calculate_position(purple):
        winner = "purple"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break
    elif calculate_position(yellow):
        winner = "yellow"
        if winner == user_bet:
            print(f"You win!\n{winner.title()} is the winner.")
        else:
            print(f"You lose!\n{winner.title()} is the winner.")
        break

screen.exitonclick()
