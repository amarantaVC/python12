#Dada una secuencia de caracteres sec y un entero r devolver en la variable secRot la secuencia rotada r posiciones a la derecha. Ejemplo: si sec="abbcd" y r=3 entonces en secRot="bcdab"

sec = raw_input("Ingrese una secuencia de letras:")
N = int(input("Ingrese el numero de rotaciones hacia la derecha: "))

i = 0
newText = ''
aux = sec
while (i < N):
    newText = aux[len(sec)-1]
    newText += aux[:len(sec)-1]
    aux = newText
    i += 1

print(aux)