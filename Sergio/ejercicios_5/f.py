# Dada una secuencia de enteros calcular el numero de valores primos almacenados en la secuencia.

#Funcion es primo
def esPrimo(num):

    esPrimo = True
    i = 2
    while (esPrimo and i < num):
        if (num % i == 0):
            esPrimo = False
        i += 1

    return esPrimo

list = [1, 5, 6, 8, 2, 20, 21, 33, 49]
primo = []

i, contador = 0, 0
while (i < len(list)):
    if (esPrimo(list[i])):
        primo.append(list[i])
        contador += 1
    i += 1
print(primo, contador)