from naldeo import NaldeoTableQuestionning
import pandas as pd

# prestation	unit	prix	entreprise
table1 = pd.read_excel('tabdata.xlsx', dtype={'prix': 'str'})
question = "quel prix pour Amiante?"
tqa = NaldeoTableQuestionning()
reponse = tqa.do(table=table1, question=question)
print(reponse)



# question = "quel prestation coute 4?"
# question = "combien pour un constat et une démolition?"
# print(tqa.response)
