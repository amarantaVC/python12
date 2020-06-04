#Dada una secuencia ordenada de n enteros, determinar si el valor x esta en la secuencia
N = int(input("ingresee el valor de N="))

x=14

lista= [int(input("Lista[" + str(i) + "] =")) for i in range(0,N)]
print(lista)
if x in lista:
    print(x,"esta en la lista")
else:
    print(x,"no se encontro en la lista")    

         
                  