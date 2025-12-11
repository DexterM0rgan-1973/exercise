#si vuole creare un programma che leggendo da un file di testo contenente una serie
#di valori misurati di temperatura, calcoli la media, varianza e la mediana della distribuzione

#sottoproblema:
#1) leggere il file riga per riga e creare una lista
#2) calcolo della media della lista
#3) calcola la varianza di una lista
#4) calcola la mediana di una lista

def creaLista (lista):
    temperature = []
    with open(lista) as f:
        for line in f:
            elemento= int(line.strip())
            temperature.append(elemento)
    return (temperature)

lista= creaLista("temperature.csv")

#media con iterator    
def media_iterator(lista):
    somma=0
    for element in lista:
        somma= somma+element
    media_c=somma/len(lista)
    print(media_c)
#media senza iterator    
def media(lista):
    somma=0
    for i in range (0,len(lista)):
        somma= somma+lista[i]
    media_c=somma/len(lista)
    print(media_c)


#richiamo la funzione
lista = creaLista("temperature.csv")
#richiamo la procedura
media(lista)
media_iterator(lista)


def varianza (lista):
    
    