import random
import time
class Enemy:
   def choose_enemy(self):
      self.hp = 100
      self.type = ["joe", "bob"]
      self.nom = random.choice(self.type)
