import random
import turtle
import time
from random import randint

written = 0
game_over=False

def draw_random():
    x=random.randint(-window_width,window_width)
    y=random.randint(-window_height, window_height)
    turtle_instance.goto(x,y)


def create_turtle():
    if not game_over:
        while True:
            draw_random()
            time.sleep(0.5)

def click(x, y):
    global written
    print(x,y)
    written += 1
    score.clear()
    score.write(f"Score: {written}",align="center",font=("Verdana",15,"normal"))

def countdown(time):
    global game_over
    window.onclick(None)  # disable click until countdown completes
    timerTurtle.clear()

    if time > 0:
        timerTurtle.clear()
        timerTurtle.write(f"Time: {time}", align='center',font=("Verdana",15,"normal"))
        window.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over=True
        timerTurtle.clear()
        turtle_instance.hideturtle()
        timerTurtle.write("Game Over!", align='center',font=("Verdana",15,"normal"))



#game screen
window = turtle.Screen()
window.title("Catch The Turtle")
window.bgcolor("Light Blue")
window.setup(width=600,height=600)
window.onclick(lambda x, y: countdown(20))

#timer turtle
timerTurtle = turtle.Turtle()
timerTurtle.hideturtle()
timerTurtle.penup()
timerTurtle.color("Red")
top_height=window.window_height() / 2
y=top_height *0.9
timerTurtle.setpos(+100,y)
timerTurtle.write("Click Screen", align='center',font=("Verdana",15,"normal"))


#green turtle
turtle_instance=turtle.Turtle()
turtle_instance.shape('turtle')
turtle_instance.color('dark green')
turtle_instance.shapesize(1.5)
turtle_instance.penup()
turtle_instance.onclick(click)


#score turtle
score = turtle.Turtle()
score.hideturtle()
score.penup()
top_height=window.window_height() / 2
y=top_height *0.9
score.setpos(-100,y)
score.color("Purple")
score.write(f"Score: {written}", align="center",font=("Verdana",15,"normal"))


# Ekran boyutlarını al
window_width = window.window_width() // 2
window_height = window.window_height() // 2


create_turtle()

window.mainloop()