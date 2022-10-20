print('Introduce 15 numeros por teclado ')
numero=0
for i in range(1,15+1):
    numero+=int(input('Introduce un numero: '))

media=numero/15
print('La media de los 15 numeros introducidos es: ',media)