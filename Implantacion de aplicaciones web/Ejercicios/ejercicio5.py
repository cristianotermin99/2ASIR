cantidadNumerosMedia=int(input('Introduce cuantos numeros quieres introducir oara hacer la media: '))

numero=0
for i in range(1,cantidadNumerosMedia+1):
    numero+=int(input('Introduce un numero: '))

media=numero/cantidadNumerosMedia
print('La media de los ',cantidadNumerosMedia, ' numeros introducidos es: ',media)