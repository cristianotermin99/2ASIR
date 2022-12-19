# (3pto) Se quiere llevar un control de asistencia a los estadios en el mundial, para ellos se iran
#pidiendo dato de asistencia por día. Para probarlo se mirará solamente 7 días, cada día hay 4
#partidos y se tendrá que pedir la asistencia por partido , se pide el público local, visitante y
#neutral, sacando la asistencia total diaria además de la media de público neutral por día y
#después de meter todos los días se mostrará la asistencia total de publico en los 7 días,
#además de la asistencia total del publico neutral para ver cuantos qataries van al mundial.
    #a. ENTRADAS se pide por consola asistencia de publico local, visitante y neutral por
    #partido y día
    #b. SALIDAS, se saca a consola la asistencia total diaria, la media de publico neutral
    #diaria, el total de asistencia en los 7 días, y el total de publico neutral.


cantidadPublicoLocalPorPartido=0
cantidadPublicoVisitantePorPartido=0
cantidadPublicoNeutralPorPartido=0
asistenciaPublicoTotalDia=0
mediaPublicoNeutralPorDia=0
totalAsistenciaSemana=0
totalAsistenciaSemanaPublicoNeutral=0

for i in range (7):
    cantidadPublicoLocalPorDia=0
    cantidadPublicoVisitantePorDia=0
    cantidadPublicoNeutralPorDia=0
    print("Dia "+str(i+1))
    for x in range (4):
        print("Partido "+str(x+1))
        cantidadPublicoLocalPorPartido=int(input("Cantidad de publico local en el partido: "))
        cantidadPublicoVisitantePorPartido=int(input("Cantidad de publico visitante en el partido: "))
        cantidadPublicoNeutralPorPartido=int(input("Cantidad de publico neutral en el partido: "))
        cantidadPublicoLocalPorDia+=cantidadPublicoLocalPorPartido
        cantidadPublicoVisitantePorDia+=cantidadPublicoVisitantePorPartido
        cantidadPublicoNeutralPorDia+=cantidadPublicoNeutralPorPartido
    asistenciaPublicoTotalDia=cantidadPublicoLocalPorDia+cantidadPublicoVisitantePorDia+cantidadPublicoNeutralPorDia
    mediaPublicoNeutralPorDia=cantidadPublicoLocalPorDia/4
    totalAsistenciaSemana+=asistenciaPublicoTotalDia
    totalAsistenciaSemanaPublicoNeutral+=cantidadPublicoNeutralPorDia
    print("Asistencia total del dia: ",asistenciaPublicoTotalDia)
    print("Asistencia media publico neutral del dia: ",mediaPublicoNeutralPorDia)

print("Asistencia total en los 7 dias: ",totalAsistenciaSemana)
print("Asistencia total publico neutral en los 7 dias: ",totalAsistenciaSemanaPublicoNeutral)