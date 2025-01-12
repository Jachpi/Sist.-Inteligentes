from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from controllers.pelicula_controller import PeliculaController
import requests

class SimilaresDialog(QtWidgets.QDialog):
    def __init__(self, id_pelicula, id_usuario, parent=None):
        super().__init__(parent)
        self.id_usuario = id_usuario
        self.id_pelicula = id_pelicula
        self.controlador_pelicula = PeliculaController()
        self.setupUi()
        self.cargar_datos_similares()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(900, 600)
        self.mainLayout = QtWidgets.QVBoxLayout(self)

        # --- Parte Superior: Información de la Película Seleccionada ---
        self.infoLayout = QtWidgets.QHBoxLayout()

        # Imagen de la película
        self.imagenLabel = QtWidgets.QLabel(self)
        self.imagenLabel.setFixedSize(200, 300)
        self.imagenLabel.setScaledContents(True)
        self.infoLayout.addWidget(self.imagenLabel)

        # Detalles de la película
        self.detalleLayout = QtWidgets.QVBoxLayout()

        self.tituloLabel = QtWidgets.QLabel(self)
        self.tituloLabel.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.tituloLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.detalleLayout.addWidget(self.tituloLabel)

        self.anioLabel = QtWidgets.QLabel(self)
        self.detalleLayout.addWidget(self.anioLabel)

        self.generoLabel = QtWidgets.QLabel(self)
        self.detalleLayout.addWidget(self.generoLabel)

        self.sinopsisText = QtWidgets.QTextEdit(self)
        self.sinopsisText.setReadOnly(True)
        self.sinopsisText.setFixedHeight(120)
        self.detalleLayout.addWidget(self.sinopsisText)

        self.infoLayout.addLayout(self.detalleLayout)
        self.mainLayout.addLayout(self.infoLayout)
        
        # --- Mostrar valoración actual ---
        self.valoracionLabel = QtWidgets.QLabel(self)
        self.valoracionLabel.setStyleSheet("font-size: 14px; color: blue;")
        self.valoracionLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.detalleLayout.addWidget(self.valoracionLabel)

        # --- Parte Inferior: Lista de Películas Similares ---
        self.labelSimilares = QtWidgets.QLabel("Películas Similares")
        self.labelSimilares.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSimilares.setStyleSheet("font-size: 16px; margin-top: 20px;")
        self.mainLayout.addWidget(self.labelSimilares)

        # Lista de películas similares
        self.listaSimilares = QtWidgets.QListWidget(self)
        self.listaSimilares.itemClicked.connect(self.abrir_pelicula_similar)
        self.mainLayout.addWidget(self.listaSimilares)
        
        # Botón para valorar la película
        self.valorarBtn = QtWidgets.QPushButton(self)
        self.valorarBtn.setText("Valorar esta película")
        self.valorarBtn.clicked.connect(self.valorar_pelicula)
        self.mainLayout.addWidget(self.valorarBtn)

        
        # Botón Volver
        self.volverBtn = QtWidgets.QPushButton(self)
        self.volverBtn.setText("Volver")
        self.volverBtn.clicked.connect(self.close)
        self.mainLayout.addWidget(self.volverBtn)

    def cargar_datos_similares(self):
        """Carga los datos de la pelicula seleccionada y sus similares."""
        pelicula = self.controlador_pelicula.obtener_info_pelicula(self.id_pelicula)
        similares = self.controlador_pelicula.obtener_similares(self.id_pelicula)

        if pelicula:
            titulo, anio, sinopsis, genero, imagen_url = pelicula[1], pelicula[2], pelicula[3], pelicula[11], pelicula[-1]

            # Mostrar título, año, género y sinopsis
            self.tituloLabel.setText(f"Título: {titulo}")
            self.anioLabel.setText(f"Año: {anio}")
            self.generoLabel.setText(f"Género: {genero}")
            self.sinopsisText.setText(sinopsis)

            # Cargar imagen desde URL
            self.cargar_imagen(imagen_url)
            
            # --- Obtener y mostrar la valoración actual del usuario ---
            valoracion = self.controlador_pelicula.obtener_valoracion(self.id_usuario, self.id_pelicula)
            if valoracion:
                self.valoracionLabel.setText(f"Tu valoración: {valoracion} estrellas ⭐")
            else:
                self.valoracionLabel.setText("Aún no has valorado esta película.")
            
        # Llenar la lista con películas similares
        self.listaSimilares.clear()
        for similar in similares:
            item = QtWidgets.QListWidgetItem(f"{similar[1]} ({similar[2]})")  # Título (Año)
            item.setData(QtCore.Qt.UserRole, similar[0])  # Guardar ID de la película
            self.listaSimilares.addItem(item)

    def abrir_pelicula_similar(self, item):
        """Cierra la ventana actual y abre la info de la pelicula seleccionada."""
        id_pelicula_similar = item.data(QtCore.Qt.UserRole)
        self.close()  # Cierra la ventana actual
        nueva_ventana = SimilaresDialog(id_pelicula_similar, self.id_usuario)
        nueva_ventana.exec_()
        
    def valorar_pelicula(self):
        """Permite al usuario valorar o actualizar la valoración de la película actual."""
        # Verificar si ya existe una valoración
        valoracion_existente = self.controlador_pelicula.obtener_valoracion(self.id_usuario, self.id_pelicula)

        if valoracion_existente:
            mensaje = f"Ya valoraste esta película con {valoracion_existente} estrellas. ¿Deseas actualizarla?"
        else:
            mensaje = "¿Qué nota le das a esta película? (1-5):"

        # Cuadro de diálogo para seleccionar la valoración
        valor, ok = QtWidgets.QInputDialog.getInt(
            self, "Valorar Película", mensaje,
            min=1, max=5
        )

        if ok:
            # Si ya existe, actualizar; si no, insertar
            if valoracion_existente:
                self.controlador_pelicula.actualizar_valoracion(self.id_usuario, self.id_pelicula, valor)
                QtWidgets.QMessageBox.information(self, "Valoración Actualizada", "¡Tu valoración ha sido actualizada!")
            else:
                self.controlador_pelicula.guardar_valoracion(self.id_usuario, self.id_pelicula, valor)
                QtWidgets.QMessageBox.information(self, "Valoración Guardada", "¡Gracias por valorar esta película!")

            
            
    def guardar_valoracion(self, id_usuario, id_pelicula, valoracion):
        """Guarda la valoración de la película en la base de datos."""
        self.modelo_pelicula.guardar_valoracion(id_usuario, id_pelicula, valoracion)


    def cargar_imagen(self, url):
        """Carga la imagen desde una URL en el QLabel usando requests."""
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                imagen = QtGui.QImage()
                imagen.loadFromData(response.content)
                pixmap = QtGui.QPixmap.fromImage(imagen)
                self.imagenLabel.setPixmap(pixmap.scaled(300, 400, QtCore.Qt.KeepAspectRatio))
            else:
                self.imagenLabel.setText("Error al descargar la imagen")
        except Exception as e:
            self.imagenLabel.setText(f"Error: {str(e)}")

    def mostrar_imagen(self, reply):
        """Muestra la imagen descargada en el QLabel."""
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        self.imagenLabel.setPixmap(pixmap)
