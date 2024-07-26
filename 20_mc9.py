#Recursión Factorial: Implementa una función recursiva para calcular el factorial de un número pequeño (por ejemplo, 5).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))