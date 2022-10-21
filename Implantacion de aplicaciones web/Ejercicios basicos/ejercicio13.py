#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se
#puede calcular?

import math

numero=float(input('Introduce un numero: '))

raiz2=math.sqrt(numero)
raiz3=numero**(1/3)
print('La raiz cuadrada es: ', float(round(raiz2,2)), ' y la raiz cubica es: ',float(round(raiz3,2)))