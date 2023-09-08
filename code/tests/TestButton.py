import arcade
import arcade.gui
from arcade.gui import UIManager
import sys

class MyFlatButtton(arcade.gui.UIFlatButton):

    def __init__(self,text, center_x, center_y, width, height, ):#
        super().__init__(
            text = text,
            center_x = center_x,
            center_y = center_y,
            width=width,
            height=height,
        )


    def on_press(self):
        self.on_press = True

    def on_release(self):
        self.on_press = False


class Class(arcade.gui.UIManager):

    def __init__(self):
        super().__init__()

    def add_ui_element(self, ui_element):
        ui_element.render()

    def dispatch_ui_event(self, event):
        self.dispatch_event(event)

class MyView(arcade.View):

    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        arcade.start_render()

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def action_func(self):
        pass

    def setup(self):
        self.ui_manager.purge_ui_elements()

        #action = GameWindow

        self.button = MyFlatButtton(
            "Играть",
            center_x= self.window.width // 2,
            center_y= self.window.height // 2,
            width=120,
            height=50,
        )

        self.ui_manager.add_ui_element(self.button)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        x_poz = range(241, 351)
        y_poz = range(177, 228)

        if button == arcade.MOUSE_BUTTON_LEFT and x in x_poz and y in y_poz:
            print(True)

    # def on_mouse_release(self, x, y, button, modifiers):
    #     print(False)


def main():
    window = arcade.Window(width=600, height=400, title = "BUTTON")
    view = MyView()
    window.show_view(view)
    arcade.run()



