#Dado un entero N, calcular la suma de los numeros primos menores que N. 

N = int(input("ingrese el valor de N="))
def primo(N): #funcion que indica si el num es primo o no 
    cont=0
    for i in range(1,N):#para todo i desde 1, a N verificmos 
        if (N%i==0): #un numero es primo si se puede dividir entre 1 y el mismo 
            cont+=1 # Si se puede dividir por algun numero mas de una vez, no es primo
            if cont>1:
                return False
    return True       #cuando la funcion devuelva true, el numero es primo      

suma = 0
lista = []

for i in range(2,N):
    if primo(i): #si se cumple la funcion primo entonces es primo y se incorpora a la lista y se va sumando en un contador
        lista.append(i)
        suma +=i
    else:
        pass


print("Los numeros primos menores que ", N,"son:", lista)
print("la suma de los numeros primos es", suma)        