# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:22:38 2020

@author: omarg
"""
import turtle 
import random 
import math 

# Algoritmo para generar n cantidad de paredes.En este caso las paredes representan objetos reales que tiene que detectar la protesis
def pared_aleatoria (a, b):
    #xi, yi, determinan la posicion de las paredes con respecto a un plano. e
    xi = random.uniform(a, b)
    yi = random.uniform(a, b)
    # ang = angulo de la recta. 
    ang = random.uniform(-math.pi, math.pi) # Math.pi = los radianes de un circulo
    # Despues voy a determinar la longitud aleatoria de los segmentos, teniendo un rango que va de 100 a 200
    long = random.uniform(100, 200)
    # xf, yf, es la posicion final de la recta con respecto a cierta long y una pendiente ang. 
    xf = xi + long * math.cos(ang)
    yf = yi + long * math.sin(ang)
    # Se regresa una linea mediante la generacion del doble conjunto entre ((xi, yi con xf, yf))
    return ((xi, yi), (xf, yf))

def goto(p):
    turtle.up()
    turtle.goto(p)
    turtle.down()
    
def linea(p):
    turtle.down()
    turtle.goto(p)
    turtle.up()
    
# Se genera un bucle de 20 paredes aleatorias, y se le asigna un valor de -200, 200 (a, b)
paredes = [pared_aleatoria(-400, 400) for i in range(20)]
    
#Dibujamos las paredes
for pared in paredes:
    pi, pf = pared # pi, pf = puntos del  segmento
    goto(pi) 
    linea(pf)
    
goto((0, 0)) #La tortuga regresa la origen. 

#Algoritmo que genera el sendor, en este caso el sensor opera con la distancia entre dos segmentos, uno siendo el campo de vision del sensor, 
# y el otro la pared, la interseccion se puede dar en multiples puntos del segemento, puede que se de en el punto A (a, b) o en el punto B (c,d)
# Si la interseccion de de en el punto A, t = 0, y si se da en el punto B, t =1, (t es dada por la formula p = a + (b-1) * t), si t es menor a 0,
# entonces no existe interseccion, y lo mismo aplica si t es mayor a 1, es importante recalcar que por ejemplo si t = 0.5, entones la interseccion 
# esta en la mitad del segmento.

def sensor(A, B):
    a,b = A #RECORDEMOS, que A es el conjunto de las cordenadas ax, ay, bx y by de un segmento, y en el caso de B es lo mismo. 
    c, d = B 
    # Descomponenmos las cordenadas a,b,c y d
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d
    
    #Determinamos la longitud del segmento A (Sensor)
    L = ((bx - ax) ** 2 + (by - ay)** 2)**0.5
    alpha_1 = bx - ax
    alpha_2 = by - ay
    alpha_3 = dx - cx
    alpha_4 = dy - cy
    beta_1 = cx - ax
    beta_2 = cy - ay
    
    #Se calcula el determinate
    d = alpha_1 *  alpha_4 - alpha_2 * alpha_3
    # Con el fin de facilitar aritmeticamente la obtencion de t (S en el caso de B), si d = 0, se regresa el doble de L. 
    if d == 0:
        return 2 * L
    
    t = (alpha_4 * beta_1 - alpha_3 * beta_2)/ d
    s = (-alpha_2 * beta_1 - alpha_1 * beta_2)/ d
    if t < 0 or t > 1 or s <0 or s> 1:
        return 2 * L
    return L * t
    
    
#Este algoritmo se encarga de generar el movimiento de los objetos. 
turtle.color("red")

while True:
    
    R = 90 #Longitud maxima del sensor
    x, y = turtle.position()
    ang = turtle.heading() * math.pi / 180.
    
    # Lo que viene es usado para calcular el punto final del sensor.
    xp = x + R * math.cos(ang)
    yp = y + R * math.sin(ang)
    
    #Finalmente construimos el segmento del sensor.
    A = ((x, y), (xp, yp))
    # El campo de vision del sensor es equivalente a 2 veces R, es decir todo lo que se encuentre mas alejado de 2R, no va a ser detectado.
    cv = 2 * R
    
    for pared in paredes:
        dp = sensor(A, pared) #dp = distancia de la pared
        if dp < cv:
            cv = dp
            
    #Fijamos los limites de distancia entre las paredes y la tortuga
    if cv < 10:
        turtle.left(5)
        continue #No permite la ejecucion del movimiento aleatorrio. 
    
    
    m = random.choice(["FORWARD", "TURN_LEFT", "TURN_RIGHT"])
    if m == "FORWARD":
        turtle.forward(10)
    elif m == "TUR_LEFT":
        turtle.left(20)
    elif m == "TURN_RIGHT":
        turtle.right(20)