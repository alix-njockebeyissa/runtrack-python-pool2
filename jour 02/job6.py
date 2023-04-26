class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print("Marque:", self.marque)
        print("Année:", self.annee)
        print("Prix:", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes:", self.portes)
voiture1 = Voiture("Renault", 2020, 15000)
voiture1.informationsVehicule()
class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")


moto1 = Moto("Yamaha", 2022, 12000)
moto1.informationsVehicule()
class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nAnnée: {self.annee}\nPrix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")
        
    def demarrer(self):
        print("Je suis une voiture, je démarre !")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roue}")
        
    def demarrer(self):
        print("Je suis une moto, je démarre !")