#Algoritmo que invierte e imprime el vector de un programa que lee 50 números y los almacena en un vector,
# y obtiene e imprime cuáles son el mayor y el menor número almacenados y cuántas veces se repite cada uno.

def leer_numeros():
    """Lee 50 números y los almacena en un vector."""
    numeros = []
    for i in range(50):
        while True:
            try:
                numero = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Error: Debe ingresar un número.")
    return numeros

def invertir_vector(vector):
    """Invierte el vector."""
    return vector[::-1]

def encontrar_mayor_menor(vector):
    """Encuentra el mayor y el menor número en el vector."""
    mayor = max(vector)
    menor = min(vector)
    return mayor, menor

def contar_repeticiones(vector, numero):
    """Cuenta cuántas veces se repite un número en el vector."""
    return vector.count(numero)

def main():
    numeros = leer_numeros()
    print("\nVector original:")
    print(numeros)
    
    vector_invertido = invertir_vector(numeros)
    print("\nVector invertido:")
    print(vector_invertido)
    
    mayor, menor = encontrar_mayor_menor(numeros)
    print(f"\nMayor número: {mayor}")
    print(f"Menor número: {menor}")
    
    repeticiones_mayor = contar_repeticiones(numeros, mayor)
    repeticiones_menor = contar_repeticiones(numeros, menor)
    print(f"\nEl mayor número se repite {repeticiones_mayor} veces.")
    print(f"El menor número se repite {repeticiones_menor} veces.")

if __name__ == "__main__":
    main()
