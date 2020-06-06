#Dada una secuencia ordenada de n enteros, determinar si el valor x esta en la secuencia. 

def busquedaBinaria(lista, item):
    izq = 0
    der = len(lista)-1
    num = False

    while (izq <= der and not num):
        puntoMedio = (izq + der)//2
        if (lista[puntoMedio] == item):
            num = True
        else:
            if (item < lista[puntoMedio]):
                der = puntoMedio-1
            else:
                izq = puntoMedio+1

    return num

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busquedaBinaria(listaPrueba, 3))
print(busquedaBinaria(listaPrueba, 13))
