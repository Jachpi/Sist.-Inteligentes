from controllers.pelicula_controller import PeliculaController
from controllers.menu_controller import MenuController
from view.n_similares import SimilaresDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Rec_Dialog(QtWidgets.QDialog):
    def __init__(self, id_usuario):
        super().__init__()
        self.id_usuario = id_usuario
        self.controlador_menu = MenuController()
        self.pelicula_controller = PeliculaController()
        self.setupUi()
        self.cargar_peliculas()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(638, 744)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)  # Cambiado a Vertical para incluir el buscador

        # --- ListView ---
        self.listView = QtWidgets.QListView(self)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.doubleClicked.connect(self.mostrar_similares)
        self.verticalLayout.addWidget(self.listView)

    def cargar_peliculas(self):
        """Carga todas las películas en el ListView."""
        self.peliculas = self.pelicula_controller.obtener_similares_a_usuario(self.id_usuario)
        self.modelo = QtGui.QStandardItemModel()

        for pelicula in self.peliculas:
            item = QtGui.QStandardItem(f"{pelicula[1]} ({pelicula[2]})")  # Título (Año)
            item.setData(pelicula[0])  # Guardar el ID de la película
            self.modelo.appendRow(item)

        self.listView.setModel(self.modelo)

    def mostrar_similares(self, index):
        """Abre el diálogo de películas similares al hacer doble clic."""
        id_pelicula = self.modelo.itemFromIndex(index).data()
        self.similares_dialog = SimilaresDialog(id_pelicula, self.id_usuario)
        self.similares_dialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Rec_Dialog(0)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
