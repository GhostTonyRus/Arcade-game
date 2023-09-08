# import arcade
# import arcade.gui
# from arcade.gui import UIManager, UIElement, UIEvent, UIException, UIClickable
# from pyglet.event import EventDispatcher
# from MapObjects import HumanBot1, HumanBot2, Line, PlayerCar, BotCar
#
# import random
# import sys
#
# # КОНСТАНТЫ ЭКРАНА
# SCREEN_WIDTH = 1920
# SCREEN_HEIGHT = 1080
# SCREEN_TITLE = "FirstTest"
# MARGIN = 20
#
# # КОНСТАНТЫ ПАРАМЕТРОВ МАШИНЫ ИГРОКА
# STRAIGHT_SPEED = 5
# TURN_SPEED = 4.5
# PLAYER_SIZE = 2.5
# BOOST_CAR_SPEED = 5
# PLAYER_MASS = 2.0
#
# # КОНСТАНТЫ ПАРМАТЕРОВ БОТОВ ПЕШЕХДОВ
# BOT_HUMAN_SPEED = 5
# BOT_HUMAN_SIZE = 4
# BOT_HUMAN_IN_TOTAL = 10
#
# # КОНСТАНТЫ ПАРМАТЕРОВ МАШИНЫ ИГРОКА
# BOT_CAR_SPEED = 20
# BOT_CAR_SIZE = 2.5
# BOT_CAR_IN_TOTAL = 5
#
# # КОНСТАНТЫ ПАРМАТЕРОВ ЛИНИЙ
# LINE_IN_TOTAL = 4
# LINE_SIZE = 2
#
# # СЧЁТ
# SCORE = 0
#
# class GameWindow:
#
#     def start_game_map_1(self):
#         pass
#         # game_map_1 = GameMap_1()
#         # game_map_1.setup()
#         # self.window.show_view(game_map_1)
#
#     def start_game_map_2(self):
#         pass
#
# class MyFlatButton(arcade.gui.UIFlatButton):
#
#     def __init__(self, text, width, height, center_x, center_y, ):
#         super().__init__(text = text,
#                          width = width,
#                          height = height,
#                          center_x = center_x,
#                          center_y = center_y,
#                          )
#
#     def on_focus(self):
#         self.focused = True
#
#     def on_press(self):
#         self.pressed = True
#
#
#     def on_release(self):
#         self.pressed = False
#
# class StartWindow(arcade.View):
#
#     def __init__(self):
#         super().__init__()
#
#         self.ui_manager = UIManager()
#
#     def on_show_view(self):
#         self.setup()
#
#     def on_hide_view(self):
#         self.ui_manager.unregister_handlers()
#
#     def on_show(self):
#         arcade.set_background_color(arcade.color.BLACK)
#
#         arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
#
#     def on_draw(self):
#         arcade.start_render()
#
#         # НАЗВАНИЕ ИГРЫ
#         arcade.draw_text("PythonRace", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
#                          arcade.color.WHITE, font_size=150, anchor_x="center")
#
#     def setup(self):
#         self.button_play = MyFlatButton(
#             "Играть",
#             center_x=self.window.width // 2,
#             center_y=self.window.height // 2 - 100,
#             width=120,
#             height=50,
#         )
#
#         self.ui_manager.add_ui_element(self.button_play)
#
#         self.button_exit = MyFlatButton(
#             "Выход из игры",
#             center_x=self.window.width // 2,
#             center_y=self.window.height // 2 - 200,
#             width=200,
#             height=50,
#         )
#
#         self.ui_manager.add_ui_element(self.button_exit)
#
#     def action_func(self):
#         pass
#         # window = GameWindow()
#         # window.start_game_map_1()
#
#     def on_mouse_press(self, x, y, button, modifiers):
#         x_poz_play = range(900, 1200)
#         y_poz_play = range(420, 490)
#
#         x_poz_exit = range(850, 1070)
#         y_poz_exit = range(300, 370)
#
#         if button == arcade.MOUSE_BUTTON_LEFT and x in x_poz_play and y in y_poz_play:
#             # self.action_func()
#             game_window = GameMap_1()
#             game_window.setup()
#             self.window.show_view(game_window)
#
#         if button == arcade.MOUSE_BUTTON_LEFT and x in x_poz_exit and y in y_poz_exit:
#             sys.exit()
#
#     def on_mouse_release(self, x, y, button, modifiers):
#         if button == arcade.MOUSE_BUTTON_LEFT:
#             print("не нажато")
#
#
# class GameMap_1(arcade.View):
#
#     def __init__(self):
#         super().__init__()
#
#         self.players_car_list = None
#
#         self.bot_human_list = None
#
#         self.background = None
#
#         self.player_car = None
#
#         self.background_texture = None
#
#         self.line_list = None
#
#         self.physics_engine = None
#
#         self.bot_car = None
#         self.bot_car_list = None
#
#         self.score = 0
#
#         # ВРЕМЕННОЕ УПРАВЛЕНИЕ
#         self.left_pressed = None
#         self.right_pressed = None
#         self.up_pressed = None
#         self.down_pressed = None
#
#     def add_car(self, delta_time):
#         car = BotCar("sprites/cars/mycar.png", 2.5)
#         car.center_x = 1100
#         car.center_y = SCREEN_HEIGHT / 2
#         car.velocity = (random.randint(5, 2), 0)
#         self.bot_car_list.append(car)
#
#
#     # ОСНОВНЫЕ НАСТРОЙКИ СПРАЙТОВ
#     def setup(self):
#         self.background_texture = arcade.SpriteList()
#         self.background = arcade.Sprite("textures/ROAD_2.png")
#         self.background.center_x = 960
#         self.background.center_y = 530
#         self.background_texture.append(self.background)
#
#         self.players_car_list = arcade.SpriteList()
#         self.player_car = PlayerCar("sprites/cars/mycar.png", PLAYER_SIZE)
#         self.player_car.center_x = SCREEN_WIDTH / 2 + 150
#         self.player_car.center_y = 200
#         self.players_car_list.append(self.player_car)
#
#         self.bot_human_list = arcade.SpriteList()
#
#         for human_1 in range(BOT_HUMAN_IN_TOTAL):
#             human_1 = HumanBot1("sprites/humans/Human_bot_yellow.png", BOT_HUMAN_SIZE)
#             human_1.center_x = random.randrange(20, 100)
#             human_1.center_y = random.randrange(SCREEN_HEIGHT + 10)
#             self.bot_human_list.append(human_1)
#
#         for human_2 in range(BOT_HUMAN_IN_TOTAL):
#             human_2 = HumanBot2("sprites/humans/Human_bot_2.png", BOT_HUMAN_SIZE)
#             human_2.center_x = random.randrange(1800, 1850)
#             human_2.center_y = random.randrange(SCREEN_HEIGHT + 10)
#
#             self.bot_human_list.append(human_2)
#
#         self.line_list = arcade.SpriteList()
#
#         # ВЕРХНИЕ 1 ДВЕ ЛИНИИ
#         # СЛЕВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 440
#         line.center_y = 1164
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 700
#         line.center_y = 1164
#         self.line_list.append(line)
#
#         # СПРАВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1210
#         line.center_y = 1164
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1480
#         line.center_y = 1164
#         self.line_list.append(line)
#
#         # ВЕРХНИЕ 2 ДВЕ ЛИНИИ
#         # СЛЕВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 440
#         line.center_y = 864
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 700
#         line.center_y = 864
#         self.line_list.append(line)
#
#         # СПРАВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1210
#         line.center_y = 864
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1480
#         line.center_y = 864
#         self.line_list.append(line)
#
#         # ВЕРХНИЕ 3 ДВЕ ЛИНИИ
#         # СЛЕВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 440
#         line.center_y = SCREEN_HEIGHT / 2 + 10
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 700
#         line.center_y = SCREEN_HEIGHT / 2 + 10
#         self.line_list.append(line)
#
#         # СПРАВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1210
#         line.center_y = SCREEN_HEIGHT / 2 + 10
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1480
#         line.center_y = SCREEN_HEIGHT / 2 + 10
#         self.line_list.append(line)
#
#         # ВЕРХНИЕ 4 ДВЕ ЛИНИИ
#         # СЛЕВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 700
#         line.center_y = SCREEN_HEIGHT / 5 + 20
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 440
#         line.center_y = SCREEN_HEIGHT / 5 + 20
#         self.line_list.append(line)
#
#         # СПРАВА
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1210
#         line.center_y = SCREEN_HEIGHT / 5 + 20
#         self.line_list.append(line)
#
#         line = Line("textures/LINE.png", 1)
#         line.center_x = 1480
#         line.center_y = SCREEN_HEIGHT / 5 + 20
#         self.line_list.append(line)
#
#         # СПАВН МАШИН
#         self.bot_car_list = arcade.SpriteList()
#
#         car_bot = BotCar("sprites/cars/Red_car.png", BOT_CAR_SIZE)
#         car_bot.center_x = 300
#         car_bot.center_y = SCREEN_HEIGHT / 2 + 300
#         car_bot.angle = -180
#         self.bot_car_list.append(car_bot)
#
#         car_bot = BotCar("sprites/cars/Green_car.png", BOT_CAR_SIZE)
#         car_bot.center_x = 830
#         car_bot.center_y = SCREEN_HEIGHT / 2
#         car_bot.angle = -180
#         self.bot_car_list.append(car_bot)
#
#         car_bot = BotCar("sprites/cars/Blue_car.png", BOT_CAR_SIZE)
#         car_bot.center_x = 1350
#         car_bot.center_y = SCREEN_HEIGHT / 2 - 300
#         car_bot.angle = -180
#         self.bot_car_list.append(car_bot)
#
#         self.player_car.angle = 0
#
#         self.score = 0
#
#         self.physics_engine = arcade.PhysicsEngineSimple(self.player_car, self.bot_car_list)
#
#         SCORE = 0
#
#     # РИСУЕМ ОБЪЕКТЫ НА КАРТЕ
#     def on_draw(self):
#         arcade.start_render()
#
#         # РИСУЕМ BACKGROUND
#         self.background_texture.draw()
#
#         # РИСУЕМ БОТОВ ПЕШЕХОДОВ
#         self.bot_human_list.draw()
#
#         # РИСУЕМ БОТОВ МАШИН
#         self.line_list.draw()
#
#         # РИСУЕМ ЛИНИИ
#         self.bot_car_list.draw()
#
#         # РИСУЕМ МАШИНА ИГРОКА
#         self.players_car_list.draw()
#
#         score_info = f"Счёт: {'%.2f' % self.score}"
#         arcade.draw_text(score_info, 1520, 1000, arcade.color.WHITE, 39)
#
#     def update(self, delta_time):
#
#         # ОБНОВЛЯЕМ ДВИЖОК
#         self.physics_engine.update()
#
#         # ОБНОВЛЯЕМ МАШИНУ ИГРОКА
#         self.player_car.update()
#
#         # ОБНОВЛЯЕМ БОТОВ ПЕШЕХОДОВ
#         self.bot_human_list.update()
#
#         # ОБНОВЛЯЕМ ЛИНИИ
#         self.line_list.update()
#
#         # ОБНОВЛЯЕМ МАШИНЫ БОТОВ
#         self.bot_car_list.update()
#
#         # ОБНОВЛЕНИЕ СЧЁТА
#         self.score += delta_time
#
#         # СТОЛКНОВЕНИЕ С МАШИНАМИ
#         car_hits = arcade.check_for_collision_with_list(self.player_car, self.bot_car_list)
#
#         # СТОЛКНОВЕНИЕ С ПЕШЕХОДАМИ
#         bot_hits = arcade.check_for_collision_with_list(self.player_car, self.bot_human_list)
#
#         # for car_hit in car_hits:
#         #     #sys.exit()
#         #     window = arcade.Window(title='PythonRace', True)
#         #     end_view = GameOverWindow()
#         #     window.show_view(end_view)
#
#         # for bot_hit in bot_hits:
#         #     view = GameOverWindow()
#         #     self.window.show_view(view)
#
#     # БЛКОКИ УПАРВЛЕНИЯ МАШИНОЙ
#     def on_key_press(self, key, modifiers):
#
#         if key == arcade.key.UP or key == arcade.key.W:
#             self.player_car.change_y = STRAIGHT_SPEED
#             # self.player_car.angle = 0
#
#         if key == arcade.key.DOWN or key == arcade.key.S:
#             self.player_car.change_y = -STRAIGHT_SPEED
#             # self.player_car.angle = 0
#
#         elif key == arcade.key.RIGHT or key == arcade.key.D:
#             self.player_car.change_x = TURN_SPEED
#             self.player_car.angle = -90
#
#         elif key == arcade.key.LEFT or key == arcade.key.A:
#             self.player_car.change_x = -TURN_SPEED
#             self.player_car.angle = 90
#
#         elif key == arcade.key.SPACE:
#             self.player_car.change_y = 0
#
#     def on_key_release(self, key, modifiers):
#
#         if key == arcade.key.UP or key == arcade.key.W:
#             self.player_car.change_y = 0
#
#         elif key == arcade.key.DOWN or key == arcade.key.S:
#             self.player_car.change_y = 0
#
#         elif key == arcade.key.RIGHT or key == arcade.key.D:
#             self.player_car.change_x = 0
#             self.player_car.angle = 0
#
#         elif key == arcade.key.LEFT or key == arcade.key.A:
#             self.player_car.change_x = 0
#             self.player_car.angle = 0
#
#         elif key == arcade.key.SPACE:
#             self.player_car.change_y = 0
#
#
# def main():
#     window = arcade.Window(title='PythonRace', fullscreen=True)
#     start_view = StartWindow()
#     window.show_view(start_view)
#     arcade.run()
#
#
# main()
#
# #         self.flashlight_list = arcade.SpriteList()
# #         flashlight = Flashlight("textures/lamp.png", 3)
# #         flashlight.center_x = SCREEN_WIDTH / 2 + 770
# #         flashlight.center_y = SCREEN_HEIGHT / 2 + 300
# #         flashlight.angle = -90
# #         self.flashlight_list.append(flashlight)
# #
# #         flashlight = Flashlight("textures/lamp.png", 3)
# #         flashlight.center_x = SCREEN_WIDTH / 2 + 770
# #         flashlight.center_y = SCREEN_HEIGHT / 2 - 300
# #         flashlight.angle = -90
# #         self.flashlight_list.append(flashlight)
# #
# #         flashlight = Flashlight("textures/lamp.png", 3)
# #         flashlight.center_x = SCREEN_WIDTH / 2 - 770
# #         flashlight.center_y = SCREEN_HEIGHT / 2 - 300
# #         flashlight.angle = 90
# #         self.flashlight_list.append(flashlight)
# #
# #         flashlight = Flashlight("textures/lamp.png", 3)
# #         flashlight.center_x = SCREEN_WIDTH / 2 - 770
# #         flashlight.center_y = SCREEN_HEIGHT / 2 + 300
# #         flashlight.angle = 90
# #         self.flashlight_list.append(flashlight)


