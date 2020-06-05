#Dado el valor del lado de un cuadrado, calcular el perimetro y el area. 
#El perimetro de un cuadrado es cuatro veces el valor del lado
#El area de un cuadrado es igual al cuadrado de la longitud del lado.

lado = int(input("ingrese el valor del Lado del cuadrado="))
perimetro = 4*lado
area = (lado)**2

print("el lado del cuadrado es:" + str(lado))
print("su perimetro es:", perimetro)
print("su area es:",area)