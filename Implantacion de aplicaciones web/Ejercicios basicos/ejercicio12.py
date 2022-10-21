#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos.

import math

x1=float(input('Introduce x1: '))
y1=float(input('Introduce y1: '))
x2=float(input('Introduce x2: '))
y2=float(input('Introduce y2: '))

distancia=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

print('La distancia entre los puntos es de:', float(round(distancia,2)))
