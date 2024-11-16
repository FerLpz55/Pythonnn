def clasificar_personas():
    # Inicializamos las listas
    edad = []
    mayores = []
    menores = []
    
    while True:
        # Ingreso del nombre
        nombre = input("\nIngrese el nombre de la persona: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío")
            continue
            
        # Ingreso de la edad
        while True:
            try:
                edad_persona = int(input(f"Ingrese la edad de {nombre}: "))
                if 0 <= edad_persona <= 120:
                    break
                print("Por favor ingrese una edad válida (entre 0 y 120 años)")
            except ValueError:
                print("Por favor ingrese un número válido")
        
        # Agregamos la edad y clasificamos
        edad.append(edad_persona)
        if edad_persona >= 18:
            mayores.append(nombre)
        else:
            menores.append(nombre)
            
        # Preguntamos si desea continuar
        while True:
            respuesta = input("¿Desea agregar otra persona? (s/n): ").lower()
            if respuesta in ['s', 'n']:
                break
            print("Por favor responda 's' para sí o 'n' para no")
            
        if respuesta == 'n':
            break
    
    # Mostramos resultados
    print("\nLas personas mayores de edad son:", mayores)
    print("Las personas menores de edad son:", menores)

if __name__ == "__main__":
    clasificar_personas()