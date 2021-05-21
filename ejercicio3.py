def factorial(n):
    if n > 1:
        n = n*factorial(n-1)
    return n

n = int(input("Ingrese un número: "))
resultado = factorial(n)
print(resultado)