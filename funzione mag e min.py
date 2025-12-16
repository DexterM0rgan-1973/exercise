#scrivere un programma che calcoli il minimo e il massimo di una lista
#di interi random compresi nell' intervall0 0,100

#sottoproblemi: 1) calcolare il minimo di una lista
#				2) calcolare il massimo di una lista
#				3) generare una lista di n numeri random nell'intervallo 0,100

import random
def generaLista(n):
    myList=[]
    for i in range (0,n):
        elemento = random.randint(0,100)
        myList.append(elemento)
    return(myList)
    
def minimoLista(lista,n):
    massimo=lista[0]
    for i in range (1,n):
        if lista[i]>massimo:
            massimo=lista[i]
    print(massimo)


if __name__=="__main__":
    dimensione=10
    listaB=generaLista(10)
    minimoLista(listaB,10)
    massimoLista(listaB,10)
