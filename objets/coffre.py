from objet import ObjetRamassable
from endgame import Endgame

class Coffre(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self):
        """ Arguments :
        - energie : la quantité d'energie récupérée lorsque l'on utilise la potion
        """
        
    def utiliser(self, joueur):
        Endgame().afficheur()
        joueur.gagnerEnergie(5)
        input("#>")

    def description(self):
        return "Coffre de fin"