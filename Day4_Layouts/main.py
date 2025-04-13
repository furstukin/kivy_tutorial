from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Custom_Layouts import BgBoxLayout, BgAnchorLayout


# class Interface(BgBoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

# class BoxLayoutApp(App):
#     pass
#
# BoxLayoutApp().run()

# class NestedLayoutApp(App):
#     pass
#
# NestedLayoutApp().run()
class Interface3(BgBoxLayout):
    pass

class Interface2(BgBoxLayout):
    pass

class Interface(BgAnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class AnchorLayoutApp(App):
    pass

AnchorLayoutApp().run()