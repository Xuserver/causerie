from app import NaldeoTraductionModel, NaldeoClassificationModel
from poo import Cylindre
from naldeo import printSysOK , printB, categories, printI
mon_cylindre = Cylindre( hauteur=2, rayon=4)

textSolar = f"""Solar Horizon is an innovative photovoltaic project aimed at harnessing the power of solar energy to create a sustainable and eco-friendly 
solution for energy production. Located in Tarnos, this state-of-the-art solar facility encompasses cutting-edge photovoltaic technology to convert sunlight into electricity efficiently.
The project incorporates the latest advancements in solar cell technology, utilizing high-efficiency photovoltaic EMS to maximize energy conversion and output.
This adaptability ensures NALDEO the ability to provide Green Energy all around any cylinder dtarting from {mon_cylindre.volume()} meters and beyond"""


printB("le texte à traduire est : " )
print (textSolar)

Traducteur = NaldeoTraductionModel()
traduction = Traducteur.do(textSolar)[0]['translation_text'] # json
printB("le texte traduit est : " )
print (traduction)

printB ("Le texte traduit doit être catégorisé dans cette liste : ")
print(categories)

printB("La représentation graphique correspondante est donc : " )
Classificateur = NaldeoClassificationModel(categories)
Classificateur.do(traduction)
Classificateur.plot()
