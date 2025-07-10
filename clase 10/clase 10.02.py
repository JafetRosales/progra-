'''
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    10.3.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.

Autor:        Cristian Jafet Rosales Martinez
Fecha:        2025-07-09
Estado:       [Terminado]
'''
n = int(input("Ingrese la dimensión de la matriz cuadrada: "))
m = []
for i in range(n):
    fila = list(map(int, input(f"Ingrese {n} números separados por coma para la fila {i}: ").split(",")))
    m.append(fila)

simetrica = True
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")