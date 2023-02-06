import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider


class ImageProcessor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original_image = cv2.imread("image.jpg")
        self.processed_image = self.original_image.copy()
        self.img = Image(source='image.jpg')
        self.sharpness_slider = Slider(min=0, max=10, value=0, on_value=self.apply_sharpness)
        self.blur_slider = Slider(min=0, max=10, value=0, on_value=self.apply_blur)
        self.add_widget(self.img)
        self.add_widget(self.sharpness_slider)
        self.add_widget(self.blur_slider)

    def apply_sharpness(self, value, *args):
        sharpness = float(value) / 10
        self.processed_image = cv2.addWeighted(self.original_image, sharpness, self.original_image, 0, 0)
        self.img.reload()

    def apply_blur(self, value, *args):
        blur = int(value)
        self.processed_image = cv2.GaussianBlur(self.original_image, (blur, blur), 0)
        self.img.reload()


class MyApp(App):
    def build(self):
        return ImageProcessor()


if __name__ == '__main__':
    MyApp().run()
