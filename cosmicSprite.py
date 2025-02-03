import time
import random
from sprite import Sprite
from LEDColorTable import LEDColorTable
from TetrisBlocks import TetrisBlocks
from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY

cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)
sprites = []

@micropython.native  # noqa: F821
def setup():
    global width, height
    width = CosmicUnicorn.WIDTH
    height = CosmicUnicorn.HEIGHT
    LEDColorTable.CreateColorTable()
    sprites.append(newSprite())

@micropython.native  # noqa: F821
def draw():
    pass

@micropython.native  # noqa: F821
def update():
    pass

# Creates a new random Tetris shape sprite for testing
def newSprite(index = 0, debug = False) -> Sprite:
    #sprite = Sprite("Block" + str(index),TetrisBlocks.RandomBlockColor(["R","B","V"]),0,random.randrange(0,10),TetrisBlocks.RandomBlockShape([TetrisBlocks.S,TetrisBlocks.Sq,TetrisBlocks.Z,TetrisBlocks.T,TetrisBlocks.L,TetrisBlocks.J]))
    sprite = Sprite("Block" + str(index),TetrisBlocks.RandomBlockColor(),0,random.randrange(0,10),TetrisBlocks.RandomBlockShape())
    sprite.setSpeed(1,0)
    if debug:
        print(sprite)
    return sprite

setup()
cu.set_brightness(0.5)

while True:

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_UP):
        cu.adjust_brightness(+0.01)

    if cu.is_pressed(CosmicUnicorn.SWITCH_BRIGHTNESS_DOWN):
        cu.adjust_brightness(-0.01)

    start = time.ticks_ms()

    draw()
    update()

    # pause for a moment (important or the USB serial device will fail)
    time.sleep(0.001)

    print("total took: {} ms".format(time.ticks_ms() - start))
    for sprite in sprites:
        print(sprite)
