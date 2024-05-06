import pandas as pd
import csv


with open('archive/Top_Anime_data.csv', newline='' ,encoding="utf-8") as archivo:
    lector_csv= csv.reader(archivo, delimiter=',', quotechar='"')
    
    animes = {}
    animes_series = {

    }

    animes_peliculas= {

    }

    animes_series_genero={

    }
    series_contador = {

    }

    animes_peliculas_genero={

    }
    peliculas_contador = {

    }

    series_peliculas_popularity={
        "series": 0,
        "peliculas": 0
    }

    estudios_popularidad = {
        
    }

    estudio_contador = {

    }        

    for row in lector_csv:
        if row[0] != 'Score':
            animes[row[7]] = float(row[2])
            if row[8] == 'TV':
                animes_series[row[7]]= float(row[0])

                if row[18] not in animes_peliculas_genero:
                    animes_series_genero[row[18]] = float(row[0])
                    series_contador[row[18]] = 1
                else:
                    animes_series_genero[row[18]] = animes_series_genero.get(row[18], 0) + float(row[0])
                    series_contador[row[18]] = series_contador.get(row[18], 0) + 1

                series_peliculas_popularity["series"] = series_peliculas_popularity["series"] + float(row[1])
            
            if row[8] == 'Movie':
                animes_peliculas[row[7]] = float(row[0])

                if row[18] not in animes_peliculas_genero:
                    animes_peliculas_genero[row[18]] = float(row[0])
                    peliculas_contador[row[18]] = 1
                else:
                    peliculas_contador[row[18]] = peliculas_contador.get(row[18], 0) + 1
                    animes_peliculas_genero[row[18]] = animes_peliculas_genero.get(row[18], 0) + float(row[0])
                
                series_peliculas_popularity["peliculas"] = series_peliculas_popularity["peliculas"] + float(row[1])
                estudios_popularidad[row[16]] = estudios_popularidad.get(row[16], 0) + float(row[1])
                estudio_contador[row[16]] = estudio_contador.get(row[16], 0) + 1


print(animes)

df_animes = pd.DataFrame({"anime": animes.keys(), "rank": animes.values()})
df_animes = df_animes[(df_animes["rank"] < 11)]
df_anime_dic = df_animes.to_dict(orient="records")

animes_ranking = "const animes_populares= " + repr(df_anime_dic)


with open("animes_ranking.js", "w", encoding="utf-8") as f:
    f.write(animes_ranking)

# estudio_promedio_popularidad = {}
# for clave, valor in estudios_popularidad.items():
#     estudio_promedio_popularidad[clave] = estudios_popularidad[clave] / estudio_contador[clave]

# df_estudio_popularidad = pd.DataFrame({"estudios": estudios_popularidad.keys(), "popularidad": estudios_popularidad.values()})

# df_estudio_popularidad = df_estudio_popularidad.sort_values(by='popularidad', ascending=False)
# dic_estudio_popularidad = df_estudio_popularidad.to_dict(orient="records")


# promedio_peliculas = {}
# promedio_series = {}

# for clave,valor in animes_series_genero.items():
#     promedio_series[clave] = valor / series_contador[clave]

# for clave, valor in animes_peliculas_genero.items():
#     promedio_peliculas[clave] = valor / peliculas_contador[clave]



# df_promedio_peliculas = pd.DataFrame({"genero": promedio_peliculas.keys(), "score": promedio_peliculas.values()})
# df_promedio_series = pd.DataFrame({"genero": promedio_series.keys(), "score": promedio_series.values()})
# dfSeries = pd.DataFrame({"anime": animes_series.keys(), "score": animes_series.values()})
# dfPeliculas = pd.DataFrame({"anime": animes_peliculas.keys(),"score": animes_peliculas.values()})


# peliculas_mejor_promedio = df_promedio_peliculas[(df_promedio_peliculas["score"] > 8.5)]
# series_mejor_promedio = df_promedio_series[(df_promedio_series["score"] > 8.5)]
# peliculas_mejor_rating = dfPeliculas[(dfPeliculas["score"] > 8.5)]
# series_mejor_rating = dfSeries[(dfSeries["score"] > 8.8)]



# pmp = peliculas_mejor_promedio.to_dict(orient="records")
# smp = series_mejor_promedio.to_dict(orient="records")
# smr = series_mejor_rating.to_dict(orient="records")
# pmr = peliculas_mejor_rating.to_dict(orient="records") 

# variable_pmp = "const genero_peliculas_promedio =" + repr(pmp)
# variable_smp = "const genero_series_promedio =" + repr(smp)
# variable_pmr = "peliculas_mejor_rating = " + repr(pmr)
# variable_smr = "series_mejor_rating =" + repr(smr)

# variable_psp = "const peliculas_series_popularidad = " + repr(series_peliculas_popularity)


# with open("peliculas_series_popularidad.js", "w", encoding="utf-8") as f:
#     f.write(variable_psp)

# with open("peliculas_mejor_promedio.js", "w", encoding="utf-8") as f:
#     f.write(variable_pmp)

# with open("series_mejor_promedio.js", "w", encoding="utf-8") as f:
#     f.write(variable_smp)

# with open("peliculas_mejor_rating.py", "w", encoding="utf-8") as f:
#      f.write(variable_pmr)


# with open("series_mejor_rating.py", "w", encoding="utf-8") as f:
#     f.write(variable_smr)