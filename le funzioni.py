#scrivere una funzione che data un lista stampi a video il numero
#degli elementi pari

def sommaLista (lista): 
    somma=0
    for element in lista:
        somma = somma + element
    print(somma)
    
def numeriPari (lista):
    contatore= 0
    for element in lista:
        if element%2==0:
            contatore=contatore+1
    print(contatore)

lista = [1,2,3,4]
sommaLista(lista)
lista2 = [2,3,4,5]
sommaLista (lista)
numeriPari(lista)
numeriPari(lista2)