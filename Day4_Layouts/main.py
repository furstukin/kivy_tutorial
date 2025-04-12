from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Custom_Layouts import BgBoxLayout


class Interface(BgBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class BoxLayoutApp(App):
    pass

BoxLayoutApp().run()