import csv
import pandas as pd
from collections import Counter

with open('archive/muestra.csv', 'r', encoding='utf-8') as file:
    lector = csv.reader(file, delimiter=',', quotechar='"')
    data = []
    for row in lector:
        data.append(row)
    

fr=[]
animes=[]

for i in range(len(data)):
    animes.append(data[i][5])
    # if data[i][5] not in animes:
    #     animes.append(data[i][5])

def obtener_fi(lista_de_datos):
    lista_de_datos.sort()
    fi = {}
    for i in lista_de_datos:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    return fi

tabla = obtener_fi(animes)

print(tabla)