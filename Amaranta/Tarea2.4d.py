#Dados dos numeros naturales, decidir si uno es divisor del otro. 

a=int(input("ingrese el valor de a:"))
b=int(input("ingrese el valor de b:"))

if (a%b == 0):
    print(b, "es divisor de", a)
elif (b%a == 0):
    print(a, "es divisor de",b)
else:
    print("ninguno es divisor del otro")        