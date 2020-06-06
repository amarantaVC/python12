#Dado una secuencia de caracteres de tamano N, diga cuantas veces aparece cada una de las vocales.

def contadorVocales(lista):
    contadores = [0, 0, 0, 0, 0] # 5 vocales, 5 contadores
    i = 0
    while (i < len(lista)):
        if(sec[i] == 'a'):
            contadores[0] += 1
        elif(sec[i] == 'e'):
            contadores[1] += 1
        elif (sec[i] == 'i'):
            contadores[2] += 1
        elif (sec[i] == 'o'):
            contadores[3] += 1
        elif (sec[i] == 'u'):
            contadores[4] += 1
        i += 1
    return contadores

sec = raw_input("Ingrese una secuencia: ").lower()
for i in range(0, len(contadorVocales(sec))):
    if (i == 0):
        print('La letra a se repite: '+str(contadorVocales(sec)[i]))
    elif(i == 1):
        print('La letra e se repite: '+str(contadorVocales(sec)[i]))
    elif(i == 2):
        print('La letra i se repite: '+str(contadorVocales(sec)[i]))
    elif (i == 3):
        print('La letra o se repite: '+str(contadorVocales(sec)[i]))
    else:
        print('La letra u se repite: '+str(contadorVocales(sec)[i]))