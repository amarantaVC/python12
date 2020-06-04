#Dada una secuencia de n enteros, hallar el segundo menor de la secuencia. 
N= int(input("ingrese el valor de N="))
A= [ int(input("A[" + str(i) + "] = ")) for i in range(0,N) ]

def ordenamiento(lista):#Ordenamiento por insercion
    for indice in range(1,len(lista)): #pasamos por cada espacio de la lista
         #comenzamos en 1 porque no tiene sentido comparar con el primer elemento 0 de la lista. 
        valor = lista[indice] #Aqui obtener el valor del elemento de nuestro indice
        i = indice - 1 #comparamos valor con los elementos a la izquiera, por eso lo restamos
        while i>=0: #comparamos siempre con cada cosa a la izquiera hasta que valga 0
            if valor < lista[i]: 
                lista[i+1] = lista[i] #cambia el numero del espacio i al espacio de la derecha i+1

                lista[i]= valor #cmbia el valor del espacio i
                i = i - 1
            else: #si no es menor, entonces valor esta en el lugar correcto
                break    
ordenamiento(A) 
print(A)        #imprime el nuevo orden de A 
print("El segundo menor de A es:", A[1])    