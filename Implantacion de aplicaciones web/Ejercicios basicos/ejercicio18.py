#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre=input('Introduce tu nombre: ')
primerApellido=input('Introduce tu primer apellido: ')
segundoApellido=input('Introduce tu segundo apellido: ')

inicialNombre=nombre[0].upper()
inicialPrimerApellido=primerApellido[0].upper()
inicialSegundoApellido=segundoApellido[0].upper()

print(inicialNombre,inicialPrimerApellido,inicialSegundoApellido)
