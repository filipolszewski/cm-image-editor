import sys

from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from editorGUI import Ui_EditorForm
from EditorController import EditorController

class MyForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_EditorForm()
        self.ui.setupUi(self)
        self._create_handlers(self.ui)
        self.current_filename = None
        self.image_controller = EditorController(self.ui.image_container.frameGeometry())

    def _create_handlers(self, ui):
        ui.load_image_btn.clicked.connect(self.load_btn_click)
        ui.save_image_btn.clicked.connect(self.save_btn_click)
        ui.apply_btn.clicked.connect(self.apply_btn_click)

    def load_btn_click(self):

        filters = "Images (*.png *.jpg)"
        filename, _ = QFileDialog.getOpenFileName(None, "Wybierz zdjęcie", "input/", filters)
        if filename is not None:
            self.current_filename = filename
            self.image_controller.set_working_image(self.current_filename)
            self.refresh_image_container()

    def save_btn_click(self):
        pass

    def apply_btn_click(self):
        self.image_controller.apply_changes()
        self.ui.brightness_slider.setValue(0)
        self.ui.contrast_slider.setValue(0)

    def refresh_image_container(self):
        current_image = self.image_controller.get_current_image()
        if current_image:
            pixmap = QPixmap.fromImage(ImageQt(current_image))
            self.ui.image_container.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyForm()
    my_app.show()
    sys.exit(app.exec_())
