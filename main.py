import player
import random
import time
import enemy
import sys


player = player.Player()
enemy = enemy.Enemy()

player.fight()
player.printInfo()


def show_intro_menu():
    print("bla bla bla\nblablabla")
    print("\t 1- Commencer la partie")
    print("\t 2- Afficher les règles du jeu")
    print("\t 3- Quitter")

    action = int(input("Que voulez-vous faire ?"))  # qu'il faudrait blinder comme dans votre travail précédent

    if action == 1:
        start_game()

    elif action == 2:
        show_rules_of_the_game()
        show_intro_menu()

    elif action == 3:
        print("Merci et à bientôt...")
        exit()

    else:
        print("Choix invalide")
        show_intro_menu()


def start_game():
    #fonction qui permet fait litroduction
    player.introduction()

    # une mise en contexte et un choix d'action devraient être proposés ici au joueur
    
    
    # action = int(input("Que voulez-vous faire ?"))


def show_rules_of_the_game():
    """ On affiche les règles du jeu """
    print("Ceci sont les règles du jeu...")


#fonction de combat
def fight():
    num_ash_av = 5
    num_ash_arr = 5
    num_ash_e_arr = 5
    spd = 2

    #le mouvement
    while player.hp > 0 and enemy.hp > 0: 
        spd = 2        

        print("tu a ", player.hp, "hp")
        print("lenemy a", enemy.hp, "hp")

        #aficher la distance entre le joueur et lenemy
        ash_av = '#' * num_ash_av
        ash_arr = '#' * num_ash_arr
        ash_e_arr = '#' * num_ash_e_arr
        print(ash_arr + "P" + ash_av + "E" + ash_e_arr)
        
        print("atention tu a devan toi un ", enemy.nom, "sauvage")
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
                if num_ash_av > 2:
                    print("ton arme est ineficasse passe ton tour")
                    if enemy.nom == "bob":
                        print("lenemy te lance un boule de feu et tu te prend 20 de degat")
                        player.hp -= 20

                else:
                    print("tu a fait 20 de degat a lenemy")
                    enemy.hp -= 20
                    print(enemy.hp)

            #le fusil
            if choix == 2:
                choix = random.randint(1,6)
                if choix == 6:
                    print("ton arme ne fais rien")
                else:
                    print("tu fais 15 degat a lenemy")
                    enemy.hp -= 15
            
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
            spd = 4
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

#fonction pour ramasser des objet
def rammasser():
    objet = ["plaque dacier", "reacteur", "bandage"]

    #rammasser des objet pour linventaire
    if random.choice(objet) == "bandage":
        choix = int(input("en tuant lenemy tu a trouver un bandage\n\n1-lutiliser et reprendre des force\n2-le mettre dans son inventaire pour plus tard\nque veut tu faire?: "))
        if choix == 1:
            player.hp += 10
            print("tu est maintenant a ", player.hp, "hp")
        
        elif choix == 2:
            player.enventory.append("bandage")
        
        else:
            print("choix invalide je vais le metre dans ton inventaire")

    elif random.choice(objet) == "plaque dacier":
        print("la plaque dacier va dans ton inventaire")
        player.enventory.append("plaque dacier")

    else:
        print("le reacteur va dans ton iventaire")


show_intro_menu()
print("on est parti")



#chapitre un
#liste dobjet a gagner
print("chapite 1")
print("\n vous decidez daller explorer pour trouver une forme de vie")
time.sleep(1)
print("vous vous premenez sur une planet tropicale qui vous semble deserte")
time.sleep(1)
print("apres plusieur heures de marche et dexploration vous trouvez une forme de vie,\nmais se nest pas celle que vous vouliez decouvrir")
time.sleep(1)
print("la bete semble hostile\n")
fight()


print("bravo tu a gagner ton premier combat")
time.sleep(1)
print("tu continue a explorez la planete")
time.sleep(4)
print("\n")
print("tu tombe sur une creature gentille")
#discution avec une creature
choix = int(input("le monstre parle ta langue\n\n1-tu vas lui parler pour en aprendre plus sur ta location\n2-tu passe a coter\nque fait tu? "))
if choix == 1:
    print("tu vas voir la bibitte")
    time.sleep(2)
    print(player.nom, ":\n bonjour je me demande je suis ou?")
    time.sleep(0.5)
    print("la crature:\ntu est sur la planete kepler186-b")
    time.sleep(0.5)
    input("la creature:\nest ce que cest toi le voyageur venu de lespace\n")
    time.sleep(0,5)
    print("la creature:\nparceque jai vu un vaisseau se planter dernierement")
    time.sleep(0.5)
    input("la creature:\naurevoir epuis fait atention se n'est pas une planete gentile\n")

elif choix == 2:
    print("tu continu ton chemin")

#combat
if choix == 1:
    print("comme te lavait prevenu la crature tu fait face a un enemy")
    fight()

if choix == 2:
    print("tu fait face a un enemy")
    fight()

