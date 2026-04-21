import random
import math
import matplotlib.pyplot as plt
def media(mylist, arrotondamento=0):
    
    """
    questa funzione calcola la media di una distibuzione numerica
    parms lista: lista contenente come valore i giorni
    """

    somma=0
    for i in range (0,len(mylist)):
        somma=somma+mylist[i]
        media= somma/len(mylist)
        media=round(media,arrotondamento)
    return (media)

def riempiTemperature (lista):
    for i in range (0,24):
        lista.append(random.randint(0,20))
        
 

def varianza (media, varianza):
    """
    questa funzione calcola la varianza di una distribuzione numerica
    parms lista= lista contenente media e giorni
    """
    somma=0
    for i in range (0,len(varianza)):
        num= (lista_giorni[i]-media)**2
        somma=somma+num
        somma/(media-1)
    return (somma)

def crea_istogramma(dati, num_bins=10, titolo="Istogramma", colore="skyblue"):
    """
    Crea e visualizza un istogramma a partire da una lista o array di numeri.
 
    :param dati: Lista o array di valori numerici
    :param num_bins: Numero di intervalli (bins) dell'istogramma
    :param titolo: Titolo del grafico
    :param colore: Colore delle barre
    """
    plt.figure(figsize=(8, 5))
    plt.hist(dati, bins=num_bins, color=colore, edgecolor="black", alpha=0.7)
    plt.title(titolo)
    plt.xlabel("Valori")
    plt.ylabel("Frequenza")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
    