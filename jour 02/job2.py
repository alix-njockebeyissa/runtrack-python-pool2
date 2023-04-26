class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("Age :", self.age)
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, newAge):
        self.age = newAge

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.affichageAge()