
#algoritmo que permite calcular el promedio de un grupo de empleados 
def calcular_promedio_empleados():
    # Inicializamos variables
    total_empleados = 0
    suma_salarios = 0
    
    # Solicitamos la cantidad de empleados
    while True:
        try:
            total_empleados = int(input("Ingrese el número de empleados: "))
            if total_empleados > 0:
                break
            else:
                print("Por favor ingrese un número mayor a 0")
        except ValueError:
            print("Por favor ingrese un número válido")
    
    # Recolectamos los salarios de cada empleado
    for i in range(total_empleados):
        while True:
            try:
                salario = float(input(f"Ingrese el salario del empleado {i + 1}: "))
                if salario >= 0:
                    suma_salarios += salario
                    break
                else:
                    print("El salario no puede ser negativo")
            except ValueError:
                print("Por favor ingrese un monto válido")
    
    # Calculamos el promedio
    promedio = suma_salarios / total_empleados
    
    # Mostramos los resultados
    print("\n=== Resultados ===")
    print(f"Total de empleados: {total_empleados}")
    print(f"Suma total de salarios: ${suma_salarios:,.2f}")
    print(f"Promedio de salarios: ${promedio:,.2f}")

# Ejecutamos el programa
if __name__ == "__main__":
    print("Bienvenido al calculador de promedios de salarios")
    calcular_promedio_empleados()