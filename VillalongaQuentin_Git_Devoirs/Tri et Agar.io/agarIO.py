import turtle
import random
import math

maTortue = turtle.Turtle()
maFenetre = turtle.Screen()

maFenetre.colormode(255)
maTortue.shape("circle")
maTortue.speed(0)
turtle.delay(0)
turtle.listen()

#Dessin d'un cercle
"""
for i in range(360):
    maTortue.forward(1)
    maTortue.left(1)
    maFenetre.update()
"""

#Dessin d'un carré
"""
for i in range(4):
    maTortue.forward(10)
    maTortue.left(90)
    maFenetre.update()
"""

#Dessin d'un carré escargot
"""
distance = 5
for i in range(100):
    maTortue.forward(distance)
    maTortue.left(90)
    distance += 3
"""

#Dessin d'un rond escargot
"""
for i in range(36000):
    maTortue.forward(i/1000)
    maTortue.left(1)
"""

def goUp():
    maTortue.setheading(90)
    #maTortue.forward(playerSpeed)

def goLeft():
    maTortue.setheading(180)
    #maTortue.forward(playerSpeed)

def goDown():
    maTortue.setheading(270)
    #maTortue.forward(playerSpeed)

def goRight():
    maTortue.setheading(0)
    #maTortue.forward(playerSpeed)

turtle.onkeypress(goUp,"Up")
turtle.onkeypress(goLeft,"Left")
turtle.onkeypress(goDown,"Down")
turtle.onkeypress(goRight,"Right")


#Fonction distance
def distance(A, B):
    return(math.sqrt((float(A[0]) - float(B[0]))**2 + (float(A[1]) - float(B[1]))**2))

#Dessin d'une marche aléatoire
pas = 3
nbDeTortues = 15
startingSquareWidth = 300
listeDeTortues = []
facteurDeTaille = 12.0
playerSpeed = 5

for i in range(nbDeTortues):
    tempTortue = turtle.Turtle()
    tempTortue.shape('circle')

    #Initialisation à une couleur aléatoire
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tempTortue.color((R, G, B))

    #Initialisation à une position aléatoire
    posX = random.random() * startingSquareWidth - startingSquareWidth//2
    posY = random.random() * startingSquareWidth - startingSquareWidth//2
    tempTortue.penup()
    tempTortue.setpos(posX, posY)
    tempTortue.pendown()
    tempTortue.speed(10)

    listeDeTortues.append(tempTortue)

while 1:
    
    for k in listeDeTortues:
        k.forward(pas)

        facteurAleatoire = random.randint(0, 2)
        if facteurAleatoire == 0:
            k.left(90)
        elif facteurAleatoire == 1:
            k.right(90)
        else:
            pass

    maTortue.forward(playerSpeed)

    for k in listeDeTortues:
        for l in listeDeTortues:
            if (k.isvisible() and l.isvisible() and k != l and distance(k.position(), l.position()) <= facteurDeTaille * max(k.shapesize()[0], l.shapesize()[0])):
                #Si les conditions sont remplies, il y a phagocytose
                if (k.shapesize()[0] >= l.shapesize()[0]):
                    k.speed(k.speed() - 2)
                    k.shapesize(k.shapesize()[0] * 1.5, k.shapesize()[1]* 1.5)
                    l.hideturtle()
                    l.penup()
                else:
                    l.speed(l.speed() - 2)
                    l.shapesize(l.shapesize()[0]* 1.5, l.shapesize()[1]* 1.5)
                    k.hideturtle()
                    k.penup()
        
        if (k.isvisible() and maTortue.isvisible() and k != maTortue and distance(k.position(), maTortue.position()) <= facteurDeTaille * max(k.shapesize()[0], maTortue.shapesize()[0])):
                #Si les conditions sont remplies, il y a phagocytose
                if (k.shapesize()[0] > maTortue.shapesize()[0]):
                    k.shapesize(k.shapesize()[0] * 1.5, k.shapesize()[1]* 1.5)
                    maTortue.hideturtle()
                    maTortue.penup()
                else:
                    maTortue.speed(maTortue.speed() - 2)
                    playerSpeed /= 1.8
                    maTortue.shapesize(maTortue.shapesize()[0]* 1.5, maTortue.shapesize()[1]* 1.5)
                    k.hideturtle()
                    k.penup()
        

#Fin du programme
input()