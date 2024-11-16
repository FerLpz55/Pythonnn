#elaborar un algoritmo que calcule el factorial de un numero entero positivo en python
def calcular_factorial():
    # Solicitamos el número y validamos la entrada
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero >= 0:
                break
            print("Por favor ingrese un número positivo.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    # Calculamos el factorial
    factorial = 1
    
    # Caso especial: factorial de 0 es 1
    if numero == 0:
        print(f"El factorial de 0 es: 1")
        return
    
    # Calculamos el factorial multiplicando los números del 1 al número ingresado
    for i in range(1, numero + 1):
        factorial *= i
        print(f"{i} x ", end="") if i < numero else print(f"{i} = {factorial}")
    
    # Mostramos el resultado
    print(f"\nEl factorial de {numero} es: {factorial}")

# Ejecutamos el programa
if __name__ == "__main__":
    print("=== Calculadora de Factorial ===")
    calcular_factorial()