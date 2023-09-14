import player
import random
import time

player = player.Player()

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

def fight():
    #variable de fonction
    spd = 2
    num_hash_arr = 5
    num_hash_av = 5
    num_hash_e_arr = 5
    movement = int(input("Que voulez-vous faire:\n\n1-Allez en arriere\n2-Allez en avant\n3-Ne pas bouger\n"))
    
    #verification
    if movement == 1:
        print("Vous reculer de deux metres.")
        num_hash_arr -= spd
        num_hash_av += spd
    elif movement == 2:
        print("Vous avancerr de deux metres.")
        num_hash_arr += spd
        num_hash_av -= spd

    #afficher les position    
    hash_e_arr = "#" * num_hash_e_arr
    hash_arr = "#" * num_hash_arr
    hash_av = "#" * num_hash_av
    print("#################\n" + hash_arr + "P" + hash_av + "E" + hash_e_arr)

    action = int(input("Que voulez-vous faire:\n\n1-Attaquer\n2-Prendre de la morphine\n3-Ce redeplacer\n"))
    if action == 1:
        re_attack = True
        #boucle qui permet dattaquer a plusieur reprise
        while re_attack == True:
          attack = int(input("Quelle type d'attaque voulez-vous faire:\n\n1-Corps a Corps\n2-Distance\n"))
          if attack == 2:
            re_attack = False
          elif attack == 1 and num_hash_av == 1:
            print("Vous etiez suffisament pres pour attaquer, causant un desequilibre ce qui vous a fais avancer")
            num_hash_arr += spd
            num_hash_av -= spd
            re_attack = False 
          elif attack == 1 and num_hash_av == 0:
            re_attack = False   
          elif attack == 1 and num_hash_av != 1 or attack == 1 and num_hash_av != 0:
            print("Vous n'etes pas assez proche")
        if attack == 1:
            try_attack = random.randint(0,100)
            if try_attack >= 50:
                random_degat = random.randint(0,10)
                p_degat = 5 + random_degat
                enemy.hp -= p_degat
                print("Vous avez fait ",p_degat," degat, ",enemy.hp," a ",enemy.hp," point de vie.")
            else:
                print("Rater")
        else:
            #Le fusil est moin bon, faut donner un avantage
            try_attack = random.randint(0,100)
            
            #calcule des degat
            if try_attack >= 60:
                random_degat = random.randint(0,5)
                p_degat = 5 + random_degat
                enemy.hp -= p_degat
                print("Vous avez fait ",player.hp," degat, ",enemy.hp," a ",e_hp," point de vie.")
            else:
                print("Rater")



show_intro_menu()
print("on est parti")
fight()
