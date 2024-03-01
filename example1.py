
import math

# définition d'un cercle, avec sa méthode aire
# avantage : définit une fois, réutilisable partout
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):
        return math.pi * self.rayon**2
    def circonférence(self):
        return 2* math.pi * self.rayon
    def faire(self):
        return "fait"



# définition d'un cylindre 
# objet qui hérite d'être un cercle avec une hauteur en plus
# super() désigne le cercle sous jacent

class Cylindre(Cercle):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon)
        self.hauteur = hauteur
    
    def section(self):
        return super().aire()
        
    def volume(self):
        return self.section() * self.hauteur
    
    def aire(self):
        aire_latérale = super().circonférence()*self.hauteur
        aire_haut = super().aire()
        aire_bas = super().aire()
        aire_cylindre = aire_latérale + aire_bas + aire_haut
        return aire_cylindre



if __name__ == "__main__":
    rayon = 1
    hauteur = 1
    mon_cylindre = Cylindre(hauteur=hauteur, rayon=rayon)
    
    print("section du cylindre ",mon_cylindre.section())
    print("aire du cylindre ",mon_cylindre.aire())
    print("volume du cylindre ", mon_cylindre.volume())
    print("circonférence du cylindre = ", mon_cylindre.circonférence())
