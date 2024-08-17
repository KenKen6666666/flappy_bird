import os

"""
Constants
"""
BACKGROUND_SCALE = 1.5
BIRD_SCALE = 1.1

CAPTION = "Flappy Bird"
FPS = 75
SCREEN_WIDTH = 288 * BACKGROUND_SCALE
SCREEN_HEIGHT = 512 * BACKGROUND_SCALE

# images size related
BASE_WIDTH = 336 * BACKGROUND_SCALE
BASE_HEIGHT = 112 * BACKGROUND_SCALE
PIPE_WIDTH = 52 * BACKGROUND_SCALE
PIPE_HEIGHT = 320 * BACKGROUND_SCALE
BIRD_WIDTH = 34 * BIRD_SCALE
BIRD_HEIGHT = 24 * BIRD_SCALE
NUMBER_WIDTH = 24 * BACKGROUND_SCALE
NUMBER_HEIGHT = 36 * BACKGROUND_SCALE
GAME_OVER_WIDTH = 288 * BACKGROUND_SCALE
GAME_OVER_HEIGHT = 48 * BACKGROUND_SCALE

# images paths
CURRENT_WORKINGDIR_PATH = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_IMG_PATH = os.path.join(CURRENT_WORKINGDIR_PATH, "img", "background.png")

BASE_IMG_PATH = os.path.join(CURRENT_WORKINGDIR_PATH, "img", "base.png")
PIPE_IMG_PATH = os.path.join(CURRENT_WORKINGDIR_PATH, "img", "pipe-green.png")

BIRD_IMG_PATHS = (
    os.path.join(CURRENT_WORKINGDIR_PATH, "img", "bluebird-downflap.png"),
    os.path.join(CURRENT_WORKINGDIR_PATH, "img", "bluebird-midflap.png"),
    os.path.join(CURRENT_WORKINGDIR_PATH, "img", "bluebird-upflap.png"),
    os.path.join(CURRENT_WORKINGDIR_PATH, "img", "bluebird-midflap.png"),
)

NUMBER_IMG_PATHS = (
    os.path.join(CURRENT_WORKINGDIR_PATH, "img", "numbers", f"{i}.png")
    for i in range(10)
)

GAMEOVER_IMG_PATH = os.path.join(CURRENT_WORKINGDIR_PATH, "img", "gameover.png")

BASE_SCROLLING_SPEED = 2


HEIGHT_LIMIT = SCREEN_HEIGHT - BASE_HEIGHT