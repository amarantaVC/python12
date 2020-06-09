#Verificar si una fracción es irreducible. Una fracción es irreducible si el máximo común divisor del numerador y denominador es uno. El máximo común divisor de un par de números es el máximo de los divisores que dividen a ambos números.

def irreducible(x, y):
    
    i, irredX, irredY = 2, True, True

    while (i < x and irredX):
        if (x % i == 0):
            irredX = False
        i += 1

    i = 2
    while (i < y and irredY):
        if (y % i == 0):
            irredY = False
        i += 1

    if (irredX and irredY):
        return True
    else:
        return False

# ENTRADA
a = int(input('x = '))
b = int(input('y = '))

# SALIDA

print('¿ ' + str(a)+'/'+str(b) + ' es irreducible? \n'+str(irreducible(a,b)))