#Dada una secuencia de enteros calcular el numero de valores primos almacenados en la secuencia. 
N = int(input("ingrese el valor de N="))
lista = [ int(input("lista[" + str(i) + "] = ")) for i in range(0,N) ]
def primo(N):
    cont=0
    for i in range(1,N):
        if (N%i==0):
            cont+=1 # Si se puede dividir por algun numero mas de una vez, no es primo
            if cont>1:
                return False
    return True            
def ordenamiento(listas):#Ordenamiento por insercion
    for indice in range(1,len(lista)): #pasamos por cada espacio de la lista
         #comenzamos en 1 porque no tiene sentido comparar con el primer elemento 0 de la lista. 
        valor = lista[indice] #Aqui obtener el valor del elemento de nuestro indice
        i = indice - 1 #comparamos valor con los elementos a la izquiera, por eso lo restamos
        while i>=0: #comparamos siempre con cada cosa a la izquiera hasta que valga 0
            if valor < lista[i]: 
                lista[i+1] = lista[i] #cambia el numero del espacio i al espacio de la derecha i+1

                lista[i]= valor #cambia el valor del espacio i
                i = i - 1
            else: #si no es menor, entonces valor esta en el lugar correcto
                break    
suma = 0
listaprima = []

ordenamiento(lista)
print("lista:",lista)
for i in lista:
    if primo(i): #si se cumple la funcion primo entonces es primo y se añade a la lista y se va sumando en un contador
        listaprima.append(i)
        
    else:
        pass
ordenamiento(listaprima)  
print("los numeros primos en lista son:",listaprima)            