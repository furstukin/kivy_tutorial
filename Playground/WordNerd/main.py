import random
from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.graphics import Rectangle, Color
from Custom_Layouts import BgFloatLayout, BgBoxLayout
from data import WORDS_5L, WORDS_5L_EASY, WORDS_5L_MED
from kivy.core.window import Window

Window.softinput_mode = "below_target"

TRIES_DICT = {
    '1': ['lbl_ans1_1', 'lbl_ans1_2', 'lbl_ans1_3', 'lbl_ans1_4', 'lbl_ans1_5'],
    '2': ['lbl_ans2_1', 'lbl_ans2_2', 'lbl_ans2_3', 'lbl_ans2_4', 'lbl_ans2_5'],
    '3': ['lbl_ans3_1', 'lbl_ans3_2', 'lbl_ans3_3', 'lbl_ans3_4', 'lbl_ans3_5'],
    '4': ['lbl_ans4_1', 'lbl_ans4_2', 'lbl_ans4_3', 'lbl_ans4_4', 'lbl_ans4_5'],
    '5': ['lbl_ans5_1', 'lbl_ans5_2', 'lbl_ans5_3', 'lbl_ans5_4', 'lbl_ans5_5']
}

def get_word():
    my_word = random.choice(WORDS_5L)
    print(my_word)
    return my_word


class Interface(BgFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.word = ''
        self.tries = 0

        # Add background image using canvas instructions
        with self.canvas.before:
            self.bg_image = Image('images/word_game_bg.png').texture  # Replace with your image file path
            Rectangle(size=self.size, pos=self.pos, texture=self.bg_image)

        # Ensure the background resizes with the layout
        self.bind(size=self.update_bg_image, pos=self.update_bg_image)

    def update_bg_image(self, instance, value):
        # Ensure the background rectangle matches the size and position of the layout
        self.canvas.before.clear()
        with self.canvas.before:
            Rectangle(size=self.size, pos=self.pos, texture=self.bg_image)

    def on_kv_post(self, base_widget):
        self.ids.btn.on_press = self.start_game

    def update_label_background(self, label_id, rgba_color):
        # Access the label by its ID
        label = self.ids[label_id]

        # Add canvas instructions for the background
        with label.canvas.before:
            Color(rgba_color[0], rgba_color[1], rgba_color[2], rgba_color[3])  # Set the background color
            label.bg_rect = Rectangle(size=label.size, pos=label.pos)

        # Bind the label's size and position to update the background rectangle dynamically
        label.bind(size=self.update_bg_rect, pos=self.update_bg_rect)

    def update_bg_rect(self, instance, value):
        # Ensure the background rectangle matches the label's size and position
        instance.bg_rect.size = instance.size
        instance.bg_rect.pos = instance.pos

    def start_game(self):
        self.word = get_word()
        self.tries = 0
        main_ids = self.ids
        for row in range(1,6):
            for label in TRIES_DICT[str(row)]:
                self.update_label_background(label, (1, 1, 1, 1))
                main_ids[label].text = '-'
        main_ids.btn.text = 'Submit'
        main_ids.btn.on_press = self.check_response
        main_ids.user_input.disabled = False
        Clock.schedule_once(lambda dt: setattr(main_ids.user_input, 'focus', True), 0.25)

    def check_response(self):
        main_ids = self.ids
        response = main_ids.user_input.text.upper()
        #Check if response is 5 letters long
        if len(response) < 5:
            main_ids.lbl_help.text = 'Must be a 5 letter word.'
            return

        #Check if response is a real 5 letter word
        elif response not in WORDS_5L:
            main_ids.lbl_help.text = "Don't test me friend! That's not a real word."
            return
        else:
            self.tries += 1
            place_holder = list(self.word)
            cur_char = 0
            for char in response:
                index = 0
                cur_id = TRIES_DICT[f'{self.tries}'][cur_char]
                main_ids[cur_id].text = char.upper()
                used=False
                while index < 5 and not used:
                    if char == place_holder[index]:
                        place_holder[index] = '-'
                        used=True
                        if index == cur_char:
                            self.update_label_background(cur_id, (0, 1, 0, 0.75))  # Green background
                        else:
                            self.update_label_background(cur_id, (1, 1, 0, 0.75))  # Yellow background
                    index+=1
                if not used:
                    self.update_label_background(cur_id, (1, 0, 0, 0.75))  # Red background
                cur_char += 1
            main_ids.user_input.text = ""
            Clock.schedule_once(lambda dt: setattr(main_ids.user_input, 'focus', True), 0)
            if response == self.word:
                main_ids.lbl_help.text = 'WOW! Nice job.'
                main_ids.user_input.disabled = True
                main_ids.btn.text = 'Try Again?'
                main_ids.btn.on_press = self.start_game
            elif self.tries == 5:
                main_ids.lbl_help.text = f'Sorry you have run out of tries. The word was {self.word}.'
                main_ids.user_input.disabled = True
                main_ids.btn.text = 'Try Again?'
                main_ids.btn.on_press = self.start_game

class Logo(BgBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Bind the background update to resizing events
        self.bind(size=self.update_bg_image, pos=self.update_bg_image)

    def on_kv_post(self, base_widget):
        # Ensure the background is properly initialized after the widget is set up
        Clock.schedule_once(lambda dt: self.setup_bg(), 0)

    def setup_bg(self):
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White border
            self.border_rect = Rectangle(size=(self.size[0] + 4, self.size[1] + 4),
                                         pos=(self.pos[0] - 2, self.pos[1] - 2))

            self.bg_image = Image('images/logo_bg.png').texture
            self.bg_rect = Rectangle(size=self.size, pos=self.pos, texture=self.bg_image)

        # Ensure both background and border update on resize
        self.bind(size=self.update_bg_image, pos=self.update_bg_image)

    def update_bg_image(self, instance, value):
        if hasattr(self, 'bg_rect') and hasattr(self, 'border_rect'):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

            # Ensure the border resizes with the background
            self.border_rect.size = (self.size[0] + 4, self.size[1] + 4)
            self.border_rect.pos = (self.pos[0] - 2, self.pos[1] - 2)

class WordNerdApp(App):
    pass

WordNerdApp().run()