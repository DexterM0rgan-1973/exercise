#il sottoproblema del calcolo dell'area del rettangolo è costituito
#da due input (base e altezza) e un solo output (area)
import random

def proceduraCalcoloAreaRettangolo (base, altezza):
    area= base* altezza
    print (area)
    
def funzioneCalcoloAreaRettangolo (base,altezza):
    area= base*altezza
    return(area)


if __name__ == "__main__" :
    a = random.randint(1,20)
    b= random.randint(1,20)
    proceduraCalcoloAreaRettangolo(a,b)
    area = funzioneCalcoloAreaRettangolo (a,b)
    print (area)
    