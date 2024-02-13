
from naldeo import NaldeoStdModel, printB, printI, repertoire_courant, joblib_backups
from matplotlib import pyplot as plt


###########################################################################################
#
#   Classes Métier Heritant de NaldeoStdModel et transformers
#
###########################################################################################



class NaldeoTraductionModel2(NaldeoStdModel):
    def __init__(self):
        # Pipeline pour la traduction ()
        super().__init__("translation", "PaulineSanchez/Modele_traduction_HF")

class NaldeoTraductionModel(NaldeoStdModel):
    def __init__(self):
        # Pipeline pour la traduction (Anglais vers Français par exemple)
        super().__init__("translation_en_to_fr", "t5-base")
    def traduit(self, texte):
        return self.do(texte)[0]['translation_text']
        
class NaldeoClassificationModel(NaldeoStdModel):
    def __init__(self,labels):
        self.labels = labels
        super().__init__("zero-shot-classification", "facebook/bart-large-mnli")

    def do(self,text):
        printI("Analyse "+ self.task +"...")
        self.result = self.pipeline(
            text,
            self.labels,
            hypothesis_template="Cet article est sur {}."
        )
        return self.result

    def plot(self):
        plt.figure(figsize=(15, 6))
        plt.barh(self.result['labels'], self.result['scores'], color='skyblue')
        plt.xlabel('Scores')
        plt.title('Scores pour chaque catégorie')
        chemin_fichier = joblib_backups + 'ZeroShotModel.png'
        plt.savefig(chemin_fichier)
        plt.show()


class NaldeoResumeModel(NaldeoStdModel):
    def __init__(self):
        super().__init__("summarization", "facebook/bart-large-cnn")
    def do(self,text):
        self.result = self.pipeline(text, max_length=50, min_length=30, do_sample=False)
        return self.result
    

class NaldeoImageDescriber(NaldeoStdModel):
    def __init__(self):
        super().__init__("image-to-text", "Sof22/image-caption-large-copy")
    def do(self,image):
        self.result = self.pipeline(image)
        return self.result


class NaldeoTableQuestionning(NaldeoStdModel):
    def __init__(self):
        super().__init__("table-question-answering", "google/tapas-large-finetuned-wtq")
    def do(self,table,question):
        self.response = self.pipeline(table=table, query=question)
        self.result = self.response['cells'][0]
        return self.result




if __name__ == "__main__":

    #######################################################

    textSolar = """Solar Horizon is an innovative photovoltaic project aimed at harnessing the power of solar energy to create a sustainable and eco-friendly 
    solution for energy production. Located in Tarnos, this state-of-the-art solar facility encompasses cutting-edge photovoltaic technology to convert sunlight into electricity efficiently.
    The project incorporates the latest advancements in solar cell technology, utilizing high-efficiency photovoltaic EMS to maximize energy conversion and output.
    This adaptability ensures NALDEO the ability to provide Green Energy all arounde the world and beyond"""



    textWater = """
    The document is a public service delegation contract for drinking water. It includes several chapters that cover general provisions, rights and obligations of the delegatee, resources allocated to the delegation, delegatee's responsibility and insurance, preparation period for the service, water resource and production, as well as safety measures and water quality monitoring.
    The document provides information on the monitoring, operation, maintenance of drinking water production facilities, management of green spaces, handling of liquid discharges, bulk water delivery and importation, right of use of public roads and private properties, regime of pipelines under public roads, distributed water quality, network purging operations, relations with third parties, connection regulations, network accessories, and fire hydrants, water theft prevention, and general conditions of water supply to subscribers. The document fragment pertains to the management of subscribers to public sanitation services, customer reception, expected service performance for users, management of subscribers in difficulty, perceived quality measurement, meter regulations, communication and visibility of the service, works regulations, environmental aspects, and the information system. The document fragment covers various articles related to the management of the public drinking water service.
        """


    testFinance = """
    In the fiscal year ending December 31, 2023, Imaginary Corporation continued its commitment to financial excellence, achieving remarkable results across various financial indicators. The company's strategic initiatives, robust cost management, and revenue diversification efforts contributed to a solid financial performance.
        """

    textBDThorgal = """
    The story revolves around Thorgal Aegirsson, a Viking warrior with a mysterious and troubled past. Thorgal's life takes a dramatic turn when he discovers an alien spacecraft and rescues Aaricia, the daughter of the Viking chief. As Thorgal navigates the challenges of Viking society, he grapples with supernatural forces, encounters gods and mythological creatures, and confronts powerful adversaries. The series beautifully weaves Norse mythology into its narrative, creating a rich and immersive world for readers.
    """

    textBDTintin = """
    "Tintin" and "Captain Haddock" are iconic characters from the world of Belgian comics, specifically created by the cartoonist Hergé (pseudonym of Georges Remi). The adventures of Tintin and Captain Haddock are part of the comic series called "The Adventures of Tintin" ("Les Aventures de Tintin" in French), which was first introduced in 1929. The series became immensely popular and is considered one of the greatest achievements in the comic book medium.
    """

    textOther = """
    To be, or not to be: that is the question
    """


    # Exemple de texte long à résumer

    c = input("""
    choose a topic for local driven IA Transformer
        solar (s) 
        water (w)
        finance (f)
        BD thorgal (t)
        captain (h)
        ... other
    """) 
        
    if c =="w":
        text = textWater
    elif c=="s":
        text = textSolar
    elif c=="f":
        text = testFinance
    elif c=="t":
        text = textBDThorgal
    elif c=="h":
        text = textBDTintin
    else :
        text = textOther

    printI(text)
    Resumeur = NaldeoResumeModel()
    summary = Resumeur.do(text)
    printB(summary[0]['summary_text'])



    Traducteur = NaldeoTraductionModel()
    traduction = Traducteur.do(text)[0]['translation_text']
    printI(f"Texte traduit en français via le modèle : {Traducteur.model}")
    printB(traduction)


    labels=[
    "Eau potable",
    "Assainissement",
    "Voirie Réseaux",
    "Chauffage urbain",
    "Energie Photovoltaique",
    "Informatique",
    "finance",
    "bande dessinée"
    ]

    print ("Liste des catégories de texte : ", labels)
    Classificateur = NaldeoClassificationModel(labels)
    result = Classificateur.do(traduction)
    printI("affichage du type de contenu")
    Classificateur.plot()


    
