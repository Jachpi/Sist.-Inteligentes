from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controllers.login_controller import LoginController
from view.initialrating import Ui_Dialog
from view.registrar import RegistrarDialog
from view.menu import MenuDialog 

class LoginDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controlador_login = LoginController()  # Controlador de Login

        # Conectar botones
        self.login.clicked.connect(self.verificar_credenciales)
        self.registrar.clicked.connect(self.abrir_ventana_registro)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(548, 478)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        # Spacer superior
        spacer_top = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_top)

        self.userInput = QtWidgets.QLineEdit(Dialog)
        self.userInput.setAlignment(QtCore.Qt.AlignCenter)
        self.userInput.setPlaceholderText("Correo electrónico")
        self.verticalLayout.addWidget(self.userInput)

        # Spacer entre campos
        spacer_middle1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacer_middle1)

        self.passInput = QtWidgets.QLineEdit(Dialog)
        self.passInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passInput.setPlaceholderText("Contraseña")
        self.passInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.passInput)

        # Spacer entre campos
        spacer_middle2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacer_middle2)

        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setText("Iniciar Sesión")
        self.verticalLayout.addWidget(self.login)

        # Spacer entre botones
        spacer_middle3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacer_middle3)

        self.registrar = QtWidgets.QPushButton(Dialog)
        self.registrar.setText("Registro")
        self.verticalLayout.addWidget(self.registrar)

        # Spacer inferior
        spacer_bottom = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_bottom)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        Dialog.setLayout(self.verticalLayout_2)

    def verificar_credenciales(self):
        correo = self.userInput.text()
        contrasena = self.passInput.text()

        usuario_id = self.controlador_login.verificar_credenciales(correo, contrasena)

        if usuario_id:
            if self.controlador_login.verificar_valoraciones_usuario(usuario_id) < 10:
                self.abrir_ventana_valoracion_inicial(usuario_id)
            else:
                self.abrir_menu(usuario_id)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

    def abrir_ventana_valoracion_inicial(self, usuario_id):
        print(f"[DEBUG] Abriendo ventana de valoración para usuario ID: {usuario_id}")
        dialog = QtWidgets.QDialog()
        self.ventana_valoracion = Ui_Dialog(usuario_id)
        self.ventana_valoracion.setupUi(dialog)
        
        # Asegurarse de que se llama a mostrar_pelicula
        self.ventana_valoracion.mostrar_pelicula()
        
        dialog.exec_()
        
    def abrir_menu(self, id_usuario):
        """Cierra el login y abre el menú principal."""
        self.close()  # Cerramos la ventana de login
        
        self.menu_dialog = MenuDialog(id_usuario)
        self.menu_dialog.exec_()  # Ahora se abre el menú principal







    def abrir_ventana_registro(self):
        self.ventana_registro = RegistrarDialog()
        self.ventana_registro.exec_()
        
    def recomendar_pelicula(self):
        """Abre la ventana de initialrating.py para calificar una película aleatoria si el usuario tiene menos de 10 valoraciones."""
        usuario_id = 1  # Debes obtener el ID del usuario actual (esto puede venir del login)
        if self.controlador_pelicula.verificar_valoraciones_usuario(usuario_id) < 10:
            self.ventana_rating = Ui_Dialog(usuario_id)
            self.ventana_rating.exec_()
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = LoginDialog()
    dialog.exec_()