"""
Show how to use lights.

.. note:: This uses features from the upcoming version 2.4. The API for these
          functions may still change. To use, you will need to install one of the
          pre-release packages, or install via GitHub.

Artwork from http://kenney.nl

"""

# import arcade
# import pyglet
# import pyglet.media as media
# class Music(arcade.Window):
#
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#
#         self.driving_music = arcade.load_sound("music/engine_sound.mp3")
#         self.silence_sound = arcade.load_sound("music/silence-sound.mp3")
#
#     def on_key_press(self, key: int, modifiers: int):
#         if key == arcade.key.SPACE:
#             arcade.play_sound(self.driving_music)
#
#     def on_key_release(self, key: int, modifiers: int):
#         if key == arcade.key.SPACE:
#             pass
#
#
#
#
# def main():
#     window = Music(300, 300, "TEST")
#     arcade.run()
#
#
# main()


import arcade
from FirstMap import GameMap_1

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "TEST"
HERO_SIZE = 3
HERO_SPEED = 1.5
CAR_SIZE = 2.5


class StartGameWindow(arcade.View):
    def __init__(self):
        super().__init__()

        self.hero_sprite = None
        self.sprites = None
        self.background_texture = None
        self.textures = None
        self.hero_car = None
        self.cars = None

        arcade.set_background_color(arcade.color.BLACK)

        self.up_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.left_pressed = False
        self.lshift_pressed = False
        self.space_pressed = False

        self.physics_engine = None

    def setup(self):
        self.sprites = arcade.SpriteList()
        self.hero_sprite = arcade.Sprite("../../resources/sprites/humans/HERO.png", HERO_SIZE)
        self.hero_sprite.center_x = SCREEN_WIDTH / 2
        self.hero_sprite.center_y = SCREEN_HEIGHT / 2 - 450
        self.sprites.append(self.hero_sprite)

        self.cars = arcade.SpriteList()
        self.hero_car = arcade.Sprite("../../resources/sprites/cars/Mycar.png", CAR_SIZE)
        self.hero_car.center_x = SCREEN_WIDTH / 2 + 300
        self.hero_car.center_y = SCREEN_HEIGHT / 2 - 260
        self.cars.append(self.hero_car)

        self.textures = arcade.SpriteList()
        self.background_texture = arcade.Sprite("../../resources/textures/PARKING.png")
        self.background_texture.center_x = 960
        self.background_texture.center_y = 450
        self.textures.append(self.background_texture)

        self.physics_engine = arcade.PhysicsEngineSimple(self.hero_sprite, self.cars)

    def on_draw(self):
        arcade.start_render()
        self.textures.draw()
        self.sprites.draw()
        self.cars.draw()

        arcade.draw_text("Подойди к CyberTruck и нажмите F", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 410,
                         arcade.color.WHITE, font_size=60, anchor_x="center")

    def update(self, delta_time):
        if self.up_pressed and not self.down_pressed:
            self.hero_sprite.change_y = HERO_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.hero_sprite.change_y = -HERO_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.hero_sprite.change_x = HERO_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.hero_sprite.change_x = -HERO_SPEED
        if self.down_pressed and self.right_pressed:
            self.hero_sprite.angle = 0
        if self.up_pressed and self.left_pressed or self.up_pressed and self.right_pressed:
            self.hero_sprite.change_x = 0
        if self.left_pressed and self.down_pressed or self.right_pressed and self.down_pressed:
            self.hero_sprite.change_x = 0

        self.sprites.update()

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.up_pressed = True
            self.hero_sprite.angle = 0
        elif key == arcade.key.S:
            self.down_pressed = True
            self.hero_sprite.angle = 180
        elif key == arcade.key.A:
            self.left_pressed = True
            self.hero_sprite.angle = 90
        elif key == arcade.key.D:
            self.right_pressed = True
            self.hero_sprite.angle = -90
        if key == arcade.key.F:
            game_map_1 = GameMap_1()
            game_map_1.setup()
            self.window.show_view(game_map_1)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.up_pressed = False
            self.hero_sprite.change_y = 0
        elif key == arcade.key.S:
            self.down_pressed = False
            self.hero_sprite.change_y = 0
        elif key == arcade.key.A:
            self.left_pressed = False
            self.hero_sprite.change_x = 0
        elif key == arcade.key.D:
            self.right_pressed = False
            self.hero_sprite.change_x = 0


# def main():
#     window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     view = StartGameWindow()
#     view.setup()
#     window.show_view(view)
#     arcade.run()
#
#
# main()