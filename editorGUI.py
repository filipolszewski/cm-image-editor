# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorForm(object):
    def setupUi(self, EditorForm):
        EditorForm.setObjectName("EditorForm")
        EditorForm.resize(750, 400)
        EditorForm.setMinimumSize(QtCore.QSize(750, 400))
        EditorForm.setMaximumSize(QtCore.QSize(750, 400))
        self.image_container = QtWidgets.QLabel(EditorForm)
        self.image_container.setGeometry(QtCore.QRect(180, 40, 560, 315))
        self.image_container.setMinimumSize(QtCore.QSize(560, 315))
        self.image_container.setMaximumSize(QtCore.QSize(560, 315))
        self.image_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_container.setLineWidth(10)
        self.image_container.setText("")
        self.image_container.setObjectName("image_container")
        self.load_image_btn = QtWidgets.QPushButton(EditorForm)
        self.load_image_btn.setGeometry(QtCore.QRect(20, 40, 121, 27))
        self.load_image_btn.setObjectName("load_image_btn")
        self.save_image_btn = QtWidgets.QPushButton(EditorForm)
        self.save_image_btn.setGeometry(QtCore.QRect(20, 80, 121, 27))
        self.save_image_btn.setObjectName("save_image_btn")
        self.monolith_cbox = QtWidgets.QCheckBox(EditorForm)
        self.monolith_cbox.setGeometry(QtCore.QRect(20, 140, 121, 22))
        self.monolith_cbox.setObjectName("monolith_cbox")
        self.brightness_slider = QtWidgets.QSlider(EditorForm)
        self.brightness_slider.setGeometry(QtCore.QRect(20, 200, 121, 29))
        self.brightness_slider.setMinimum(-123)
        self.brightness_slider.setMaximum(122)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightness_slider")
        self.contrast_slider = QtWidgets.QSlider(EditorForm)
        self.contrast_slider.setGeometry(QtCore.QRect(20, 260, 121, 29))
        self.contrast_slider.setMinimum(-123)
        self.contrast_slider.setMaximum(122)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.label = QtWidgets.QLabel(EditorForm)
        self.label.setGeometry(QtCore.QRect(50, 180, 68, 17))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditorForm)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 68, 17))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.apply_btn = QtWidgets.QPushButton(EditorForm)
        self.apply_btn.setGeometry(QtCore.QRect(20, 320, 121, 27))
        self.apply_btn.setObjectName("apply_btn")
        self.label_3 = QtWidgets.QLabel(EditorForm)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(EditorForm)
        QtCore.QMetaObject.connectSlotsByName(EditorForm)

    def retranslateUi(self, EditorForm):
        _translate = QtCore.QCoreApplication.translate
        EditorForm.setWindowTitle(_translate("EditorForm", "CM Image Editor"))
        self.load_image_btn.setText(_translate("EditorForm", "Wczytaj Zdjęcie"))
        self.save_image_btn.setText(_translate("EditorForm", "Zapisz Zdjęcie"))
        self.monolith_cbox.setText(_translate("EditorForm", "Dodaj Monolit"))
        self.label.setText(_translate("EditorForm", "Jasność"))
        self.label_2.setText(_translate("EditorForm", "Kontrast"))
        self.apply_btn.setText(_translate("EditorForm", "Zastosuj"))
        self.label_3.setText(_translate("EditorForm", "Podgląd"))

