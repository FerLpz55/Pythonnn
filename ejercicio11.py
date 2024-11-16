def generar_matriz_unitaria(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        matriz[i][i] = 1
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

N = int(input("Ingrese el orden de la matriz: "))
matriz_unitaria = generar_matriz_unitaria(N)
print("Matriz unitaria de orden", N, ":")
imprimir_matriz(matriz_unitaria)

