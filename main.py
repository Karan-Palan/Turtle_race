from turtle import Turtle, Screen
import random

is_race_on = False
can_play = True
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
colors_remove = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)  # use positional arguments

number_players = int(screen.textinput(title="players", prompt="how many people want to play"))
if number_players < 1 or number_players > 6:
    can_play = False
else:
    can_play = True

while can_play == False:
    number_players = int(screen.textinput(title="players", prompt="how many people want to play"))
    if number_players < 1 or number_players > 6:
        can_play = False
    else:
        can_play = True

guess_list = []
for i in range(number_players):
    player_bet = screen.textinput(title="make a bet", prompt="pick what colour of turtle you think will win the race")
    if player_bet in colors_remove:
        guess_list.append(player_bet)
        colors_remove.remove(player_bet)
    else:
        while player_bet not in colors_remove:
            player_bet = screen.textinput(title="error",
                                          prompt="pick a valid option")
        guess_list.append(player_bet)
        colors_remove.remove(player_bet)

x_cor = -230
y_cor = -100
turtle_list = []

for turtle_index in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x_cor, y_cor)
    y_cor += 50
    turtle_list.append(tim)

if player_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour in guess_list:
                print(f"player: {guess_list.index(winning_colour) + 1} won, with {winning_colour} turtle")
                break
            else:
                print(f"no one won, {winning_colour} turtle won")
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()