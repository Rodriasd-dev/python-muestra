import pandas as pd
import csv


with open('archive/Top_Anime_data.csv', newline='' ,encoding="utf-8") as archivo:
    lector_csv= csv.reader(archivo, delimiter=',', quotechar='"')
    animes_series = {

    }

    animes_peliculas= {

    }

    animes_series_genero={

    }
    series_promedio = {

    }

    animes_peliculas_genero={

    }
    peliculas_promedio = {
        
    }

    for row in lector_csv:
        if row[0] != 'Score':
            if row[8] == 'TV':
                animes_series[row[7]]= float(row[0])

                if row[18] not in animes_peliculas_genero:
                    animes_series_genero[row[18]] = float(row[0])
                else:
                    animes_series_genero[row[18]] = animes_series_genero.get(row[18], 0) + float(row[0])
            
            if row[8] == 'Movie':
                animes_peliculas[row[7]] = float(row[0])

                if row[18] not in animes_peliculas_genero:
                    animes_peliculas_genero[row[18]] = float(row[0])
                else:
                    animes_peliculas_genero[row[18]] = animes_peliculas_genero.get(row[18], 0) + float(row[0])

print(animes_peliculas_genero)  
print(animes_series_genero) 



# dfSeries = pd.DataFrame({"anime": animes_series.keys(), "score": animes_series.values()})
# dfPeliculas = pd.DataFrame({"anime": animes_peliculas.keys(),"score": animes_peliculas.values()})




# peliculas_mejor_rating = dfPeliculas[(dfPeliculas["score"] > 8.5)]
# series_mejor_rating = dfSeries[(dfSeries["score"] > 8.8)]




# smr = series_mejor_rating.to_dict(orient="records")
# pmr = peliculas_mejor_rating.to_dict(orient="records") 


# variable_pmr = "peliculas_mejor_rating = " + repr(pmr)
# variable_smr = "series_mejor_rating =" + repr(smr)

# with open("peliculas_mejor_rating.py", "w", encoding="utf-8") as f:
#      f.write(variable_pmr)


# with open("series_mejor_rating.py", "w", encoding="utf-8") as f:
#     f.write(variable_smr)