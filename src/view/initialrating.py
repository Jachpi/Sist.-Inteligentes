from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from controllers.pelicula_controller import PeliculaController
import requests
from view.menu import MenuDialog  # Importar MenuDialog

class Ui_Dialog(object):
    def __init__(self, id_usuario=None):
        self.id_usuario = id_usuario
        self.pelicula_controller = PeliculaController()
        self.pelicula = None
        self.contador_valoraciones = 0  # Contador de valoraciones
        self.manager = QtNetwork.QNetworkAccessManager()  # Maneja las descargas de imágenes

    def setupUi(self, Dialog):
        self.dialog = Dialog  # Guardar referencia
        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 561)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.imagenLabel = QtWidgets.QLabel(Dialog)
        self.imagenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenLabel.setObjectName("imagenLabel")
        self.imagenLabel.setText("Cargando imagen...")  # Texto por defecto
        self.imagenLabel.setMaximumWidth(200)  # Limitar el ancho máximo
        self.verticalLayout.addWidget(self.imagenLabel)
        
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("Título de la película")
        self.titleLabel.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.verticalLayout.addWidget(self.titleLabel)

        self.descripcionLabel = QtWidgets.QLabel(Dialog)
        self.descripcionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descripcionLabel.setObjectName("descripcionLabel")
        self.descripcionLabel.setText("Descripción de la película")
        self.descripcionLabel.setWordWrap(True)  # Permitir texto multilinea
        self.descripcionLabel.setMaximumWidth(400)  # Limitar el ancho máximo
        self.verticalLayout.addWidget(self.descripcionLabel)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)

        self.ratingBox = QtWidgets.QComboBox(Dialog)
        self.ratingBox.setObjectName("ratingBox")
        self.ratingBox.addItems(["1 Estrella", "2 Estrellas", "3 Estrellas", "4 Estrellas", "5 Estrellas"])
        self.verticalLayout.addWidget(self.ratingBox)

        self.boton_valorar = QtWidgets.QPushButton("Valorar", Dialog)
        self.boton_valorar.clicked.connect(self.calificar_pelicula)
        self.verticalLayout.addWidget(self.boton_valorar)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Valoración Inicial"))
        self.label.setText(_translate("Dialog", "# ¿Qué nota le darías a esta película?"))

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
        if reply.error() == QtNetwork.QNetworkReply.NoError:
            datos = reply.readAll()
            imagen = QtGui.QImage()
            imagen.loadFromData(datos)
            pixmap = QtGui.QPixmap.fromImage(imagen)
            self.imagenLabel.setPixmap(pixmap.scaled(300, 400, QtCore.Qt.KeepAspectRatio))
        else:
            self.imagenLabel.setText("Error al cargar la imagen")

    def mostrar_pelicula(self):
        """Muestra una película aleatoria con imagen descargada."""
        self.pelicula = self.pelicula_controller.obtener_pelicula_aleatoria()
        if self.pelicula:
            self.titleLabel.setText(self.pelicula[1])
            self.descripcionLabel.setText(self.pelicula[3])  # Sinopsis
            imagen_url = str(self.pelicula[26])  # Convertir explícitamente a str
            self.cargar_imagen(imagen_url)
        else:
            self.descripcionLabel.setText("No se pudo cargar la película.")


    def calificar_pelicula(self):
        """Guarda la valoración y muestra otra película si no ha valorado 10."""
        valoracion = self.ratingBox.currentIndex() + 1  # De 1 a 5
        self.pelicula_controller.guardar_valoracion(self.id_usuario, self.pelicula[0], valoracion)
        self.contador_valoraciones += 1

        if self.contador_valoraciones < 10:
            self.mostrar_pelicula()
        else:
            QtWidgets.QMessageBox.information(None, "Completado", "¡Has valorado 10 películas!")
            self.abrir_menu()
                
    def abrir_menu(self):
        """Abre el menú principal una vez completadas las valoraciones."""
        self.menu_dialog = QtWidgets.QDialog()
        self.menu_ui = MenuDialog(self.id_usuario)
        self.menu_ui.setupUi(self.menu_dialog)
        self.menu_dialog.exec_()
        if self.dialog:
            self.dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
