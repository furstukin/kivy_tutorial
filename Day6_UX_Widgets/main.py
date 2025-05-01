from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Interface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def checking(self, checkbox, label_id):
        if checkbox.active:
            print(label_id.text)

class WidgetsApp(App):
    pass

WidgetsApp().run()