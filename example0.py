
# calcul procédural
# beaucoup d'inconvénients (copier coller, peu maintenable)
rayon = 1
aire = 3.14 * rayon * rayon
print("calcul pour 1 ", aire)

rayon = 2
aire = 3.14 * rayon * rayon
print("calcul pour 2 ", aire)


# fonction écrite une fois
# inconvénient : autant de fonction aire que de forme géométrique
def aire(rayon):
    return 3.14 * rayon**2

print("calcul pour 3 ", aire(3))
print("calcul pour 4 ", aire(4))


# avec le programmation objet => import d'une classe prédéfinie
# avantage : ne pas rééinventer la roue
from example1 import Cercle
c = Cercle(5)
print("calcul pour 5 ", c.aire())



