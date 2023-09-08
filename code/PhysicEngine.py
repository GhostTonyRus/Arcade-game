import arcade
import math
from arcade.experimental.lights import LightLayer
from MapObjects import Lights

WIDTH = 1920
HEIGHT = 1080
TITLE = "TEST"

PLAYER_SIZE = 2.5
PLAYER_SPEED = 10
PLAYER_BOOST_SPEED = 5
PLAYER_ANGLE_SPEED = 10

AMBIENT_COLOR = (10, 10, 10)

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.speed = 0

    def update(self):

        angle_rad = math.radians(self.angle)

        self.angle += self.change_angle
        self.change_speed = 0

        # self.center_x = self.change_x
        # self.center_y = self.center_y

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class Mygame(arcade.View):
    def __init__(self):
        super().__init__()

        self.background_sprite_list = None
        self.player_list = None
        self.player_sprite = None
        self.player_light_up_left = None
        self.player_light_up_right = None
        self.player_light_down_left = None
        self.player_light_down_right = None
        self.light_layer = None

        self.up_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.left_pressed = False
        self.lshift_pressed = False
        self.space_pressed = False

    def setup(self):
        self.background_sprite_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("sprites/cars/mycar.png", PLAYER_SIZE)
        # self.player_sprite = Player("sprites/cars/mycar.png", PLAYER_SIZE)
        self.player_sprite.center_x = WIDTH / 2
        self.player_sprite.center_y = HEIGHT / 2 - 400
        self.player_list.append(self.player_sprite)

        x = WIDTH / 2
        y = HEIGHT / 2
        background = arcade.Sprite("textures/ROAD.png")
        background.position = x, y
        self.background_sprite_list.append(background)

        self.light_layer = LightLayer(WIDTH, HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)

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

        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render()

        with self.light_layer:
            self.background_sprite_list.draw()
            self.player_list.draw()

        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

    def update(self, delta_time):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_sprite.angle = 0
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_SPEED
            self.player_sprite.angle = 0
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_SPEED
            self.player_sprite.angle = 0
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_SPEED
            self.player_sprite.angle = -90
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_SPEED
            self.player_sprite.angle = 90
        if self.up_pressed and self.lshift_pressed:
            self.player_sprite.change_y = PLAYER_BOOST_SPEED * 4
            self.player_sprite.change_x = 0
        if self.space_pressed:
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
        if self.down_pressed and self.right_pressed:
            self.player_sprite.angle = 0
        self.player_list.update()

        # ПОЗИЦИЯ МАШИНЫ
        car_poz = self.player_sprite.position

        # ПОЗИЦИЯ ПЕРЕДНИХ ФАР ПРИ ДВИЖЕНИИ ВПЕРЁД
        light_up_left = (-50, 140)
        poz_up_left_1 = car_poz[0] + light_up_left[0]
        poz_up_left_2 = car_poz[1] + light_up_left[1]
        light_poz_up_1 = (poz_up_left_1, poz_up_left_2)
        self.player_light_up_left.position = light_poz_up_1

        light_up_right = (10, 140)
        poz_up_right_1 = car_poz[0] + light_up_right[0]
        poz_up_right_2 = car_poz[1] + light_up_right[1]
        light_poz_up_2 = (poz_up_right_1, poz_up_right_2)
        self.player_light_up_right.position = light_poz_up_2

        # ПОЗИЦИЯ БОКОВЫХ ПЕРЕДНИХ ФАР ПРИ ДВИЖЕНИИ НАЛЕВО
        light_up_left_side_1 = (-130, 10)
        poz_up_left_side_1 = car_poz[0] + light_up_left_side_1[0]
        poz_up_left_side_2 = car_poz[1] + light_up_left_side_1[1]
        light_poz_up_left_side_1 = (poz_up_left_side_1, poz_up_left_side_2)
        self.player_light_up_left_side_1.position = light_poz_up_left_side_1

        light_up_left_side_2 = (-130, -40)
        poz_up_left_side_1 = car_poz[0] + light_up_left_side_2[0]
        poz_up_left_side_2 = car_poz[1] + light_up_left_side_2[1]
        light_poz_up_left_side_2 = (poz_up_left_side_1, poz_up_left_side_2)
        self.player_light_up_left_side_2.position = light_poz_up_left_side_2

        # ПОЗИЦИЯ БОКОВЫХ ПЕРЕДНИХ ФАР ПРИ ДВИЖЕНИИ НАПРАВО
        light_up_right_side_1 = (130, 40)
        poz_up_right_side_1 = car_poz[0] + light_up_right_side_1[0]
        poz_up_right_side_2 = car_poz[1] + light_up_right_side_1[1]
        light_poz_up_right_side_1 = (poz_up_right_side_1, poz_up_right_side_2)
        self.player_light_up_right_side_1.position = light_poz_up_right_side_1

        light_up_right_side_2 = (130, -10)
        poz_up_right_side_1 = car_poz[0] + light_up_right_side_2[0]
        poz_up_right_side_2 = car_poz[1] + light_up_right_side_2[1]
        light_poz_up_right_side_2 = (poz_up_right_side_1, poz_up_right_side_2)
        self.player_light_up_right_side_2.position = light_poz_up_right_side_2

        # ПОЗИЦИЯ ЗАДНИЙ ФАР ПРИ ДВИЖЕНИИ ВПЕРЁД
        light_down_left = (-50, -120)
        poz_down_left_1 = car_poz[0] + light_down_left[0]
        poz_down_left_2 = car_poz[1] + light_down_left[1]
        light_poz_down_1 = (poz_down_left_1, poz_down_left_2)
        self.player_light_down_left.position = light_poz_down_1

        light_down_right = (10, -120)
        poz_down_right_1 = car_poz[0] + light_down_right[0]
        poz_down_right_2 = car_poz[1] + light_down_right[1]
        light_poz_down_2 = (poz_down_right_1, poz_down_right_2)
        self.player_light_down_right.position = light_poz_down_2


    # def on_resize(self, width: float, height: float):
    #
    #     self.light_layer.resize(width, height)

    # УПРАВЛЕНИЕ МАШИНОЙ
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
            self.player_sprite.change_y = -PLAYER_SPEED
            self.player_sprite.angle = 0
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
        elif key == arcade.key.D:
            self.right_pressed = True
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
        elif key == arcade.key.A:
            self.left_pressed = True
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
            if self.player_light_up_left in self.light_layer and self.player_light_up_right:
                self.light_layer.remove(self.player_light_up_left)
                self.light_layer.remove(self.player_light_up_right)
        elif key == arcade.key.S:
            self.down_pressed = False
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)
        elif key == arcade.key.D:
            self.right_pressed = False
            if self.player_light_up_right_side_1 in self.light_layer and self.player_light_up_right_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_right_side_1)
                self.light_layer.remove(self.player_light_up_right_side_2)
        elif key == arcade.key.A:
            self.left_pressed = False
            if self.player_light_up_left_side_1 in self.light_layer and self.player_light_up_left_side_2 in self.light_layer:
                self.light_layer.remove(self.player_light_up_left_side_1)
                self.light_layer.remove(self.player_light_up_left_side_2)
        elif key == arcade.key.LSHIFT:
            self.lshift_pressed = False
        elif key == arcade.key.SPACE:
            self.space_pressed = False
            if self.player_light_down_left in self.light_layer and self.player_light_down_right in self.light_layer:
                self.light_layer.remove(self.player_light_down_left)
                self.light_layer.remove(self.player_light_down_right)

def main():

    window = arcade.Window(fullscreen=True)
    game_window = Mygame()
    game_window.setup()
    window.show_view(game_window)
    arcade.run()

main()

