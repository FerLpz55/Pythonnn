#elaborar un algoritmo que solicite letras hasta que se ingrese una vocal

# Definimos una función para verificar si una letra es vocal
def es_vocal(letra):
    # Convertimos la letra a minúscula para hacer la comparación
    letra = letra.lower()
    # Lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    return letra in vocales

# Iniciamos el bucle principal
while True:
    # Solicitamos una letra al usuario
    letra = input("Ingrese una letra: ")
    
    # Verificamos que se haya ingresado solo una letra
    if len(letra) != 1:
        print("Por favor, ingrese solo una letra")
        continue
    
    # Verificamos si es una vocal
    if es_vocal(letra):
        print(f"¡Has ingresado la vocal '{letra}'!")
        break
    else:
        print(f"'{letra}' no es una vocal, intente nuevamente")