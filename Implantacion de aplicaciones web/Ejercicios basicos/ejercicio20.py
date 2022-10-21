#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
#pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

monedas2Euros=int(input('Cantidad de monedas de 2 euros: '))
monedas1Euro=int(input('Cantidad de monedas de 1 euro: '))
monedas50cent=int(input('Cantidad de monedas de 50 centimos: '))
monedas20cent=int(input('Cantidad de monedas de 20 centimos: '))
monedas10cent=int(input('Cantidad de monedas de 10 centimos: '))


totalCentimos=monedas2Euros*200+monedas1Euro*100+monedas50cent*50+monedas20cent*20+monedas10cent*10
euros=int(totalCentimos/100)
totalCentimos=totalCentimos%100

print('Tienes: ',euros,'euros y ', totalCentimos,' centimos')