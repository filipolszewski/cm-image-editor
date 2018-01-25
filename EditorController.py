from PIL import Image
import copy

class EditorController:
    def __init__(self, cont_size):
        self.cont_width = cont_size.width()
        self.cont_height = cont_size.height()
        self.working_image = None
        self.current_image = None
        self.file_path = None

    def set_working_image(self, filename):
        self.file_path = filename
        # TODO Parametrize which part of image to cut(?)
        img = Image.open(filename).convert("RGBA")
        # expected img size at this point - 4592x3072
        # 3072 -> 2583
        crop_rectangle = (0, 244, 4592, 2828)
        cropped_img = img.crop(crop_rectangle)
        self.working_image = cropped_img
        self.current_image = self.working_image.copy()
        print(self.current_image)

    def get_current_image(self):
        return self._resize_to_cont(self.current_image)

    def _resize_to_cont(self, current_image):
        current_image.thumbnail((self.cont_width, self.cont_height), Image.ANTIALIAS)
        return current_image

    def apply_changes(self):
        self.working_image = self.current_image.copy()


