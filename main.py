from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur

from objets.potion import Potion
from objets.steak import Steak
from personnes.perroquet import Perroquet
from personnes.lion import Lion
from personnes.mage import Mage
from menu import Menu
from endgame import Endgame

import random
import datetime


import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# now, to clear the screen


menu = Menu()
cls()

continuer = True
while continuer:
    print("""
    
       .____                                                          
       |    |    ____                                                 
       |    |  _/ __ \                                                
       |    |__\  ___/                                                
       |_______ \___  >                                               
               \/   \/                                                
    .____          ___.                 .__        __  .__            
    |    |   _____ \_ |__ ___.__._______|__| _____/  |_|  |__   ____  
    |    |   \__  \ | __ <   |  |\_  __ \  |/    \   __\  |  \_/ __ \ 
    |    |___ / __ \| \_\ \___  | |  | \/  |   |  \  | |   Y  \  ___/ 
    |_______ (____  /___  / ____| |__|  |__|___|  /__| |___|  /\___  >
            \/    \/    \/\/                    \/          \/     \/
            

    """)
    entree = input(
    "   Appuyer sur 'Entrée' pour entrer dans le labyrinthe ou 'Menu' pour afficher le menu ")

    if entree == "menu":
        menu.StartMenu()
    else:
        cls()

    l = menu.SpawnLabyrinthe()
    joueur = menu.GetJoueur()
    l.deposerJoueurAleatoirement(joueur)
    menu.StartGame(l)


    while True:
        cls()  # Effacer la console
        joueur.printEnergie()
        print()
        l.afficher()
        print()

    # TODO: oulàlà que c'est mocche, utiliser un design pattern !
        action = input("Que dois-je faire ? ")
        if action == "n":
            try:
                joueur.avancerNord()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif action == "s":
            try:
                joueur.avancerSud()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif action == "e":
            try:
                joueur.avancerEst()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif action == "o":
            try:
                joueur.avancerOuest()
            except:
                print("Ouch, ce mur fait mal...")
                input()
        elif action == "regarder":
            case = joueur.getCaseCourante()
            personnages = case.getPersonnages()
            objets = case.getObjets()
            if(len(personnages) == 0 and len(objets) == 0):
                print(random.choice([
                    "Je vois une salle poussièreuse, sans rien de plus que quelques cailloux.",
                    "Des toiles d'araignées un peu partout.",
                    "C'ets déseperement vide..."
                ]))
            else:
                print("Je vois :")
                for objet in objets:
                    print(" - " + objet.description())
                for personnage in personnages:
                    print(" - " + personnage.description())
            input()

        elif action == "ramasser":
            case = joueur.getCaseCourante()
            if len(case.getObjets()) == 0:
                print("Mais... il n'y a rien à ramasser !")
            else:
                print("J'ai ramassé :")
                for objet in case.getObjets():
                    objet.ramasser(joueur)
                    print(" - " + objet.description())
                # On est obliger de tout supprimer après avoir ramassé, car on ne peut pas modifier la liste sur laquelle on itere...
                case.getObjets().clear()
            input()

        elif action == "sac":
            sac = joueur.getSac()
            if(len(sac)) == 0:
                print("Le sac est vide")
                input()
            else:
                print("Le sac contient: ")
                index = 0
                for obj in sac:
                    print(str(index+1)+" - "+obj.description())
                    index += 1
                choice = input(
                    "Pour utiliser un objet, taper son numéro, ou entrée pour ne rien faire. ")
                try:
                    num = int(choice)
                    obj = sac[num-1]
                    sac.remove(obj)
                    obj.utiliser(joueur)
                except:
                    pass  # En cas d'erreur, c'est que l'entrée est invalide, on ne fait rien

        elif action == "parler":
            personnages = joueur.getCaseCourante().getPersonnages()
            if len(personnages) == 0:
                print("Allo ? allo allo allo allo allo répète l'écho")
            else:
                for personnage in personnages:
                    personnage.parler(joueur)
            input()

        else:
            print("Moi pas comprendre...")
            print(
                "Mon vocabulaire est limité  à n, s, e, o, regarder, ramasser, sac et parler.")
            input()

        joueur.perdreEnergie()
        #if Endgame().GetStopGame()==False:
        #    continuer=False
        # Il faut le finir
