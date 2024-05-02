import csv
import pandas as pd
from collections import Counter

with open('archive/muestra.csv', 'r', encoding='utf-8') as file:
    lector = csv.reader(file, delimiter=',', quotechar='"')
    data = []
    next(lector)  # Saltar la primera fila si contiene encabezados
    for row in lector:
        data.append(row)

animes = [row[5] for row in data]  # Obtener solo los nombres de los animes

def obtener_frecuencia_absoluta(lista_de_animes):
    frecuencia_absoluta = Counter(lista_de_animes)
    return frecuencia_absoluta

frecuencia_absoluta_animes = obtener_frecuencia_absoluta(animes)

print(frecuencia_absoluta_animes)
