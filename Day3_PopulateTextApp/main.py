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
            self.bg = Rectangle(source='../images/JamieLeeIcon.png', pos=self.pos, size=self.size)

        # Bind the size and position of the background to the layout
        self.bind(size=self.update_bg, pos=self.update_bg)

        self.btn=Button(
            text='Submit',
            size_hint=(0.5,0.1),
            pos_hint={'center_x':0.5, 'center_y':0.35}
        )
        self.label = Label(
            font_size="32sp",
            text='',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            font_name = "seguiemj"  # Emoji-compatible font
        )
        self.text_input = TextInput(
            hint_text="Enter the secret word!",
            font_size="32sp",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            multiline=False,
            on_text_validate=self.display_info
        )
        self.btn.bind(on_press=self.display_info)
        self.add_widget(self.btn)
        self.add_widget(self.label)
        self.add_widget(self.text_input)

    def display_info(self, obj):
        info = self.text_input.text
        if info.lower() == 'boobies':
            self.label.text='Nice! Now you can see my boobies \U0001F609 \U0001F48B'
            self.remove_widget(self.btn)
            self.remove_widget(self.text_input)
            # self.text_input.text = ''
            # self.btn.pos_hint={'center_x':0.5, 'center_y':0.10}
            # self.text_input.hint_text = 'Good job!'
        else:
            if self.btn.pos_hint!={'center_x':0.5, 'center_y':0.10}:
                self.label.text = 'Rent is not the only thing that costs money around here!'
                self.text_input.text = ''
                self.text_input.hint_text = 'Hint: Try the app title.'

    def update_bg(self, instance, value):
        self.bg.size = instance.size
        self.bg.pos = instance.pos

class BoobiesApp(App):
    def build(self):
        return Interface()

BoobiesApp().run()