
import numpy as np

# Lista basica convertida en arreglo NumPy
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

# Crear un arreglo de ceros con 5 elementos
zeros = np.zeros(5)
print(zeros)

# Crear un arreglo lleno de unos con 5 posiciones
ones = np.ones(5)
print(ones)

# Operaciones entre dos arreglos: suma y multiplicacion
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2
resultado = arr1 * arr2

# Otra vez operaciones entre arreglos (suma y multiplicacion)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2
# print(resultado)
resultado = arr1 * arr2
# print(resultado)

# Ejemplo de broadcasting: se suma 5 a todos los elementos
arr = np.array([1, 2, 3])
result = arr + 5
# print(result)

# Suma entre vectores de diferente forma: fila + columna (broadcasting 2D)
arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2
# print(result)

# Extraer los elementos en las posiciones 2, 3 y 4 (por indice)
arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
# print

# Filtrar elementos mayores que 2 usando condicion booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
# print(result)

# Seleccionar elementos especificos usando un arreglo de indices
arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices]
# print(result)

# Combinar dos arreglos unidimensionales en uno solo
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
# print(concatenated)

# Dividir un arreglo de 6 elementos en 3 fragmentos iguales
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3)
# print(split)

# Matriz con datos de consumo energetico por hogar durante la semana
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# Informacion basica sobre la estructura del arreglo de consumo
# print("Dimensiones:", consumo.ndim)
# print("Forma:", consumo.shape)
# print("Tipo de datos:", consumo.dtype)
# print("Consumo del primer hogar:", consumo[0])
# print("Consumo del dia miercoles (columna 2):", consumo[:, 2])

# Calcular la media semanal de cada hogar
promedio_por_hogar = np.mean(consumo, axis=1)
# Calcular el promedio diario entre todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)
# Sumar todo el consumo semanal de todos los hogares
total_consumo = np.sum(consumo)

# print(promedio_por_hogar)
# print(promedio_por_dia)
# print(total_consumo)

# Obtener el valor mas alto de consumo por hogar
maximos = np.max(consumo, axis=1)
# Obtener el consumo mas bajo por dia
minimos = np.min(consumo, axis=0)
# Desviacion estandar total del conjunto de datos
desviacion = np.std(consumo)

# print(maximos)
# print(minimos)
# print(desviacion)

# Calcular el total de consumo semanal por hogar
consumo_total_hogar = np.sum(consumo, axis=1)
# Encontrar el hogar con mas consumo en la semana
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# Detectar cual fue el hogar mas eficiente (menos consumo)
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

# print(consumo_total_hogar)
# print(hogar_mayor_consumo)
# print(hogar_mas_eficiente)

# Identificar hogares que consumieron mas de 100 en total
consumo_total_hogar = np.sum(consumo, axis=1)
# print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")
altos = consumo_total_hogar > 100
consumo_mayor_100 = np.where(altos)[0]
# print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

# Normalizacion tipo MinMax para ajustar el rango de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())
# print(consumo_normalizado)

# 1. Mostrar el consumo del hogar numero 5 el dia viernes
print("Consumo del hogar 5 el viernes (dia 5):", consumo[4,4])

# 2. Mostrar el consumo del domingo (ultimo dia) de los 3 hogares finales
print("Consumo domingo (ultimos 3 hogares):", consumo[-3:, 6])

# 3. Calcular el promedio considerando sabado y domingo
fin_de_semana = consumo[:, [5, 6]]
promedio_fin_semana = np.mean(fin_de_semana)
print("Promedio de consumo durante fines de semana (sabado y domingo):", promedio_fin_semana)

# 4. Que dia presenta mayor diferencia entre hogares?
desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_por_dia)
print("Dia con mayor desviacion estandar:", dia_mayor_desviacion)
'''
Un valor alto en desviacion estandar significa que los hogares tienen consumos muy distintos ese dia.
'''

# 5. Mostrar los 3 hogares que menos consumieron durante la semana
consumo_total = np.sum(consumo, axis=1)
indices_menor_consumo = np.argsort(consumo_total)[:3]
valores_menor_consumo = consumo_total[indices_menor_consumo]
print("indices de los 3 hogares con menor consumo:", indices_menor_consumo)
print("Valores de consumo:", valores_menor_consumo)

# 6. Calcular el nuevo consumo del hogar 3 si sube 10% su gasto diario
hogar3 = consumo[2]
hogar3_incrementado = hogar3 * 1.10
nuevo_total = np.sum(hogar3_incrementado)
print("Nuevo consumo total del hogar 3 con aumento del 10%:", nuevo_total)

