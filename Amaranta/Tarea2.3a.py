#Dado una secuencia de caracteres de tamano N, diga cuantas veces aparece cada una de las vocales. 

palabra = str(input("ingrese la palabra:").lower())
a=0
e=0
i=0
o=0
u=0
for elemento in palabra:
    if elemento == "a":
        a= a+1
    elif elemento == "e":    
        e = e +1
    elif elemento == "i":
        i= i+1
    elif elemento =="o":
        o = o+1
    elif elemento =="u":
        u = u+1
    else:
        pass
print("hay",a,"a")                   
print("hay",e,"e")
print("hay",i,"i")
print("hay",o,"o")
print("hay",u,"u")