#Dadas dos matrices, una NxM y otra MxN, dice si la primera matriz es la traspuesta de la
#segunda. #Valores iniciales:
F1= int(input("Indique el numero de filas de A:"))
C1= int(input("Indique el numero de columnas de A:"))
F2 = int(input("Indique el numero de filas de B:"))	
C2= int(input("Indique el numero de columnas de B:"))
A=[[int(input("A["+str(i)+","+str(j)+"]="))for i in range(0,F1)] for j in range(0,C1)]
B=[[int(input("B["+str(k)+","+str(l)+"]="))for k in range(0,F2)] for l in range(0,C2)]

#inicializamos las variables
i,j,k,l = 0,0,0,0

transpuesta = True 

while i < F1 and j < C1:
    while k < F2 and l < C2:
        if A[i][j] != B[l][k]:
            transpuesta =  False
        elif A[i][j] == B[l][k]: 
            pass 
        else:
            pass 
        j = j+1
        l = l+1
    i = i+1
    k = k+1 


if transpuesta == True:
    print("La matriz B es la Transpuesta de A")
else:
    print("La matriz B no es la transpuesta de A")    

print("A:", A)
print("B:", B)
