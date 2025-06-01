numero = int(input("Ingresa un número: "))
original = numero

print("separacion de numero", original)


while numero >= 10:
    suma = 0
   
    for digito in str(numero):
        suma = suma + int(digito)
    print(numero, "=", suma)
    numero = suma

print("El resultado final es:", numero)
