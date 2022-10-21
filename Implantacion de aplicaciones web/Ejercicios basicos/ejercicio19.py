#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada
#respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el
#resultado obtenido por el estudiante.

respuestasCorrectas=int(input('Introduce el numero de respuestas correctas: '))
respuestasIncorrectas=int(input('Introduce el numero de respuestas incorrectas: '))
respuestasVacias=int(input('Introduce el numero de respuestas vacias: '))

totalRespuestas=respuestasCorrectas+respuestasIncorrectas+respuestasVacias
if respuestasIncorrectas>0:
    puntuacion=(respuestasCorrectas*5)+(respuestasIncorrectas*(-1))
else:
    puntuacion=(respuestasCorrectas*5)


notaFinal=(puntuacion*10/(totalRespuestas*5))

print(notaFinal)



