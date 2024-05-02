import csv
import pandas as pd
from collections import Counter

with open('archive/muestra.csv', 'r', encoding='utf-8') as file:
    lector = csv.reader(file, delimiter=',', quotechar='"')
    data = []
    next(lector)
    for row in lector:
        data.append(row)

animes = [row[5] for row in data]  

def obtener_frecuencia_absoluta(lista_de_animes):
    frecuencia_absoluta = Counter(lista_de_animes)
    return frecuencia_absoluta

fi = obtener_frecuencia_absoluta(animes)

filter_fi = {}
for clave,valor in fi.items():
    if valor > 8:
        filter_fi[clave] = valor

df = pd.DataFrame({"animes": filter_fi.keys(), "fi": filter_fi.values()})

scores_por_anime = {}


for row in data:
    nombre_anime = row[5]
    score = float(row[8]) 
    if nombre_anime in scores_por_anime:
        scores_por_anime[nombre_anime].append(score)
    else:
        scores_por_anime[nombre_anime] = [score]


media_scores_por_anime = {}
for nombre_anime, scores in scores_por_anime.items():
    media = sum(scores) / len(scores)
    media_scores_por_anime[nombre_anime] = media

for clave,valor in media_scores_por_anime.items():
    if valor >= 9:
        print(clave ,':', valor)