import random

class Enemy:
    def __init__(self):
        self.type = ["joe", "bob"]
        self.hp = 100
        self.distanceToPlayer = 0

    def choisir_enemy(self):
        self.nom = random.choice(self.type)
        print(self.nom)
    
   def attaque(self):
      if self.nom == "joe":
         print("je suuis joe")
         choix = random.randint(1,2)
         if choix == 1:
            print("javance")
         
         elif choix == 2:
            print("jattaque")
         
      elif self.nom == "bob":
         print("je suis bob")
         choix = random.randint(1,2)
         if choix == 1:
            print("je maproche")

         elif choix == 2:
            print("jattaque")
         
      else:
         print("erreur")