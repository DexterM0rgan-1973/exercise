from jarvis import *


lunedì=giorni()

print (lunedì)

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
 
calda=giornata_calda(media_lunedì,media_martedì,media_mercoledì,media_giovedì,media_venerdì,media_sabato,media_domenica)

print("la giornata più calda è", calda)
 
fredda=giornata_fredda(media_lunedì,media_martedì,media_mercoledì,media_giovedì,media_venerdì,media_sabato,media_domenica)

print("la giornata più fredda è", fredda)
 
lun =varianza(media_lunedì,lunedì)

print("la varianza del lunedi è",lun)

mart=varianza(media_martedì,martedì)

print("la varianza del martedi é",mart)

merc=varianza(media_mercoledì,mercoledì)

print("la varianza del mercoledi è ",merc)

giov=varianza(media_giovedì,giovedì)

print("la varianza del giovedi è ",giov)

ven=varianza(media_venerdì,venerdì)

print("la varianza del venerdi è ", ven)

sab=varianza(media_sabato,sabato)

print("la varianza del sabato è ",sab)

dom=varianza(media_domenica,domenica)

print("la varianza della domeinca é",dom)

deviaz_lun= deviazione_standard(lun)

print("deviazione_standard lunedì è", deviaz_lun)

deviaz_mart= deviazione_standard(mart)

print("deviazione_standard martedì è", deviaz_mart)

deviaz_merc= deviazione_standard(merc)

print("deviazione_standard mercoledì è", deviaz_merc)

deviaz_giov= deviazione_standard(giov)

print("deviazione_standard giovedì è", deviaz_giov)

deviaz_ven= deviazione_standard(ven)

print("deviazione_standard venerdì è", deviaz_ven)

deviaz_sab= deviazione_standard(sab)

print("deviazione_standard sabato è", deviaz_sab)

deviaz_dom= deviazione_standard(dom)

print("deviazione_standard domenica è", deviaz_dom)
 
moda_lunedì=moda(lunedì)

print("la moda del lunedi è ",moda_lunedì)

moda_martedì=moda(martedì)

print("la moda del martedi è ",moda_martedì)

moda_mercoledì=moda(mercoledì)

print("la moda del mercoledi è ",moda_mercoledì)

moda_giovedì=moda(giovedì)

print("la moda del giovedi è ",moda_giovedì)

moda_venerdì=moda(venerdì)

print("la moda del venrdi è ",moda_venerdì)

moda_sabato=moda(sabato)

print("la moda del sabato è ",moda_sabato)

moda_domenica=moda(domenica)

print("la moda della doomenica è ",moda_domenica)
 
errore_lun=errore_standard(lun,lunedì)

print("l'errore standard lunedi :",errore_lun)

errore_mart=errore_standard(mart,martedì)

print("l'errore standard martedi :",errore_mart)

errore_merc=errore_standard(merc,mercoledì)

print("l'errore standard mercoledi :",errore_merc)

errore_giov=errore_standard(giov,giovedì)

print("l'errore standard giovedi :",errore_giov)

errore_ven=errore_standard(ven,venerdì)

print("l'errore standard venrdi:",errore_ven)

errore_sab=errore_standard(sab,sabato)

print("l'errore standard sabato :",errore_sab)

errore_dom=errore_standard(dom,domenica)

print("l'errore standard domenica :",errore_dom)
 
 
crea_istogramma(lunedì)

 