import csv
import pandas as pd

with open('archive/muestra.csv', 'r', encoding='utf-8') as file:
    lector = csv.reader(file, delimiter=',', quotechar='"')
    data = []
    for row in lector:
        data.append(row)
    

a = pd.Series(data)
for i in range(len(data)):
    print(data[i][5])