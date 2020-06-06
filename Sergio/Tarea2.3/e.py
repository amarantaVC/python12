# Calcular el índice académico de un trimestre. Suponga que en una secuencia de enteros de tamaño N se almacena la nota obtenida en cada materia y en otra secuencia se almacena el número de créditos correspondientes a esas materia. N representa el número de materias inscritas en el trimestre.

def indice(A, B):
    sumaPuntos, sumaCreditos, i, puntos = 0, 0, 0, []
    
    while(i < len(A)):
        puntos.append(A[i]*B[i])
        sumaPuntos += puntos[i]
        sumaCreditos += B[i]
        i += 1

    return sumaPuntos/sumaCreditos

N = int(input('Numero de materias inscritas, M = '))
Notas = [int(input('Nota[' + str(i) + '] = ')) for i in range (0, N)]
Creditos = [int(input('Creditos[' + str(i) + '] = ')) for i in range (0, N)]

print('Indice Academico: ' + str(indice(Notas, Creditos)))