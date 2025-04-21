from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

from Custom_Layouts import BgBoxLayout, BgAnchorLayout, BgGridLayout, BgStackLayout


class Interface(BgBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Interface2(BgBoxLayout):
    pass


class Interface3(BgBoxLayout):
    pass


class Interface4(BgAnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Interface5(BgBoxLayout):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)

    def shuffle(self):
        texts=[]
        count=8
        children=self.ids.grid_layout.children
        for child in reversed(children):
            texts.append(child.text)

        print(texts)

        for r in range(3,0,-1):
            for c in range(r-1, r+2*3, 3):
                children[count].text=texts[c]
                count-=1


class Interface6(BgBoxLayout):
    def __init__(self, **kwargs):
          super().__init__(**kwargs)
          Clock.schedule_once(self.generate_buttons)

    def generate_buttons(self, dt=0):
        for i in range(10):
            btn = Button(text=str(i), size_hint=(None,None), size=(dp(100), dp(50)))
            self.ids.stack_layout.add_widget(btn)

    def clear_buttons(self, dt=0):
        self.ids.stack_layout.clear_widgets()


class Interface7(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LayoutsApp(App):
    pass

LayoutsApp().run()