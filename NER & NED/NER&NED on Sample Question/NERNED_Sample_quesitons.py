from pororo import Pororo
import pandas as pd
ner = Pororo(task="ner", lang="ko")

df = pd.read_csv("newQuestions.csv")
df_questions = df['A']

entity_list = []
for question in df_questions:
    entities = ner(question)
    entity_list.append(entities)

print(entity_list)
