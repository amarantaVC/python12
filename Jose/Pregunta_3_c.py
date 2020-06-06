# Dados dos vectores A y B, calcular un tercer
# vector C que almacena la suma de ellos. Suponga
# que los vectores se almacenan en dos secuencias
# de valores reales

N = int(input(" ingrese el tamano deL vector A: "))
A = [ int(input("A [" + str(i) +"] = " ))  for i in range(0,N) ]
M = int(input(" ingrese el tamano del vector B: "))
B = [ int(input("B [" + str(i) +"] = " ))  for i in range (0,M)]

C = []
if N > M:
	for i in range (0, N):
		C.append(A[i])
	for i in range (0, M):
		C[i] = C[i] + B[i]

elif N < M:
	for i in range (0, M):
		C.append(B[i]) 
	for i in range (0,N):
		C[i] = C[i] + A[i]

elif N == M:
	for i in range (0, N):
		C.append( A[i] + B[i])


print(A)
print(B)
print(" la suma de los vectores es: " + str(C) )
