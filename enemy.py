import time
import random

class Enemy:
    def __init__(self):
        self.type = ["joe", "bob"]
        self.hp = 100
        self.distanceToPlayer = 0

    def choisir_enemy(self):
        self.nom = random.choice(self.type)
        print(self.nom)
    