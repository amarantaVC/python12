#Dado un vector V, calcular su norma; es decir ka raiz de la suma de sus elementos alc uadrados
N=int(input("ingrese el valor de N="))
V = [int(input("V[" + str(i) + "]=")) for i in range(0,N)]
print("V=",V)

i = 0
suma = 0
norma = 0
while i < N:
    suma = suma + (V[i])**2
    i = i+1

norma = (suma)**0.5

print("la norma del vector V es =", norma)


