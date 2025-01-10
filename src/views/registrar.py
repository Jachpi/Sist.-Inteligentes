from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox

class RegistrarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar el botón de registro
        self.pushButton.clicked.connect(self.registrar_usuario)

    def setupUi(self, Dialog=None):
        if Dialog is None:
            Dialog = self

        Dialog.setObjectName("Dialog")
        Dialog.resize(457, 499)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.usuarioInput = QtWidgets.QLineEdit(Dialog)
        self.usuarioInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usuarioInput.setObjectName("usuarioInput")
        self.verticalLayout.addWidget(self.usuarioInput)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.passInput = QtWidgets.QLineEdit(Dialog)
        self.passInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passInput.setObjectName("passInput")
        self.verticalLayout.addWidget(self.passInput)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registro"))
        self.usuarioInput.setPlaceholderText(_translate("Dialog", "Usuario"))
        self.passInput.setPlaceholderText(_translate("Dialog", "Contraseña"))
        self.pushButton.setText(_translate("Dialog", "Registrarse"))

    def registrar_usuario(self):
        usuario = self.usuarioInput.text()
        contraseña = self.passInput.text()

        if usuario and contraseña:
            QMessageBox.information(self, "Registro Exitoso", f"Usuario '{usuario}' registrado correctamente.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Debes completar ambos campos.")
