#Dado un vector V, calcular su norma v[1]**2 + ... + v[n]**2
import math

def normaV(vector):
    i = 0
    suma = 0
    while (i < len(vector)):
        suma += vector[i]**2
        i += 1
        
    return math.sqrt(suma)

N = int(input('N = '))
A = [int(input('A[' + str(i) + '] = ')) for i in range (0, N)]

print('||A||  = ' + str(normaV(A)))