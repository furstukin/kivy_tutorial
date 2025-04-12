from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import BoundedNumericProperty, StringProperty


class RoundedButton(Button):
    alpha = BoundedNumericProperty(1, min=0, max=1)  # Default transparency
    hex_code = StringProperty("#FFFFFF")  # Hex color for the button background

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

    def hex_to_rgb(self, hex):
        """Convert hex color code to RGB values (0 to 1 range)."""
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i + 2], 16)
            rgb.append(decimal / 255)
        return rgb

    def create_background(self, dt=None):  # Add the optional 'dt' parameter
        """Create the rounded rectangle background."""
        with self.canvas.before:
            # Parse the hex color and apply RGBA color
            self.hex_code = str(self.hex_code).split("#")[-1]
            r, g, b = self.hex_to_rgb(self.hex_code)
            Color(r, g, b, self.alpha)  # Initial RGBA color
            self.rect = RoundedRectangle(
                radius=[25],  # Rounded corners
                pos=self.pos,
                size=self.size
            )

        # Update position and size dynamically
        self.bind(pos=self.update_rect, size=self.update_rect)

        # Update position and size when the button moves or resizes
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        """Update the rectangle's position and size."""
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_button_press(self, *args):
        """Simulate a click animation by dimming the button."""
        self.canvas.before.children[0].a = 0.7  # Reduce alpha to make it semi-transparent

    def on_button_release(self, *args):
        """Restore the original background after the button is released."""
        self.canvas.before.children[0].a = self.alpha  # Restore the original alpha value



class RoundedButtonApp(App):
    def build(self):
        return RoundedButton(
            text="Rounded Button",
            size_hint=(0.5, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=24,
            hex_code="#5214FF"
        )


if __name__ == '__main__':
    RoundedButtonApp().run()