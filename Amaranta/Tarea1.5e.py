#Dado un numero n calcule la suma de los cuadrados entre 0 y n, almacene el resultado en la
#variable d. 

N = int(input("ingrese el valor de N:"))

def cuadrado(N):
    D =  N**2
    return(D)
    
L=[]
A = [] 
suma= 0 

for i in range(1,N+1):#le digo que inicie en 1 porque 0^2 es 0 y que llegue hasta N+1 para que tome en cuenta a N
    L.append(i)
    A.append(cuadrado(i))
    suma = suma + cuadrado(i)

print("valores :",L)
print("cuadrado de los valores:",A)
print("suma se los cuadrados es:", suma)


