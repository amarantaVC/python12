#Dados dos vectores A y B, calcular un tercer vector C que almacena la suma de ellos. Suponga que los vectores se almacenan en dos secuencias de valores reales

def sumaVectores(a, b):
    i = 0
    suma = []
    while (i < len(a)):
        suma.append(a[i]+b[i])
        i += 1
    
    return suma

N = int(input('Ingrese el valor de N = '))
A = [int(input('A[' + str(i) + '] = ')) for i in range(0, N)]
B = [int(input('A[' + str(i) + '] = ')) for i in range(0, N)]

print('Vector C = '+ str(sumaVectores(A, B)))