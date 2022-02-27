import tkinter as tk
import turtle
from datetime import datetime
from math import sin
from time import time, sleep
from random import seed
import random

random.seed(datetime.now())

def average(n1,n2):
    return int((n1 + n2)/2)

def blendCols(col1: str, col2: str):
    r1 = int(col1[1:3],16)
    g1 = int(col1[3:5],16)
    b1 = int(col1[5:7],16)
    r2 = int(col2[1:3],16)
    g2 = int(col2[3:5],16)
    b2 = int(col2[5:7],16)
    return "#" + str(hex(average(r1,r2))[2:]).zfill(2) + str(hex(average(g1,g2))[2:]).zfill(2) + str(hex(average(b1,b2))[2:]).zfill(2)


class Planta:
    def __init__(self, axiom, rulesP):
        self.axiom = axiom
        self.sentence = axiom
        self.rules = rulesP
        self.angle = 25;
        self.distance = 150
        self.initialDistance = 150
        r = lambda: random.randint(0, 255)
        self.color = ('#%02X%02X%02X' % (r(), r(), r()))

    def iter(self):                                                                     #Iteracion siguiendo las reglas en self.rules
        sentenceTemp = list(self.sentence)
        i = 0
        while i < len(sentenceTemp):
            aCambiar = str(sentenceTemp[i])
            reglas = self.rules.get(aCambiar,[aCambiar])                                #Si no tiene una regla asignada, no hacer nada
            tamanioRegla = len(reglas)
            if tamanioRegla >= 1:
                indiceAleatorio = random.randint(0,tamanioRegla-1)
                sentenceTemp[i] = (self.rules.get(aCambiar, aCambiar)[indiceAleatorio])

            i += 1
        self.sentence = "".join(sentenceTemp)
        self.distance *= 0.5

    def reset(self):                                                                    #Devuelve la planta a su estado inicial
        self.sentence = self.axiom
        self.distance = self.initialDistance

    def grow(self, n : int):                                                            #desarrolla la planta con N iteraciones
        for x in range(0,n):
            self.iter()

    def print(self):
        print(self.sentence)

c = turtle.Screen()
t = turtle.RawTurtle(c)
t.hideturtle()
t.speed(0)
c.tracer(0,0)
t.penup()   # Regarding one of the comments
t.pendown() # Regarding one of the comments

def fusion(father : Planta, mother : Planta):
    axiom = father.axiom

    rules = {}
    for k in father.rules.keys():
           rules[k] = father.rules[k]

    for k in mother.rules.keys():
        if (not rules.get(k)):
            rules[k] = mother.rules[k]
        else:
            rules[k] = rules[k] + mother.rules[k]

    for k in rules.keys():
        random.shuffle(rules[k])
        rules[k] = rules[k][:int(len(rules[k])/2)]

    p = Planta(axiom,rules)
    p.color = blendCols(father.color,mother.color)

    return p

def draw(plant: Planta, x, y):
    t.penup()
    t.setheading(90 - sin(time())*2)
    t.setpos((x,y))
    t.pendown()
    stack = []
    h = 1

    for char in plant.sentence:
        if char == "F":
            t.pencolor("#095e16")
            t.forward(plant.distance)
            h += 1
        elif char == "+":
            t.right(plant.angle + sin(time()+h*2)*2*sin(h))
        elif char == "-":
            t.left(plant.angle - sin(time()+h*2)*2*sin(h))
        elif char == "[":
            stack.append(t.position())
            stack.append(t.heading())
            stack.append(h)
        elif char == "]":
            t.penup()
            h = stack.pop()
            t.setheading(stack.pop())
            t.setpos(stack.pop())
            t.pendown()
        elif char == ".":
            t.pencolor(plant.color)
            t.fillcolor(plant.color)
            t.begin_fill()
            t.circle(plant.distance/2)
            t.end_fill()

def onClick(x,y):
    p1.reset()
    p1.grow(5)
    p2.reset()
    p2.grow(5)
    p3.reset()
    p3.grow(5)


rules1 = {}
rules1["F"] = ["FF"]
rules1["X"] = ["AF-[[X]+X]+F[<+F>X]-X","BF-[[<X]+>X]+F[+FX]X","CF[[X]+>X<]-X","DF-[X+[>X]][+X]-X","EF[X]+F[+>X.]-X"]
p1 = Planta("X",rules1) #i did this a long time ago and i think < and > are just from a copy-paste and are ignored
p1.grow(5)



rules2 = {}
rules2["B"] = [ "F[--FFFB][-FFFB]FB","FFB"]
rules2["X"] = ["XFB[+FXF][++FXF]"]
rules2["."] = ["."]
p2 = Planta("X",rules2)
p2.grow(5)

p3 = fusion(p1,p2)
p3.grow(5)

print(p3.sentence)

onClick(0,0)

c.onscreenclick(onClick)

while True:
    t.clear()
    draw(p1,-300,0)
    draw(p2,300,0)
    draw(p3,0,-200)
    c.update()
    sleep(0.01)

