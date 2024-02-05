import os
from transformers import pipeline
import joblib


# répertoire de sauvegarde locale pour les pipelines HF
joblib_backups = "C:\\pydev\\hfgj\\"

# variable globale
repertoire_courant = os.getcwd()

# catégories métier
categories=["Eau potable","Assainissement","Voirie Réseaux","Chauffage urbain","Energie Photovoltaique","Informatique","finance","bande dessinée","french","belge","other"]

###########################################################################################
#
#   Fonctions de mise en forme / terminal 
#
###########################################################################################
# jaune
def printI(str):
    print()
    print("\033[93m"+str+"\033[0m")
    print()
# bleu
def printB(str):
    print()
    print("\033[94m"+str+"\033[0m")
    print()

# system  : red
def printSysNOK(str):
    print()
    print("\033[91m"+str+"\033[0m")
    print()


# system : OK
def printSysOK(str):
    print()
    print("\033[1m"+str+"\033[0m")
    print()


###########################################################################################
#
#   Interface  standard implémentant les transformers Huggingface (pipelines), 
#   et leur sauvegarde locale si non préexistante (joblib)
#
###########################################################################################

class NaldeoStdModel():
    # instantiation 
    def __init__(self, task="text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment"):
        self.task = task
        self.model = model
        # chemin de sauvegarde du pipeline dans un répertoire spécifique
        self.chemin_sauvegarde = joblib_backups+self.__class__.__name__+".joblib"
        self.result = None
        self.load()
    
    # chargement ou compilation
    def load(self):
        # Chargement du pipeline depuis la sauvegarde du modèle et des paramètres du réseau
        # @todo implémenter autrement
        try:
            # Chargement du pipeline depuis le fichier local
            self.pipeline = joblib.load(self.chemin_sauvegarde)
            printSysOK(" >> Sauvegarde locale du pipeline déjà disponible pour le transformer "+self.__class__.__name__)
        except FileNotFoundError:
            # Si le fichier n'est pas trouvé, créez un nouveau pipeline
            # Sauvegarde du nouveau pipeline
            printSysNOK(" >> Sauvegarde locale du pipeline en cours pour le transformer "+self.__class__.__name__)
            self.dump()

    # dump local joblib du pipeline
    def dump(self):
        self.pipeline = pipeline(self.task, self.model)
        joblib.dump(self.pipeline, self.chemin_sauvegarde)
        return self.pipeline

    # to be overriden 
    def do(self,text="question de l'utilisateur final, ici"):
        return self.pipeline(text)
    
    # effacer le modèle
    def forget(self):
        if os.path.exists(self.chemin_sauvegarde):
            os.remove(self.chemin_sauvegarde)
            print(f"Le modèle {self.chemin_sauvegarde} a été supprimé avec succès.")
        else:
            print(f"Le modèle {self.chemin_sauvegarde} n'existe pas.")
        