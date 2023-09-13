import time

def demande_du_nom():
    #variable de programe
    nom = ""

    #introduction
    print("vous etiez parti explorez le systeme planetaire de kepler-186 et un astreoide a percuter le vessaux et vous a fait tomber sur la planete kepler-186b")
    time.sleep(1)

    while True:
        nom = input("vous ne vous rappelr pas de vorte nom donc comment voulez vous vous appeler:")

        if nom == "":
            print("svp entrez un nom")
        else:
            break

demande_du_nom()