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
    BLUE = (0, 0, 255)
    OFF_RED = (64, 0, 0)
    YELLOW = (255,255,0)
    GREEN = (0,255,0)
    OFF_RED = (64, 0, 0)
    BORDER_RED = (128, 0, 0)
    OFF_YELLOW = (64,64,0)
    OFF_GREEN = (0,64,0)
    OFF_BLUE = (0,0,64)

def clear_board():
    if sys.implementation.name == 'micropython':
        graphics.remove_clip()
        graphics.set_pen(BLACK)
        graphics.clear()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def displaySignal(signalState=None, debug=False):
    if signalState is None:
        return
    BLUE_MODE = True
    if debug:
        print("Next...")
    sleep_time=signalState[3]
    print(u'\033[H', end="")
    #print(u'\033[40m\u250F\u2501\u2513\033[m')
    print(u'\033]8;;http://www.yahoo.com\033\\This is a link\033]8;;\033\\\n')
    print(u'\033[40m\033[38;2;180;0;158m\u250F\u2501\u2513\033[m')
    print(u'\033[40m\u2503\033[91m' + ('\u25CF' if signalState[0] == RED else '\u25CB') + '\033[0;40m\u2503\033[m')
    print(u'\033[40m\u2503\033[93m' + ('\u25CF' if signalState[1] == YELLOW else '\u25CB') + '\033[0;40m\u2503\033[m')
    if BLUE_MODE:
        print(u'\033[40m\u2503\033[94m' + ('\u25CF' if signalState[2] == BLUE else '\u25CB') + '\033[0;40m\u2503\033[m')
    else:    
        print(u'\033[40m\u2503\033[92m' + ('\u25CF' if signalState[2] == GREEN else '\u25CB') + '\033[0;40m\u2503\033[m')
    print(u'\033[40m\u2517\u2501\u251B\033[m')
    if sys.implementation.name == 'micropython':
        graphics.set_pen(signalState[0])
        graphics.circle(16, 5, 4)
        graphics.set_pen(signalState[1])
        graphics.circle(16, 15, 4)
        graphics.set_pen(signalState[2])
        graphics.circle(16, 25, 4)
        i75.update()
    time.sleep(sleep_time)

def run_signal():
    quit = False
    print("Running Signal...")
    while not quit:
        for state in light_states:
            displaySignal(state)
    pass

#light_states = [[OFF_RED,OFF_YELLOW,GREEN,5],[OFF_RED,YELLOW,OFF_GREEN,2],[RED,OFF_YELLOW,OFF_GREEN,7]]
light_states = [
    [OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.3],
    [RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.1],[RED,OFF_YELLOW,OFF_BLUE,0.1],[OFF_RED,OFF_YELLOW,OFF_BLUE,0.4],
    [OFF_RED,OFF_YELLOW,BLUE,0.2],[RED,OFF_YELLOW,OFF_BLUE,0.2],
    [OFF_RED,OFF_YELLOW,BLUE,0.2],[RED,OFF_YELLOW,OFF_BLUE,0.2],
    [OFF_RED,OFF_YELLOW,OFF_BLUE,0.2]]

if __name__ == "__main__":
    print("Trafic signal")
    clear_board()
    displaySignal(light_states[2])
    run_signal()
