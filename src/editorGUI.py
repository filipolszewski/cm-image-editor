# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_EditorForm(object):
    def setupUi(self, EditorForm):
        EditorForm.setObjectName(_fromUtf8("EditorForm"))
        EditorForm.resize(750, 400)
        EditorForm.setMinimumSize(QtCore.QSize(750, 400))
        EditorForm.setMaximumSize(QtCore.QSize(750, 400))
        self.image_container = QtGui.QLabel(EditorForm)
        self.image_container.setGeometry(QtCore.QRect(180, 40, 560, 315))
        self.image_container.setMinimumSize(QtCore.QSize(560, 315))
        self.image_container.setMaximumSize(QtCore.QSize(560, 315))
        self.image_container.setFrameShape(QtGui.QFrame.StyledPanel)
        self.image_container.setLineWidth(10)
        self.image_container.setText(_fromUtf8(""))
        self.image_container.setObjectName(_fromUtf8("image_container"))
        self.load_image_btn = QtGui.QPushButton(EditorForm)
        self.load_image_btn.setGeometry(QtCore.QRect(20, 40, 121, 27))
        self.load_image_btn.setObjectName(_fromUtf8("load_image_btn"))
        self.save_image_btn = QtGui.QPushButton(EditorForm)
        self.save_image_btn.setGeometry(QtCore.QRect(20, 80, 121, 27))
        self.save_image_btn.setObjectName(_fromUtf8("save_image_btn"))
        self.monolith_cbox = QtGui.QCheckBox(EditorForm)
        self.monolith_cbox.setGeometry(QtCore.QRect(20, 140, 121, 22))
        self.monolith_cbox.setObjectName(_fromUtf8("monolith_cbox"))
        self.brightness_slider = QtGui.QSlider(EditorForm)
        self.brightness_slider.setGeometry(QtCore.QRect(20, 200, 121, 29))
        self.brightness_slider.setMinimum(-123)
        self.brightness_slider.setMaximum(122)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName(_fromUtf8("brightness_slider"))
        self.contrast_slider = QtGui.QSlider(EditorForm)
        self.contrast_slider.setGeometry(QtCore.QRect(20, 260, 121, 29))
        self.contrast_slider.setMinimum(-123)
        self.contrast_slider.setMaximum(122)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName(_fromUtf8("contrast_slider"))
        self.label = QtGui.QLabel(EditorForm)
        self.label.setGeometry(QtCore.QRect(50, 180, 68, 17))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(EditorForm)
        self.label_2.setGeometry(QtCore.QRect(50, 240, 68, 17))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.apply_btn = QtGui.QPushButton(EditorForm)
        self.apply_btn.setGeometry(QtCore.QRect(20, 320, 121, 27))
        self.apply_btn.setObjectName(_fromUtf8("apply_btn"))
        self.label_3 = QtGui.QLabel(EditorForm)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(EditorForm)
        QtCore.QMetaObject.connectSlotsByName(EditorForm)

    def retranslateUi(self, EditorForm):
        EditorForm.setWindowTitle(_translate("EditorForm", "CM Image Editor", None))
        self.load_image_btn.setText(_translate("EditorForm", "Wczytaj Zdjęcie", None))
        self.save_image_btn.setText(_translate("EditorForm", "Zapisz Zdjęcie", None))
        self.monolith_cbox.setText(_translate("EditorForm", "Dodaj Monolit", None))
        self.label.setText(_translate("EditorForm", "Jasność", None))
        self.label_2.setText(_translate("EditorForm", "Kontrast", None))
        self.apply_btn.setText(_translate("EditorForm", "Zastosuj", None))
        self.label_3.setText(_translate("EditorForm", "Podgląd", None))
