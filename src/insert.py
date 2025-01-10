import requests
from lxml import html
import sqlite3  # O el conector adecuado según tu base de datos

# Conectar a la base de datos
conn = sqlite3.connect('peliculas.db')  # Cambia esto si usas otro tipo de base de datos
cursor = conn.cursor()

# Obtener todas las películas
cursor.execute("SELECT id, link FROM peliculas")
peliculas = cursor.fetchall()

# Recorrer las películas y obtener la imagen
for pelicula in peliculas:
    id_pelicula, link = pelicula
    if link:  # Asegúrate de que haya un enlace
        try:
            # Hacer una solicitud HTTP al enlace
            response = requests.get(link)
            tree = html.fromstring(response.content)
            print(response)
            # Extraer la URL de la imagen usando el XPath
            image_url = tree.xpath('/html/body/div[3]/main/div/div[1]/div[2]/div[1]/div[1]/media-scorecard/rt-img[1]/@src')
            
            if image_url:
                image_url = image_url[0]  # Si hay una imagen, tomar la primera (debe ser solo una)
                # Actualizar la base de datos con la URL de la imagen
                cursor.execute("UPDATE peliculas SET img = ? WHERE id = ?", (image_url, id_pelicula))
                conn.commit()
                print(f"Imagen actualizada para la película {id_pelicula} en {link}")
            else:
                print(f"No se encontró imagen para la película {id_pelicula} en {link}")
        except Exception as e:
            print(f"Error al procesar la película {id_pelicula} en {link}: {e}")

# Cerrar la conexión a la base de datos
conn.close()
