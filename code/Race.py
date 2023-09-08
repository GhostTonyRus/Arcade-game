import arcade
from arcade.gui import UIManager

# КОНСТАНТЫ ЭКРАНА
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "FirstTest"


# class UIImageButton(UIClickable):
#     def __init__(self):

# class MyImageButton(arcade.gui.UIImageButton):
#
#     #def __init__(self, hover_texture, press_texture, center_x, center_y, text):
#     def __init__(self):
#         super().__init__(normal_texture=None,
#                          center_x=0,
#                          center_y=0)
#
class InstructionWindow(arcade.View):

    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()

        # НАЗВАНИЕ ИГРЫ
        arcade.draw_text("Выбор карты", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 300,
                         arcade.color.WHITE, font_size=150, anchor_x="center")

        arcade.draw_text("ДЕНЬ", SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("W - вперёд\nS - назад\nA - направо\nD - налево", SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

        arcade.draw_text("LShift - ускорение\nSPACE - ручник\nL - свет (работает только на ночной карте)", SCREEN_WIDTH / 2 + 300, SCREEN_HEIGHT / 2 - 250,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def setup(self):
        first_map_picture = arcade.load_texture("textures/MAP_BUTTON.png")
        choice = arcade.load_texture("textures/CHOICE.png")
        first_map_button = arcade.gui.UIImageButton(center_x=SCREEN_WIDTH / 2 - 300,
                                                    center_y=SCREEN_HEIGHT / 2 + 150,
                                                    normal_texture=first_map_picture,
                                                    press_texture=first_map_picture,
                                                    hover_texture=choice,
                                                    text="")

        self.ui_manager.add_ui_element(first_map_button)

    def action_func(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        x_poz_play = range(401, 910)
        y_poz_play = range(380, 790)

        # x_poz_exit = range(850, 1070)
        # y_poz_exit = range(300, 370)

        if button == arcade.MOUSE_BUTTON_LEFT and x in x_poz_play and y in y_poz_play:
            #self.action_func()
            print(True)

        # if button == arcade.MOUSE_BUTTON_LEFT and x in x_poz_exit and y in y_poz_exit:
        #     pass

def main():
    window = arcade.Window(title="TEST",fullscreen=True)
    instruction_view = InstructionWindow()
    instruction_view.setup()
    window.show_view(instruction_view)
    arcade.run()

main()