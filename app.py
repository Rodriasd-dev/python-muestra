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

print(filter_fi)