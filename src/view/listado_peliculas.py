from PyQt5 import QtCore, QtWidgets
from controllers.menu_controller import MenuController

class ListadoDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.controlador_menu = MenuController()  # Conectar con el controlador
        self.setupUi()
        self.cargar_peliculas()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(638, 744)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.listView = QtWidgets.QListView(self)
        self.listView.setAutoFillBackground(False)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)

        self.volverBtn = QtWidgets.QPushButton(self)
        self.volverBtn.setObjectName("volverBtn")
        self.volverBtn.setText("Volver")
        self.volverBtn.clicked.connect(self.close)
        self.verticalLayout_2.addWidget(self.volverBtn)

        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Listado de Películas"))
        self.label.setText(_translate("Dialog", "# Listado de películas"))

    def cargar_peliculas(self):
        """Carga las películas desde el modelo al ListView."""
        peliculas = self.controlador_menu.obtener_peliculas()
        modelo = QtCore.QStringListModel()

        # Convertir los resultados en una lista legible
        lista_peliculas = [f"{pelicula[1]} ({pelicula[2]})" for pelicula in peliculas]  # Título (Año)
        modelo.setStringList(lista_peliculas)

        self.listView.setModel(modelo)
