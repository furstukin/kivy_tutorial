from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add a background image to the interface
        with self.canvas.before:
            self.bg = Rectangle(source='../../images/JamieLeeIcon.png', pos=self.pos, size=self.size)
            self.bind(size=self.update_bg, pos=self.update_bg)

    def update_bg(self, instance, value):
        self.bg.size = instance.size
        self.bg.pos = instance.pos

    def display_info(self):
        ids = self.ids
        info = ids.text_input.text
        if info.lower() == 'boobies':
            ids.label.text='Nice! Now you can see my boobies \U0001F609 \U0001F48B'
            self.remove_widget(ids.btn)
            self.remove_widget(ids.text_input)
        else:
            if ids.btn.pos_hint!={'center_x':0.5, 'center_y':0.10}:
                ids.label.text = 'Rent is not the only thing that costs money around here!'
                ids.text_input.text = ''
                ids.text_input.hint_text = 'Hint: Try the app title.'

class BoobiesApp(App):
    pass

BoobiesApp().run()