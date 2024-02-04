#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Color
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()
motorB = Motor(Port.B)
motorC = Motor(Port.C)
colorSensor = ColorSensor(Port.S1)

# Write your program here.
diametro_roda = 6.0
distancia_entre_rodas = 13.5


def reto(dist):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = (dist * 360) / (diametro_roda * 3.14)
    while media_motor < graus_motor:
        motorB.run(200)
        motorC.run(200)
        media_motor = (motorB.angle() + motorC.angle()) / 2

def curva(angulo):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = angulo * distancia_entre_rodas / diametro_roda
    while media_motor < graus_motor:
        motorB.run(200)
        motorC.run(-200)
        media_motor = (motorB.angle() - motorC.angle()) / 2
    motorB.hold()
    motorC.hold()

def comando(comand):
    if comand == "W":
        reto(10)
    elif comand == "D":
        curva(90)
    elif comand == "A":
        curva(-90)
    elif comand == "S":
        reto(-10)
    else:
        print("Comando invalido")

def para(stop):
    motorB.hold()
    motorC.hold()


flag = 1
while flag == 1:
    a = colorSensor.color()
    while a == None:
        wait(1000)
        reto(5)
        a = colorSensor.color()
        if a == Color.RED:
            curva(90)
        elif a == Color.YELLOW:
            motorB.hold()
            motorC.hold()
            comando(input())
        elif a == Color.GREEN:
            para(0)
            flag = 0
            break
        else:
            continue
