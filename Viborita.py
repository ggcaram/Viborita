#Importamos turtle para la interfaz grafica y damos los valores por defecto al programa
import turtle
import time
import random

delay = 0.1
puntaje = 0
mayor_puntaje = 0

#Creamos la ventana de inicio
ventana = turtle.Screen()
ventana.title("Viborita")
ventana.bgcolor("black")

#Seteamos ancho y alto de la pantalla de seleccion como algo variable
ventana.setup(width=600, height=600)
ventana.tracer(0)

##Viborita
#Cabeza de la viborita
cabeza = turtle.Turtle()
cabeza.shape("square")
cabeza.color("#174C26")
cabeza.left(50)
cabeza.right(10)
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'Stop'

##Comida
comida = turtle.Turtle()
colores =random.choice(['red','green','yellow'])
formas = random.choice(['square','triangle','circle'])
comida.speed(0)
comida.shape(formas)
comida.color(colores)
comida.penup()
comida.goto(0,100)

##Titulo
titulo = turtle.Turtle()
titulo.speed(0)
titulo.shape("square")
titulo.color("white")
titulo.penup()
titulo.hideturtle()
titulo.goto(0,250)
titulo.write("Puntaje : 0 Puntaje mas alto : 0",align="center",font=("candara",24,"bold"))

##Controles
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

##Direccion sobre el eje
def movimiento():
    if cabeza.direction =="up":
        y= cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction =="down":
        y= cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction =="left":
        x= cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction =="right":
        x= cabeza.xcor()
        cabeza.setx(x+20)

##Teclas
ventana.listen()
ventana.onkeypress(arriba,"w")
ventana.onkeypress(abajo,"s")
ventana.onkeypress(izquierda,"a")
ventana.onkeypress(derecha,"d")
segmentos = []

##Gameplay
while True:
    ventana.update()
    if cabeza.xcor()>290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "Stop"
        colores = random.choice(['red','blue','green'])
        formas = random.choice(['square','circle'])
        for segmento in segmentos:
            segmento.goto(1000,1000)
        segmentos.clear()
        puntaje = 0
        delay = 0.1
        titulo.clear()
        titulo.write("Puntaje : {} Mayor Puntaje : {} ".format(puntaje,mayor_puntaje),align="center",font=("candera",24,"bold"))
    if cabeza.distance(comida) < 20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        comida.goto(x,y)

        #Agragado a la cola de la serpiente
        largo = turtle.Turtle()
        largo.speed(0)
        largo.shape("square")
        largo.color("#045327") #Color de la cola
        largo.left(50)
        largo.right(10)
        largo.penup()
        segmentos.append(largo)
        delay -= 0.001
        puntaje += 10
        #Se guarda el puntaje mayor
        if puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
        titulo.clear()
        titulo.write("Puntaje : {} Mayor Puntaje : {} ".format(puntaje,mayor_puntaje),align="center",font=("candera",24,"bold"))

    #Choques entre la serpiente y su cola
    for index in range(len(segmentos)-1,0,-1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)
    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    movimiento()
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            colores = random.choice(['red','blue','green'])
            formas = random.choice(['square','circle'])
            for segmento in segmentos:
                segmento.goto (1000,1000)
            segmento.clear()

            puntaje = 0
            delay = 0.1
            titulo.clear()
            titulo.write("Puntaje : {} Mayor Puntaje : {} ".format(puntaje,mayor_puntaje),align="center",font=("candera",24,"bold"))
    time.sleep(delay)

ventana.mainloop()


