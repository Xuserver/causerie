import math

# parent
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def aire(self):
        return math.pi * self.rayon**2
    def circonférence(self):
        return 2* math.pi * self.rayon

# enfant
class Cylindre(Cercle):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon)
        self.hauteur = hauteur
        
    def volume(self):
        return self.section() * self.hauteur
    
    def section(self):
        return super().aire()

    def aire(self):
        # calcul_sans_heritage = 2 * PI.val() * self.rayon * self.hauteur  + 2 *  PI.val() * self.rayon**2

        aire_latérale = super().circonférence()*self.hauteur
        aire_haut = super().aire()
        aire_bas = super().aire()
        aire_cylindre = aire_latérale + aire_bas + aire_haut
        return aire_cylindre



if __name__ == "__main__":
    rayon = 5
    hauteur = 6
    mon_cercle = Cercle(rayon)
    print("cercle.aire = ", mon_cercle.aire())
    print("cercle.circonférence = ", mon_cercle.circonférence())
    
    mon_cylindre = Cylindre( hauteur=hauteur, rayon=rayon)
     # on peut inverser les arguments, parce qu'on les nomme
    print("mon_cylindre.volume = ", mon_cylindre.volume())
    print("mon_cylindre.circonférence = ", mon_cylindre.circonférence())
    print("mon_cylindre.aire = ",mon_cylindre.aire())
