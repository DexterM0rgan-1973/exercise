import pygame
import random
import math
 
# --- Inizializzazione ---

pygame.init()
LARGHEZZA = 500
ALTEZZA = 250
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Colpisci i cerchi")
clock = pygame.time.Clock()
 
# --- Variabili ---

punteggio = 0
 
c1={
    "x" : 50,
    "y" : 50,
    "colore" : (255,0,0),
    "raggio" : 25
    }

c2={
    "x" : 150,
    "y" : 50,
    "colore" : (0,255,0),
    "raggio" : 25
    }

c3={
    "x" : 250,
    "y" : 50,
    "colore" : (0,0,255),
    "raggio" : 25
    }
 
cerchi = [c1,c2,c3]# lista di cerchi: [x, y, colore, raggio]
 
 
# --- Funzioni ---

def disegna_cerchi(lista_cerchi):
    """Disegna tutti i cerchi"""
    for cerchio in lista_cerchi:
        pygame.draw.circle(schermo,cerchio["colore"],(cerchio["x"],cerchio["y"]),cerchio["raggio"])
    # TODO: ciclo for per disegnare i cerchi con pygame.draw.circle
 
 
def sposta_cerchi(lista_cerchi, speed):
    """Aggiorna posizione verticale"""
    global punteggio
    for cerchio in lista_cerchi:
        cerchio["y"] += speed
        if cerchio["y"]-cerchio["raggio"] >= ALTEZZA:
            cerchio["y"]=0
            punteggio -= 1
    # TODO: far scendere i cerchi
    # TODO: se un cerchio tocca il fondo, riportarlo in alto e togliere 1 punto
 
 
def aggiungi_cerchio(lista_cerchi):
    """Aggiunge un nuovo cerchio in alto con valori casuali"""
    x=random.randint(0, LARGHEZZA)
    y=0
    colore=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    c = {
        "x" : x,
        "y" : y,
        "colore" : colore,
        "raggio" : 25
        }
    lista_cerchi.append(c)
    # TODO: posizione x casuale tra 0 e LARGHEZZA, y=0
    # TODO: colore casuale
    # TODO: raggio fisso (es. 25)
    # TODO: aggiungerlo alla lista
 
 
def premi_cerchi(lista, pos_mouse):
    """Controlla se il clic è dentro un cerchio"""
    global punteggio
    for cerchio in lista:
        distanza=math.sqrt((cerchio["x"]-pos_mouse[0])**2+(cerchio["y"]-pos_mouse[1])**2)
        if distanza <= cerchio["raggio"]:
            punteggio += 1
            lista.remove(cerchio)
    # TODO: calcolare distanza mouse-centro
    # TODO: se distanza <= raggio → punteggio +1 e rimuovere il cerchio
 
 
# --- Ciclo principale ---

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            premi_cerchi(cerchi, event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aggiungi_cerchio(cerchi)
 
    sposta_cerchi(cerchi, 2)
 
    schermo.fill((255,255,255))
    disegna_cerchi(cerchi)
 
    # Punteggio
    font = pygame.font.SysFont(None, 40)
    testo = font.render(f"Punteggio: {punteggio}", True, (0,0,0))
    schermo.blit(testo, (10,10))
 
    pygame.display.flip()
    clock.tick(30)
 
pygame.quit()