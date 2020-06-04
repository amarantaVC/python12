#calcular indice de trimeste: est se calcula (notaMateria x creditos Materia)/ creditos total

N = int(input("ingrese el  numeros de materiass inscritas="))
nota = [int(input("NotaMateria[" + str(i) + "]=")) for i in range(0,N)]
creditos = [int(input("CreditosMateria[" + str(i) + "]=")) for i in range(0,N)]
multi = []
credicars = 0
for i in range(len(nota)):
        multi.append( nota[i] * creditos[i])
        credicars = credicars + creditos[i]
multisuma=0
for i in range(len(multi)):
        multisuma= (multisuma+ multi[i])
total = 0
total = multisuma / credicars


print("Notas:",nota)
print("Creditos:",creditos)        
print("Notas x Creditos",multi)
print("Suma total de Notas x creditos=", multisuma)
print(" creditos del trimestre=", credicars)
print("Tu indice academico del trimestre es=", total)