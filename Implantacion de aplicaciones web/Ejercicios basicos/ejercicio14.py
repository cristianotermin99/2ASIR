#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
#Ejemplo, si se introduce 23 que muestre 32.

numero=input('Introduce un numero: ')

primerCaracter=numero[0]
segundoCaracter=numero[1]

numeroInvertido=int(segundoCaracter+primerCaracter)

print(numeroInvertido)