#pedir numero trabajadores
numeroTrabajadores = int(input("¿Cuantos trabajadores hay en la empresa? "))

costeSemanalEmpresa = 0

for i in range(numeroTrabajadores):
    #pedir sueldo un trabajador
    print("Trabajador "+str(i+1))
    sueldo = float(input("¿Cual es su sueldo por hora? "))
    #pedir numero de dias trabajados
    diasTrabajados = int(input("¿Cuantos dias ha trabajado? "))
    #pedir horas cada dia
    horasTotalTrabajadas=0
    for x in range(diasTrabajados):
        horasTotalTrabajadas += float(input("¿Cuantas horas ha hecho dia "+str(x+1)+"? "))

    sueldoDeUnTrabajador = sueldo*horasTotalTrabajadas
    print("El sueldo de este trabajador es "+str(sueldoDeUnTrabajador))
    costeSemanalEmpresa += sueldoDeUnTrabajador

print("El coste semanal de la empresa es "+str(costeSemanalEmpresa))