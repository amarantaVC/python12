#Dadas dos matrices, una NxM y otra MxN, dice si la primera matriz es la traspuesta de la segunda.

def transpuesta(A, B, N, M):

    esTrans = True
    i = 0
    while (i < N and esTrans):
        j = 0
        while(j < M and esTrans):
            if (A[i][j] != B[j][i]):
                esTrans = False
            j += 1
        i += 1 

    return esTrans

# Entrada
N = int(input("Indique el numero de filas de A:"))
M = int(input("Indique el numero de columnas de A:"))
A = [[int(input("A["+str(i)+"]["+str(j)+"]="))for i in range(0, N)] for j in range(0, M)]
B = [[int(input("B["+str(k)+"]["+str(l)+"]="))for k in range(0, M)] for l in range(0, N)]

# Salida
print('A = ' + str(A)+'\nB = ' + str(B)+'\n ¿B es transpuesta de A?\nR: '+str(transpuesta(A,B,N,M)))