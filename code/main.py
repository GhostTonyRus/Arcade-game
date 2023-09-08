from AllViews import StartWindow
import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Race"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, title=SCREEN_TITLE, fullscreen=False)
    start_view = StartWindow()
    window.show_view(start_view)
    arcade.run()


main()
