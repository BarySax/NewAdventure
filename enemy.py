import random
import time
class Enemy:
   def __init__(self):
      bloup = 30
   def choose_enemy(self):
      self.hp = 100
      self.type = ["joe", "bob"]
      self.nom = random.choice(self.type)