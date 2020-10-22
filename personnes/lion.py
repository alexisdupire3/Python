from personnage import Personnage
import random

class Lion(Personnage):
    """ Cette classe représente un Perroquet qui salue le joueur lorsqu'il arrive sur la même case, et qui répète
    bêtement ce qu'on lui dit. Le perroquet a une couleur qu'on lui passe à la création dans le constructeur. """

    def __init__(self, type):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """
        self._type = type

    def description(self):
        """ Renvoie la description du perroquet."""
        return "Un lion" + self._type

    def rencontrer(self, joueur):
        if self._type=="feroce":
            print("Un lion "+self._type+" vous attaque ! Vous fuyez et perdez 10 points d'energies")
            joueur.perdreEnergieValeur(10)      
        else:
            print("Un lion "+self._type+" vous fait une lechouille")
        input()

    def parler(self, joueur):
        if self._type=="feroce":
            print("Lion "+self._type+": GRRRRHHHHHHHH !!!")      
        else:
            print("Lion "+self._type+": Rhalut l'ami, veux-tu entrendre un blague ? [oui - non]")
            entree = input("#>")
            if entree == "oui":
                print("Lion "+self._type+": Rhomment s'appelle le petit du mouton ?")
                entree = input("#>")
                print("Lion "+self._type+": Un bèèèh bèèèh !")
            else:
                print("Lion "+self._type+": Rhe voie que tu n'as pas le temps Rheune aventurié. Bonne journée !")
        entree = input("#>")