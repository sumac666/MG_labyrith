#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""Mac Gyver Labyrinth Game Classes"""

import pygame

from pygame.locals import *

from constantes_LBMG import *

# Class to create a level

class Niveau:
    """Class to create a level"""

    def __init__(self, fichier):

        self.fichier = os.path.join(repertoire_fichiers, fichier)

        self.structure = 0

    def generer(self):

        """Method for generating the level according to the file.

        We create a general list, containing a list by line to display"""

        # Open the file

        with open(self.fichier, "r") as fichier:

            structure_niveau = []

            # We browse the lines of the file

            for ligne in fichier:

                ligne_niveau = []

                # We go through the sprites (letters) contained in the file

                for sprite in ligne:

                    # We ignore the end of line "\ n"

                    if sprite != '\n':
                        # Add the sprite to the list of the line

                        ligne_niveau.append(sprite)

                # Add the line to the level list

                structure_niveau.append(ligne_niveau)

            # We save this structure

            self.structure = structure_niveau

    def afficher(self, fenetre, liste):

        """Method for displaying the level according to

        of the structure list returned by generer ()"""

        # Loading images (only the arrival one contains transparency)

        mur = pygame.image.load(image_mur).convert()

        depart = pygame.image.load(image_depart).convert()

        arrivee = pygame.image.load(image_arrivee).convert_alpha()

        aiguille = pygame.image.load(image_aiguille).convert()

        batterie = pygame.image.load(image_batterie).convert()

        couteau = pygame.image.load(image_couteau).convert_alpha()

        bobine = pygame.image.load(image_bobine).convert()

        epave = pygame.image.load(image_epave_voiture).convert()

        flacon = pygame.image.load(image_flacon).convert_alpha()

        trombone = pygame.image.load(image_trombone).convert()

        tube = pygame.image.load(image_tube).convert()


        # We go through the level list

        num_ligne = 0

        for ligne in self.structure:

            # We browse the lists of lines

            num_case = 0

            for sprite in ligne:

                # The actual position in pixels is calculated

                x = num_case * taille_sprite

                y = num_ligne * taille_sprite

                if sprite == 'm':  # m = Mur

                    fenetre.blit(mur, (x, y))

                elif sprite == 'd':  # d = Départ

                    fenetre.blit(depart, (x, y))

                elif sprite == 'g':  # a = Gardien

                    fenetre.blit(arrivee, (x, y))

                elif sprite == 'u' and sprite not in liste:  # u = aiguille

                    fenetre.blit(aiguille, (x, y))

                elif sprite == 'b' and sprite not in liste:  # b = batterie

                    fenetre.blit(batterie, (x, y))

                elif sprite == 'c' and sprite not in liste:  # c = couteau

                    fenetre.blit(couteau, (x, y))

                elif sprite == 'h' and sprite not in liste:  # h = bobine

                    fenetre.blit(bobine, (x, y))

                elif sprite == 'e' and sprite not in liste:  # e = epave

                    fenetre.blit(epave, (x, y))

                elif sprite == 'f' and sprite not in liste:  # f = flacon

                    fenetre.blit(flacon, (x, y))

                elif sprite == 't' and sprite not in liste:  # t = trombone

                    fenetre.blit(trombone, (x, y))

                elif sprite == 'p' and sprite not in liste:  # p = tube plastique

                    fenetre.blit(tube, (x, y))

                num_case += 1

            num_ligne += 1


class Perso:
    """Class to create a character"""

    def __init__(self, image, niveau):

        self.image = pygame.image.load(image_McG)

        # Position of the character in boxes and pixels

        self.case_x = 0

        self.case_y = 0

        self.x = 0

        self.y = 0

        # Default direction

        self.direction = self.image

        # Level in which the character is located

        self.niveau = niveau

    def deplacer(self, direction, indicateur):

        """Method for moving the character"""

        self.indicateur = indicateur

        # Move to the right

        if direction == 'droite':

            # Not to exceed the screen

            if self.case_x < (nombre_sprite_cote - 1):

                # Check that the destination box is not a wall

                if self.niveau.structure[self.case_y][self.case_x + 1] != 'm':
                    # Moving a box

                    self.case_x += 1

                    # Calculation of the "real" position in pixel

                    self.x = self.case_x * taille_sprite

                    if self.niveau.structure[self.case_y][self.case_x] == 'u':
                        self.indicateur = 'u'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'b':
                        self.indicateur = 'b'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'c':
                        self.indicateur = 'c'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'h':
                        self.indicateur = 'h'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'e':
                        self.indicateur = 'e'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'f':
                        self.indicateur = 'f'

                    elif self.niveau.structure[self.case_y][self.case_x] == 't':
                        self.indicateur = 't'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'p':
                        self.indicateur = 'p'

                    else:
                        self.indicateur = '0'


            self.direction = self.image

            indicateur = self.indicateur

            return indicateur

        # Move to the left

        if direction == 'gauche':

            if self.case_x > 0:

                if self.niveau.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1

                    self.x = self.case_x * taille_sprite

                    if self.niveau.structure[self.case_y][self.case_x] == 'u':
                        self.indicateur = 'u'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'b':
                        self.indicateur = 'b'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'c':
                        self.indicateur = 'c'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'h':
                        self.indicateur = 'h'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'e':
                        self.indicateur = 'e'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'f':
                        self.indicateur = 'f'

                    elif self.niveau.structure[self.case_y][self.case_x] == 't':
                        self.indicateur = 't'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'p':
                        self.indicateur = 'p'

                    else:
                        self.indicateur = '0'

            self.direction = self.image

            indicateur = self.indicateur

            return indicateur

        # Move up

        if direction == 'haut':

            if self.case_y > 0:

                if self.niveau.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1

                    self.y = self.case_y * taille_sprite

                    if self.niveau.structure[self.case_y][self.case_x] == 'u':
                        self.indicateur = 'u'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'b':
                        self.indicateur = 'b'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'c':
                        self.indicateur = 'c'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'h':
                        self.indicateur = 'h'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'e':
                        self.indicateur = 'e'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'f':
                        self.indicateur = 'f'

                    elif self.niveau.structure[self.case_y][self.case_x] == 't':
                        self.indicateur = 't'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'p':
                        self.indicateur = 'p'

                    else:
                        self.indicateur = '0'

            self.direction = self.image

            indicateur = self.indicateur

            return indicateur

        # Move down

        if direction == 'bas':

            if self.case_y < (nombre_sprite_cote - 1):

                if self.niveau.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1

                    self.y = self.case_y * taille_sprite

                    if self.niveau.structure[self.case_y][self.case_x] == 'u':
                        self.indicateur = 'u'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'b':
                        self.indicateur = 'b'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'c':
                        self.indicateur = 'c'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'h':
                        self.indicateur = 'h'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'e':
                        self.indicateur = 'e'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'f':
                        self.indicateur = 'f'

                    elif self.niveau.structure[self.case_y][self.case_x] == 't':
                        self.indicateur = 't'

                    elif self.niveau.structure[self.case_y][self.case_x] == 'p':
                        self.indicateur = 'p'

                    else:
                        self.indicateur = '0'

            self.direction = self.image

            indicateur = self.indicateur

            return indicateur
