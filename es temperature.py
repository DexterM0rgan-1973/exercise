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



if __name__=="__main__" :
    
    lunedi=giorni()
    print (lunedi)
    martedi=giorni()
    print (martedi)
    mercoledi=giorni()
    print (mercoledi)
    giovedi=giorni()
    print (giovedi)
    venerdi=giorni()
    print (venerdi)
    sabato=giorni()
    print (sabato)
    domenica=giorni()
    print (domenica)
    
    media_lunedi=media(lunedi)
    print("la media del lunedi è ", media_lunedi)
    media_martedi=media(martedi)
    print("la media del martedi è ", media_martedi)
    media_mercoledi=media(mercoledi)
    print("la media del mercoledi è ", media_mercoledi)
    media_giovedi=media(giovedi)
    print("la media del giovedi è ", media_giovedi)
    media_venerdi=media(venerdi)
    print("la media del venerdi è ", media_venerdi)
    media_sabato=media(sabato)
    print("la media del sabato è ", media_sabato)
    media_domenica=media(domenica)
    print("la media del domenica è ", media_domenica)


