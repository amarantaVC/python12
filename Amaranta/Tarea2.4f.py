#f) Dados tres numeros naturales, calcular el maximo y el promedio de esos numeros.

def max(a, b, c):
    d = 0
    if (a >= b and a >= c):
        d = a
    elif (b >= a and b >= c):
        d = b
    else:
        d = c
    
    return d

def promedio(a,b,c):
    promedio = (a + b + c )/3
    return promedio

a = int(input("Ingrese el valor de a:"))
b = int(input("Ingrese el valor de b:"))
c = int(input("Ingrese el valor de c:"))

print("El maximo es:", max(a, b, c))
print("el promedio entre",str(a) + "," + str(b) + "," + str(c),"es:",promedio(a,b,c))