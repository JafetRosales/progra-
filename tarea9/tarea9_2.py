# Tarea 9.2
lista = input("Mete una lista de números: ")
lideres = lista.split()
numeros = []
for i in lideres:
    n = int(i)
    if n not in numeros:
        numeros.append(n)
numeros.sort(reverse=True)
print("Lista de lideres: ", numeros)

