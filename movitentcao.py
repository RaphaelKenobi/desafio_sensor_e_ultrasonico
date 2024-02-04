#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Função para fazer o robô se mover para frente por um determinado período de tempo
def mover_para_frente(tempo, velocidade=200):
    wait(2000)
    motor_esquerdo.run(speed=velocidade)
    motor_direito.run(speed=velocidade)
    wait(tempo)

# Função para fazer o robô fazer uma curva para a direita
def curva_direita():
    motor_esquerdo.run(speed=200)
    motor_direito.run(speed=-200)
    wait(3000)

# Função para fazer o robô fazer uma curva para a esquerda
def curva_esquerda():
    motor_esquerdo.run(speed=-200)
    motor_direito.run(speed=200)
    wait(3000)


# Criar o objeto EV3Brick e motores
ev3 = EV3Brick()
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

# Loop principal
while True:

    for i in range(2):
        mover_para_frente(3000)
        curva_direita()
        mover_para_frente(3000)
        curva_esquerda()

