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


show_intro_menu()
print("on est parti")