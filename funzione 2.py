#scrivere una funzione che dati 2 numeri interi restituisca il maggiore

def nMag(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
#scrivere una procedura che dato un numero intero stampi a video
#se è pari o dispari
    
def nPD (num1):
    if num1%2==0:
        print("il numero è pari")
    else:
        print("il numero è dispari")
        
uno=input("inserire il primo numero")
uno=int(uno)
due=input("inserire il secondo numero")
due=int(due)

ris=nMag(uno,due)
print(ris)
nPD(ris)



#scrivere un programma che dati due  interi stampi a video se il maggiore
#è pari o dispari









