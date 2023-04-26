import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

    def __init__(self):
        self.paquet = []
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def valeur_carte(self, carte):
        if carte.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif carte.valeur == 'As':
            return 11
        else:
            return int(carte.valeur)

    def valeur_main(self, main):
        total = 0
        as_count = 0
        for carte in main:
            valeur = self.valeur_carte(carte)
            if valeur == 11:
                as_count += 1
            total += valeur
        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1
        return total

    def afficher_main(self, main):
        for carte in main:
            print(carte.valeur, carte.couleur)

    def jouer(self):
        self.melanger()
        main_joueur = [self.tirer_carte(), self.tirer_carte()]
        main_croupier = [self.tirer_carte(), self.tirer_carte()]
        print("Main du joueur :")
        self.afficher_main(main_joueur)
        print("Main du croupier :")
        print(main_croupier[0].valeur, main_croupier[0].couleur)
        while True:
            choix = input("Voulez-vous prendre une carte ? (o/n) ")
            if choix == 'o':
                nouvelle_carte = self.tirer_carte()
                main_joueur.append(nouvelle_carte)
                print("Vous avez pioché :")
                print(nouvelle_carte.valeur, nouvelle_carte.couleur)
                total_joueur = self.valeur_main(main_joueur)
                print("Votre main vaut maintenant :", total_joueur)
                if total_joueur > 21:
                    print("Vous avez dépassé 21, vous avez perdu !")
                    return
            else:
                break
        total_joueur = self.valeur_main(main_joueur)
        total_croupier = self.valeur_main(main_croupier)
        print("Main du joueur :")
        self.afficher_main(main_joueur)
        print("Votre main vaut :", total_joueur)
        print("Main du croupier :")
        self.afficher_main(main_croupier)
        print("La main du croupier")
