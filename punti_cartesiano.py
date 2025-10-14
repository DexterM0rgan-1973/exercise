#dato un insieme di 20 punti su un piano cartesiano
#random compresi nell'intervallo 0,10 calcolare il punto
#con ascissa massima e il punto con ordinata minima

import random
x=[]
y=[]

for i in range (0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
#ascissa massima?
#scorrere la lista delle x, trovare il massimo e salvarlo in indice
indice_max=0
massimo=x[0]
for i in range (1,20):
    if x[i]>massimo:
        massimo=x[i]
        indice_max=i
    

print(massimo,y[indice_max])

indice_min=0
minimo=y[0]
for i in range (1,20):
    if x[i]<minimo:
        minimo=x[i]
        indice_min=i
print(minimo,x[indice_min])


    




punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
#accedere alla x del primo punto
print(punti_cartesiano[0][0])
#accedere alla y del primo punto
print(punti_cartesiano[0][1])