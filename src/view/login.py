from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.login_controller import LoginController
from view.registrar import RegistrarDialog

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
        self.controlador_login.verificar_credenciales(correo, contrasena, self)

    def abrir_ventana_registro(self):
        self.ventana_registro = RegistrarDialog()
        self.ventana_registro.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = LoginDialog()
    dialog.exec_()
