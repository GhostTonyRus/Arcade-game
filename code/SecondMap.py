import arcade
import arcade.gui
import random
from MapObjects import HumanBot1, HumanBot2, Line, Flashlight, PlayerCar, BotCar, Lights, Obstacles, Save
from arcade.experimental.lights import LightLayer
import AllViews


# КОНСТАНТЫ ЭКРАНА
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "NightMap"

# КОНСТАНТЫ ПАРАМЕТРОВ МАШИНЫ ИГРОКА
PLAYER_STRAIGHT_SPEED = 15
PLAYER_SIZE = 2.5
TURN_SPEED = 5
BOOST_CAR_SPEED = 5
PLAYER_MASS = 2.0

# КОНСТАНТЫ ПАРМАТЕРОВ БОТОВ ПЕШЕХДОВ
BOT_HUMAN_SPEED = 5
BOT_HUMAN_SIZE = 4
BOT_HUMAN_IN_TOTAL = 5

# КОНСТАНТЫ ПАРМАТЕРОВ МАШИНЫ ИГРОКА
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

AMBIENT_COLOR = (10, 10, 10)

# ИГРОВОЕ ОКНО
class GameMap_2(arcade.View):

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

        self.score = 0

        # УПРАВЛЕНИЕ
        self.up_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.left_pressed = False
        self.lshift_pressed = False
        self.space_pressed = False

        self.flashlight_right_1 = None

        self.player_light_up_left = None
        self.player_light_up_right = None
        self.player_light_down_left = None
        self.player_light_down_right = None
        self.light_layer = None

        self.red_bot_light_up_left = None
        self.red_bot_light_up_right = None
        self.green_bot_light_up_left = None
        self.green_bot_light_up_right = None
        self.blue_bot_light_up_left = None
        self.blue_bot_light_up_right = None
        self.black_bot_light_up_left = None
        self.black_bot_light_up_right = None
        self.truck_bot_light_up_left = None
        self.truck_bot_light_up_right = None

        self.flashlight_light_right_1 = None
        self.flashlight_light_right_2 = None
        self.flashlight_light_right_3 = None

        self.flashlight_light_left_1 = None
        self.flashlight_light_left_2 = None
        self.flashlight_light_left_3 = None

        # ПРЕПЯТСТВИЯ
        self.crack = None
        self.crack_2 = None
        self.pit = None
        self.puddle = None
        self.obstacles_list = None

    # ОСНОВНЫЕ НАСТРОЙКИ СПРАЙТОВ
    def setup(self):
        self.background_texture = arcade.SpriteList()
        self.background = arcade.Sprite("../resources/textures/ROAD_2.png")
        self.background.center_x = 960
        self.background.center_y = 530
        self.background_texture.append(self.background)

        self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)

        self.players_car_list = arcade.SpriteList()
        self.player_car_sprite = PlayerCar("../resources/sprites/cars/Mycar.png", PLAYER_SIZE)
        self.player_car_sprite.center_x = SCREEN_WIDTH / 2 + 150
        self.player_car_sprite.center_y = 200
        self.players_car_list.append(self.player_car_sprite)

        # ПЕРЕДНИЕ ФАРЫ
        self.player_light_up_left = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.player_light_up_right = Lights(0, 0, 70, arcade.color.WHITE, "soft")

        # ПЕРЕДНИЕ ФАРЫ ПРИ ПОВОРОТЕ НАЛЕВО
        self.player_light_up_left_side_1 = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.player_light_up_left_side_2 = Lights(0, 0, 70, arcade.color.WHITE, "soft")

        # ПЕРЕДНИК ФАРЫ ПРИ ПОВОРОТЕ НАПРАВО
        self.player_light_up_right_side_1 = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.player_light_up_right_side_2 = Lights(0, 0, 70, arcade.color.WHITE, "soft")

        # ЗАДНИЕ ФАРЫ
        self.player_light_down_left = Lights(0, 0, 50, arcade.color.RED, "soft")
        self.player_light_down_right = Lights(0, 0, 50, arcade.color.RED, "soft")

        #ПЕРЕДНИЕ ФАРЫ МАШИНЫ БОТОВ
        self.red_bot_light_up_left = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.red_bot_light_up_right = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.light_layer.add(self.red_bot_light_up_left)
        self.light_layer.add(self.red_bot_light_up_right)

        self.green_bot_light_up_left = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.green_bot_light_up_right = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.light_layer.add(self.green_bot_light_up_left)
        self.light_layer.add(self.green_bot_light_up_right)

        self.blue_bot_light_up_left = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.blue_bot_light_up_right = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.light_layer.add(self.blue_bot_light_up_left)
        self.light_layer.add(self.blue_bot_light_up_right)

        self.black_bot_light_up_left = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.black_bot_light_up_right = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.light_layer.add(self.black_bot_light_up_left)
        self.light_layer.add(self.black_bot_light_up_right)

        self.truck_bot_light_up_left = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        self.truck_bot_light_up_right = Lights(0, 0, 70, arcade.color.WHITE, "soft")
        # self.light_layer.add(self.truck_bot_light_up_left)
        # self.light_layer.add(self.truck_bot_light_up_right)

        #СВЕТ НА ПРАВОЙ СТОРОНЕ
        self.flashlight_light_right_1 = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        self.light_layer.add(self.flashlight_light_right_1)

        self.flashlight_light_right_2 = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        self.light_layer.add(self.flashlight_light_right_2)

        self.flashlight_light_right_3 = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        self.light_layer.add(self.flashlight_light_right_3)

        # СВЕТ НА ЛЕВОЙ СТОРОНЕ
        self.flashlight_light_left_1 = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        self.light_layer.add(self.flashlight_light_left_1)

        self.flashlight_light_left_2 = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        self.light_layer.add(self.flashlight_light_left_2)

        self.flashlight_light_left_3 = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        self.light_layer.add(self.flashlight_light_left_3)

        #СВЕТ НА ЛЕВОЙ СТОРОНЕ
        # self.flashlight_light_left = Lights(0, 0, 300, arcade.color.WHITE, "soft")
        # self.light_layer.add(self.flashlight_light_left)

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

        self.flashlight_right_1 = Flashlight("../resources/textures/lamp.png", 2.5)
        self.flashlight_right_1.center_x = SCREEN_WIDTH / 2 + 770
        self.flashlight_right_1.center_y = SCREEN_HEIGHT / 2 + 420
        self.flashlight_right_1.angle = -90
        self.flashlight_list.append(self.flashlight_right_1)

        self.flashlight_right_2 = Flashlight("../resources/textures/lamp.png", 2.5)
        self.flashlight_right_2.center_x = SCREEN_WIDTH / 2 + 770
        self.flashlight_right_2.center_y = SCREEN_HEIGHT / 2 + 20
        self.flashlight_right_2.angle = -90
        self.flashlight_list.append(self.flashlight_right_2)

        self.flashlight_right_3 = Flashlight("../resources/textures/lamp.png", 2.5)
        self.flashlight_right_3.center_x = SCREEN_WIDTH / 2 + 770
        self.flashlight_right_3.center_y = SCREEN_HEIGHT / 2 - 410
        self.flashlight_right_3.angle = -90
        self.flashlight_list.append(self.flashlight_right_3)

        self.flashlight_left_1 = Flashlight("../resources/textures/lamp.png", 2.5)
        self.flashlight_left_1.center_x = SCREEN_WIDTH / 2 - 770
        self.flashlight_left_1.center_y = SCREEN_HEIGHT / 2 + 420
        self.flashlight_left_1.angle = 90
        self.flashlight_list.append(self.flashlight_left_1)

        self.flashlight_left_2 = Flashlight("../resources/textures/lamp.png", 2.5)
        self.flashlight_left_2.center_x = SCREEN_WIDTH / 2 - 770
        self.flashlight_left_2.center_y = SCREEN_HEIGHT / 2 + 20
        self.flashlight_left_2.angle = 90
        self.flashlight_list.append(self.flashlight_left_2)

        self.flashlight_left_3 = Flashlight("../resources/textures/lamp.png", 2.5)
        self.flashlight_left_3.center_x = SCREEN_WIDTH / 2 - 770
        self.flashlight_left_3.center_y = SCREEN_HEIGHT / 2 - 410
        self.flashlight_left_3.angle = 90
        self.flashlight_list.append(self.flashlight_left_3)

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

        self.car_red_bot = BotCar("../resources/sprites/cars/Red_car.png", BOT_CAR_SIZE)
        self.car_red_bot.center_x = 300
        self.car_red_bot.center_y = SCREEN_HEIGHT / 2 + 700
        self.car_red_bot.angle = -180
        self.bot_car_list.append(self.car_red_bot)

        self.car_green_bot = BotCar("../resources/sprites/cars/Green_car.png", BOT_CAR_SIZE)
        self.car_green_bot.center_x = 830
        self.car_green_bot.center_y = SCREEN_HEIGHT / 2 + 400
        self.car_green_bot.angle = -180
        self.bot_car_list.append(self.car_green_bot)

        self.car_blue_bot = BotCar("../resources/sprites/cars/Blue_car.png", BOT_CAR_SIZE)
        self.car_blue_bot.center_x = 1350
        self.car_blue_bot.center_y = SCREEN_HEIGHT / 2 - 300
        self.car_blue_bot.angle = -180
        self.bot_car_list.append(self.car_blue_bot)

        self.car_black_bot = BotCar("../resources/sprites/cars/Black_car.png", BOT_CAR_SIZE)
        self.car_black_bot.center_x = 1650
        self.car_black_bot.center_y = SCREEN_HEIGHT / 2 - 10
        self.car_black_bot.angle = - 180
        self.bot_car_list.append(self.car_black_bot)

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

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_car_sprite, self.bot_car_list)

    # РИСУЕМ ОБЪЕКТЫ НА КАРТЕ
    def on_draw(self):
        arcade.start_render()

        with self.light_layer:
            # РИСУЕМ BACKGROUND
            self.background_texture.draw()
            # РИСУЕМ БОТОВ ПЕШЕХОДОВ
            self.bot_human_list.draw()
            # РИСУЕМ ЛИНИИ
            self.line_list.draw()
            # РИСУЕМ ПРЕПЯТСТВИЯ
            self.obstacles_list.draw()
            # РИСУЕМ БОТОВ МАШИН
            self.bot_car_list.draw()
            # РИСУЕМ МАШИНА ИГРОКА
            self.players_car_list.draw()
            # РИСУЕМ ФОНАРНЫЕ СТОЛБЫ
            self.flashlight_list.draw()

        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

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

        # ПОЗИЦИЯ МАШИНЫ
        car_poz = self.player_car_sprite.position

        # ПОЗИЦИЯ ПЕРЕДНИХ ФАР ПРИ ДВИЖЕНИИ ВПЕРЁД
        light_up_left = (-50, 160)
        poz_up_left_1 = car_poz[0] + light_up_left[0]
        poz_up_left_2 = car_poz[1] + light_up_left[1]
        light_poz_up_1 = (poz_up_left_1, poz_up_left_2)
        self.player_light_up_left.position = light_poz_up_1

        light_up_right = (40, 160)
        poz_up_right_1 = car_poz[0] + light_up_right[0]
        poz_up_right_2 = car_poz[1] + light_up_right[1]
        light_poz_up_2 = (poz_up_right_1, poz_up_right_2)
        self.player_light_up_right.position = light_poz_up_2

        # ПОЗИЦИЯ БОКОВЫХ ПЕРЕДНИХ ФАР ПРИ ДВИЖЕНИИ НАЛЕВО
        light_up_left_side_1 = (-160, 40)
        poz_up_left_side_1 = car_poz[0] + light_up_left_side_1[0]
        poz_up_left_side_2 = car_poz[1] + light_up_left_side_1[1]
        light_poz_up_left_side_1 = (poz_up_left_side_1, poz_up_left_side_2)
        self.player_light_up_left_side_1.position = light_poz_up_left_side_1

        light_up_left_side_2 = (-160, -50)
        poz_up_left_side_1 = car_poz[0] + light_up_left_side_2[0]
        poz_up_left_side_2 = car_poz[1] + light_up_left_side_2[1]
        light_poz_up_left_side_2 = (poz_up_left_side_1, poz_up_left_side_2)
        self.player_light_up_left_side_2.position = light_poz_up_left_side_2

        # ПОЗИЦИЯ БОКОВЫХ ПЕРЕДНИХ ФАР ПРИ ДВИЖЕНИИ НАПРАВО
        light_up_right_side_1 = (160, 50)
        poz_up_right_side_1 = car_poz[0] + light_up_right_side_1[0]
        poz_up_right_side_2 = car_poz[1] + light_up_right_side_1[1]
        light_poz_up_right_side_1 = (poz_up_right_side_1, poz_up_right_side_2)
        self.player_light_up_right_side_1.position = light_poz_up_right_side_1

        light_up_right_side_2 = (160, -40)
        poz_up_right_side_1 = car_poz[0] + light_up_right_side_2[0]
        poz_up_right_side_2 = car_poz[1] + light_up_right_side_2[1]
        light_poz_up_right_side_2 = (poz_up_right_side_1, poz_up_right_side_2)
        self.player_light_up_right_side_2.position = light_poz_up_right_side_2

        # ПОЗИЦИЯ ЗАДНИЙ ФАР ПРИ ДВИЖЕНИИ ВПЕРЁД
        light_down_left = (-40, -130)
        poz_down_left_1 = car_poz[0] + light_down_left[0]
        poz_down_left_2 = car_poz[1] + light_down_left[1]
        light_poz_down_1 = (poz_down_left_1, poz_down_left_2)
        self.player_light_down_left.position = light_poz_down_1

        light_down_right = (30, -130)
        poz_down_right_1 = car_poz[0] + light_down_right[0]
        poz_down_right_2 = car_poz[1] + light_down_right[1]
        light_poz_down_2 = (poz_down_right_1, poz_down_right_2)
        self.player_light_down_right.position = light_poz_down_2

        #ПЕРЕДНИЕ ФАРЫ МАШИНЫ БОТОВ

        self.red_bot_light_up_left.position = BotCar.set_light_left(self.car_red_bot, -35, -165,
                                                                    self.car_red_bot.position[0], self.car_red_bot.position[1])
        self.red_bot_light_up_right.position = BotCar.set_light_right(self.car_red_bot, 35, -165,
                                                                      self.car_red_bot.position[0], self.car_red_bot.position[1])

        self.green_bot_light_up_left.position = BotCar.set_light_left(self.car_green_bot, -35, -165,
                                                                    self.car_green_bot.position[0], self.car_green_bot.position[1])
        self.green_bot_light_up_right.position = BotCar.set_light_right(self.car_green_bot, 35, -165,
                                                                      self.car_green_bot.position[0], self.car_green_bot.position[1])

        self.blue_bot_light_up_left.position = BotCar.set_light_left(self.car_blue_bot, -35, -165,
                                                                      self.car_blue_bot.position[0], self.car_blue_bot.position[1])
        self.blue_bot_light_up_right.position = BotCar.set_light_right(self.car_blue_bot, 35, -165,
                                                                        self.car_blue_bot.position[0], self.car_blue_bot.position[1])

        self.black_bot_light_up_left.position = BotCar.set_light_left(self.car_black_bot, -35, -165,
                                                                self.car_black_bot.position[0], self.car_black_bot.position[1])
        self.black_bot_light_up_right.position = BotCar.set_light_right(self.car_black_bot, 35, -165,
                                                                  self.car_black_bot.position[0], self.car_black_bot.position[1])

        #СВЕТ ПО ПРАВОЙ СТОРОНЕ
        self.flashlight_light_right_1.position = Flashlight.set_light(self.flashlight_right_1, -200, 0,
                                                                      self.flashlight_right_1.position[0], self.flashlight_right_1.position[1])

        self.flashlight_light_right_2.position = Flashlight.set_light(self.flashlight_right_2, -200, 0,
                                                                      self.flashlight_right_2.position[0], self.flashlight_right_2.position[1])

        self.flashlight_light_right_3.position = Flashlight.set_light(self.flashlight_right_3, -200, 0,
                                                                      self.flashlight_right_3.position[0], self.flashlight_right_3.position[1])

        # СВЕТ ПО ЛЕВОЙ СТОРОНЕ
        self.flashlight_light_left_1.position = Flashlight.set_light(self.flashlight_left_1, 200, 0,
                                                                      self.flashlight_left_1.position[0], self.flashlight_left_1.position[1])

        self.flashlight_light_left_2.position = Flashlight.set_light(self.flashlight_left_2, 200, 0,
                                                                     self.flashlight_left_2.position[0], self.flashlight_left_2.position[1])

        self.flashlight_light_left_3.position = Flashlight.set_light(self.flashlight_left_3, 200, 0,
                                                                     self.flashlight_left_3.position[0], self.flashlight_left_3.position[1])

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
            self.window.show_view(end_view)

        for bot_hit in bot_hits:
            end_view = AllViews.GameOverWindow()
            end_view.setup()
            self.window.show_view(end_view)

        for obs_hit in obs_hits:
            self.player_car_sprite.angle = random.randint(0, 360)
            self.player_car_sprite.change_x = random.randint(-3, 3)
            self.player_car_sprite.change_y = random.randint(-3, 3)

    # БЛКОКИ УПАРВЛЕНИЯ МАШИНОЙ
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.up_pressed = True
            if self.player_light_up_left in self.light_layer and self.player_light_up_right in self.light_layer:
                self.light_layer.remove(self.player_light_up_left)
                self.light_layer.remove(self.player_light_up_right)
            else:
                self.light_layer.add(self.player_light_up_left)
                self.light_layer.add(self.player_light_up_right)
            if self.player_light_up_left_side_1 in self.light_layer and self.player_light_up_left_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_left_side_1)
                self.light_layer.remove(self.player_light_up_left_side_2)
            if self.player_light_up_right_side_1 in self.light_layer and self.player_light_up_right_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_right_side_1)
                self.light_layer.remove(self.player_light_up_right_side_2)
        elif key == arcade.key.S:
            self.down_pressed = True
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
            else:
                self.light_layer.add(self.player_light_down_left)
                self.light_layer.add(self.player_light_down_right)
            if self.player_light_up_left_side_1 in self.light_layer and self.player_light_up_left_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_left_side_1)
                self.light_layer.remove(self.player_light_up_left_side_2)
            if self.player_light_up_right_side_1 in self.light_layer and self.player_light_up_right_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_right_side_1)
                self.light_layer.remove(self.player_light_up_right_side_2)
        elif key == arcade.key.A:
            self.right_pressed = True
            if self.player_light_up_left_side_1 in self.light_layer and self.player_light_up_left_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_left_side_1)
                self.light_layer.remove(self.player_light_up_left_side_2)
            else:
                self.light_layer.add(self.player_light_up_left_side_1)
                self.light_layer.add(self.player_light_up_left_side_2)
            if self.player_light_up_left in self.light_layer and self.player_light_up_right in self.light_layer:
                self.light_layer.remove(self.player_light_up_left)
                self.light_layer.remove(self.player_light_up_right)
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
            if self.player_light_up_right_side_1 in self.light_layer and self.player_light_up_right_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_right_side_1)
                self.light_layer.remove(self.player_light_up_right_side_2)
        elif key == arcade.key.D:
            self.left_pressed = True
            if self.player_light_up_right_side_1 in self.light_layer and self.player_light_up_right_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_right_side_1)
                self.light_layer.remove(self.player_light_up_right_side_2)
            else:
                self.light_layer.add(self.player_light_up_right_side_1)
                self.light_layer.add(self.player_light_up_right_side_2)
            if self.player_light_up_left in self.light_layer and self.player_light_up_right in self.light_layer:
                self.light_layer.remove(self.player_light_up_left)
                self.light_layer.remove(self.player_light_up_right)
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
            if self.player_light_up_left_side_1 in self.light_layer and self.player_light_up_left_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_left_side_1)
                self.light_layer.remove(self.player_light_up_left_side_2)
        elif key == arcade.key.LSHIFT:
            self.lshift_pressed = True
        elif key == arcade.key.SPACE:
            self.space_pressed = True
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
            else:
                self.light_layer.add(self.player_light_down_left)
                self.light_layer.add(self.player_light_down_right)
        elif key == arcade.key.L:
            if self.player_light_up_left in self.light_layer and self.player_light_up_right in self.light_layer:
                self.light_layer.remove(self.player_light_up_left)
                self.light_layer.remove(self.player_light_up_right)
            else:
                self.light_layer.add(self.player_light_up_left)
                self.light_layer.add(self.player_light_up_right)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.up_pressed = False
            self.player_car_sprite.change_y = 0
            if self.player_light_up_left in self.light_layer and self.player_light_up_right:
                self.light_layer.remove(self.player_light_up_left)
                self.light_layer.remove(self.player_light_up_right)
        elif key == arcade.key.S:
            self.down_pressed = False
            self.player_car_sprite.change_y = 0
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
        elif key == arcade.key.A:
            self.right_pressed = False
            self.player_car_sprite.change_x = 0
            if self.player_light_up_left_side_1 in self.light_layer and self.player_light_up_left_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_left_side_1)
                self.light_layer.remove(self.player_light_up_left_side_2)
        elif key == arcade.key.D:
            self.left_pressed = False
            self.player_car_sprite.change_x = 0
            if self.player_light_up_right_side_1 in self.light_layer and self.player_light_up_right_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_right_side_1)
                self.light_layer.remove(self.player_light_up_right_side_2)
        elif key == arcade.key.LSHIFT:
            self.lshift_pressed = False
        elif key == arcade.key.SPACE:
            self.space_pressed = False
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
