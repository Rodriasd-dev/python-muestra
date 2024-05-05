import pandas as pd
import csv


with open('archive/Top_Anime_data.csv', newline='' ,encoding="utf-8") as archivo:
    lector_csv= csv.reader(archivo, delimiter=',', quotechar='"')
    animes_series = {

    }

    animes_peliculas= {

    }

    for row in lector_csv:
        if row[0] != 'Score':
            if row[8] == 'TV':
                animes_series[row[7]]= float(row[0])
            
            if row[8] == 'Movie':
                animes_peliculas[row[7]] = float(row[0])




dfSeries = pd.DataFrame({"anime": animes_series.keys(), "score": animes_series.values()})
dfPeliculas = pd.DataFrame({"anime": animes_peliculas.keys(),"score": animes_peliculas.values()})




peliculas_mejor_rating = dfPeliculas[(dfPeliculas["score"] > 8.5)]
series_mejor_rating = dfSeries[(dfSeries["score"] > 8.8)]




smr = series_mejor_rating.to_dict(orient="records")
pmr = peliculas_mejor_rating.to_dict(orient="records") 


variable_pmr = "peliculas_mejor_rating = " + repr(pmr)
variable_smr = "series_mejor_rating =" + repr(smr)

with open("peliculas_mejor_rating.py", "w", encoding="utf-8") as f:
     f.write(variable_pmr)


with open("series_mejor_rating.py", "w", encoding="utf-8") as f:
    f.write(variable_smr)