# autre design pattern : le décorateur


# Définition du décorateur voiture
def voiture(classe):
    classe.type = "Engin roulant, avec quatre roures et un moteur"
    return classe


# Définition de la classe Porsche décorée
@voiture
class Porsche:
    def __init__(self, modèle):
        self.modèle = modèle

    def afficher_details(self):
        print("Type:", self.type)
        print("Modèle:", self.modèle)


# Création d'une Porsche 911
p = Porsche("911")
p.afficher_details()