from turtle import Turtle, Screen
import random



is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title='Make your bet', prompt='Who do you think is gonna Win! ')

colors = ['red', 'green', 'blue', 'yellow', 'pink']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if choice:
    is_race_on = True
'''We use while loop so it keeps generating random forward steps'''
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == choice:
                print(f'You have won! {wining_color} won the race!')
            else:
                print(f'You have lost! {wining_color} won the race!')
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()