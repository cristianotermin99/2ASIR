#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
#algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las
#dos variables.

primerNumero=int(input('Introduce un numero A: '))
segundoNumero=int(input('Introduce oro numero B: '))

intercambio=primerNumero
primerNumero=segundoNumero
segundoNumero=intercambio

print('El numero A es: ',primerNumero,'\nEl numero B es: ',segundoNumero)