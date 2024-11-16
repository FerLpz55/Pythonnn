#elaborar un programa que lee 50 numeros y los almacena en un vector, y obtiene e imprime cuales son el mayor
#  y el menor numero
#almacenados y cuantas veces se repite cada uno

# Inicializar una lista para almacenar los números
numeros = []

# Leer 50 números del usuario
for i in range(50):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    numeros.append(numero)

# Encontrar el mayor y el menor número
mayor = max(numeros)
menor = min(numeros)

# Contar cuántas veces se repite el mayor y el menor
repeticiones_mayor = numeros.count(mayor)
repeticiones_menor = numeros.count(menor)

# Imprimir los resultados
print(f"El mayor número es: {mayor} y se repite {repeticiones_mayor} veces.")
print(f"El menor número es: {menor} y se repite {repeticiones_menor} veces.")