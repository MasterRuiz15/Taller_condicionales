#Programa que lea coordenadas cartesianas (x, y) de un punto en el plano  y Calcule el cuadrante al cual pertenece el punto.

# input
X = int(input("ingrese la coordenada x: "))
Y = int(input("ingrese la coordenada y: "))

# Processing
if X == 0:
    if Y == 0:
        print("La coordenada" ,(X  , Y), "esta en el origen")
    else:
        print("La coordenada" ,(X  , Y), "esta en el eje Y")
elif Y == 0:
    print("La coordenada" ,(X  , Y), "esta en el eje Y")
elif X == 0:
    if Y > 0:
        print("La coordenada" ,(X  , Y), "esta en el cuadrante 1")
    else:
        print("La coordenada" ,(X  , Y), "esta en el cuadrante 4")
elif Y < 0:
    print("La coordenada" ,(X  , Y), "esta en el cuadrante 3")
else:
    print("La coordenada" ,(X  , Y), "esta en el cuadrante 2")