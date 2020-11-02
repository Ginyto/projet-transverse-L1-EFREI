import pygame
import math
from jeu import juego
import  math

pygame.init()

#fenetre du jeu
pygame.display.set_caption("neige")
screen = pygame.display.set_mode((1280,720))

#charment du fond
fond = pygame.image.load("pic/bg/fond.jpg")
fond = pygame.transform.scale(fond,(1280,720))
rfond = fond.get_rect()

fond2 = pygame.image.load("pic/bg/fond2.jpg")
fond2 = pygame.transform.scale(fond2,(1280,720))
rfond2 = fond2.get_rect()

rfond2.x = 1280


#chargement menu
bouton = pygame.image.load("pic/start.png")
rbouton = bouton.get_rect()
rbouton.x = math.ceil(screen.get_width()/2.5)

#choix du personnage
x = 5

niveau = juego(x)

partie = True

#boucle infini
while partie:

    # collage du fond
    rfond = rfond.move(-1,0)
    rfond2 = rfond2.move(-1, 0)

    if rfond.x > -1280:
        screen.blit(fond, rfond)
        screen.blit(fond2, rfond2)

    if rfond. x == -1280:
        rfond2.x = 0
        rfond.x = 1280
        screen.blit(fond, rfond)
        screen.blit(fond2, rfond2)




    myfont = pygame.font.SysFont("", 50)
    score_display = myfont.render(str(niveau.jugador.score), 1, (0, 0, 0))
    screen.blit(score_display, (0, 0))


    #link start ?
    if niveau.link_start:
        #start
        niveau.start(screen,x)

    else:
        #bienvenue
        screen.blit(bouton, rbouton)

    # rafraichissement
    pygame.display.flip()

    #evenement
    for event in pygame.event.get():
        #sortie
        if event.type == pygame.QUIT:
            jeu = False
            pygame.quit()

        #clavier
        elif event.type == pygame.KEYDOWN:
            niveau.pressed[event.key] = True

            #detection de la touche de tir
            if event.key == pygame.K_SPACE:
                niveau.jugador.tir(x)
                if niveau.jugador.score > 500:
                    niveau.jugador.tir(x)

            elif event.key == pygame.K_s:
                niveau.jugador.tir(x+10)

                if niveau.jugador.pv - 20 > 0:
                    niveau.jugador.pv -= 20
                else:
                    niveau.death()




        elif event.type == pygame.KEYUP:
            niveau.pressed[event.key] = False

        elif  event.type == pygame.MOUSEBUTTONDOWN:
            #cliquable
            if rbouton.collidepoint(event.pos):
                niveau.hunter()







        