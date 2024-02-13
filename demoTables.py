from app import NaldeoTableQuestionning
import pandas as pd

if False : 
    data = {"Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"], "Number of movies": ["87", "53", "69"]}
    table = pd.DataFrame.from_dict(data)
    question = "how many movies does Leonardo Di Caprio have?"
    tqa = NaldeoTableQuestionning()
    reponse = tqa.do(table=table, question=question)
    print(reponse)


# prestation	unit	prix	entreprise
table1 = pd.read_excel('tabdata.xlsx', dtype={'prix': 'str'})
question = "quel prix pour décharge?"
question = "quel prestation coute 4?"
question = "combien pour un constat et une démolition?"
tqa = NaldeoTableQuestionning()
reponse = tqa.do(table=table1, question=question)
print(reponse)
# print(tqa.response)
