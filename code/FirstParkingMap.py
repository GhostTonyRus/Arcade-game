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
        self.hero_sprite = arcade.Sprite("../resources/sprites/humans/HERO.png", HERO_SIZE)
        self.hero_sprite.center_x = SCREEN_WIDTH / 2
        self.hero_sprite.center_y = SCREEN_HEIGHT / 2 - 450
        self.sprites.append(self.hero_sprite)

        self.cars = arcade.SpriteList()
        self.hero_car = arcade.Sprite("../resources/sprites/cars/Mycar.png", CAR_SIZE)
        self.hero_car.center_x = SCREEN_WIDTH / 2 + 300
        self.hero_car.center_y = SCREEN_HEIGHT / 2 - 260
        self.cars.append(self.hero_car)

        self.textures = arcade.SpriteList()
        self.background_texture = arcade.Sprite("../resources/textures/PARKING.png")
        self.background_texture.center_x = 960
        self.background_texture.center_y = 450
        self.textures.append(self.background_texture)

        self.physics_engine = arcade.PhysicsEngineSimple(self.hero_sprite, self.cars)

    def on_draw(self):
        arcade.start_render()
        self.textures.draw()
        self.sprites.draw()
        self.cars.draw()

        arcade.draw_text("Подойди к CyberTruck и нажмите F", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 450,
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

        if self.hero_sprite.center_y > SCREEN_HEIGHT:
            self.hero_sprite.change_y = 0

        if self.hero_sprite.center_x > SCREEN_WIDTH - 180:
            self.hero_sprite.change_x = -1
        elif self.hero_sprite.center_x < HERO_SIZE + 180:
             self.hero_sprite.change_x = 1
        if self.hero_sprite.center_y > SCREEN_HEIGHT - 100:
            self.hero_sprite.change_y = -1
        elif self.hero_sprite.center_y < HERO_SIZE:
            self.hero_sprite.change_y = 1

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
