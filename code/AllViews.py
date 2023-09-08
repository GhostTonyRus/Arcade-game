import arcade
import arcade.gui
from arcade.gui import UIManager, UIElement, UIEvent, UIException, UIClickable
from pyglet.event import EventDispatcher
import sys
from FirstMap import GameMap_1
from SecondMap import GameMap_2
from FirstParkingMap import StartGameWindow
import random
from MapObjects import Save
import shelve
import pyglet

# КОНСТАНТЫ ЭКРАНА
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Race"
MARGIN = 20

# КОНСТАНТЫ ПАРАМЕТРОВ МАШИНЫ ИГРОКА
STRAIGHT_SPEED = 5
TURN_SPEED = 4.5
PLAYER_SIZE = 2.5
BOOST_CAR_SPEED = 5
PLAYER_MASS = 2.0

# КОНСТАНТЫ ПАРМАТЕРОВ БОТОВ ПЕШЕХДОВ
BOT_HUMAN_SPEED = 5
BOT_HUMAN_SIZE = 4
BOT_HUMAN_IN_TOTAL = 10

# КОНСТАНТЫ ПАРМАТЕРОВ МАШИНЫ ИГРОКА
BOT_CAR_SPEED = 20
BOT_CAR_SIZE = 2.5
BOT_CAR_IN_TOTAL = 5

# КОНСТАНТЫ ПАРМАТЕРОВ ЛИНИЙ
LINE_IN_TOTAL = 4
LINE_SIZE = 2

# СЧЁТ
SCORE = 0

class GameWindow(arcade.View):
    # старт игры
    def action_func(self):
        instruction_window = InstructionWindow()
        instruction_window.setup()
        self.window.show_view(instruction_window)

    # меню выбора карт
    def menu_func(self):
        instruction_window = InstructionWindow()
        instruction_window.setup()
        self.window.show_view(instruction_window)

    def start_game_map_1(self):
        # game_map_1 = GameMap_1()
        # game_map_1.setup()
        # self.window.show_view(game_map_1)
        parking_map_1 = StartGameWindow()
        parking_map_1.setup()
        self.window.show_view(parking_map_1)

    def start_game_map_2(self):
        game_map_2 = GameMap_2()
        game_map_2.setup()
        self.window.show_view(game_map_2)

class PlayButton(arcade.gui.UIFlatButton):

    def on_click(self):
        window = GameWindow()
        window.action_func()

class ExitButton(arcade.gui.UIFlatButton):

    def on_click(self):
        pyglet.app.exit()

class DayMapSelect(arcade.gui.UIImageButton):

    def on_click(self):
        window = GameWindow()
        window.start_game_map_1()

class NightMapSelect(arcade.gui.UIImageButton):

    def on_click(self):
        window = GameWindow()
        window.start_game_map_2()

class MenuWindowButton(arcade.gui.UIFlatButton):

    def on_click(self):
        window = GameWindow()
        window.menu_func()

class StartWindow(arcade.View):

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
        arcade.draw_text("Race", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=150, anchor_x="center")

        # ВЕРСИЯ ИГРЫ
        arcade.draw_text("v.1.0", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 500,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

    def setup(self):
        self.ui_manager.purge_ui_elements()

        self.button_play = PlayButton(
            "Играть",
            center_x=self.window.width // 2,
            center_y=self.window.height // 2 - 100,
            width=120,
            height=50,
        )

        self.ui_manager.add_ui_element(self.button_play)

        self.button_exit = ExitButton(
            "Выход из игры",
            center_x=self.window.width // 2,
            center_y=self.window.height // 2 - 200,
            width=200,
            height=50,
        )

        self.ui_manager.add_ui_element(self.button_exit)

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

        arcade.draw_text("ДЕНЬ", SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 120,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("НОЧЬ", SCREEN_WIDTH / 2 + 300, SCREEN_HEIGHT / 2 - 120,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        arcade.draw_text("W - вперёд\nS - назад\nA - направо\nD - налево", SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 280,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

        arcade.draw_text("LShift - ускорение\nSPACE - ручник\nL - свет (работает только на ночной карте)", SCREEN_WIDTH / 2 + 300, SCREEN_HEIGHT / 2 - 280,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def setup(self):
        first_map_picture = arcade.load_texture("../resources/textures/MAP_BUTTON_DAY.png")
        choice = arcade.load_texture("../resources/textures/CHOICE.png")
        first_map_button = DayMapSelect(center_x=SCREEN_WIDTH / 2 - 300,
                                        center_y=SCREEN_HEIGHT / 2 + 120,
                                        normal_texture=first_map_picture,
                                        press_texture=first_map_picture,
                                        hover_texture=choice,
                                        text="")

        self.ui_manager.add_ui_element(first_map_button)

        second_map_picture = arcade.load_texture("../resources/textures/MAP_BUTTON_NIGHT.png")
        choice = arcade.load_texture("../resources/textures/CHOICE.png")
        second_map_button = NightMapSelect(center_x=SCREEN_WIDTH / 2 + 300,
                                            center_y=SCREEN_HEIGHT / 2 + 120,
                                            normal_texture=second_map_picture,
                                            press_texture=second_map_picture,
                                            hover_texture=choice,
                                            text="")

        self.ui_manager.add_ui_element(second_map_button)

        self.button_exit = ExitButton(
            "Выход из игры",
            center_x=self.window.width // 2,
            center_y=self.window.height // 2 - 400,
            width=200,
            height=50,
        )

        self.ui_manager.add_ui_element(self.button_exit)

# КОНЕЦ ИГРЫ
class GameOverWindow(arcade.View):

    def __init__(self):
        super().__init__()

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        self.window.set_mouse_visible(True)

        self.ui_manager = UIManager()

        self.score = 0

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=150, anchor_x="center")

        # with shelve.open("resources/saves/save_distance") as distance:
        #     for dist in distance.values():
        #         pass

        try:
            with open("../resources/saves/save_distance.txt", "r") as file:
                dist = file.read()
        except FileNotFoundError:
            pass
        # else:
        #     return dist

        score_info = f"Счёт: {'%.2f' % float(dist)}"
        arcade.draw_text(score_info, 1555, 1000, arcade.color.WHITE, 39)

    def setup(self):
        button = MenuWindowButton(
            "В меню выбора",
            center_x=self.window.width // 2,
            center_y=self.window.height // 2 - 100,
            width=220,
            height=50,
        )

        self.ui_manager.add_ui_element(button)

        button = ExitButton(
            "Выход из игры",
            center_x=self.window.width // 2,
            center_y=self.window.height // 2 - 200,
            width=220,
            height=50,
        )

        self.ui_manager.add_ui_element(button)






