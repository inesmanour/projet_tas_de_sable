#########################################
# informations liées au groupe
# groupe LDDBI
# LAURA LEFEVRE
# ADAM KEDDIS
# MANOUR INES 
#https://github.com/uvsq22103405/projet_tas_de_sable.git
#########################################
# import des librairies
from tkinter import *


#########################################
# définition des constantes

# hauteur du canevas 
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600 

#########################################
# définition des variables globales


#########################################
# définition des fonctions (chaque fonction devra contenir une docstring)

#########################################
# partie principale 


# Création des widgets 
FENETRE = Tk()
FENETRE.title("Tas de sable")
canvas = Canvas(FENETRE, height=HAUTEUR, width=LARGEUR)

#Placement des widgets
canvas.grid(column=1, row=0)

#Boucle principale
FENETRE.mainloop()

