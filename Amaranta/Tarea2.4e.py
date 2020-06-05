#Calcular las raices de una ecuación cuadrada Ax2+Bx+C
import math
print("este programa calcula las raices del polinimio de la forma AX2 + BX + C")  

a = float(input("inserte valor de termino cuadratico="))
b = float(input("inserte valor de termino lineal="))
c = float(input("insert valor de termino independiente="))
print(str(a)+"x^2"+"+"+str(b)+ "x"+"+"+str(c))
determinante = ((b**2) - (4*(a*c)))

raiz1=0
raiz2=0
if determinante > 0:
        raiz1=((-1*b)+math.sqrt(determinante)) // (2*a)
        raiz2=((-1*b)-math.sqrt(determinante)) // (2*a)	
        print("las raices del polinomio son:",raiz1,raiz2)
if determinante == 0:
    raiz1=((-1*b)+math.sqrt(determinante)) // (2*a)  
    print("ambas raices son iguales a:")
if determinante <0:
    print("el polinomio no posee raices reales")    