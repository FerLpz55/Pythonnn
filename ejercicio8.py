# Inicializar una lista para almacenar los números
numeros = []

# Leer 50 números del usuario
for i in range(50):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Ingrese un número válido.")

# Encontrar el mayor y el menor número
mayor = max(numeros)
menor = min(numeros)

# Contar cuántas veces se repite el mayor y el menor
repeticiones_mayor = numeros.count(mayor)
repeticiones_menor = numeros.count(menor)

# Imprimir los resultados del mayor y menor
print(f"El mayor número es: {mayor} y se repite {repeticiones_mayor} veces.")
print(f"El menor número es: {menor} y se repite {repeticiones_menor} veces.")

# Inicializar las sumas
suma_pares = 0
suma_impares = 0

# Calcular las sumas de los índices pares e impares
for i in range(len(numeros)):
    if i % 2 == 0:  # Índice par
        suma_pares += numeros[i]
    else:           # Índice impar
        suma_impares += numeros[i]

# Imprimir las sumas
print(f"La suma de los números en índices pares es: {suma_pares}")
print(f"La suma de los números en índices impares es: {suma_impares}")