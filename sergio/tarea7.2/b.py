#Dado una matriz A de dimensión NxN, determine si A es una matriz perfecta. Se dice que una matriz es perfecta si cada una de sus filas y cada una de sus columnas suman lo mismo.

def perfecta(A, N):

    aux, perf = 0, True
    i = 0
    while (i < N and perf):

        j, sumaF, sumaC = 0, 0, 0
        while (j < N and perf):
            sumaF += A[i][j]
            sumaC += A[j][i]
            j += 1

        if(i == 0):
            aux = sumaF                
        if(sumaF != sumaC or sumaF != aux):
            perf = False
        
        i += 1

    return perf

N = int(input("Indique el numero de filas de A\nN = "))
A = [[int(input("A["+str(i)+"]["+str(j)+"]="))for i in range(0, N)] for j in range(0, N)]

print(perfecta(A,N))
