#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:51:09 2025

@author: eliibatista26
"""

import random
import sqlite3
from initialrating import show_random_movies  .
from menu import show_menu  


DATABASE_PATH = "peliculas.db"

# Función para verificar si el usuario ya hizo valoraciones iniciales
def has_user_rated_initially(id_usuario):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    query = "SELECT COUNT(*) FROM valoraciones WHERE id_usuario = ?"
    cursor.execute(query, (id_usuario,))
    count = cursor.fetchone()[0]
    
    conn.close()
    return count > 0

# Función para registrar las valoraciones en la base de datos
def save_ratings_to_db(id_usuario, valoraciones):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    query = "INSERT INTO valoraciones (id_usuario, id_pelicula, valoraciones) VALUES (?, ?, ?)"
    for id_pelicula, valoraciones in valoraciones.items():
        cursor.execute(query, (id_usuario, id_pelicula, valoraciones))
    
    conn.commit()
    conn.close()

# Función principal para gestionar el sistema de valoraciones
def main(id_usuario):
    # Verificar si el usuario ya hizo valoraciones iniciales
    if not has_user_rated_initially(id_usuario):
        print("No has realizado valoraciones iniciales. Vamos a empezar.")

        # Mostrar películas aleatorias para valorar
        ratings = show_random_movies()  # Esta función debería devolver un diccionario {movie_id: rating}

        # Guardar las valoraciones en la base de datos
        save_ratings_to_db(id_usuario, valoraciones)

        print("Gracias por completar tus valoraciones iniciales.")
    
    # Mostrar el menú principal
    show_menu(id_usuario)

if __name__ == "__main__":
    id_usuario = input("Introduce tu ID de usuario: ")
    main(id_usuario)