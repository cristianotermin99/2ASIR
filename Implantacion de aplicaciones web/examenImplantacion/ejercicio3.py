golesMarcadosPorMessi=int(input("Introduce cuantos goles ha marcado messi: "))
porcentajeParadasUnaiSimon=int(input("Introduce el porcentaje de paradas de Unai Simon: "))
posesionMediaEspaña=int(input("Introduce la posesion media de España: "))
numeroTarjetasRojasBrasil=int(input("Introduce cuantas tarjetas rojas tiene brasil: "))
golesMarcadosPorMbape=int(input("Introduce cuantos goles ha marcado Mbape: "))
primasArabiaSaudi=int(input("Introduce la prima de arabia saudi: "))


paisGanador=""
if golesMarcadosPorMessi>8:
    paisGanador="argentina"
elif golesMarcadosPorMessi>4 and golesMarcadosPorMessi<8:
    if porcentajeParadasUnaiSimon>90 and numeroTarjetasRojasBrasil>1:
        paisGanador="alemania"
    elif posesionMediaEspaña>75 and golesMarcadosPorMbape<3:
        paisGanador="españa"
    elif golesMarcadosPorMbape>5 or posesionMediaEspaña<60:
        paisGanador="brasil"
elif primasArabiaSaudi>=1000000000:
    paisGanador="arabia saudi"
elif primasArabiaSaudi<1000000000 and numeroTarjetasRojasBrasil>3 and golesMarcadosPorMbape<3 and posesionMediaEspaña<50 and porcentajeParadasUnaiSimon<50:
    paisGanador="japon"
else:
    paisGanador="desconocido"


print("El pais ganador es: "+paisGanador+"!!!!!!!!!!!!!!!!!!!")