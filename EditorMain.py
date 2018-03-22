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
        self.current_filepath = "/home/filip/come_meditate_channel/" \
                                "cm-image-editor/"
        self.image_controller = EditorController(self.ui.image_container.frameGeometry())
        # these 2 lines just for testing!
        # self.image_controller.set_working_image("input/DSC_0429.JPG")
        # self.refresh_image_container()

    def _create_handlers(self, ui):
        ui.load_image_btn.clicked.connect(self.load_btn_click)
        ui.save_image_btn.clicked.connect(self.save_btn_click)
        ui.apply_btn.clicked.connect(self.apply_btn_click)
        ui.brightness_slider.sliderReleased.connect(self.b_or_c_changed)
        ui.contrast_slider.sliderReleased.connect(self.b_or_c_changed)
        ui.monolith_cbox.stateChanged.connect(self.monolith_clicked)

    def load_btn_click(self):
        filters = "Images (*.png *.jpg)"
        filename, _ = QFileDialog.getOpenFileName(None, "Wybierz zdjęcie", self.current_filepath, filters)
        if filename:
            self.clear()
            self.current_filepath = "/".join(filename.split('/')[:-1])
            self.image_controller.set_working_image(filename)
            self.refresh_image_container()

    def save_btn_click(self):
        self.image_controller.save_final_img()

    def apply_btn_click(self):
        self.image_controller.apply_changes()
        self.ui.brightness_slider.setValue(0)
        self.ui.contrast_slider.setValue(0)

    def b_or_c_changed(self):
        self.image_controller.change_brightness_contrast(self.ui.brightness_slider.value(),
                                                         self.ui.contrast_slider.value())
        self.refresh_image_container()

    def monolith_clicked(self):
        self.image_controller.monolith_change(self.ui.monolith_cbox.isChecked())
        self.refresh_image_container()

    def refresh_image_container(self):
        current_image = self.image_controller.get_current_image()
        if current_image:
            pixmap = QPixmap.fromImage(ImageQt(current_image))
            self.ui.image_container.setPixmap(pixmap)
        else:
            self.ui.image_container.clear()

    def clear(self):
        self.image_controller.clear()
        self.ui.contrast_slider.setValue(0)
        self.ui.brightness_slider.setValue(0)
        self.ui.monolith_cbox.setChecked(False)
        self.refresh_image_container()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyForm()
    my_app.show()
    sys.exit(app.exec_())
