#Dadas tres matrices A, B y C de dimensión NxM, diga si C es igual a la suma de las matrices A y B
"""ALERTA: Recuerden que la suma de matrices de acepta matrices de tamaños distintos entre si"""
N = int(input("ingrese el valor de N:"))
M = int(input("ingrese el valor de M:"))
A=[[int(input("A["+str(i)+","+str(j)+"]="))for i in range(0,N)] for j in range(0,M)]

B=[[int(input("B["+str(i)+","+str(j)+"]="))for i in range(0,N)] for j in range(0,M)]
C=[[int(input("C["+str(i)+","+str(j)+"]="))for i in range(0,N)] for j in range(0,M)]
print("A=",A)
print("B=",B)
print("C=",C)
i,j=0,0
suma = True 
while i<N and j<M:
    if C[i][j] != A[i][j]+B[i][j]:
        suma = False

    else:
        C[i][j] == A[i][j] + B[i][j]
        pass    
    i = i+1
    j= j+1

if suma == False:
    print("La Matriz C no es la suma de A +B")
else:
    print("La Matric C es la suma A + B")    

