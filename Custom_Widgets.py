from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import StringProperty, ListProperty, BoundedNumericProperty
from kivy.clock import Clock
from kivy.uix.textinput import TextInput


class RoundedButton(Button):
    alpha = BoundedNumericProperty(1, min=0, max=1)  # Default transparency
    hex_code = StringProperty("#FFFFFF")  # Hex color for the button background
    inner_glow_color = StringProperty("#FFD700")  # Default inner glow color (gold)
    gradient_colors = ListProperty(["#FFFFFF", "#000000"])  # Default gradient colors (white to black)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Schedule background creation after properties are set
        Clock.schedule_once(self.create_background)

        # Remove the default background and border of the button
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''

        # Bind touch events for click animation
        self.bind(on_press=self.on_button_press)
        self.bind(on_release=self.on_button_release)

    def hex_to_rgb(self, hex_code):
        """Convert hex color code to RGB values (0 to 1 range)."""
        hex_code = str(hex_code).lstrip("#")
        return [int(hex_code[i:i + 2], 16) / 255 for i in (0, 2, 4)]

    def create_gradient_texture(self, color1, color2, size):
        """Create a vertical gradient texture."""
        from kivy.graphics.texture import Texture
        size = (int(size[0]), int(size[1]))  # Ensure size is integer
        texture = Texture.create(size=(1, size[1]), colorfmt='rgb')
        gradient = []

        # Generate gradient pixels from color1 to color2
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)
        for i in range(size[1]):
            ratio = i / size[1]
            r = r1 * (1 - ratio) + r2 * ratio
            g = g1 * (1 - ratio) + g2 * ratio
            b = b1 * (1 - ratio) + b2 * ratio
            gradient.extend([int(r * 255), int(g * 255), int(b * 255)])

        gradient = bytes(gradient)
        texture.blit_buffer(gradient, colorfmt='rgb', bufferfmt='ubyte')
        texture.wrap = 'repeat'
        return texture

    def create_background(self, dt=None):
        """Create the rounded rectangle background with a 3D shadow effect, inner glow, and gradient."""
        with self.canvas.before:
            # Shadow effect below the button
            Color(0, 0, 0, 0.3)  # Black color with some transparency
            self.shadow = RoundedRectangle(
                radius=[25],  # Same corner radius as the button
                pos=(self.pos[0] + 2, self.pos[1] - 2),  # Slight offset for shadow
                size=self.size
            )

            # Inner glow effect (adjusted for subtle appearance)
            glow_r, glow_g, glow_b = self.hex_to_rgb(self.inner_glow_color)
            Color(glow_r, glow_g, glow_b, 0.75)  # Higher alpha for better visibility
            self.inner_glow = RoundedRectangle(
                radius=[25],  # Same radius as the button
                pos=(self.pos[0] - 1.5, self.pos[1] + 0.25),  # Slightly extended glow outward
                size=(self.size[0] + 2, self.size[1] + 2)  # Subtle spreading
            )

            # Gradient effect
            self.gradient_texture = self.create_gradient_texture(
                color1=self.gradient_colors[0],
                color2=self.gradient_colors[1],
                size=(self.size[0], int(self.size[1]))  # Gradient over button's height
            )
            Color(1, 1, 1, self.alpha)  # Base color for blending
            self.gradient = RoundedRectangle(
                texture=self.gradient_texture,
                radius=[25],
                pos=self.pos,
                size=self.size
            )

            # Button background
            r, g, b = self.hex_to_rgb(self.hex_code)
            self.background_color_instruction = Color(r, g, b, self.alpha)  # Store the color reference
            self.rect = RoundedRectangle(
                radius=[25],  # Rounded corners
                pos=self.pos,
                size=self.size
            )

        # Bind position and size updates
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        """Update the rectangle's position and size."""
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.shadow.pos = (self.pos[0] + 2, self.pos[1] - 2)
        self.shadow.size = self.size
        self.inner_glow.pos = (self.pos[0] - 2, self.pos[1] + 0.5)
        self.inner_glow.size = (self.size[0] + 2, self.size[1] + 2)
        self.gradient.pos = self.pos
        self.gradient.size = self.size

    def on_button_press(self, *args):
        """Simulate a click animation by dimming only the button background."""
        self.background_color_instruction.a = 0.7  # Reduce alpha for click effect

    def on_button_release(self, *args):
        """Restore the original background alpha after release."""
        self.background_color_instruction.a = self.alpha  # Restore the original alpha value

class LimitedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = 'center'
        self.valign = 'middle'
        self.text_size = self.size  # Align text with widget size
        self.multiline = False
        self.padding_y = [self.height / 3.5, 0]  # Center the text vertically (adjust as needed)

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

    def insert_text(self, substring, from_undo=False):
        # Limit input to 5 characters
        if len(self.text) + len(substring) > 5:
            substring = substring[:5 - len(self.text)]
        return super().insert_text(substring, from_undo=from_undo)

    def on_size(self, *args):
        # Ensure text alignment updates dynamically when size changes
        self.text_size = self.size
        self.padding_y = [self.height / 3.5, 0]  # Recalculate padding

