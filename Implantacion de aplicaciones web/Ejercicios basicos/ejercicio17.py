#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
#viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la
#hora de llegada a la ciudad B.

horas=int(input('Horas: '))
minutos=int(input('Minutos: '))
segundos=int(input('Segundos: '))
tiempoViajeSegudnos=int(input('Duración del viaje en segundos: '))

totalSegundos=int(horas*3600+minutos*60+segundos+tiempoViajeSegudnos)

horas=int(totalSegundos/3600)
restoSegundos=totalSegundos%3600
minutos=int(restoSegundos/60)
segundos=restoSegundos%60


print('Llegará a las: ',horas,'h ',minutos,'m ',segundos,'s')



