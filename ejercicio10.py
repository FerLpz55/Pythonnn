def analizar_matriz():
    # Inicializar la matriz vacía
    matriz = []
    filas = 4
    columnas = 8
    
    print("=== Ingreso de datos para matriz 4x8 ===")
    
    # Llenar la matriz
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = int(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Por favor ingrese un número entero válido.")
        matriz.append(fila)
    
    # Encontrar máximo y mínimo con sus posiciones
    maximo = matriz[0][0]
    minimo = matriz[0][0]
    pos_maximo = [1, 1]
    pos_minimo = [1, 1]
    
    # Buscar máximo y mínimo
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                pos_maximo = [i+1, j+1]
            if matriz[i][j] < minimo:
                minimo = matriz[i][j]
                pos_minimo = [i+1, j+1]
    
    # Mostrar la matriz
    print("\n=== Matriz ingresada ===")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4}", end=" ")
        print()
    
    # Mostrar resultados
    print("\n=== Resultados ===")
    print(f"Valor máximo: {maximo}")
    print(f"Posición del máximo: Fila {pos_maximo[0]}, Columna {pos_maximo[1]}")
    print(f"Valor mínimo: {minimo}")
    print(f"Posición del mínimo: Fila {pos_minimo[0]}, Columna {pos_minimo[1]}")

# Ejecutar el programa
analizar_matriz()