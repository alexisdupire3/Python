from personnage import Personnage
from labyrinthe.case import Case
import random

class Mage(Personnage):
    """ Cette classe représente un Perroquet qui salue le joueur lorsqu'il arrive sur la même case, et qui répète
    bêtement ce qu'on lui dit. Le perroquet a une couleur qu'on lui passe à la création dans le constructeur. """

    def __init__(self):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """

    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un mage"

    def rencontrer(self, joueur):
        case = joueur.getCaseCourante()
        print("Un mage vous lance un sort !")
        sort=random.randint(0, 15)
        if sort>=0 and sort<=12:
            print("Mage : c'est ton jour de chance !")
            print("[Vous gagnez", sort ,"points d'energie]")
            joueur.gagnerEnergie(sort)      
        else:
            print("Mage : Vous êtes sur mon territoire ! Payez la taxe")
            print("[Votre inventaire a été vidé]")
            joueur.clearSac()
        case.supprimerPersonnage(self)
        input()