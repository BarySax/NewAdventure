import random
import time
class Enemy:
   def __init__(self):
      self.hp = 100
      
   def choose_enemy(self):
      self.hp = 100
      self.type = ["joe", "bob",  "tatie michel"]
      self.nom = random.choice(self.type)

