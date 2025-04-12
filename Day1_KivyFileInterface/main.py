from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def print_press_msg(self):
        print('See my boobs!')
    def print_release_msg(self):
        print('Ok you saw enough!')
    def print_submit_msg(self):
        print('You submitted the text.')
    def print_focus_msg(self):
        print('You focused on this widget.')


class FirstApp(App):
    def print_msg(self):
        print('See my boobs! From the app class')

FirstApp().run()