#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su
#diferencia, de modo que el resultado sea siempre positivo).

primerNumero=float(input('Introduce un numero: '))
segundoNumero=float(input('Introduce otro numero: '))

distancia=abs(primerNumero-segundoNumero)

print('La distancia entre los numeros es de:', float(distancia))
