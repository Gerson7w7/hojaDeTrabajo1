def serieFibonacci(numero):
    if numero == 0: 
        return 0
    elif numero == 1:
        return 1
    else:
        return serieFibonacci(numero-1) + serieFibonacci(numero-2)

numero = int(input("Ingrese un número: "))
resultado = serieFibonacci(numero)
print(resultado)



