#Dado un entero N, calcular la suma de los numeros primos menores que N. 

#Funcion es primo
def esPrimo(num):

    esPrimo = True
    i = 2
    while (esPrimo and i < num):
        if (num % i == 0):
            esPrimo = False
        i += 1

    return esPrimo

# N > -1
N = int(input("Ingrese el valor de N = "))
while (N < 0):
    N = int(input("Ingrese el valor de N = "))

lista, primos, suma = [0, 1], [], 0

i = 2
while (i < N):
    lista.append(i)
    if(esPrimo(lista[i])):
        suma += lista[i]
        primos.append(lista[i])
    i += 1

#for i in range(2, N):
#   lista.append(i)
#    if(esPrimo(lista[i])):
#        suma += lista[i]
#        primos.append(lista[i])

print("Lista de numeros primos: " + str(primos) + "\nSu suma es: " + str(suma))
