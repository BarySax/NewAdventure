##W##########################################################A CHANGAERAREWRERERAERAEEARRAERAERAEWRAWWWRF
import random
import time
class Enemy:
   def __init__(self):
      bloup = 30
      #self.num_hash_e_arr = 5
      #self.num_hash_av = 5
      #a ebnlev
      #self.num_hash_arr = 5
      #self.hash_arr = "#" * self.num_hash_arr
      #
      #self.hash_av = "#" * self.num_hash_av
      #self.hash_e_arr = "#" * self.num_hash_e_arr
      self.type = ["joe", "bob"]
      self.hp = 100
      #self.distanceToPlayer = 0
      self.nom = random.choice(self.type)
      

      
   """
   def attaque(self):
      if self.nom == "joe":
         self.hash_av = "#" * self.num_hash_av
         self.hash_e_arr = "#" * self.num_hash_e_arr
         #print("#################\n" + self.hash_arr + "P" + self.hash_av + "E" + self.hash_e_arr)
         if self.num_hash_av <= 0:
            print("Erika")
         else:
            self.num_hash_e_arr += 1
            self.num_hash_av -= 1
            if self.num_hash_av < 0:
               self.num_hash_av = 0
            if self.num_hash_e_arr < 0:
               self.num_hash_e_arr = 0
            if self.num_hash_av > 15:
               self.num_hash_av = 15
            if self.num_hash_e_arr > 9:
               self.num_hash_e_arr = 9
            time.sleep(1)
         
      elif self.nom == "bob":
         print("je suis bob")
         choix = random.randint(1,3)
         if choix == 1:
            self.num_hash_e_arr += 1
            self.num_hash_av -= 1
            self.hash_av = "#" * self.num_hash_av
            self.hash_e_arr = "#" * self.num_hash_e_arr
            #print("#################\n" + self.hash_arr + "P" + self.hash_av + "E" + self.hash_e_arr)
            if self.num_hash_av < 0:
               self.num_hash_av = 0
            if self.num_hash_e_arr < 0:
               self.num_hash_e_arr = 0
            if self.num_hash_av > 15:
               self.num_hash_av = 15
            if self.num_hash_e_arr > 9:
               self.num_hash_e_arr = 9
         if choix == 2:
            self.num_hash_e_arr -= 1
            self.num_hash_av += 1
            self.hash_av = "#" * self.num_hash_av
            self.hash_e_arr = "#" * self.num_hash_e_arr
            #print("#################\n" + self.hash_arr + "P" + self.hash_av + "E" + self.hash_e_arr)
            if self.num_hash_av < 0:
               self.num_hash_av = 0
            if self.num_hash_e_arr < 0:
               self.num_hash_e_arr = 0
            if self.num_hash_av > 15:
               self.num_hash_av = 15
            if self.num_hash_e_arr > 9:
               self.num_hash_e_arr = 9
         elif choix == 3:
            print("Erika")
         time.sleep(1)

      else:
         print("erreur")
      """