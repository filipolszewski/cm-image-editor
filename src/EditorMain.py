import sys
from PyQt4 import QtCore, QtGui
from editorGUI import Ui_Form


class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app = MyForm()
    my_app.show()
    sys.exit(app.exec_())
