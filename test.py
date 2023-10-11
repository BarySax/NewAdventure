import enemy
import player
import random
import sys

player = player.Player()
enemy = enemy.Enemy()


def fight():
    num_ash_av = 5
    num_ash_arr = 5
    num_ash_e_arr = 5
    spd = 2

    #le mouvement
    while player.hp > 0 and enemy.hp > 0: 
        print("tu a ", player.hp, "hp")
        print("lenemy a", enemy.hp, "hp")
        print(num_ash_arr, "P", num_ash_av, "E", num_ash_e_arr)
        choix = int(input("que veux tu faire:\n\n1-avancer\n2-reculer\n3-attaquer\n4-prendre de la morphine pour reprendre des force\n"))
        
        if choix == 1:
            print("on avance")
            num_ash_arr += spd
            num_ash_av -= spd

        elif choix == 2:
            num_ash_av += spd
            num_ash_arr -= spd

        #les attaque
        elif choix == 3:
            choix = int(input("quel arme veux tu prendre:\n\n1-couteau corps a corps\n2-fusil\n"))
            #corp a corp
            if choix == 1:
                if num_ash_av > 1:
                    print("ton arme est ineficasse passe ton tour")
                    if enemy.nom == "bob":
                        print("lenemy te lance un boule de feu et tu te prend 20 de degat")
                        player.hp -= 20

                elif num_ash_av < 1:
                    print("tu a fait 20 de degat a lenemy")
                    enemy.hp -= 20

            #le fusil
            if choix == 2:
                print("tu fais 15 degat a lenemy")
            
        #reprendre des force
        elif choix == 4:
            print("tu a repris 20 hp")
            player.hp += 20
        #tour de lenemy
        #attaque de bob
        if enemy.nom == "bob":
            attaque = random.randint(0,3)
            if attaque == 0:
                print("tu est chanceux lenemmy fais rien")
            
            elif attaque == 1:
                print("quel malchance lenemy tataque avec un boule de feu\ntu te prend 15 de degat")
                player.hp -= 15

            elif attaque == 2:
                print("tu est chanceux lenemmy recule")
                num_ash_e_arr -= spd
                num_ash_av += spd

            elif attaque == 3:
                print("tu est chanceux lenemmy avance")
                num_ash_e_arr += spd
                num_ash_av -= spd

        #attaque de joe
        elif enemy.nom == "joe":
            #si la distance est de moin de deux metre
            attaque = random.randint(0,3)
            if attaque == 0:
                print("tu est chanceux lenemmy fais rien")
            
            elif attaque == 1:
                if num_ash_av < 2:
                    print("quel malchance lenemy tataque avec ses grosse griffe\ntu te prend 15 de degat")
                    player.hp -= 15
        
            elif attaque == 2:
                print("tu est chanceux lenemmy recule")
                num_ash_e_arr -= spd
                num_ash_av += spd

            elif attaque == 3:
                print("tu est chanceux lenemmy avance")
                num_ash_e_arr += spd
                num_ash_av -= spd

    #message de fin de combat
    if player.hp <= 0:
        print("vous ete mort vous avez perdu")
        sys.exit(0)
    elif enemy.hp <= 0:
        print("bravo vous avez gagnez le combat")


fight()