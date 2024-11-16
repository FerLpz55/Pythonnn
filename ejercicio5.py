#elabora un algoritmo que permita ingresar 15 letras cuales quiera. e indique al final cuantas consonantes se ingresaron
#y cuantas vocales se ingresaron
def contar_vocales_consonantes():
    vocales = 'aeiouAEIOU'
    consonantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    conteo_vocales = 0
    conteo_consonantes = 0

    for i in range(15):
        letra = input(f"Ingrese la letra {i + 1}: ")
        
        if letra in vocales:
            conteo_vocales += 1
        elif letra in consonantes:
            conteo_consonantes += 1
        else:
            print("No es una letra válida, por favor ingrese solo letras.")

    print(f"Se ingresaron {conteo_vocales} vocales y {conteo_consonantes} consonantes.")

contar_vocales_consonantes()