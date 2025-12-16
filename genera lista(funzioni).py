#scrivere un programma che generi una lista di numeri
#casuali compresi tra 1 e 100 che rappresentano
#misurazioni di intensità di un segnale. il programma dopo
#aver generato la lista deve essere in grado di modificarla in questa maniera
#gli elementi di indice pari devono essere azzerati. inoltre, dopo la modifica,
#si vuole contare il numero di elementi dopra una soglia numerica.
#sottoproblemi:
#1)genrare una lista di numeri compresi tra 1 e 100
#2)modificare la lista con la regola sopra
#3)contare il numero di elementi sopra soglia

import random

def generaLista (n):
    myList=[]
    for i in range (0,n):
        elemento=random.randint(1,100)
    myList.append(elemento)
    return(myList)

#oppure
def proceduraGeneraLista (n,lista):
    for i in range (0,n):
        elemento=random.randint(1,100)
        lista.append(elemento)

def modificaLista(lista):
    n=len(lista)
    for i in range(0,n):
        if i%2==0:
            lista[i]=0
            
            
def soglia (lista,nsoglia):
    n=len(lista)
    contatore=0
    for i in range (0,n):
        if lista [i]>nsoglia:
            contatore=contatore+1
    return(contatore)
    
listax=generaLista(6)
listap=[]
proceduraGeneraLista(6,listap)
proceduraGeneraLista(lista=listap,n=6)
modificaLista (listax)
nsoglia=soglia(listax,50)