import random
spd = 2
enemy = "Joe"
e_hp = 30
p_hp = 50
p_dead = False
e_dead = False
num_hash_arr = 5
num_hash_av = 5
num_hash_e_arr = 5
print("DEvant vous fais face un ",enemy," sauvage, il a ",e_hp," point de vie.")
while p_dead == False or e_dead == False:
    hash_e_arr = "#" * num_hash_e_arr
    hash_arr = "#" * num_hash_arr
    hash_av = "#" * num_hash_av
    print("#################\n" + hash_arr + "P" + hash_av + "E" + hash_e_arr)
    movement = int(input("Que voulez-vous faire:\n\n1-Allez en arriere\n2-Allez en avant\n3-Ne pas bouger\n"))
    if movement == 1:
        print("Vous reculer de deux metres.")
        num_hash_arr -= spd
        num_hash_av += spd
    elif movement == 2:
        print("Vous avancerr de deux metres.")
        num_hash_arr += spd
        num_hash_av -= spd
    else:
        print("Vous ne bouger pas")
    if num_hash_av < 0:
        num_hash_av = 0
    if num_hash_e_arr < 0:
        num_hash_av = 0
    if num_hash_arr < 0:
        num_hash_arr = 0
    if num_hash_av > 15:
        num_hash_av = 15
    if num_hash_e_arr > 10:
        num_hash_av = 10
    if num_hash_arr > 10:
        num_hash_arr = 10
    hash_arr = "#" * num_hash_arr
    hash_av = "#" * num_hash_av
    print("#################\n" + hash_arr + "P" + hash_av + "E" + hash_e_arr)
    action = int(input("Que voulez-vous faire:\n\n1-Attaquer\n2-Prendre de la morphine\n3-Ce redeplacer\n"))
    if action == 1:
        re_attack = True
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
                e_hp -= p_degat
                print("Vous avez fait ",p_degat," degat, ",enemy," a ",e_hp," point de vie.")
            else:
                print("Rater")
        else:
            #Le fusil est moin bon, faut donner un avantage
            try_attack = random.randint(0,100)
            if try_attack >= 60:
                random_degat = random.randint(0,5)
                p_degat = 5 + random_degat
                e_hp -= p_degat
                print("Vous avez fait ",p_degat," degat, ",enemy," a ",e_hp," point de vie.")
            else:
                print("Rater")
    elif action == 2:
        p_hp += 5
        if p_hp >= 100:
            p_hp = 100
        print("Vous avez ", p_hp, "point de vie.")
    else:
      movement = int(input("Que voulez-vous faire:\n\n1-Allez en arriere\n2-Allez en avant\n"))
      if movement == 1:
        print("Vous reculer de deux metres.")
        num_hash_arr -= spd
        num_hash_av += spd
      elif movement == 2:
        print("Vous avancerr de deux metres.")
        num_hash_arr += spd
        num_hash_av -= spd
      else:
        print("Vous ne bouger pas")
      if num_hash_av < 0:
        num_hash_av = 0
      if num_hash_e_arr < 0:
        num_hash_av = 0
      if num_hash_arr < 0:
        num_hash_arr = 0
      if num_hash_av > 15:
        num_hash_av = 15
      if num_hash_e_arr > 10:
        num_hash_av = 10
      if num_hash_arr > 10:
        num_hash_arr = 10
      hash_arr = "#" * num_hash_arr
      hash_av = "#" * num_hash_av
    if e_hp <= 0:
        print("Vous avez gagner.")
        e_dead = True