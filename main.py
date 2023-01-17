from turtle import Turtle, Screen
import random


def turtle_race():
    is_race_on = False
    s = Screen()
    s.setup(width=500, height=400)
    user_bet = s.textinput(title="MAKE A BET", prompt="Which turtle will win the race? Enter a color: ").lower()
    colors = ["red", "green", "blue", "yellow", "orange"]
    y_co_ordinates = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    for i in range(5):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(colors[i])
        t.goto(x=-230, y=y_co_ordinates[i])
        all_turtles.append(t)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                win_color = turtle.pencolor()
                is_race_on = False
                if win_color == user_bet:
                    print(f"You've Won! {win_color} Turtle is the Winner.")
                else:
                    print(f"You've Lost! {user_bet} Turtle is not the Winner.")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    s.exitonclick()


turtle_race()
