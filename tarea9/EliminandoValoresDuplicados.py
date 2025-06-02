entrada = input("mete una lista de numeros: ")
lista = entrada.split()
print("listado de numeros ingresados: ", lista)

cajita = []

for i in lista:
    if i not in cajita:
        cajita.append(i)

print("lista arreglada con un solo numero: ", cajita)