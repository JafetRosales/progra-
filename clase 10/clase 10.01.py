"""
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    10.2.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Cristian Jafet Rosales Martinez 
Fecha:        2025-07-09
Estado:       [Terminado]
"""

'''
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    10.3.2
Descripción:  Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).

Autor:        Julio Roberto Guardado Quijano 
Fecha:        2025-06-10
Estado:       [Terminado]
'''
n = int(input("Ingrese la dimensión de la matriz cuadrada: "))
m = []
for i in range(n):
    fila = list(map(int, input(f"Ingrese {n} números (0 o 1) separados por coma para la fila {i}: ").split(",")))
    m.append(fila)

vecinos = []
for i in range(n):
    fila_vecinos = []
    for j in range(n):
        contador = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    if m[ni][nj] == 1:
                        contador += 1
        fila_vecinos.append(contador)
    vecinos.append(fila_vecinos)

for fila in vecinos:
    print(fila)
