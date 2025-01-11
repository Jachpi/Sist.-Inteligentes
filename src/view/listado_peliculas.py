from PyQt5 import QtCore, QtWidgets, QtGui
from controllers.menu_controller import MenuController
from view.n_similares import SimilaresDialog

class ListadoDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.controlador_menu = MenuController()
        self.setupUi()
        self.cargar_peliculas()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(638, 744)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)  # Cambiado a Vertical para incluir el buscador

        # --- Buscador ---
        self.buscadorInput = QtWidgets.QLineEdit(self)
        self.buscadorInput.setPlaceholderText("Buscar película...")
        self.buscadorInput.textChanged.connect(self.filtrar_peliculas)  # Conectar el buscador
        self.verticalLayout.addWidget(self.buscadorInput)

        # --- ListView ---
        self.listView = QtWidgets.QListView(self)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.doubleClicked.connect(self.mostrar_similares)
        self.verticalLayout.addWidget(self.listView)

    def cargar_peliculas(self):
        """Carga todas las películas en el ListView."""
        self.peliculas = self.controlador_menu.obtener_peliculas()
        self.modelo = QtGui.QStandardItemModel()

        for pelicula in self.peliculas:
            item = QtGui.QStandardItem(f"{pelicula[1]} ({pelicula[2]})")  # Título (Año)
            item.setData(pelicula[0])  # Guardar el ID de la película
            self.modelo.appendRow(item)

        self.listView.setModel(self.modelo)

    def filtrar_peliculas(self, texto):
        """Filtra las películas en el ListView según el texto ingresado."""
        texto = texto.lower()
        self.modelo.clear()  # Limpiar la lista antes de aplicar el filtro

        for pelicula in self.peliculas:
            titulo = pelicula[1].lower()
            anio = str(pelicula[2])

            # Si el texto coincide con el título o el año, mostrarla
            if texto in titulo or texto in anio:
                item = QtGui.QStandardItem(f"{pelicula[1]} ({pelicula[2]})")
                item.setData(pelicula[0])
                self.modelo.appendRow(item)

    def mostrar_similares(self, index):
        """Abre el diálogo de películas similares al hacer doble clic."""
        id_pelicula = self.modelo.itemFromIndex(index).data()
        self.similares_dialog = SimilaresDialog(id_pelicula)
        self.similares_dialog.exec_()
