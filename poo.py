# static
class PI:
    @staticmethod
    def val():
        return 3.14 

# parent
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return PI.val() * self.rayon**2
    
    def circonférence(self):
        return 2* PI.val() * self.rayon

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


# sans héritage, passage par argument 
class CylindreFromCercle:
    def __init__(self, cercle : Cercle, hauteur):
        self.cercle = cercle
        self.hauteur = hauteur
        
    def volume(self):
        return self.cercle.aire() * self.hauteur
    
    def aire(self):
        return 2 * (self.cercle.aire() + self.cercle.circonférence() * self.hauteur)
    
    def circonférence(self):
        return self.cercle.circonférence()

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

    mon_autrecylindre = CylindreFromCercle( cercle=mon_cercle, hauteur=hauteur) 
    # autre design pattern de type factory
    print("mon_autrecylindre.volume = ", mon_autrecylindre.volume())
    print("mon_autrecylindre.circonférence = ", mon_autrecylindre.circonférence())
    print("mon_autrecylindre.aire = ",mon_autrecylindre.aire())
