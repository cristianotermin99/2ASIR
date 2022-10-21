#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una
#distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para
#ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con
#esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro

velocidad1=int(input('Introduce la velocidad del primer vehiculo(km/h): '))
velocidad2=int(input('Introduce la velocidad del segundo vehiculo (mas rapido que el primero)(km/h): '))
distancia=int(input('Introduce la distancia entre vehiculos(km): '))

diferenciaVelocidad=velocidad2-velocidad1
tiempo=distancia/diferenciaVelocidad

tiempo=tiempo*60

print('Lo alcanzará en ',int(tiempo),' minutos')


