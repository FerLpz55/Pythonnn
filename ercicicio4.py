#escribe un algoritmo que muestre los terminos de la serie de fibnacci que sean menores a 1000
def fibonacci_menores_a_1000():
    a, b = 0, 1
    while a < 1000:
        print(a)
        a, b = b, a + b

fibonacci_menores_a_1000()