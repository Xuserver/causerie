from stdmodel import printSysOK , printB, printI
from naldeo import NaldeoTraductionModel, NaldeoClassificationModel


textAnglais = f"""Solar Horizon is an innovative photovoltaic project aimed at harnessing the power of solar energy to create a sustainable and eco-friendly 
solution for energy production. Located in Tarnos, this state-of-the-art solar facility encompasses cutting-edge photovoltaic technology to convert sunlight into electricity efficiently.
The project incorporates the latest advancements in solar cell technology, utilizing high-efficiency photovoltaic EMS to maximize energy conversion and output.
"""
# catégories 
categories=["Eau potable","Assainissement","Voirie Réseaux","Chauffage Urbain","Energie Photovoltaique","Informatique"]

printB("le texte à traduire est : " )
print(textAnglais)

Traducteur = NaldeoTraductionModel()
traductionFrançais = Traducteur.traduit(textAnglais)
printB("le texte traduit est : " )
printSysOK(traductionFrançais)

printB ("Le texte traduit doit être catégorisé dans cette liste : ")
print(categories)

printB("La représentation graphique correspondante est donc : " )
Classificateur = NaldeoClassificationModel(categories)
Classificateur.do(traductionFrançais)
Classificateur.plot()
