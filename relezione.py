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
 
def varianza (media_lunedi,lunedi):
    for i in range(24):
        lun=lunedi[i]-media_lunedi
        return(lun)
def varianza (media_martedi,martedi):
    for i in range(24):
        mar=martedi[i]-media_martedi
        return(mar)
def varianza (media_mercoledi,mercoledi):
    for i in range(24):
        mer=mercoledi[i]-media_mercoledi
        return(mer)
def varianza (media_giovedi,giovedi):
    for i in range(24):
        gio=giovedi[i]-media_giovedi
        return(gio)
def varianza (media_venerdi,venerdi):
    for i in range(24):
        ven=venerdi[i]-media_venerdi
        return(ven)
def varianza (media_sabato,sabato):
    for i in range(24):
        sab=sabato[i]-media_sabato
        return(sab)
def varianza (media_domenica,domenica):
    for i in range(24):
        dom=domenica[i]-media_domanica
        return(dom)
 
if__name__=="__main__":
    lunedì=giorni()
    print lunedi
    martedì=giorni()
    print martedi
    mercoledì=giorni()
    print mercoledi
    giovedì=giorni()
    print giovedi
    venerdì=giorni()
    print venerdi
    sabato=giorni()
    print sabato
    domenica=giorni()
    print domenica
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
    lun=varianza_lunedi(media_lunedi,lunedi)
    mar=varianza_martedi(media_martedi,martedi)
    mer=varianza_mercoledi(media_mercoledi,mercoledi)
    gio=varianza_giovedi(media_giovedi,giovedi)
    ven=varianza_venerdi(media_venerdi,venerdi)
    sab=varianza_sabato(media_sabato,sabato)
    dom=varianza_domenica(media_domenica,domenica)