from __future__ import division
import pygame
import random
from sympy import symbols, S, pi, solve, sin, cos
import math

# projectile
class disparo(pygame.sprite.Sprite):

    #definition
    def __init__(self, joueur, x):
        super().__init__()
        self.vitesse = 4
        self.joueur = joueur
        if x == 1:
            self.image = pygame.image.load("pic/projectiles/flamme.png")
            self.image = pygame.transform.scale(self.image, (40,40))
            self.attack = [30, 35, 5, 55]
            self.aiguille = 1
            self.rota = 1

        elif x == 2:
            self.image = pygame.image.load("pic/projectiles/fleche.png")
            self.attack = [15, 40, 0, 80]
            self.aiguille = 1
            self.rota = 0

        elif x == 3:
            self.image = pygame.image.load("pic/projectiles/sword.png")
            self.attack = [20, 40, 15, 60]
            self.aiguille = 1
            self.rota = 1

        elif x == 4:
            self.image = pygame.image.load("pic/projectiles/blowpipe.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.attack = [60, 60, 0, 65]
            self.aiguille = 1
            self.rota = 0

        elif x == 5:
            self.image = pygame.image.load("pic/projectiles/shuriken.png")
            self.attack = [30, 35, 25, 90]
            self.aiguille = 1
            self.rota = 1


        elif x == 11:
            self.image = pygame.image.load("pic/projectiles/oeuf.png")
            self.image = pygame.transform.scale(self.image, (250,100))
            self.attack = [100, 95, 120, 99]
            self.aiguille = 11
            self.mode = 1

        elif x == 12:
            self.image = pygame.image.load("pic/projectiles/hatchet.png")
            self.attack = [100, 95, 120, 99]
            self.aiguille = 11
            self.mode = 1

        elif x == 13:
            self.image = pygame.image.load("pic/projectiles/hat.png")
            self.attack = [100, 95, 120, 99]
            self.aiguille = 11
            self.mode = 0

        elif x == 14:
            self.image = pygame.image.load("pic/projectiles/stone.png")
            self.image = pygame.transform.scale(self.image, (250, 100))
            self.attack = [100, 95, 120, 99]
            self.aiguille = 11
            self.mode = 1

        elif x == 15:
            self.image = pygame.image.load("pic/projectiles/kunai.png")
            self.attack = [100, 95, 120, 99]
            self.aiguille = 11
            self.mode = 1


        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 100
        self.rect.y = joueur.rect.y + 50
        self.origine_image = self.image
        self.angulo = 0


    def rotation(self, rad):
        #tourner le projectile
        self.angulo += rad
        self.image = pygame.transform.rotozoom(self.origine_image, self.angulo, 1)
        self.rect = self.image.get_rect(center = self.rect.center)


    def suppression(self):
        self.joueur.all_tir.remove(self)


    def move(self):
        def sinuo(self):
            return 10*cos(self/40)

        def gravity(self):
            return 0.0056 * self ** 2 - 5 * self + 900

        if self.aiguille == 1:
            self.rect.x += self.vitesse
            if self.rota == 1:
                self.rotation(8)

        elif self.aiguille == 11:
            for i in range (1):
                if self.mode == 0:
                    self.rect.x += self.vitesse
                    self.rect.y += int(sinuo(self.rect.x))

                if self.mode == 1:
                    self.rect.x += self.vitesse
                    self.rect.y = int(gravity(self.rect.x))
                    self.rotation(-1)



            #si projectile entre en contacte avec un monstre
        for monstre in self.joueur.jeu.detection_collision(self, self.joueur.jeu.all_ennemis):
            #suppresion du projectile
            self.suppression()

            #infliger des degats
            monstre.dommage(random.choice(self.attack))

        #destruction du projectile à la sortie de l'écran
        if self.rect.x > 1200:
            self.suppression()



