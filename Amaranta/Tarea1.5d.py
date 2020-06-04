#Dadas tres variables enteras a, b y c con valores diferentes, determinar el valor maximo y almacenarlo en d y el promedio de esos numeros
A = int(input("Ingrese el valor de A:"))
B = int(input("Ingrese el valor de B:"))
C = int(input("Ingrese el valor de C:"))

assert(A != B != C)
D = 0
if A > B and B > C:
    D = A  
    
elif B > C and C > A:
    D = B 

elif C > A and A > B:
    D = C

elif C > B and B > A:
    D = C

elif B > A and A > C:
    D = B

elif A > C and C > B:
    D = A

def promedio(A,B,C):
    promedio = (A + B + C)/2
    return(promedio)    
print ("el Valor maximo es", D)  
print("El promedio entre", A,B,C,"Es =",promedio(A,B,C))  


        

    