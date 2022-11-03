numeroAlumnos=int(input("Introduce numero de alumnos: "))
precioPorAlumno=0
precioTotal=0
if numeroAlumnos>=100:
    precioPorAlumno=65
elif numeroAlumnos>=50:
    precioPorAlumno=70
elif numeroAlumnos>=30:
    precioPorAlumno=95
elif numeroAlumnos>0 and numeroAlumnos<30:
    precioTotal=4000
    precioPorAlumno=precioTotal/numeroAlumnos

if numeroAlumnos>=30:
    precioTotal=precioPorAlumno*numeroAlumnos


print(precioTotal,"€ cuesta el autobus en total")
print(precioPorAlumno,"€ por cada alumno")

