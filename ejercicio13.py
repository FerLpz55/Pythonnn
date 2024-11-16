#elaborar un algortimo que imprima un cuadro latino de orden N 
# un cuadro latino de orden N  es una matriz cuadrada en la que la primera fila contiene los primeros : N numeros 
#naturales  y cada una de las siguientes filas contiene la fila anterior rotada a una posicion a la derecha.
def generar_cuadro_latino(n):
    # Crear la primera fila con los primeros N números naturales
    cuadro = [list(range(1, n + 1))]
    
    # Generar las siguientes filas rotando la fila anterior
    for i in range(1, n):
        # Rotar la fila anterior a la derecha
        fila_anterior = cuadro[i - 1]
        nueva_fila = [fila_anterior[-1]] + fila_anterior[:-1]
        cuadro.append(nueva_fila)
    
    return cuadro

def imprimir_cuadro_latino(cuadro):
    for fila in cuadro:
        print(' '.join(map(str, fila)))

# Ejemplo de uso
n = int(input("Introduce el orden N del cuadro latino: "))
cuadro_latino = generar_cuadro_latino(n)
imprimir_cuadro_latino(cuadro_latino)

