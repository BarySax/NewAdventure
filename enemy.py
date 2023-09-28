import random
import time
class Enemy:
   def __init__(self):
      bloup = 30
      self.hp = 100
   def choose_enemy(self):
      self.type = ["joe", "bob"]
      self.nom = random.choice(self.type)