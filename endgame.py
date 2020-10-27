import random
import os
import datetime
import sys


class Endgame:
    def __init__(self):
        self.x = datetime.datetime.now()

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    heure=0
    minute=0

    def tempsdepart(self):
        global heure
        global minute
        heure = self.x.strftime("%H")
        minute = self.x.strftime("%M")
        return heure, minute

    def tempspartie(self):
        global heure
        global minute
        heure2 = self.x.strftime("%H")
        minute2 = self.x.strftime("%M")
        heure=int(heure2) - int(heure)
        minute=int(minute2) - int(minute)
        print("   Vous avez réalisé un temps de ",heure,":",minute," !")

    def afficheur(self):
        self.cls()
        print("""
           __________
          /\____;;___\\
         | /         /
         `. ())oo() .
          |\(%()*^^()^\\
         %| |-%-------|
         % \ | %  ))   |
         %  \|%________|

        Vous avez gagné, félicitation !   
        """)
        self.tempspartie()
        input("#>")
        sys.exit()