notaPrimerParcial=float(input('Introduce la nota de la primera clasificación parcial: '))
notaSegundoParcial=float(input('Introduce la nota de la segunda clasificación parcial: '))
notaTercerParcial=float(input('Introduce la nota de la primera clasificación parcial: '))

notaExamenFinal=float(input('Introduce la nota del examen final: '))

notaTrabajoFinal=float(input('Introduce la nota del trabajo final: '))


mediaParciales=(((notaPrimerParcial+notaSegundoParcial+notaTercerParcial)/3)*0.55)
notaExamenFinal=notaExamenFinal*0.3
notaTrabajoFinal=notaTrabajoFinal*0.15

notaFinal=mediaParciales+notaExamenFinal+notaTrabajoFinal
print('Tu nota final es:', notaFinal)




