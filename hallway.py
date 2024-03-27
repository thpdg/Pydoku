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
    GREY = graphics.create_pen(169,168,169)
    MX_BLUE = graphics.create_pen(62,141,221)
    MX2_BLUE = graphics.create_pen(87,141,218)
    FANDANGO = graphics.create_pen(181,51,137)

    BLUE = graphics.create_pen(0, 0, 255)
    RED = graphics.create_pen(255, 0, 0)
    YELLOW = graphics.create_pen(255,255,0)
    GREEN = graphics.create_pen(0,255,0)
    OFF_RED = graphics.create_pen(64, 0, 0)
    BORDER_RED = graphics.create_pen(128, 0, 0)
    OFF_YELLOW = graphics.create_pen(64,64,0)
    OFF_GREEN = graphics.create_pen(0,64,0)
else:
    RED = (255, 0, 0)
    OFF_RED = (64, 0, 0)
    YELLOW = (255,255,0)
    GREEN = (0,255,0)
    OFF_RED = (64, 0, 0)
    BORDER_RED = (128, 0, 0)
    OFF_YELLOW = (64,64,0)
    OFF_GREEN = (0,64,0)

def clear_board():
    if sys.implementation.name == 'micropython':
        graphics.remove_clip()
        graphics.set_pen(BLACK)
        graphics.clear()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def displaySignal(signalState=None, debug=False):
    if debug:
        print("Next...")
    sleep_time=signalState[3]
    print(u'\033[H', end="")
    print(u'\033[40m\u250F\u2501\u2513\033[m')
    print(u'\033[40m\u2503\033[91m' + ('\u25CF' if signalState[0] == RED else '\u25CB') + '\033[0;40m\u2503\033[m')
    print(u'\033[40m\u2503\033[93m' + ('\u25CF' if signalState[1] == YELLOW else '\u25CB') + '\033[0;40m\u2503\033[m')
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
def draw_polygon(points):
    print(f"Drawing polygon with points: {points}")
    graphics.polygon(points)
    pass

def drw_hallway():
    # Define the vanishing point
    vanishing_point = (16, 16)
    distance_gap = (1,2)

    # Define the points for the floor, walls, ceiling
    floor_points = [(0, 31), vanishing_point, (31, 31)]
    left_wall_points = [(0, 0), vanishing_point, (0, 31)]
    right_wall_points = [(31, 0), vanishing_point, (31, 31)]
    ceiling_points = [(0, 0), vanishing_point, (31, 0)]
    distance_points = [(vanishing_point[0]-distance_gap[0],vanishing_point[1]-distance_gap[1]),(vanishing_point[0]-distance_gap[0],vanishing_point[1]+distance_gap[1]),
                       (vanishing_point[0]+distance_gap[0],vanishing_point[1]+distance_gap[1]),(vanishing_point[0]+distance_gap[0],vanishing_point[1]-distance_gap[1])]

    # Draw the hallway using the draw_polygon function
    graphics.set_pen(FANDANGO)
    draw_polygon(floor_points)
    graphics.set_pen(MX2_BLUE)
    draw_polygon(left_wall_points)
    graphics.set_pen(MX_BLUE)
    draw_polygon(right_wall_points)
    graphics.set_pen(GREY)
    draw_polygon(ceiling_points)
    graphics.set_pen(BLACK)
    draw_polygon(distance_points)
    i75.update()
    pass

def drw_hallwayx():
    # display.line(x1, y1, x2, y2)
    graphics.set_pen(RED)
    # Draw floor
    graphics.line(1, 16, 31, 16)

    # Draw walls
    graphics.line(1, 1, 1, 16)
    graphics.line(31, 1, 31, 16)

    # Draw ceiling
    graphics.line(1, 1, 31, 1)

    # Draw doors
    graphics.line(16, 1, 16, 16)

    # Draw windows
    graphics.circle(8, 8, 3)
    graphics.circle(24, 8, 3)
    i75.update()
    pass

light_states = [[OFF_RED,OFF_YELLOW,GREEN,5],[OFF_RED,YELLOW,OFF_GREEN,2],[RED,OFF_YELLOW,OFF_GREEN,7]]

if __name__ == "__main__":
    print("Hallway")
    clear_board()
    # displaySignal(light_states[2])
    # run_signal()
    drw_hallway()

