import player
import enemy

#initialization de classe
player = player.Player()
enemy  = enemy.Enemy()

player.fight()
player.printInfo()
enemy.choisir_enemy()
enemy.attaque()