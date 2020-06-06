#Dada una secuencia de enteros, calcular la suma de ellos, el total de numeros positivos y el promedio de los valores positivos.

def sumaConPromedio(lista):
    suma, promedio, i = 0, 0, 0

    while (i < len(lista)):
        if(lista[i] > 0):
            suma += lista[i]
        if(i == len(lista)-1):
            promedio += (suma/len(lista))
        i += 1

    return (suma, promedio)

N = int(input("Ingrese el valor de N = "))
sec = [int(input("A[" + str(i) + "] = ")) for i in range(0,N)]
print('La suma de los enteros positivos es: '+str(sumaConPromedio(sec)[0]))
print('El promedio es: '+str(sumaConPromedio(sec)[1]))