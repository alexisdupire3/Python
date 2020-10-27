""" Ajouter puie de TP Mode zombie
# Nombre mob (consillé)
# Taille plateau
#  """
import random
import os

from labyrinthe.labyrinthe import Labyrinthe
from joueur import Joueur
from endgame import Endgame

from objets.potion import Potion
from objets.steak import Steak
from objets.coffre import Coffre
from personnes.lion import Lion
from personnes.mage import Mage

class Menu:
    def __init__(self):
        self.tailleX = 20
        self.tailleY = 10
        self.energie = 100
        self.mage = 3
        self.lion = 15
        self.steak = 10
        self.potion = 15

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def SetTailleX(self, mini, maxi):
        self.tailleX=input("Entrez la taille X du plateau voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.tailleX.isnumeric() != True or int(self.tailleX) <= mini or int(self.tailleX) > maxi:
            self.tailleX=input("Entrez la taille X du plateau voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.tailleX=int(self.tailleX)
    
    def SetTailleY(self, mini, maxi):
        self.tailleY=input("Entrez la taille Y du plateau voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.tailleY.isnumeric() != True or int(self.tailleY) <= mini or int(self.tailleY) > maxi:
            self.tailleY=input("Entrez la taille Y du plateau voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.tailleY=int(self.tailleY)
    
    def SetEnergie(self, mini, maxi):
        self.energie=input("Entrez le nombre de d'énergie voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.energie.isnumeric() != True or int(self.energie) <= mini or int(self.energie) > maxi:
            self.energie=input("Entrez le nombre d'énergie voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.energie=int(self.energie)


    def SetSteak(self, mini, maxi):
        self.steak=input("Entrez le nombre de steak voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.steak.isnumeric() != True or int(self.steak) <= mini or int(self.steak) > maxi:
            self.steak=input("Entrez le nombre de steak voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.steak=int(self.steak)

    def SetPotion(self, mini, maxi):
        self.potion=input("Entrez le nombre de potion voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.potion.isnumeric() != True or int(self.potion) <= mini or int(self.potion) > maxi:
            self.potion=input("Entrez le nombre de potion voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.potion=int(self.potion)


    
    def SetMage(self, mini, maxi):
        self.mage=input("Entrez le nombre de mage voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.mage.isnumeric() != True or int(self.mage) <= mini or int(self.mage) > maxi:
            self.mage=input("Entrez le nombre de mage voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.mage=int(self.mage)

    def SetLion(self, mini, maxi):
        self.lion=input("Entrez le nombre de lion voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        input(" ")
        while self.lion.isnumeric() != True or int(self.lion) <= mini or int(self.lion) > maxi:
            self.lion=input("Entrez le nombre de lion voulu (compris entre "+str(mini)+" et "+str(maxi)+") ")
        self.lion=int(self.lion)


        
    def SpawnAllObjet(self, l):
        for i in range(self.potion):
            potion = Potion(random.randint(5,10))
            l.deposerObjetAleatoirement(potion)
        for i in range(self.steak):
            steak = Steak()
            l.deposerObjetAleatoirement(steak)
        for i in range(150):
            coffre = Coffre()
            l.deposerObjetAleatoirement(coffre)
    
    def SpawnAllMob(self, l):
        for i in range(self.mage):
            l.deposerPersonneAleatoirement(Mage())
        for i in range(self.lion):
            #l.deposerPersonneAleatoirement(Perroquet(random.choice(['vert','bleu','rouge','orange','jaune','rose','violet'])))
            l.deposerPersonneAleatoirement(Lion(random.choice(['feroce','mignon'])))

    def SpawnLabyrinthe(self):
        l = Labyrinthe(self.tailleX,self.tailleY)
        return l

    def GetLabyrinthe(self, l):
        return l
    
    def SpawnJoueur(self, l, joueur):
        l.deposerJoueurAleatoirement(joueur)

    def AfficherMenu(self):
        self.cls()
        print("""

        .____                                                          
        |    |    ____                                                 
        |    |  _/ __ \                                                
        |    |__\  ___/                                                
        |_______ \___  >                                               
                   \/   \/                                                
        .____    ____.          
        |    \  /    |  ____   _____  __   __
        |     \/     |_/ __ \ /    \ |  | |  |
        |    |\/|    |\  ___/|   |  \|  |_|  /
        |____|  |____| \___  |___|  /\______/
                           \/     \/

        
        """)
        print("   PARAMETRE PLATEAU :")
        print("   1> Taille X du plateau : ",self.tailleX)
        print("   2> Taille Y du plateau : ",self.tailleY)
        print("   3> Niveau d'énergie : ",self.energie)

        print("\n   PARAMETRE PERSONNAGES :")
        print("   4> Nombre de mage en jeu : ",self.mage)
        print("   5> Nombre de lion en jeu : ",self.lion)

        print("\n   PARAMETRE OBJETS :")
        print("   6> Nombre de steak en jeu : ",self.steak)
        print("   7> Nombre de potion en jeu : ",self.potion)
    
    def default(self):
        return
    
    def GetJoueur(self):
        joueur=Joueur("X",self.energie)
        return joueur

    def StartGame(self, l):
        self.SpawnAllObjet(l)
        self.SpawnAllMob(l)
        Endgame().tempsdepart()

    def StartMenu(self):
        self.AfficherMenu()
        
        choix=input("\n   Tapez 1 ou 2 ou 3... pour choisir l'option à modifier. Appuyez 'Entrée' pour quitter ")

        if choix == "1" :
            self.SetTailleX(10, 30)
            self.StartMenu()
        elif choix == "2" :
            self.SetTailleY(5, 15)
            self.StartMenu()
        elif choix == "3" :
            self.SetEnergie(30, 100)
            self.StartMenu()
        elif choix == "4" :
            self.SetMage(0, 10)
            self.StartMenu()
        elif choix == "5" :
            self.SetLion(0, 20)
            self.StartMenu()
        elif choix == "6" :
            self.SetSteak(0, 30)
            self.StartMenu()
        elif choix == "7" :
            self.SetPotion(0, 40)
            self.StartMenu()
        else :
            self.default()