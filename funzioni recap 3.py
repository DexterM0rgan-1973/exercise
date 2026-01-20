#scrive un programma che dati 2 numeri
#interi random in un intervallo 0,100 ne calcoli
#la somma, la differenza e controlli se la
#differenza è minore di una certa soglia fissata
#a priori nel main.

#sottoproblemi:
#1) somma di due numeri (procedura)
#2) differenza tra 2 numeri (funzione)
#3) verificare se un numero é minore di una soglia (procedura)

import random

def proceduraSomma ( a,b):
    somma= a+b
    print (somma)

if __name__ == "__main__":
    uno= random.randint (0,100)
    due= random.randint (0,100)
    proceduraSomma(uno,due)
   

