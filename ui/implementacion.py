import sys
import sqlite3
from PyQt5 import QtWidgets
from initialrating import Ui_Dialog as InitialRatingDialog
from menu import Ui_Menu as MenuDialog
import random

DB_PATH = "peliculas.db"

def check_database():
    """Verifica que la tabla valoraciones exista en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='valoraciones'
    """)
    if cursor.fetchone() is None:
        raise Exception("La tabla 'valoraciones' no existe en la base de datos. Por favor, crea la tabla antes de ejecutar el programa.")
    conn.close()

def check_initial_ratings():
    """Verifica si hay valoraciones iniciales en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM valoraciones")
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

class InitialRating(QtWidgets.QDialog):
    def __init__(self, peliculas):
        super().__init__()
        self.ui = InitialRatingDialog()
        self.ui.setupUi(self)
        self.peliculas = peliculas
        self.current_index = 0
        self.setup_signals()
        self.show_movie()

    def setup_signals(self):
        self.ui.ratingBox.currentIndexChanged.connect(self.save_rating)

    def save_rating(self, index):
        if index == 0:
            return  # No guardar si no se selecciona un valor
        valoracion = index
        pelicula = self.peliculas[self.current_index]
        self.store_rating(pelicula, valoracion)
        self.current_index += 1
        if self.current_index < len(self.peliculas):
            self.show_movie()
        else:
            self.accept()  # Cierra el diálogo cuando se terminan las películas

    def store_rating(self, pelicula, valoracion):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO valoraciones (pelicula, valoracion) VALUES (?, ?)", (pelicula, valoracion))
        conn.commit()
        conn.close()

    def show_movie(self):
        pelicula = self.peliculas[self.current_index]
        self.ui.imagenLabel.setText("Imagen de la película")  # Aquí podrías cargar imágenes reales
        self.ui.descripcionLabel.setText(f"Descripción de {pelicula}")

class Menu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = MenuDialog()
        self.ui.setupUi(self)

def main():
    try:
        check_database()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    app = QtWidgets.QApplication(sys.argv)

    if not check_initial_ratings():
        peliculas = ["Pelicula 1", "Pelicula 2", "Pelicula 3", "Pelicula 4", "Pelicula 5"]
        random.shuffle(peliculas)  # Muestra películas en orden aleatorio
        initial_rating_dialog = InitialRating(peliculas)
        if initial_rating_dialog.exec_() == QtWidgets.QDialog.Accepted:
            menu = Menu()
            menu.exec_()
    else:
        menu = Menu()
        menu.exec_()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
