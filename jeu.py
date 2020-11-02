import pygame
from monstre import monstro
from joueur import jugador
import random
import math


class juego:

    def __init__(self, x):
        #link start
        self.link_start = False
        #generer notre joueur
        self.all_joueurs = pygame.sprite.Group()
        self.jugador = jugador(self, x)
        self.all_joueurs.add(self.jugador)



        # groupe de ennemis
        self.all_ennemis = pygame.sprite.Group()

        # groupe de touche
        self.pressed = {}


    def hunter(self):
        self.link_start = True
        self.spawn_monster()
        self.spawn_monster()


    def death(self):
        #game over -> restart
        self.all_ennemis = pygame.sprite.Group()
        self.jugador.all_tir = pygame.sprite.Group()
        self.jugador.pv = self.jugador.pv_max
        self.jugador.score = 0
        self.link_start = False

    def start(self, screen,x):
        # collage du joueur
        screen.blit(self.jugador.image, self.jugador.rect)

        # update pv
        self.jugador.gestion_pv(screen)

        # recuperation des projectiles
        for projectile in self.jugador.all_tir:
            projectile.move()

        # recuperation des monstre
        for monstre in self.all_ennemis:
            monstre.avancer()
            monstre.gestion_pv(screen)

        # collage projectiles
        self.jugador.all_tir.draw(screen)

        # collage des ennemis
        self.all_ennemis.draw(screen)


        # special
        if self.jugador.pv < 50:
            self.jugador.pv += 0.15

        # mouvement
        if self.pressed.get(
                pygame.K_RIGHT) and self.jugador.rect.x + self.jugador.rect.width < screen.get_width():
            self.jugador.droite()

        elif self.pressed.get(pygame.K_LEFT) and self.jugador.rect.x > 0:
            self.jugador.gauche()

        elif self.pressed.get(pygame.K_UP) and self.jugador.rect.y > 30:
            self.jugador.vol()

        elif self.pressed.get(pygame.K_DOWN) and self.jugador.rect.y < 580:
            self.jugador.sage()


    def spawn_monster(self):
        ennemis = monstro(self, random.randint(1,4))
        self.all_ennemis.add(ennemis)

    def detection_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)