"""Constants of the Mac Gyver Labyrinth Game"""

import os
cwd = os.getcwd()

# image directory

repertoire_images = os.path.join(cwd, "images")

# directory of files

repertoire_fichiers = os.path.join(cwd, "files")


# window parameter

nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite
titre_Jeu = "Maze escape"

# customization of the window

# first image

titre_fenetre = os.path.join(repertoire_images, "tile-crusader-logo.png")

# second image

image_McG = os.path.join(repertoire_images,"MacGyver.png")

# lists of game images

image_accueil = os.path.join(repertoire_images, "tile-crusader-logo.png")
image_MacGyver = os.path.join(repertoire_images, "mac_gyver_title.png")
image_fond = os.path.join(repertoire_images, "image_fond.png")
image_depart = os.path.join(repertoire_images, "start_flag.png")
image_mur = os.path.join(repertoire_images, "bloc_mur_brique.png")
image_arrivee = os.path.join(repertoire_images, "Gardien.png")

# list of images of objects

image_aiguille = os.path.join(repertoire_images, "aiguille.png")
image_batterie = os.path.join(repertoire_images, "batterie.png")
image_couteau = os.path.join(repertoire_images, "couteau_suisse.png")
image_bobine = os.path.join(repertoire_images, "bobine_de_fil.png")
image_epave_voiture = os.path.join(repertoire_images, "epave_voiture.png")
image_flacon = os.path.join(repertoire_images, "ether.png")
image_trombone = os.path.join(repertoire_images, "trombone.png")
image_tube = os.path.join(repertoire_images, "tube_plastique.png")
