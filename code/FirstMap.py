import arcade
import arcade.gui
import random
from MapObjects import HumanBot1, HumanBot2, Line, Flashlight, PlayerCar, BotCar, Obstacles, Save
import AllViews


# КОНСТАНТЫ ЭКРАНА
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "DayMap"
MARGIN = 20

# КОНСТАНТЫ ПАРАМЕТРОВ МАШИНЫ ИГРОКА
PLAYER_STRAIGHT_SPEED = 15# 10
TURN_SPEED = 5
PLAYER_SIZE = 2.5
BOOST_CAR_SPEED = 5
PLAYER_MASS = 2.0

# КОНСТАНТЫ ПАРМАТЕРОВ БОТОВ ПЕШЕХДОВ
BOT_HUMAN_SPEED = 5
BOT_HUMAN_SIZE = 4
BOT_HUMAN_IN_TOTAL = 10

# КОНСТАНТЫ ПАРМАТЕРОВ МАШИНЫ БОТОВ
BOT_CAR_SPEED = 15
BOT_CAR_SIZE = 2.5
BOT_CAR_IN_TOTAL = 8
BOT_RED_CAR_IN_TOTAL = 2
BOT_GREEN_CAR_IN_TOTAL = 2
BOT_BLUE_CAR_IN_TOTAL = 2
BOT_BLACK_CAR_IN_TOTAL = 2

# КОНСТАНТЫ ПАРМАТЕРОВ ЛИНИЙ
LINE_IN_TOTAL = 4
LINE_SIZE = 2

# КОНСТАНТЫ ПРЕПЯТСТВИЙ
OBSTACLES_SIZE_1 = 3
OBSTACLES_SIZE_2 = 4

# СЧЁТ
SCORE = 0

