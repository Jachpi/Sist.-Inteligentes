from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QDialog
from controllers.registro_controller import RegistroController

class RegistrarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.controlador = RegistroController()

        # Conectar el botón de registro
        self.pushButton.clicked.connect(self.registrar_usuario)

    def setupUi(self):
        self.setObjectName("RegistrarDialog")
        self.resize(457, 499)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        
        self.emailInput = QtWidgets.QLineEdit(self)
        self.emailInput.setAlignment(QtCore.Qt.AlignCenter)
        self.emailInput.setObjectName("emailInput")
        self.verticalLayout.addWidget(self.emailInput)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        
        self.usuarioInput = QtWidgets.QLineEdit(self)
        self.usuarioInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usuarioInput.setObjectName("usuarioInput")
        self.verticalLayout.addWidget(self.usuarioInput)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        
        self.passInput = QtWidgets.QLineEdit(self)
        self.passInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passInput.setObjectName("passInput")
        self.verticalLayout.addWidget(self.passInput)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("RegistrarDialog", "Registro"))
        self.emailInput.setPlaceholderText(_translate("RegistrarDialog", "Correo electrónico"))
        self.usuarioInput.setPlaceholderText(_translate("RegistrarDialog", "Usuario"))
        self.passInput.setPlaceholderText(_translate("RegistrarDialog", "Contraseña"))
        self.pushButton.setText(_translate("RegistrarDialog", "Registrarse"))
        
    def registrar_usuario(self):
        nombre = self.usuarioInput.text()
        correo = self.emailInput.text()
        contrasena = self.passInput.text()

        # Llama al controlador para registrar el usuario
        if self.controlador.registrar_usuario(nombre, correo, contrasena, self):
            self.close()
