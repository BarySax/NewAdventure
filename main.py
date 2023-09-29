#Fait par Gabriel Foriel Fusier et Nicolas Prigge
#A debute le 7 septembre et a ete terminer le @ 
#Projet de RPG sur python

#Importation des modules
import player
import random
import time
import enemy
import sys
import os
import os

#Variable de base du programme
val_sleep = 1
big_brain = 0
invitation = False
happy_lifeform = True
#Initialization des classes
player = player.Player()
enemy = enemy.Enemy()

#Fonction du joueur
player.fight()
player.printInfo()


def show_intro_menu():
    print(" ##                      #    #              #              \n#   ###  ## ### ###     # # ### # # ### ##  ### # # ### ###\n #  # # # # #   ##      ### # # # # ##  # #  #  # # #   ##  \n  # ### ### ### ###     # # ###  #  ### # #  ## ### #   ### \n##  #                   # #                                 ")
    print("\t 1- Commencer la partie")
    print("\t 2- Afficher les règles du jeu")
    print("\t 3- Quitter")

    #blindage
    action = input("Que voulez-vous faire ?")  # qu'il faudrait blinder comme dans votre travail précédent
    while not action.isdigit():
        print("entrez un nombre valide")
        action = input("Que voulez-vous faire ?")  # qu'il faudrait blinder comme dans votre travail précédent
    action = int(action)

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
    print("Regles des combat")


#fonction de combat
def fight():
    enemy.choose_enemy()
    
    enemy.fuite_reussite = False
    num_ash_av = 10
    num_ash_arr = 5
    num_ash_e_arr = 10
    spd = 2

    print("atention tu as devan toi un ", enemy.nom, "sauvage")
    #le mouvement
    while player.hp > 0 and enemy.hp > 0:
        
        spd = 2        

        print("tu as ", player.hp, "hp")
        print("lenemy a", enemy.hp, "hp")

        #aficher la distance entre le joueur et lenemy
        ash_av = '#' * num_ash_av
        ash_arr = '#' * num_ash_arr
        ash_e_arr = '#' * num_ash_e_arr

        #verifier si un des sprite sor de larene
        if num_ash_e_arr > 10:
            num_ash_e_arr = 10
        if num_ash_e_arr <= 0:
            num_ash_e_arr = 0
        print(ash_arr + "P" + ash_av + "E" + ash_e_arr)
        
        #blindage
        choix = input("que veux tu faire:\n\n1-avancer\n2-reculer\n3-attaquer\n4-prendre de la morphine pour reprendre des forces?\n")
        while not choix.isdigit():
            print("entrez un nombre valide")
            choix = input("que veux tu faire:\n\n1-avancer\n2-reculer\n3-attaquer\n4-prendre de la morphine pour reprendre des forces?\n")
        
        choix = int(choix)
        
        if choix == 1:
            #sassurer de ne pas agrandir larene
            if num_ash_av > 0:
                tomber = random.randint(0,10)
                if tomber == 10:
                    print("Pas de chances, au moment ou tu a bouger ton pied, tu te prend une racine et tombe")
                    player.hp -= 5
                else:
                    num_ash_arr += spd
                    num_ash_av -= spd

        elif choix == 2:
            #sassurer de ne pas agrandir larene
            if num_ash_arr > 0:
                tomber = random.randint(0,10)
                if tomber == 10:
                    print("Pas de chances, au moment ou tu a bouge ton pied, tu te prend une racine et tombe")
                    player.hp -= 5
                else:
                    num_ash_arr -= spd
                    num_ash_av += spd

        #les attaque
        elif choix == 3:
            
            choix = input("quel arme veux tu prendre?:\n\n1-couteau corps a corps\n2-fusil\n")
            while not choix.isdigit():
                print("entrez un nombre valide")
                choix = input("quel arme veux tu prendre?:\n\n1-couteau corps a corps\n2-fusil\n")
            choix = int(choix)
            #corp a corp
            if choix == 1:
                if num_ash_av > 2:
                    print("ton arme est inéficasse passe ton tour")
                    if enemy.nom == "bob":
                        print("lenemy te lance un boule de feu et tu te prend 20 de degat")
                        player.hp -= 20

                else:
                    print("tu a fait 20 de degat a lenemy")
                    enemy.hp -= 20
                    print(enemy.hp)

            #le fusil
            if choix == 2:
                choix = random.randint(0,100) + big_brain
                if choix < 50:
                    print("ton arme ne fais rien")

                else:
                    print("tu fais 15 degat a lenemy")
                    enemy.hp -= 15
            
        #reprendre des force
        elif choix == 4:
            player.nb_morphine -= 1
            mauvaise_morphine = random.randint(0,10)
            if player.nb_morphine <= 0:
                print("Tu essaye de prendre une aiguille de morphine mais tu ne trouve rien")
                player.nb_morphine = 0
            elif mauvaise_morphine == 10:
                print("tu prend une aiguille de morphine et tu te la plante dans la jambe")
                print("Pas de chance, vous ressenter une douleur atroce")
                print("Il ce trouve que cette morphine etait perime")
                player.hp -= 10
            elif player.hp < 100:
                print("tu prend une aiguille de morphine et tu te la plante dans la jambe")
                print("Tu resentez un sensation agreable, un soulagement qui vous redonne 20 hp")
                player.hp += 10
                if player.hp > 100:
                    player.hp = 100
            else:
                print("tu prend une aiguille de morphine et tu te la plante dans la jambe")
                print("Tu ne ressenter rien, ces bien dommage")
            print("Il te reste " + str(player.nb_morphine) + " morphine")
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
                if enemy.hp < 35 and player.hp > 50:
                    print("lenemy a peur et il recule")
                    num_ash_e_arr -= spd
                    num_ash_av += spd

                else:
                    if num_ash_av > 0:
                        print("recule")
                        num_ash_e_arr -= spd
                        num_ash_av += spd

            elif attaque == 3:
                if num_ash_av > 0:
                    print("lenemy avance")
                    num_ash_e_arr += spd
                    num_ash_av -= spd


        #attaque de joe
        elif enemy.nom == "joe":
            spd = 4
            attaque = random.randint(0,3)
            if attaque == 0:
                print("tu est chanceux lenemmy fais rien")
            
            elif attaque == 1:
                #si la distance est de moin de deux metre
                if num_ash_av < 2:
                    print("quel malchance lenemy tataque avec ses grosse griffe\ntu te prend 15 de degat")
                    player.hp -= 15
        
            elif attaque == 2:
                if enemy.hp < 35 and player.hp > 50:
                    print("lenemy a peur et il recule")
                    num_ash_e_arr -= spd
                    num_ash_av += spd
                    num_ash_e_arr -= spd
                    num_ash_av += spd
                    

                else:
                    if num_ash_av > 0:
                        print("lenemy avance")
                        num_ash_e_arr += spd
                        num_ash_av -= spd

            elif attaque == 3:
                if num_ash_av > 0:
                    print("lenemy avance")
                    num_ash_e_arr += spd
                    num_ash_av -= spd


        
        


        
    #message de fin de combat
    if player.hp <= 0:
        print("vous ete mort vous avez perdu")
        generic()
        sys.exit(0)
    elif enemy.hp <= 0:
        print("bravo vous avez gagnez le combat")
    
    os.system("cls")

