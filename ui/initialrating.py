# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initialrating.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
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
        self.verticalLayout.addWidget(self.imagenLabel)
        self.descripcionLabel = QtWidgets.QLabel(Dialog)
        self.descripcionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descripcionLabel.setObjectName("descripcionLabel")
        self.verticalLayout.addWidget(self.descripcionLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.ratingBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(234)
        sizePolicy.setHeightForWidth(self.ratingBox.sizePolicy().hasHeightForWidth())
        self.ratingBox.setSizePolicy(sizePolicy)
        self.ratingBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.ratingBox.setObjectName("ratingBox")
        self.ratingBox.addItem("")
        self.ratingBox.addItem("")
        self.ratingBox.addItem("")
        self.ratingBox.addItem("")
        self.ratingBox.addItem("")
        self.verticalLayout.addWidget(self.ratingBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "# ¿Que nota le darías a esta película?"))
        self.imagenLabel.setText(_translate("Dialog", "Imagen"))
        self.descripcionLabel.setText(_translate("Dialog", "Descripción película"))
        self.ratingBox.setItemText(0, _translate("Dialog", "1 Estrella"))
        self.ratingBox.setItemText(1, _translate("Dialog", "2 Estrellas"))
        self.ratingBox.setItemText(2, _translate("Dialog", "3 Estrellas"))
        self.ratingBox.setItemText(3, _translate("Dialog", "4 Estrellas"))
        self.ratingBox.setItemText(4, _translate("Dialog", "5 Estrellas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
