import pygame
import random


#creation de la classe monstre
class monstro(pygame.sprite.Sprite):

    #chargement des données
    def __init__(self, jeu, x):
        super().__init__()
        self.jeu = jeu

        #caracteristiques
        self.pv = 100
        self.pv_max = 100

        if x == 1:
            self.image = pygame.image.load("pic/mechants/mrouge.png")
            self.pv += 25
            self.pv_max += 25
            self.degat = [0.5, 0.8]
        elif x == 2:
            self.image = pygame.image.load("pic/mechants/spooky.png")
            self.degat = [1, 2, 3]

        elif x == 3:
            self.image = pygame.image.load("pic/mechants/death.png")
            self.degat = [0, 0, 5]

        elif x == 4:
            self.image = pygame.image.load("pic/mechants/squid.png")
            self.degat = [3, 3, 4]

        self.vitesse = random.randint(1,4)


        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0,300)
        self.rect.y = random.randint(0, 580)


    def dommage(self, degats):
        #degat
        self.pv -= degats

        #mort
        if self.pv <= 0:
            #respawn
            self.rect.x = 1150 + random.randint(0,300)
            self.rect.y = random.randint(0, 580)
            self.pv = self.pv_max
            self.jeu.jugador.score += 50
            if self.jeu.jugador.pv < 100:
                self.jeu.jugador.pv += 5

            if self.jeu.jugador.score == 100:
                self.jeu.spawn_monster()
            if self.jeu.jugador.score == 200:
                self.jeu.spawn_monster()
            if self.jeu.jugador.score == 300:
                self.jeu.spawn_monster()
            if self.jeu.jugador.score == 400:
                self.jeu.spawn_monster()
            if self.jeu.jugador.score == 500:
                self.jeu.spawn_monster()





    def gestion_pv(self, surface):
        #dessinage de la barre de pv
        pygame.draw.rect(surface, (50,50,50), [self.rect.x+12, self.rect.y-10, self.pv_max, 5])
        pygame.draw.rect(surface, (255,0,0), [self.rect.x+12, self.rect.y-10, self.pv, 5])




    def avancer(self):
        #si aucune collision
        if not self.jeu.detection_collision(self, self.jeu.all_joueurs):
            self.rect.x -= self.vitesse
        #si collision
        else:
            #dommage
            self.jeu.jugador.dommage(random.choice(self.degat))

        if self.rect.x < -100:
            self.rect.x = 1150 + random.randint(0, 300)
            self.rect.y = random.randint(0, 580)
            self.pv = self.pv_max

            if self.jeu.jugador.pv - 15 > 0:
                self.jeu.jugador.pv -= 15
            else:
                # death
                self.jeu.death()








