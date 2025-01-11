#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:03:12 2024

@author: eliibatista26
"""
import os
import platform
import csv

import os
import platform
import csv

# Definir la ruta del archivo según el sistema operativo
if platform.system() == "Darwin":
    csv_path = os.path.join(os.path.expanduser("~"), "Downloads", "peliculas.csv")
else:
    csv_path = "../src/Dataset/peliculas.csv"

# Confirmar la ruta para depuración
print(f"Ruta del archivo: {csv_path}")

# Leer las películas desde un archivo CSV
def load_movies_from_csv(filename=csv_path):
    movies = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append({
                    "Title": row["title"],
                    "Year": int(row["year"]),
                    "Description": row["synopsis"]
                })
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encontró.")
    except KeyError as e:
        print(f"Error: Formato incorrecto en el archivo CSV. Falta la columna {e}.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return movies

# Función para mostrar las películas y pedir calificación
def rate_movies(movies):
    ratings = []
    print("\n=== Bienvenido al sistema de valoración de películas ===")
    for i, movie in enumerate(movies):
        print(f"\n{i + 1}. {movie['Title']} ({movie['Year']})")
        print(f"   {movie['Description']}")
        while True:
            try:
                rating = input(f"   ¿Qué calificación le das a '{movie['Title']}' (1-5)? (Presiona espacio para terminar): ")
                if rating.strip() == "":  # Si el usuario presiona Enter o un espacio
                    print("\n--- Has terminado la valoración ---")
                    return ratings
                rating = int(rating)
                if 1 <= rating <= 5:
                    ratings.append({"Title": movie["Title"], "Rating": rating})
                    break
                else:
                    print("   Por favor, ingresa un número entre 1 y 5.")
            except ValueError:
                print("   Entrada no válida. Ingresa un número entre 1 y 5 o presiona espacio para terminar.")
    return ratings

# Guardar las calificaciones en un archivo CSV
def save_ratings_to_csv(ratings, filename="ratings.csv"):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Rating"])
            for rating in ratings:
                writer.writerow([rating["Title"], rating["Rating"]])
        print(f"\nLas calificaciones se han guardado en el archivo '{filename}'.")
    except Exception as e:
        print(f"Error al guardar las calificaciones: {e}")

# Programa principal
def main():
    movies = load_movies_from_csv()
    if not movies:
        print("No se pudieron cargar películas. Verifica el archivo CSV.")
        return

    ratings = rate_movies(movies)
    print("\n=== Resumen de tus calificaciones ===")
    for rating in ratings:
        print(f"   {rating['Title']}: {rating['Rating']} estrellas")

    save_ratings_to_csv(ratings)

if __name__ == "__main__":
    main()
