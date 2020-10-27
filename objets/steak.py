from objet import ObjetRamassable

class Steak(ObjetRamassable):
    """ Représente une potion qui redonne de l'énergie au joueur lorsqu'il la boit. """

    def __init__(self):
        """ Constructeur. Paramètres :
        - couleur : la couleur du perroquet (chaine de caractères)
        """

    def utiliser(self, joueur):
        print("Ca pourrait m'être utile face à un prédateur...")
        print("[Vous récuperez 5 points d'energie]")
        joueur.gagnerEnergie(5)
        input("#>")

    def description(self):
        return "Un steak"