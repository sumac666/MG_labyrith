#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Mac Gyver Labyrinth Game
Game that involves moving and helping Mac Giver
to cross a labyrinth while recovering a
number of objects to get out of it.

Python script
Files: LBMG.py, LBMG.py classes, LBMG.py constants, files with levels + images
"""

# initialization of pygame and different modules

import pygame

import random

import time

import pygame.mixer

from pygame.locals import *

from classes_LBMG import *

from constantes_LBMG import *

# initialization of pygame

pygame.init()

pygame.mixer.init()

# Opening the Pygame window (square: width = height)

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

# McG, loading the image of the hero

img_McG = pygame.image.load(image_McG)

# ouverture de l'image de Mac Gyver

pygame.display.set_icon(img_McG)

# appearance of the title of the game

pygame.display.set_caption(titre_Jeu)

# loading and starting music

pygame.mixer.music.load('Tesla-Jingle.wav')
pygame.mixer.music.play(-1)

# parameters of the MAIN LOOP

continuer = 1

# Loading and splash screen display

accueil = pygame.image.load(image_accueil).convert()

fenetre.blit(accueil, (0, 0))

# Refresh and time management splash screen

pygame.display.flip()

time.sleep(3)

# Start main loop

while continuer:

    # Loading and viewing the home screen

    accueil = pygame.image.load(image_MacGyver).convert()

    # writing font parameter

    fenetre.blit(accueil, (0, 0))
    Texty = pygame.font.Font('SUPERPOI_R.TTF', 15)
    text = Texty.render('start : <F1>', 0, (255, 0, 0))
    fenetre.blit(text, (190, 0))
    text = Texty.render('Quit : <Esc>', 0, (255, 0, 0))
    fenetre.blit(text, (190, 420))

    # Refresh the homepage

    pygame.display.flip()

    # We reset these variables to 1 at each loop turn if we do not want to leave

    continuer_jeu = 1

    continuer_accueil = 1

    # beginning of the HOME LOOP

    while continuer_accueil:

        # Speed ​​limitation of the loop

        pygame.time.Clock().tick(30)

        # If the user leaves, presses the cross or pressing esc, we put the variables

        # of loop to 0 to browse none and close

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:

                continuer_accueil = 0

                continuer_jeu = 0

                continuer = 0

                choix = '0'

            elif event.type == KEYDOWN:

                # Launch a random level

                if event.key == K_F1:

                    # We leave home

                    continuer_accueil = 0

                    # levels

                    liste_choix = ['RL1', 'RL2', 'RL3', 'RL4', 'RL5', 'RL6']

                    # randomly chooses a level

                    choix = random.choice(liste_choix)

    # Generate a level from a file with a list of objects

    if choix != '0':

        Flag_objet = '0'

        # the list fills as the player progresses

        liste_objet = []

        fond = pygame.image.load(image_fond).convert()

        fenetre.blit(fond, (0, 0))

        niveau = Niveau(choix)

        niveau.generer()

        niveau.afficher(fenetre, liste_objet)

        # Creation of Mac Gyver, the main character

        mg = Perso(repertoire_images + "Mag Giver.png", niveau)

    # beginning of the GAME LOOP

    while continuer_jeu:

        # Speed ​​limitation of the loop

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If the user leaves, we put the variable that continues the game

            # AND the general variable to 0 to close the window

            if event.type == QUIT:

                continuer_jeu = 0

                continuer = 0

            elif event.type == KEYDOWN:

                # If the user presses Esc here, we only return to the menu

                # Mag Gyver move keys

                # Call the move method of the personal object to move it

                # the management of picked objects

                if event.key == K_ESCAPE:

                    continuer_jeu = 0

                elif event.key == K_RIGHT:

                    Flag_objet = mg.deplacer('droite', Flag_objet)

                elif event.key == K_LEFT:

                    Flag_objet = mg.deplacer('gauche', Flag_objet)

                elif event.key == K_UP:

                    Flag_objet = mg.deplacer('haut', Flag_objet)

                elif event.key == K_DOWN:

                    Flag_objet = mg.deplacer('bas', Flag_objet)

                if Flag_objet != '0' and Flag_objet not in liste_objet:

                    liste_objet.append(Flag_objet)

        # refresh background image

        fenetre.blit(fond, (0, 0))

        niveau.afficher(fenetre, liste_objet)

        fenetre.blit(img_McG, (mg.x, mg.y))

        pygame.display.flip()

        # Winner-looser -> Back to home

        # check if the person has picked up all objects

        if niveau.structure[mg.case_y][mg.case_x] == 'g' and len(liste_objet) == 8:
            Texty = pygame.font.Font('SUPERPOI_R.TTF', 25)
            text = Texty.render('YOU WIN !!!', 0, (255, 0, 0))
            fenetre.blit(text, (125, 210))
            pygame.display.flip()
            time.sleep(5)
            continuer_jeu = 0

        elif niveau.structure[mg.case_y][mg.case_x] == 'g' and len(liste_objet) < 8:
            Texty = pygame.font.Font('SUPERPOI_R.TTF', 25)
            text = Texty.render('YOU LOOSE !!!', 0, (255, 0, 0))
            fenetre.blit(text, (110, 210))
            pygame.display.flip()
            time.sleep(5)
            continuer_jeu = 0