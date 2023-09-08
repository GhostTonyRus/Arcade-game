import arcade
import random
import shelve
from arcade.experimental.lights import Light

# КОНСТАНТЫ ЭКРАНА
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "FirstTest"
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


class Lights(Light):
    def __init__(self, center_x, center_y, radius, color, mode):
        super().__init__(center_x, center_y, radius, color, mode)

# КЛАСС БОТОВ ПЕШЕХОДОВ ИДУЩИХ ПО ЛЕВОЙ СТОРОНЕ
class HumanBot1(arcade.Sprite):


    # ВОЗВРАТ ПОЗИЦИИ
    def reset_pos(self):

        if self.center_y < -100:
            self.center_y = 1090
            self.center_x = random.randrange(20, 80)

    # ДВИЖЕНИЕ
    def update(self):

        self.center_y -= 1

        self.reset_pos()

# КЛАСС БОТОВ ПЕШЕХОДОВ ИДУЩИХ ПО ПРАВОЙ СТОРОНЕ
class HumanBot2(arcade.Sprite):


    # ВОЗВРАТ ПОЗИЦИИ
    def reset_pos(self):

        if self.center_y > SCREEN_HEIGHT + 100:
            self.center_y = -1
            self.center_x = random.randrange(1850, 1870)

    # ДВИЖЕНИЕ
    def update(self):

        self.center_y += 1

        self.reset_pos()

# КЛАСС ЛИНИЙ
class Line(arcade.Sprite):


    # ВОЗВРАТ ПОЗИЦИИ
    def reset_pos(self):

        if self.center_y < -100:
            self.center_y = 1200

    # ДВИЖЕНИЕ
    def update(self):

        self.center_y -= 4

        self.reset_pos()

class Flashlight(arcade.Sprite):

    def reset_pos(self):
        if self.center_y < -100:
            self.center_y = 1100

    def update(self):

        self.center_y -= 4

        self.reset_pos()

    def set_light(self, x_poz_light, y_poz_light, x_poz_flashlight, y_poz_flashlight):
        light_poz = (x_poz_light, y_poz_light)
        flashlight_poz = (x_poz_flashlight, y_poz_flashlight)
        poz_light_x = (light_poz[0] + flashlight_poz[0])
        poz_light_y = (light_poz[1] + flashlight_poz[1])
        flashlight_poz = (poz_light_x, poz_light_y)

        return flashlight_poz
# КЛАСС МАШИНЫ ИГРОКА
class PlayerCar(arcade.Sprite):


    # ВОЗВРАТ ПОЗИЦИИ
    def update(self):

        if self.center_y > SCREEN_HEIGHT - 130:
            self.change_y = -1

        if self.center_y < PLAYER_SIZE + 130:
            self.change_y = 1

        if self.center_x > SCREEN_WIDTH - 290:
            self.change_x = -1

        if self.center_x < PLAYER_SIZE + 290:
            self.change_x = 1

# ДЫМ
class Smoke(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


# КЛАСС МАШИН БОТОВ
class BotCar(arcade.Sprite):

    # ВОЗВРАТ ПОЗИЦИИ
    def reset_pos(self):
        x_poz = [300, 570, 840, 1090, 1350, 1620,]

        if self.center_y < -100:
            self.center_y = 1200
            self.center_x = random.choice(x_poz)

    # ДВИЖЕНИЕ
    def update(self):

        #speed = random.randint(10, 20)

        #self.center_y -= random.randint(10, 20)
        self.center_y -= 22
        self.reset_pos()

    def set_light_left(self, x_poz_light, y_poz_light, x_poz_car, y_poz_car):
        light_up_left = (x_poz_light, y_poz_light)
        car_position = (x_poz_car, y_poz_car)
        poz_light_up_left_bot_1 = (light_up_left[0] + car_position[0])
        poz_light_up_left_bot_2 = (light_up_left[1] + car_position[1])
        light_up_left = (poz_light_up_left_bot_1, poz_light_up_left_bot_2)

        return light_up_left

    def set_light_right(self, x_poz_light, y_poz_light, x_poz_car, y_poz_car):
        light_up_right = (x_poz_light, y_poz_light)
        car_position = (x_poz_car, y_poz_car)
        poz_light_up_right_bot_1 = (light_up_right[0] + car_position[0])
        poz_light_up_right_bot_2 = (light_up_right[1] + car_position[1])
        light_up_right = (poz_light_up_right_bot_1, poz_light_up_right_bot_2)

        return light_up_right

class Obstacles(arcade.Sprite):

    def reset_pos(self):

        x_poz = [300, 570, 840, 1090, 1350, 1620,]
        if self.center_y < -100:
            self.center_y = 1200
            self.center_x = random.choice(x_poz)


    def update(self):
        self.center_y -= 10
        self.reset_pos()


class Save:
    def __init__(self):
        self.filename = "../resources/saves/save_distance.txt"

    def save(self, distance):
        try:
            with open(self.filename, "w") as file:
                file.write(str(distance))
        except FileNotFoundError:
            print("Ошибка")

        return distance

    def GetDist(self):
        try:
            with open(self.filename, "r") as file:
                dist = file.read()
        except FileNotFoundError:
            print("Ошибка")

        return dist

    # def __init__(self, result):
    #     self.result = result
    #     self.save_file = "resources/saves/save_distance"
    #
    # def save_dist(self):
    #
    #     with shelve.open(self.save_file) as save:
    #         save["dist"] = self.result
    #
    # def print_score(self):
    #     with shelve.open(self.save_file) as save:
    #         save["dist"] = self.result
    #         for value in save.values():
    #             return value




"""
    1. Сначала пишим произвольную позицию света в 1 переменной;
    2. Создаём переменную со значеним позиции мащины по координате X + произвольная
    позиция света по X;
    3. Создаём переменную со значеним позиции мащины по координате Y + произвольная
    позиция света по Y;
    4. Перезаписываем 1 переменную с аолучившимися значениями по X и по Y;
    5. Зписываем в позицию света перезаписанную переменную.
"""