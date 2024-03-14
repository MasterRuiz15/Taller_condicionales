## programa para saber si la suma de los 2 primeros numeros es el numero 3

# input

A = int(input("Porfavor ingrese el primer numero : "))
B = int(input("Porfavor ingrese el segundo numero : "))
C = int(input("Porfavor ingrese el tercer numero : "))

# procesing

if A + B == C:
    print("La suma de los numeros",A,"+",B,"es igual al numero",C,)
else:
    print("La suma de los numeros",A,"+",B,"no es igual al numero",C,)  