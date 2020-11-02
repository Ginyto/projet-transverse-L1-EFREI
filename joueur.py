import pygame
from projectile import disparo
import random


# creation de la class joueur
class jugador(pygame.sprite.Sprite):

    def __init__(self, jeu, x):
        super().__init__()
        self.jeu = jeu

        # vie
        self.pv = 100
        self.pv_max = 100

        # caracteristiques
        self.vitesse = 4
        self.all_tir = pygame.sprite.Group()

        # sprite
        if x == 1:
            self.image = pygame.image.load("pic/persos/dragon.png")
        if x == 2:
            self.image = pygame.image.load("pic/persos/archer.png")
        if x == 3:
            self.image = pygame.image.load("pic/persos/cam.png")
        if x == 4:
            self.image = pygame.image.load("pic/persos/usopp.png")
        if x == 5:
            self.image = pygame.image.load("pic/persos/ninja.png")
            self.image = pygame.transform.scale(self.image, (125,125))


        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 580
        self.score = 0

    def dommage(self, degats):
        #degat
        if self.pv - degats > degats:
            self.pv -= degats
        else:
            #death
            self.jeu.death()


    def gestion_pv(self, surface):
        #dessinage de la barre de pv
        pygame.draw.rect(surface, (50,50,50), [self.rect.x+16, self.rect.y-20, self.pv_max, 5])
        pygame.draw.rect(surface, (62,189,151), [self.rect.x+16, self.rect.y-20, self.pv, 5])

    def tir(self,x):
        #creer un nouveaux projectile
        self.all_tir.add(disparo(self,x))

    def droite(self):
        #Si aucune collision
        if not self.jeu.detection_collision(self, self.jeu.all_ennemis):
            self.rect.x += self.vitesse

    def gauche(self):
        self.rect.x -= self.vitesse

    def vol(self):
        self.rect.y -= self.vitesse + 3

    def sage(self):
        self.rect.y += self.vitesse + 4






