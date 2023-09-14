import time

class Player:
    def __init__(self):
        #variable de classe
        self.hp = 100
        self.enventory = [""]
        self.nom = ""
    
    def introduction(self):
        #introduction
        print("…")
        time.sleep(0.5)
        print("………")
        time.sleep(0.5)
        print("…………")
        time.sleep(0.5)
        print("Vous vous réveillez en sursaut, un bruit stridant vous ayant avertit dun danger.")
        time.sleep(0.5)
        print("Mais ce que vous vous attendiez a voir n'était que fiction")
        time.sleep(0.5)
        print("Vous ettiez au centre dune carcasse métallique entre ouverte, surement un vaisseau")
        time.sleep(0.5)
        print("Vous vous levez avec difficulté, puis vous regardez autour de vous.")
        time.sleep(0.5)
        print("Rien, personne, juste des tas d'objet inutilisable.")
        time.sleep(0.5)
        print("Au bout dun moment, vous remarque linexistance de vos souvenirs, aui etes vous, que faite vous ici, ou etes vous.")
        time.sleep(0.5)
        while True:
            self.nom = input("vue que vous ne connaissez pas votre nom, comment voulez vous vous appeler:")

            if self.nom == "":
                print("svp entrez un nom")
            else:
                break

    #fonction permetant de combatre
    def fight(self):
        print(self.hp)

    #fonction qui affihe les info du joueur
    def printInfo(self):
        print(self.hp)
        for i in range(len(self.enventory)):
            print(self.enventory[i])
    