# ИГРОВОЕ ОКНО
class GameMap_1(arcade.View):
    
    def __init__(self):
        super().__init__()

        self.window.set_mouse_visible(False)

        self.flashlight = None

        self.players_car_list = None

        self.bot_human_list = None

        self.background = None

        self.player_car_sprite = None

        self.background_texture = None

        self.line_list = None

        self.flashlight_list = None

        self.physics_engine = None

        self.bot_car = None
        self.bot_car_list = None

        self.smoke_list = None
        self.smoke = None

        self.score = 0

        # УПРАВЛЕНИЕ
        self.up_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.left_pressed = False
        self.lshift_pressed = False
        self.space_pressed = False

        # ПРЕПЯТСТВИЯ
        self.crack = None
        self.crack_2 = None
        self.pit = None
        self.puddle = None
        self.obstacles_list = None

        # МУЗЫКА
        self.driving_music = arcade.load_sound("../resources/music/drive_1.mp3")

        # СОХРАНЕНИЕ РЕЗУЛЬТАТА
        self.save_score = None

    # ОСНОВНЫЕ НАСТРОЙКИ СПРАЙТОВ
    def setup(self):
        self.background_texture = arcade.SpriteList()
        self.background = arcade.Sprite("../resources/textures/ROAD_2.png")
        self.background.center_x = 960
        self.background.center_y = 530
        self.background_texture.append(self.background)

        self.players_car_list = arcade.SpriteList()
        self.player_car_sprite = PlayerCar("../resources/sprites/cars/Mycar.png", PLAYER_SIZE)
        self.player_car_sprite.center_x = SCREEN_WIDTH / 2 + 150
        self.player_car_sprite.center_y = 200
        self.players_car_list.append(self.player_car_sprite)

        self.bot_human_list = arcade.SpriteList()

        for human_1 in range(BOT_HUMAN_IN_TOTAL):
            human_1 = HumanBot1("../resources/sprites/humans/Human_bot_yellow.png", BOT_HUMAN_SIZE)
            human_1.center_x = random.randrange(20, 100)
            human_1.center_y = random.randrange(SCREEN_HEIGHT + 10)
            self.bot_human_list.append(human_1)

        for human_2 in range(BOT_HUMAN_IN_TOTAL):
            human_2 = HumanBot2("../resources/sprites/humans/Human_bot_2.png", BOT_HUMAN_SIZE)
            human_2.center_x = random.randrange(1800, 1850)
            human_2.center_y = random.randrange(SCREEN_HEIGHT + 10)

            self.bot_human_list.append(human_2)

        self.line_list = arcade.SpriteList()

        # ВЕРХНИЕ 1 ДВЕ ЛИНИИ
        # СЛЕВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 440
        line.center_y = 1164
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 700
        line.center_y = 1164
        self.line_list.append(line)

        # СПРАВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1210
        line.center_y = 1164
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1480
        line.center_y = 1164
        self.line_list.append(line)

        # ВЕРХНИЕ 2 ДВЕ ЛИНИИ
        # СЛЕВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 440
        line.center_y = 864
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 700
        line.center_y = 864
        self.line_list.append(line)

        # СПРАВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1210
        line.center_y = 864
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1480
        line.center_y = 864
        self.line_list.append(line)

        # ВЕРХНИЕ 3 ДВЕ ЛИНИИ
        # СЛЕВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 440
        line.center_y = SCREEN_HEIGHT / 2 + 10
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 700
        line.center_y = SCREEN_HEIGHT / 2 + 10
        self.line_list.append(line)

        # СПРАВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1210
        line.center_y = SCREEN_HEIGHT / 2 + 10
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1480
        line.center_y = SCREEN_HEIGHT / 2 + 10
        self.line_list.append(line)

        # ВЕРХНИЕ 4 ДВЕ ЛИНИИ
        # СЛЕВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 700
        line.center_y = SCREEN_HEIGHT / 5 + 20
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 440
        line.center_y = SCREEN_HEIGHT / 5 + 20
        self.line_list.append(line)

        # СПРАВА
        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1210
        line.center_y = SCREEN_HEIGHT / 5 + 20
        self.line_list.append(line)

        line = Line("../resources/textures/LINE.png", 1)
        line.center_x = 1480
        line.center_y = SCREEN_HEIGHT / 5 + 20
        self.line_list.append(line)

        # ФОНРИ
        self.flashlight_list = arcade.SpriteList()
        flashlight = Flashlight("../resources/textures/lamp.png", 2.5)
        flashlight.center_x = SCREEN_WIDTH / 2 + 770
        flashlight.center_y = SCREEN_HEIGHT / 2 + 420
        flashlight.angle = -90
        self.flashlight_list.append(flashlight)

        flashlight = Flashlight("../resources/textures/lamp.png", 2.5)
        flashlight.center_x = SCREEN_WIDTH / 2 + 770
        flashlight.center_y = SCREEN_HEIGHT / 2 + 20
        flashlight.angle = -90
        self.flashlight_list.append(flashlight)

        flashlight = Flashlight("../resources/textures/lamp.png", 2.5)
        flashlight.center_x = SCREEN_WIDTH / 2 + 770
        flashlight.center_y = SCREEN_HEIGHT / 2 - 410
        flashlight.angle = -90
        self.flashlight_list.append(flashlight)

        flashlight = Flashlight("../resources/textures/lamp.png", 2.5)
        flashlight.center_x = SCREEN_WIDTH / 2 - 770
        flashlight.center_y = SCREEN_HEIGHT / 2 + 420
        flashlight.angle = 90
        self.flashlight_list.append(flashlight)

        flashlight = Flashlight("../resources/textures/lamp.png", 2.5)
        flashlight.center_x = SCREEN_WIDTH / 2 - 770
        flashlight.center_y = SCREEN_HEIGHT / 2 + 20
        flashlight.angle = 90
        self.flashlight_list.append(flashlight)

        flashlight = Flashlight("../resources/textures/lamp.png", 2.5)
        flashlight.center_x = SCREEN_WIDTH / 2 - 770
        flashlight.center_y = SCREEN_HEIGHT / 2 - 410
        flashlight.angle = 90
        self.flashlight_list.append(flashlight)

        # СПАВН МАШИН
        self.bot_car_list = arcade.SpriteList()

        # for car_red_bot in range(BOT_RED_CAR_IN_TOTAL):
        #     y_poz = random.randint(300, 900)
        #     car_red_bot = BotCar("sprites/cars/Red_car.png", BOT_CAR_SIZE)
        #     car_red_bot.center_x = 300
        #     car_red_bot.center_y = y_poz + 300
        #     car_red_bot.angle = -180
        #     self.bot_car_list.append(car_red_bot)
        #
        # for car_black_bot in range(BOT_BLACK_CAR_IN_TOTAL):
        #     y_poz = random.randint(300, 900)
        #     car_black_bot = BotCar("sprites/cars/Black_car.png", BOT_CAR_SIZE)
        #     car_black_bot.center_x = 300
        #     car_black_bot.center_y = y_poz + 300
        #     car_black_bot.angle = -180
        #     self.bot_car_list.append(car_black_bot)

        car_red_bot = BotCar("../resources/sprites/cars/Red_car.png", BOT_CAR_SIZE)
        car_red_bot.center_x = 300
        car_red_bot.center_y = SCREEN_HEIGHT / 2 + 700
        car_red_bot.angle = -180
        self.bot_car_list.append(car_red_bot)

        car_green_bot = BotCar("../resources/sprites/cars/Green_car.png", BOT_CAR_SIZE)
        car_green_bot.center_x = 830
        car_green_bot.center_y = SCREEN_HEIGHT / 2 + 400
        car_green_bot.angle = -180
        self.bot_car_list.append(car_green_bot)

        car_blue_bot = BotCar("../resources/sprites/cars/Blue_car.png", BOT_CAR_SIZE)
        car_blue_bot.center_x = 1350
        car_blue_bot.center_y = SCREEN_HEIGHT / 2 - 300
        car_blue_bot.angle = -180
        self.bot_car_list.append(car_blue_bot)

        car_black_bot = BotCar("../resources/sprites/cars/Black_car.png", BOT_CAR_SIZE)
        car_black_bot.center_x = 1650
        car_black_bot.center_y = SCREEN_HEIGHT / 2 - 10
        car_black_bot.angle = - 180
        self.bot_car_list.append(car_black_bot)

        # car_truck_bot = BotCar("sprites/cars/TRUCK.png", BOT_CAR_SIZE)
        # car_red_bot.center_x = 1800
        # car_truck_bot.center_y = SCREEN_HEIGHT / 2 - 100
        # self.bot_car_list.append(car_truck_bot)

        self.player_car_sprite.angle = 0

        self.obstacles_list = arcade.SpriteList()

        crack = Obstacles("../resources/textures/crack.png", OBSTACLES_SIZE_1)
        crack.center_x = 300
        crack.center_y = SCREEN_HEIGHT / 2 - 100
        self.obstacles_list.append(crack)

        crack_2 = Obstacles("../resources/textures/crack_2.png", OBSTACLES_SIZE_2)
        crack_2.center_x = 840
        crack_2.center_y = SCREEN_HEIGHT / 2 - 300
        self.obstacles_list.append(crack_2)

        pit = Obstacles("../resources/textures/pit.png", OBSTACLES_SIZE_2)
        pit.center_x = 1090
        pit.center_y = SCREEN_HEIGHT / 2 - 600
        self.obstacles_list.append(pit)

        puddle = Obstacles("../resources/textures/puddle.png", OBSTACLES_SIZE_2)
        puddle.center_x = 1620
        puddle.center_y = SCREEN_HEIGHT / 2 - 900
        self.obstacles_list.append(puddle)

        self.smoke_list = arcade.SpriteList()

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_car_sprite, self.bot_car_list)


    # РИСУЕМ ОБЪЕКТЫ НА КАРТЕ
    def on_draw(self):
        arcade.start_render()

        # РИСУЕМ BACKGROUND
        self.background_texture.draw()

        # РИСУЕМ БОТОВ ПЕШЕХОДОВ
        self.bot_human_list.draw()

        # РИСУЕМ БОТОВ МАШИН
        self.line_list.draw()

        # РИСУЕМ ПРЕПЯТСТВИЯ
        self.obstacles_list.draw()

        # РИСУЕМ ДЫМ
        self.smoke_list.draw()

        # РИСУЕМ ЛИНИИ
        self.bot_car_list.draw()

        # РИСУЕМ МАШИНА ИГРОКА
        self.players_car_list.draw()

        # РИСУЕМ ФОНАРНЫЕ СТОЛБЫ
        self.flashlight_list.draw()

        # СЧЁТ
        self.score_info = f"Счёт: {'%.2f' % self.score}"
        arcade.draw_text(self.score_info, 1520, 1000, arcade.color.WHITE, 39)

        self.save_score = Save()
        self.save_score.save(self.score)


    def update(self, delta_time):

        # self.player_car_sprite.change_x = 0
        # self.player_car_sprite.change_y = 0
        self.player_car_sprite.angle = 0
        if self.up_pressed and not self.down_pressed:
            self.player_car_sprite.change_y = PLAYER_STRAIGHT_SPEED
            self.player_car_sprite.angle = 0
        elif self.down_pressed and not self.up_pressed:
            self.player_car_sprite.change_y = -PLAYER_STRAIGHT_SPEED
            self.player_car_sprite.angle = 0
        elif self.right_pressed and not self.left_pressed:
            self.player_car_sprite.change_x = -PLAYER_STRAIGHT_SPEED
            self.player_car_sprite.angle = 90
        elif self.left_pressed and not self.right_pressed:
            self.player_car_sprite.change_x = PLAYER_STRAIGHT_SPEED
            self.player_car_sprite.angle = -90
        if self.up_pressed and self.lshift_pressed:
            self.player_car_sprite.change_y = BOOST_CAR_SPEED * 4
            self.player_car_sprite.change_x = 0
        if self.space_pressed:
            self.player_car_sprite.change_x = 0
            self.player_car_sprite.change_y = 0
        if self.down_pressed and self.right_pressed:
            self.player_car_sprite.angle = 0
        if self.up_pressed and self.left_pressed or self.up_pressed and self.right_pressed:
            self.player_car_sprite.change_x = 0
        if self.left_pressed and self.down_pressed or self.right_pressed and self.down_pressed:
            self.player_car_sprite.change_x = 0
        self.player_car_sprite.update()

        # ОБНОВЛЯЕМ ДВИЖОК
        self.physics_engine.update()

        # ОБНОВЛЯЕМ МАШИНУ ИГРОКА
        self.player_car_sprite.update()

        # ОБНОВЛЯЕМ БОТОВ ПЕШЕХОДОВ
        self.bot_human_list.update()

        # ОБНОВЛЯЕМ ЛИНИИ
        self.line_list.update()

        # ОБНОВЛЯЕМ ФОНАРНЫЕ СТОЛБЫ
        self.flashlight_list.update()

        # ОБНОВЛЯЕМ МАШИНЫ БОТОВ
        self.bot_car_list.update()

        # ОБНОВЛЕНИЕ СЧЁТА
        self.score += delta_time

        # ОБНОВЛЕНИЕ ПРЕПЯТСТВИЙ
        self.obstacles_list.update()

        # СТОЛКНОВЕНИЕ С МАШИНАМИ
        car_hits = arcade.check_for_collision_with_list(self.player_car_sprite, self.bot_car_list)

        # СТОЛКНОВЕНИЕ С ПЕШЕХОДАМИ
        bot_hits = arcade.check_for_collision_with_list(self.player_car_sprite, self.bot_human_list)

        # СТОЛКНОВЕНИЕ С ПРЕПЯТСТВИЯМИ
        obs_hits = arcade.check_for_collision_with_list(self.player_car_sprite, self.obstacles_list)

        for car_hit in car_hits:
            end_view = AllViews.GameOverWindow()
            end_view.setup()
            #arcade.stop_sound(self.driving_music)
            self.window.show_view(end_view)

        for bot_hit in bot_hits:
            end_view = AllViews.GameOverWindow()
            end_view.setup()
            #arcade.stop_sound(self.driving_music)
            self.window.show_view(end_view)

        for obs_hit in obs_hits:
            self.player_car_sprite.angle = random.randint(0, 360)
            self.player_car_sprite.change_x = random.randint(-3, 3)
            self.player_car_sprite.change_y = random.randint(-3, 3)

    # БЛКОКИ УПАРВЛЕНИЯ МАШИНОЙ
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.up_pressed = True
            #arcade.play_sound(self.driving_music)
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.right_pressed = True
        elif key == arcade.key.D:
            self.left_pressed = True
        elif key == arcade.key.LSHIFT:
            self.lshift_pressed = True
        elif key == arcade.key.SPACE:
            self.space_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.up_pressed = False
            self.player_car_sprite.change_y = 0
        elif key == arcade.key.S:
            self.down_pressed = False
            self.player_car_sprite.change_y = 0
        elif key == arcade.key.A:
            self.right_pressed = False
            self.player_car_sprite.change_x = 0
        elif key == arcade.key.D:
            self.left_pressed = False
            self.player_car_sprite.change_x = 0
        elif key == arcade.key.LSHIFT:
            self.lshift_pressed = False
        elif key == arcade.key.SPACE:
            self.space_pressed = False
