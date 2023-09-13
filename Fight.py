import time
import random
enemy = "Joe"
e_hp = 30
p_dead = False
e_dead = False
while p_dead == False or e_dead == False:
    print("DEvant vous fais face un ",enemy," sauvage, il a ",e_hp," point de vie.")
    time.sleep(0.5)
    action = int(input("Que voulez-vous faire:\n\n1-Attaquer\n2-Bloup\n"))
    time.sleep(0.5)
    if action == 1:
        attack = int(input("Quelle type d'attaque voulez-vous faire:\n\n1-Corps a Corps\n2-Distance\n1"))
        if attack == 1:
            try_attack = random.randint(0,100)
            time.sleep(0.5)
            if try_attack >= 100:
                random_degat = random.randint(0,5)
                p_degat = 5 + random_degat
                e_hp -= p_degat
                print("Vous avez fait ",p_degat," degat, ",enemy," a ",e_hp," point de vie.")
            else:
                print("Rater")