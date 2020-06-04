#Dados dos vectores A y B, calcular un tercer vector C que almacena la suma de ellos.
N = int(input("ingrese el valor de N="))
A = [int(input("A[" + str(i) + "]=")) for i in range(0,N)]
B = [int(input("B[" + str(i) + "]=")) for i in range(0,N)]
C =[]
for i in range(len(A)):
    C.append(A[i]+B[i])

print("A=",A)
print("B=",B)
print("C=",C)