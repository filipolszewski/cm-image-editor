from PIL import Image, ImageEnhance, ImageDraw


class EditorController:
    def __init__(self, cont_size):
        self.cont_width = cont_size.width()
        self.cont_height = cont_size.height()
        # working = image we work on. Apply btn saves current one to working
        self.working_image = None
        self.current_image = None
        self.file_path = None
        self.monolith_checked = False

    def save_final_img(self):
        save_path = "output/" + self.file_path.split("/")[-1]
        if self.monolith_checked:
            self.draw_monolith(self.current_image).save(save_path)
        else:
            self.current_image.save(save_path)

    def set_working_image(self, filename):
        self.file_path = filename

        # TODO Parametrize which part of image to cut(?)
        img = Image.open(filename).convert("RGBA")
        # expected img size at this point - 4592x3072
        # 3072 -> 2583
        crop_rectangle = (0, 244, 4592, 2828)
        cropped_img = img.crop(crop_rectangle)

        self.working_image = self.black_and_white(cropped_img)
        self.current_image = self.working_image.copy()
        print(self.current_image)

    def get_current_image(self):
        if self.current_image is None:
            return None
        if self.monolith_checked:
            return self._resize_to_cont(self.draw_monolith(self.current_image.copy()))
        return self._resize_to_cont(self.current_image.copy())

    def _resize_to_cont(self, current_image):
        current_image.thumbnail((self.cont_width, self.cont_height), Image.ANTIALIAS)
        return current_image

    def apply_changes(self):
        self.working_image = self.current_image.copy()

    @staticmethod
    def black_and_white(img):
        return ImageEnhance.Color(img).enhance(0.0)

    def change_brightness_contrast(self, b_param, c_param):
        b_factor = ((b_param / 123) + 1) * 1.2
        c_factor = ((c_param / 123) + 1) * 1.2
        tmp_img = self.working_image.copy()
        enhancer_b = ImageEnhance.Brightness(tmp_img)
        tmp_img = enhancer_b.enhance(b_factor)
        enhancer_c = ImageEnhance.Contrast(tmp_img)
        self.current_image = enhancer_c.enhance(c_factor)

    def monolith_change(self, checked):
        self.monolith_checked = checked

    def draw_monolith(self, img):
        a = (2000, 450)
        b = (2596,  2583 - a[1])
        draw = ImageDraw.Draw(img)
        draw.rectangle((a, b), fill="black")
        return img

    def clear(self):
        self.working_image = None
        self.current_image = None
        self.file_path = None
        self.monolith_checked = False
