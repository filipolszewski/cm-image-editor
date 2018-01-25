from PIL import Image, ImageFont, ImageDraw, ImageEnhance


class ComeMeditate():

    def change_contrast(self, img):
        factor = (259 * (self.contrast_level + 255)) / \
                 (255 * (259 - self.contrast_level))

        def contrast(c):
            return 128 + factor * (c - 128)
        return img.point(contrast)

    def build(self):
        self.contrast_level = 50

        #filename
        filename = 'before.jpg'
        output_filename = 'after.jpg'
        source_img = Image.open(filename).convert("RGBA")
        width, height = source_img.size
        # coordinates of rectangle
        rec_x, rec_y = 2 * width // 5, height // 5
        rec_width = width // 5
        rec_height = 3 * width // 5
        # bounding box (diagonal vertices)
        a = (rec_x, rec_y)
        b = (rec_x + rec_width, rec_y + rec_height)

        # b&w
        source_img = source_img.convert('L')
        # contrast
        source_img = self.change_contrast(source_img)

        draw = ImageDraw.Draw(source_img)
        draw.rectangle([a, b], fill="black")

        source_img.save(output_filename)


if __name__ == '__main__':
    try:
        ComeMeditate().build()
        print("image created successfully.")
    except Exception:   # TODO: too broad
        print("sth went wrong. check for errors.")
