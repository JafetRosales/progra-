numero_secreto = 42

print("¡Adivina el número secreto entre 1 y 100!")

for intento_num in range(1, 9999999):
    intento = int(input(f"Intento {intento_num}: Ingresa tu número: "))

    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
