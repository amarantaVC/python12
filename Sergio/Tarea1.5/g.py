#Dada una secuencia de caracteres sec devolver en la variable secInv la misma secuencia en orden inverso

def invertir(lista):
    i = len(lista) - 1
    secInv = []

    while (i > -1):
        secInv.append(lista[i])
        i -= 1
    
    return secInv

sec = [1, 5, 6, 11, 89]
print(invertir(sec))