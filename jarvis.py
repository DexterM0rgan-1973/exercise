import random

import math

import matplotlib.pyplot as plt
 
 
def giorni():

    mylist=[]

    for i in range (25):

        elemento=random.randint (3,26)

        mylist.append(elemento)

    return (mylist)
 


def media(mylist, arrotondamento=0):

    somma=0

    for i in range (0,len(mylist)):

        somma=somma+mylist[i]

        media= somma/len(mylist)

        media=round(media,arrotondamento)

    return (media)
 
"""

questa funzione calcola la mediaa d i un distribuzione numeri

parms: mylist:mylist contiene come valore chiave il giorno e come valore lista di misurazzioni

parms:arrotondament: arrotonda le medie

"""
 
def giornata_calda(media_lunedì,media_martedì,media_mercoledì,media_giovedì,media_venerdì,media_sabato,media_domenica):

    calda=media_lunedì

    giornata="lunedi"

    if media_martedì>calda:

        calda=media_martedì

        giornata="martedi"

    if media_mercoledì>calda:

        calda=media_mercoledì

        giornata="mercoledi"

    if media_giovedì>calda:

        calda=media_giovedì

        giornata="giovedi"

    if media_venerdì>calda:

        calda=media_venerdì

        giornata="venerdi"

    if media_sabato>calda:

        calda=media_sabato

        giornata="sabato"

    if media_domenica>calda:

        calda=media_domenica

        giornata="domenica"

    return giornata


def giornata_fredda(media_lunedì,media_martedì,media_mercoledì,media_giovedì,media_venerdì,media_sabato,media_domenica):

    fredda=media_lunedì

    giornata="lunedi"

    if media_martedì<fredda:

        calda=media_martedì

        giornata="martedi"

    if media_mercoledì<fredda:

        calda=media_mercoledì

        giornata="mercoledi"

    if media_giovedì<fredda:

        calda=media_giovedì

        giornata="giovedi"

    if media_venerdì<fredda:

        calda=media_venerdì

        giornata="venerdi"

    if media_sabato<fredda:

        calda=media_sabato

        giornata="sabato"

    if media_domenica<fredda:

        calda=media_domenica

        giornata="domenica"

    return giornata
 
def varianza(media,lista_giorni):

    somma=0

    for i in range(0,len(lista_giorni)):

        num=(lista_giorni[i]-media)**2

        somma=somma+num

        somma/(media-1)

    return somma
 
"questa funzione calcola la varianza"

"params:media"

"params:lista_giorni"

def deviazione_standard(varianza):

    return varianza **0.5

def moda(lista):

    moda=0

    massimo=0

    for i in range (len(lista)):

        contatore=0

        for element in range(len(lista)):

             if lista[i]==lista[element]:

                contatore=contatore+1

        if contatore> massimo:

                massimo = contatore

                moda=lista[i]

    return moda

def errore_standard(varianza,lista):

    errore_standard=varianza/len(lista)

    return errore_standard
 
 
 
def crea_istogramma(dati, num_bins=10, titolo="Istogramma", colore="skyblue"):

    """

    Crea e visualizza un istogramma a partire da una lista o array di numeri.

    :param dati: Lista o array di valori numerici

    :param num_bins: Numero di intervalli (bins) dell'istogramma

    :param titolo: Titolo del grafico

    :param colore: Colore delle barre

    """

    plt.figure(figsize=(8, 5))  # dimenzioni grafico

    plt.hist(dati, bins=num_bins, color=colore, edgecolor="black", alpha=0.7)

    plt.title(titolo) #titolo grafico

    plt.xlabel("Valori") # eltichette asse cartesiano 

    plt.ylabel("Frequenza")

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()

 