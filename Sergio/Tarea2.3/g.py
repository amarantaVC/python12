#Determinar la distribución mínima en billetes y monedas para una suma de dinero. Asuma que los billetes son de las denominaciones Bs.100, Bs.50, Bs.20, Bs.10, Bs.5 y las monedas Bs.2 y Bs.1.


def distrMinima(cantidad):

    monedas = [0, 0, 0, 0, 0, 0, 0]

    while(cantidad != 0):
        if(cantidad % 100 == 0):
            monedas[0] += 1
            cantidad -= 100
        elif(cantidad % 50 == 0):
            monedas[1] += 1
            cantidad -= 50
        elif(cantidad % 20 == 0):
            monedas[2] += 1
            cantidad -= 20
        elif(cantidad % 10 == 0):
            monedas[3] += 1
            cantidad -= 10
        elif(cantidad % 5 == 0):
            monedas[4] += 1
            cantidad -= 5
        elif(cantidad % 2 == 0):
            monedas[5] += 1
            cantidad -= 2
        elif(cantidad % 1 == 0):
            monedas[6] += 1
            cantidad -= 1

    return monedas

# ENTRADA
cantidad = int(input('Cantidad = '))

# SALIDA
for i in range(0, cantidad):
    if(i == 0 and distrMinima(cantidad)[i] != 0):
        print('Billetes de 100: ' + str(distrMinima(cantidad)[i]))
    elif(i == 1 and distrMinima(cantidad)[i] != 0):
        print('Billetes de 50: ' + str(distrMinima(cantidad)[i]))
    elif(i == 2 and distrMinima(cantidad)[i] != 0):
        print('Billetes de 20: ' + str(distrMinima(cantidad)[i]))
    elif(i == 3 and distrMinima(cantidad)[i] != 0):
        print('Billetes de 10: ' + str(distrMinima(cantidad)[i]))
    elif(i == 4 and distrMinima(cantidad)[i] != 0):
        print('Billetes de 5: ' + str(distrMinima(cantidad)[i]))
    elif(i == 5 and distrMinima(cantidad)[i] != 0):
        print('Monedas de 2: ' + str(distrMinima(cantidad)[i]))
    elif(i == 6 and distrMinima(cantidad)[i] != 0):
        print('Monedas de 1: ' + str(distrMinima(cantidad)[i]))