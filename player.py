import time

class Player:
    def __init__(self):
        #variable de classe
        self.hp = 100
        self.enventory = [""]

        #variable de fonction
        self.nom = ""

        #introduction
        print("vous etiez parti explorez le systeme planetaire de kepler-186 et un astreoide a percuter le vessaux et vous a fait tomber sur la planete kepler-186b")
        time.sleep(1)

        while True:
            self.nom = input("vous ne vous rappelr pas de vorte nom donc comment voulez vous vous appeler:")

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
        for i in range(self.enventory):
            print(self.enventory[i])
    