nota=int(input('Introduce nota: '))
edad=int(input('Introduce edad: '))
sexo=input('Sexo:')


if nota>=5 and edad>=18 and sexo=='F':
    print('ACEPTADA')
elif nota>=5 and edad>=18 and sexo=='M':
    print('POSIBLE')
else:
    print('NO ACEPTADA')


