import random
from kivy.app import App
from Custom_Layouts import BgFloatLayout
from data import WORDS

def get_word():
    my_word = random.choice(WORDS)
    print(my_word)
    return my_word

class Interface(BgFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = get_word()

    def display_info(self):
        ids = self.ids
        response = ids.user_input.text
        if response.lower() == self.word:
            ids.lbl_help.text = 'WOW!'
            ids.lbl_word.text = self.word
        else:
            place_holder = list("*****")
            for char in response:
                index = 0
                used=False
                while index < 5 and not used:
                    if char == self.word[index]:
                        print(f'yes {char} @ {index}')
                        place_holder[index] = char
                        used=True
                    index+=1
            ids.lbl_word.text = "".join(place_holder)
            ids.user_input.text = ""


class WordleApp(App):
    pass

WordleApp().run()