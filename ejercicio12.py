#elaborar un algoritmo que lea un vector de N elementos y rote todas sus componentes un lugar hacia la derecha
#teniendo en cuenta  que la ultimo componente se ha de desplazar al primer lugar.
def rotar_vector(vector):
    if len(vector) == 0:
        return vector  # Si el vector está vacío, no hay nada que rotar
    # Guardamos la última componente
    ultimo_elemento = vector[-1]
    # Rotamos el vector
    for i in range(len(vector) - 1, 0, -1):
        vector[i] = vector[i - 1]
    vector[0] = ultimo_elemento  # Colocamos el último elemento en la primera posición
    return vector

# Ejemplo de uso
n = int(input("Ingrese el número de elementos en el vector: "))
vector = []

for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    vector.append(elemento)

print("Vector original:", vector)
vector_rotado = rotar_vector(vector)
print("Vector rotado:", vector_rotado)