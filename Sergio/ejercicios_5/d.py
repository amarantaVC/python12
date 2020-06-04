#Dadas tres variables enteras a, b y c con valores diferentes, determinar el valor maximo y almacenarlo en d.

def max(a, b, c):
    d = 0
    if (a >= b and a >= c):
        d = a
    elif (b >= a and b >= c):
        d = b
    else:
        d = c
    
    return d

a, b, c = 9, 9, 9

print(max(a, b, c))


