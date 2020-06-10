#Dadas tres matrices A, B y C de dimensión NxM, diga si C es igual a la suma de las matrices A y B.

def esSuma(A, B, C, N, M):
    i = 0
    suma = True
    while(i < N and suma):
        j = 0
        while (j < M):
            if(A[i][j] + B[i][j] != C[i][j]):
                suma = False
            j += 1
        i += 1
    return suma

# Entrada
N = int(input("Indique el numero de filas de A\nN = "))
M = int(input("Indique el numero de columnas de A\nM = "))
A = [[int(input("A["+str(i)+"]["+str(j)+"]="))for i in range(0, N)] for j in range(0, M)]
B = [[int(input("B["+str(i)+"]["+str(j)+"]="))for i in range(0, N)] for j in range(0, M)]
C = [[int(input("C["+str(i)+"]["+str(j)+"]="))for i in range(0, N)] for j in range(0, M)]

# Salida
print('¿C = A + B?\n'+str(esSuma(A, B, C, N, M)))