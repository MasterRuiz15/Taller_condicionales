# input
salario_emp=int(input("Digite el salario del empleado: "))
deudas=input("¿El empleado tiene deudas?: SI , NO: ")

# processing
if salario_emp>=945200:
    if deudas=="NO":
        rta="APROBADO"
    else:
        rta="RECHAZADO"
else:
    rta="RECHAZADO"
    
# output
print("Su prestamo ha sido "+ rta)