#fonction pour ramasser des objet
def rammasser():
    objet = ["plaque dacier", "reacteur", "morphine"]

    #rammasser des objet pour linventaire
    if random.choice(objet) == "morphine":
        random_morphine = random.randint(1,10)
        player.nb_morphine += random_morphine
        
    elif random.choice(objet) == "plaque dacier":
        print("la plaque dacier va dans ton inventaire")
        player.enventory.append("plaque dacier")

    else:
        print("le reacteur va dans ton iventaire")

def generic():
    os.system("cls")
    print("directeur artistique:\n Gabriel Foriel-Fusier et nicolas prigge")
    time.sleep(0.5)
    print("directeur informatique:\nNicolas prigge et Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("développeur:\n Gabriel Foriel-Fusier et nicolas Prigge ")
    time.sleep(0.5)
    print("game creatif:\nnicolas prigge et Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("directeur de l'environnement:\n Gabriel Foriel-Fusier et nicolas Prigge")
    time.sleep(0.5)
    print("directeur de l'éclairage:\nnicolas prigge et Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("directeur gastronomique:\n Gabriel Foriel-Fusier  et nicolas prigge")
    time.sleep(0.5)
    print("préposé au chaise:\nnicolas prigge et Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("Directeur de la direction:\n Gabriel Foriel-Fusier et Nicolas Prigge")
    time.sleep(0.5)
    print("Directeur des sac de chips:\nnicolas prigge et Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("Directeur du hdawhulauiwhuaihuih:\n Gabriel Foriel-Fusier et nicolas prigge")
    time.sleep(0.5)
    print("préposé à la baguette: \n Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("directeur sportif:\nnicolas prigge")
    time.sleep(0.5)
    print("directeur du blop:\n Gabriel Foriel-Fusier")
    time.sleep(0.5)
    print("remerciement a genreic, github,stackoverflow, M. Buscarlet, frère Bogdanov et personne.\nAvec laide toute particulière de sa majeste le gateau is a lie")
    



show_intro_menu()
print("on est parti")



#chapitre un
#liste dobjet a gagner
os.system("cls")
print("chapite 1")
time.sleep(val_sleep)
print("\n vous decidez daller explorer pour trouver une forme de vie")
time.sleep(val_sleep)
print("vous vous premenez sur une planet tropicale qui vous semble deserte")
time.sleep(val_sleep)
print("apres plusieur heures de marche et dexploration vous trouvez une forme de vie,\nmais se nest pas celle que vous vouliez decouvrir")
time.sleep(val_sleep)
os.system("cls")
print("la bete semble hostile\n")
time.sleep(val_sleep)
fight()


print("bravo tu a gagner ton premier combat")
time.sleep(val_sleep)
rammasser()
time.sleep(val_sleep)
print("tu continue a explorez la planete")
time.sleep(val_sleep)
#Ptet autre choix
print("\n")
print("Un bruit resonne dans votre tête, on dirait une que quelqun vous parle, elle vous demande daller dans sa direction")
time.sleep(val_sleep)
#discution avec une creature

#blindange
choix = input("Vouslez vous suivre cette voix\n1-Oui\n2-Non\n")
while not choix.isdigit():
    print("entrez un choix valide")
    choix = input("Vouslez vous suivre cette voix\n1-Oui\n2-Non\n")
choix = int(choix)

#la discution
time.sleep(val_sleep)
if choix == 1:
  end_conv = False
  
  print("Tres rapidement vous trouvez une creature, avec un cerveau surdimensionnés")
  time.sleep(val_sleep)
  print("la crature:Bienvenue, je me nomme Sullivan, vus que tu ma entendue, tu est donc celui que je cherche\n")
  
  #boucle de discution
  while not end_conv:   #while not end_conv :
    time.sleep(val_sleep)
    
    #blindage du code
    choix = input("Que voulez-vous dire\n1-Lui demander de quoi elle parle\n2-Lui demander ou vous êtes\n3-Quitter la conversation\n")
    while not choix.isdigit():
        print("veuillez entrer un nombre valide svp")
        choix = input("Que voulez-vous dire\n1-Lui demander de quoi elle parle\n2-Lui demander ou vous êtes\n3-Quitter la conversation\n")
    
    choix = int(choix)

    time.sleep(val_sleep)
    #question 1
    if choix == 1:
      print(player.nom + ": De quoi parler-vous?")
      time.sleep(val_sleep)
      print("Sullivan: Mon enfant, ne soyez pas impatient, vous verez en temps venus")
    
    #question 2
    elif choix == 2:
      print("la creature: Nous sommes sur la sans nom, vois-tu, depuis le cataclysme seul les fous ou les d'espérer y restent, mais jaime bien appeler cette region les remparts")
      time.sleep(val_sleep)
      choix = int(input("Que voulez vous dire\n1-Le cataclysme?\n2-Pourquoi restez vous?\n3-Ne rien dire\n"))
      if choix == 1:
        time.sleep(val_sleep)
        print(player.nom + ": Le cataclysme?")
        time.sleep(val_sleep)
        print("Sullivan: Je suis bien navré mais jai ete bien trop traumatisé de cette événement, je ne veux pas en parler")
      else:
        print(player.nom + ": Pourquoi restez-vous?")
        time.sleep(val_sleep)
        print("Sullivan: Ces chez moi, de plus cela me permet de rester tranquille, de temps en temps je doit me cacher, sur mon territoire, ces parfait pour un vieux comme moi")
    
    #quiter  
    elif choix == 3:
      end_conv = True
      print(player.nom + ": Aurevoir")
      print("Sullivan: Eh bien, aurevoir explorateur, eh oui je le sais, jai vus le crash")
      time.sleep(val_sleep)
      print("Sullivan: Quand tu sera rendue a la limite entre les rempart et la zone du cataclysme, tu le reconnetra, va vers une grotte, jy serai")
      time.sleep(val_sleep)
      print("Sullivan: Ah aussi, fais attention, le cataclysme, a engendré des erreurs de la nature, ils sont tres dangereux, tu a du en voir un deja")
      time.sleep(val_sleep)
      invitation = True
    
    else:
        print(player.nom + ": " + choix)
        print("Sullivan: je en comprend pas repete")

elif choix == 2:
    print("tu continu ton chemin")

#combat
if choix == 1:
    print("comme te lavait prevenu la crature tu fait face a un enemy")
    fight()

if choix == 2:
    print("tu fait face a un enemy")
    fight()

#aller se coucher
#blindage
os.system("cls")
choix = input("Voulez-vous dormire\n1-Oui\n2-Non\n")
while not choix.isdigit():
    print("entrez un nombre valide")
    choix = input("Voulez-vous dormire\n1-Oui\n2-Non\n")

choix = int(choix)

#someil
if choix == 1:
    print("decide d'aller dormir pour la nuit\n")
    attaque = random.randint(0,3)
    #la cahnce sur trois de se faire reveiller
    if attaque == 3:
        time.sleep(2)
        print("tu te fais revailler par une creature pas trop gentille.")
        fight()
        rammasser()
        print("tu retourne te coucher")
        time.sleep(1)
        print("tu te reveille apres cette nuit ecouter par le monstre")

    else:
        time.sleep(4)
        input("bon matin a tu passer une  bonne nuit?\n")

else:
    print("Vous voyez devant vous un la creature de toute a lheure, elle dort paisiblement")
    time.sleep(val_sleep)
    
    #blindage
    choix = input("Un murmure vous traverse l'esprit, vos mains ce mette a trembler\n1-Vous l'ecraser de toutes vos forces\n2-Vous vous reprenez et vous partez\n")
    while not choix.isdigit():
        print("entrez un nombre valide")
        choix = input("Un murmure vous traverse l'esprit, vos mains ce mette a trembler\n1-Vous l'ecraser de toutes vos forces\n2-Vous vous reprenez et vous partez\n")

    choix = int(choix)
    
    #tuer la creature
    if choix == 1:
        print("Vous mettez vos mains autour de sa tete, puis lecraser avec force")
        time.sleep(val_sleep)
        print("Des cries depouvante, vous traverse la tete.")
        happy_lifeform = False
        time.sleep(val_sleep)
        
        #blindage
        choix = input("D'autres murmures sinsinues dans votres esprit, ils ont faim, vous avez faim\n1-Vous vous delectez de cette bouilli de cerveaux\n2-Vous en avez suffisament fait, vous lenterrez\n")
        while not choix.isdigit():
            print("entrez un nombre valide")
            choix = input("D'autres murmures sinsinues dans votres esprit, ils ont faim, vous avez faim\n1-Vous vous delectez de cette bouilli de cerveaux\n2-Vous en avez suffisament fait, vous lenterrez\n")
        
        choix = int(choix)
        
        #bouffer la cervelle
        if choix == 1:
            print("Vous passez la nuit a vous engoufrez de cervelles")
            time.sleep(val_sleep)
            print("Vous remarquer que vous pensez mieux, labsortion du cerveau augment votre vision et votre capaciter a penser.")
            big_brain += 10
    
    #ne pas tuer la creature
    else:
        print("plus loin vous voyez quelque chose parterre")
        time.sleep(val_sleep)
        rammasser()

os.system("cls")
print("tu est maintenant pres a aller explorer la planet")
print("tu range ton campement et tu vas explorer")
time.sleep(val_sleep)
print("tu tombe sur une construction qui te semble etre un centre spatial")
print("tu vas voir dans le centre")
time.sleep(val_sleep)
#les multiple combat
for i in range(5):
    os.system("cls")
    fight()
    rammasser()
    print("tu continue lexploration")
    time.sleep(val_sleep)

print("bravo tu a combatu tout se monde")
print("tu est rendu a la salle principale et tu voit mune fuser en construction")
time.sleep(val_sleep)

#blindage
choix = input("veut tu aller voir la fuser qui pourait etre ton moyen de rentrer a la maison?\n\n1-oui\n2-non")
while not choix.isdigit():
    print("entrez un choix valide")
    choix = input("veut tu aller voir la fuser qui pourait etre ton moyen de rentrer a la maison?\n\n1-oui\n2-non")

choix = int(choix)
    
#conclusion
if choix == 1:
    print("tu monte dans la fuser")
    time.sleep(val_sleep)
    print("il reste un dernier ingenieur dans la fuser(enemy)")
    fight()
    rammasser()
    print("tu est seule dans le cokpit")
    time.sleep(val_sleep)
    print("comme tu est un tres bon astronaute tu comprend vite comment marche la fusee")
    os.system("cls")
    print("decompte de lancement:")
    
    for i in range(10):
        print(10 - i)
        time.sleep(1)
    
    print("decollage")
    time.sleep(5)
    print("tu est dans lespace instale tpi confortablement car tu a un long voyage de trois minut(temp reel)")
    time.sleep(180)
    print("est de retour sur terre")
    generic()

if choix == 2:
    print("tu va mourir sur cette planete mais ses ton choix.")
    generic()
