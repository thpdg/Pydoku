import time
import sys
import os

if sys.implementation.name == 'micropython':
    from pimoroni_i2c import PimoroniI2C
    from pimoroni import HEADER_I2C_PINS  # or PICO_EXPLORER_I2C_PINS or HEADER_I2C_PINS
    from breakout_encoder_wheel import BreakoutEncoderWheel, UP, DOWN, LEFT, RIGHT, CENTRE, NUM_LEDS
    from interstate75 import Interstate75, DISPLAY_INTERSTATE75_32X32

    # Setup Interstate 75 Board
    # Setup graphics for i75 LED board
    i75 = Interstate75(display=DISPLAY_INTERSTATE75_32X32)
    graphics = i75.display
    width = i75.width
    height = i75.height

if sys.implementation.name == 'micropython':
    # Define Colors
    WHITE = graphics.create_pen(64, 64, 64)
    BLACK = graphics.create_pen(0,0,0)

    BLUE = graphics.create_pen(0, 0, 255)
    RED = graphics.create_pen(255, 0, 0)
    YELLOW = graphics.create_pen(255,255,0)
    GREEN = graphics.create_pen(0,255,0)
    OFF_RED = graphics.create_pen(64, 0, 0)
    BORDER_RED = graphics.create_pen(128, 0, 0)
    OFF_YELLOW = graphics.create_pen(64,64,0)
    OFF_GREEN = graphics.create_pen(0,64,0)
    OFF_BLUE = graphics.create_pen(0, 0, 64)
else:
    RED = (255, 0, 0)
    OFF_RED = (64, 0, 0)
    YELLOW = (255,255,0)
    GREEN = (0,255,0)
    OFF_RED = (64, 0, 0)
    BORDER_RED = (128, 0, 0)
    OFF_YELLOW = (64,64,0)
    OFF_GREEN = (0,64,0)

S_piece = [[1,0],
           [1,1],
           [0,1],
           [0,0],
           ]


def clear_board():
    if sys.implementation.name == 'micropython':
        graphics.remove_clip()
        graphics.set_pen(BLACK)
        graphics.clear()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def displayBoard(piece_list=None, debug=False):
    if debug:
        print("Next...")
    # sleep_time=signalState[3]
    # print(u'\033[H', end="")
    # print(u'\033[40m\u250F\u2501\u2513\033[m')
    # print(u'\033[40m\u2503\033[91m' + ('\u25CF' if signalState[0] == RED else '\u25CB') + '\033[0;40m\u2503\033[m')
    # print(u'\033[40m\u2503\033[93m' + ('\u25CF' if signalState[1] == YELLOW else '\u25CB') + '\033[0;40m\u2503\033[m')
    # print(u'\033[40m\u2503\033[92m' + ('\u25CF' if signalState[2] == GREEN else '\u25CB') + '\033[0;40m\u2503\033[m')
    # print(u'\033[40m\u2517\u2501\u251B\033[m')
    # if sys.implementation.name == 'micropython':
    #     graphics.set_pen(signalState[0])
    #     graphics.circle(16, 5, 4)
    #     graphics.set_pen(signalState[1])
    #     graphics.circle(16, 15, 4)
    #     graphics.set_pen(signalState[2])
    #     graphics.circle(16, 25, 4)
    #     i75.update()
    # time.sleep(sleep_time)
    

clear_board()
displayBoard()
print("Thanks!")