import turtle
import time
import random

delay = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")

serpente = turtle.Turtle()
serpente.speed(1)
serpente.shape("square")
serpente.penup()
serpente.goto(0,0)
serpente.direction = "stop"
serpente.color("green")

def cima():
    serpente.direction = "up"

def baixo():
    serpente.direction = "down"

def esquerda():
    serpente.direction = "left"

def direita():
    serpente.direction = "right"    

s.listen()
s.onkeypress(cima,"Up")
s.onkeypress(baixo,"Down")
s.onkeypress(esquerda,"Left")
s.onkeypress(direita,"Right")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

corpo = []
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write(f"MARCADOR: {marcador}\tMARCADOR MAIS ALTO: {marcador_alto}",align="center",font=("verdana",24,"normal"))

def movimento():
    if serpente.direction == "up":
        y = serpente.ycor()
        serpente.sety(y+20)
    if serpente.direction == "down":
        y = serpente.ycor()
        serpente.sety(y-20)
    if serpente.direction == "right":
        x = serpente.xcor()
        serpente.setx(x+20)
    if serpente.direction == "left":
        x = serpente.xcor()
        serpente.setx(x-20)

while True:
    s.update()

    if serpente.xcor() > 300 or serpente.xcor() < -300 or serpente.ycor() > 300 or serpente.ycor() < -300:
        time.sleep(2)
        for i in corpo:
            i.clear()
            i.hideturtle()
        serpente.home()
        serpente.direction = "stop"
        corpo.clear()
        marcador = 0
        texto.clear()
        texto.write(f"MARCADOR: {marcador}\tMARCADOR MAIS ALTO: {marcador_alto}",align="center",font=("verdana",24,"normal"))

    if serpente.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)

        novo_corpo = turtle.Turtle()
        novo_corpo.shape("square")
        novo_corpo.color("green")
        novo_corpo.penup()
        novo_corpo.goto(0,0)
        novo_corpo.speed(0)
        corpo.append(novo_corpo)

        marcador+=10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write(f"MARCADOR: {marcador}\tMARCADOR MAIS ALTO: {marcador_alto}",align="center",font=("verdana",24,"normal"))


    total = len(corpo)
    for i in range(total -1,0,-1):
        x = corpo[i-1].xcor()
        y = corpo[i-1].ycor()
        corpo[i].goto(x,y)

    if total > 0:
        x = serpente.xcor()
        y = serpente.ycor()
        corpo[0].goto(x,y)

    movimento()

    for i in corpo:
        if i.distance(serpente) < 20:
            for i in corpo:
                i.clear()
                i.hideturtle()
            serpente.home()
            corpo.clear()
            serpente.direction = "stop"

    time.sleep(delay)
