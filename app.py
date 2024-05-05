import pandas as pd


df = pd.read_csv("archive/anime.csv")


peliculas_mejor_rating = df[(df["rating"] > 8.5) & (df["type"] == "Movie")]


datos_json = peliculas_mejor_rating.to_dict(orient="records")


datos_py = "datos_json = " + repr(datos_json)


with open("peliculas_mejor_rating.py", "w") as f:
    f.write(datos_py)
