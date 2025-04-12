from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn=Button(font_size="32sp", text='Click Me!', size_hint=(0.25,0.15), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn.bind(on_press=self.button_press)
        label=Label(font_size="32sp", text='Bello World!', size_hint=(0.25,0.15), pos_hint={'center_x': 0.5, 'center_y': 0.25})
        text_input=TextInput(font_size="32sp", size_hint=(0.25,0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, multiline=False)
        self.add_widget(btn)
        self.add_widget(label)
        self.add_widget(text_input)

    def button_press(self, obj):
        print(obj.text)

# You can define your UI in the app but it is very limiting as you can't easily switch to a new layout where as using an Interface class allows multiple classes with their own UI.
class SecondApp(App):
    def build(self):
        # layout=FloatLayout()
        # label=Label(font_size="32sp", text='Bello World!', size_hint=(0.25,0.15), pos_hint={'center_x': 0.5, 'center_y': 0.25})
        # text_input=TextInput(font_size="32sp", size_hint=(0.25,0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, multiline=False)
        # layout.add_widget(text_input)
        # layout.add_widget(label)
        # return layout
        pass

SecondApp().run()