#Dada una secuencia de enteros, calcular la suma de ellos, el total de numeros
#positivos y el promedio de los valores positivos.
N = int(input("ingrese el valor de N="))
A = [int(input("A[" + str(i) + "]=")) for i in range(0,N)]
print(A)

def suma(N):
    suma=0
    for i in A:
        suma = suma + i
    return(suma)
posi = 0
prome = 0
for i in A:
    suma(i)
    if i >= 0:
        posi += 1
        prome += i
promedio = (prome /posi) 

print("la suma de los valores en A es=" ,suma(i))
print("el total de numeros positivos es=",posi)
print("el promedio de los valores positivos es=",promedio)

        