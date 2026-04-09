#una stazione meteo ha registrato le temperature di ogni ora per 7 giorni
#devi calcolare statistiche giornaliere e trovare la giornata più calda e fredda
#della settimana. struttura dati: lista di liste (7/24)
 
import random
def giorni():
    mylist=[]
    for i in range (0,24):
        elemento=random.randint (2,20)
        mylist.append(elemento)
    return (mylist)
 
def media(mylist, arrotondamento=0):
    somma=0
    for i in range (0,len(mylist)):
        somma=somma+mylist[i]
        media= somma/len(mylist)
        media=round(media,arrotondamento)
    return (media)
 

def varianza (media, lista_giorni):
    somma=0
    for i in range (0,len(lista_giorni)):
        num= (lista_giorni[i]-media)**2
        somma=somma+num
        somma/(media-1)
    return (somma)
    



lunedì=giorni()
print(lunedì)
martedì=giorni()
print (martedì)
mercoledì=giorni()
print (mercoledì)
giovedì=giorni()
print (giovedì)
venerdì=giorni()
print (venerdì)
sabato=giorni()
print (sabato)
domenica=giorni()
print (domenica)

media_lunedì=media(lunedì)
print("la media del lunedì è ", media_lunedì)
media_martedì=media(martedì)
print("la media del martedì è ", media_martedì)
media_mercoledì=media(mercoledì)
print("la media del mercoledì è ", media_mercoledì)
media_giovedì=media(giovedì)
print("la media del giovedì è ", media_giovedì)
media_venerdì=media(venerdì)
print("la media del venerdì è ", media_venerdì)
media_sabato=media(sabato)
print("la media del sabato è ", media_sabato)
media_domenica=media(domenica)
print("la media del domenica è ", media_domenica)

print ("la varianza del lunedì é", lunedì)
print ("la varianza del martedì é", martedì)
print ("la varianza del mercoledì é", mercoledì)
print ("la varianza del giovedì é", giovedì)
print ("la varianza del venerdì é", venerdì)
print ("la varianza del sabato é", sabato)
print ("la varianza del domenica é", domenica)