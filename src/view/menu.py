from PyQt5 import QtCore, QtWidgets
from models.session import Sesion
from view.listado_peliculas import ListadoDialog
from view.n_recomendaciones import Rec_Dialog

class MenuDialog(QtWidgets.QDialog):
    def __init__(self, id_usuario):
        super().__init__()
        self.sesion_actual = Sesion()  # Obtener la sesión actual
        self.id_usuario = id_usuario
        self.setupUi()
        self.actualizar_mensaje_bienvenida()  # Actualizar el mensaje
        self.recomendacionesButton.clicked.connect(self.recomendar_peliculas)
        self.listadoButton.clicked.connect(self.listado_peliculas)
        self.logoutButton.clicked.connect(self.cerrar_sesion)
        

    def setupUi(self):
        self.setObjectName("Menu")
        self.resize(500, 625)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.welcomeLabel = QtWidgets.QLabel(self)
        self.welcomeLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.welcomeLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout.addWidget(self.welcomeLabel)

        spacerItem = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)

        self.recomendacionesButton = QtWidgets.QPushButton(self)
        self.recomendacionesButton.setObjectName("recomendacionesButton")
        self.verticalLayout.addWidget(self.recomendacionesButton)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        self.listadoButton = QtWidgets.QPushButton(self)
        self.listadoButton.setCheckable(False)
        self.listadoButton.setChecked(False)
        self.listadoButton.setObjectName("listadoButton")
        self.verticalLayout.addWidget(self.listadoButton)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.logoutButton = QtWidgets.QPushButton(self)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout.addWidget(self.logoutButton)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Menu", "Menú principal"))
        self.welcomeLabel.setText(_translate("Menu", "# Bienvenido"))  # Se actualiza después
        self.recomendacionesButton.setText(_translate("Menu", "Recomendaciones basadas en mis gustos"))
        self.listadoButton.setText(_translate("Menu", "Listado Películas"))
        self.logoutButton.setText(_translate("Menu", "Cerrar Sesión"))

    def actualizar_mensaje_bienvenida(self):
        """Actualiza dinámicamente el mensaje de bienvenida."""
        if self.sesion_actual.nombre:
            self.welcomeLabel.setText(f"# Bienvenido, {self.sesion_actual.nombre}")
        else:
            self.welcomeLabel.setText("# Bienvenido, Usuario")
            
    def cerrar_sesion(self):
        """Cierra la sesión actual y cierra la ventana."""
        self.sesion_actual.cerrar_sesion()
        self.close()
            
    def listado_peliculas(self):
        """Abre la ventana de listado de películas."""
        self.listado = ListadoDialog(self.id_usuario)
        self.listado.exec_()

    def recomendar_peliculas(self):
        self.recomendador_menu = Rec_Dialog(self.id_usuario)
        self.recomendador_menu.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = MenuDialog(0)
    menu.show()
    sys.exit(app.exec_())
