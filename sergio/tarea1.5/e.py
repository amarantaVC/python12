#Dado un numero n calcule la suma de los cuadrados entre 0 y n, almacene el resultado en la variable d.

def sumaCuadrados(num):
    i, suma = 1, 0
    while (i < num+1):
        suma += i**2
        i += 1

    return suma

N = int(input("Ingrese el valor de N: "))

print(sumaCuadrados(N))
