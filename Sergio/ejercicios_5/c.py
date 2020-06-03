#Dada una secuencia de n enteros, hallar el segundo menor de la secuencia.

def selecccionSort(Lista):
    for i in range(len(Lista)):
        menor = i
        for k in range(i+1, len(Lista)):
            if Lista[k] < Lista[menor]:
                menor = k
                 
        swap(Lista, menor, i)

#Intercambio         
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

lista = [5, 6, 3, 2]
seleccioncSort(lista)
print(lista[1])

