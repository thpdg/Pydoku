import os
import time
import sys
import BoardUtils

if sys.implementation.name == 'micropython':
    from pimoroni_i2c import PimoroniI2C
    from breakout_ioexpander import BreakoutIOExpander
    from cosmic import CosmicUnicorn
    from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY

    # from pimoroni import HEADER_I2C_PINS  # or PICO_EXPLORER_I2C_PINS or HEADER_I2C_PINS
    # from interstate75 import Interstate75, DISPLAY_INTERSTATE75_32X32

    PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
    up_button = 8
    down_button = 12
    left_button = 10
    right_button = 14
    white_top_button = 6
    white_bottom_button = 3
    start_button = 6

    # Setup Cosmic Unicorn Board
    # Setup graphics for CU LED board
    i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
    ioe = BreakoutIOExpander(i2c, address=0x18)

    cu = CosmicUnicorn()
    graphics = PicoGraphics(DISPLAY)
    width = CosmicUnicorn.WIDTH
    height = CosmicUnicorn.HEIGHT

    # cu.set_brightness(0.75)
    cu.set_brightness(1.0)

    for setup_pin in range(1,15):
        ioe.set_mode(setup_pin, BreakoutIOExpander.PIN_IN_PU)

last_state = True

BLOCK_SIZE = 3
BOARD_SIZE = 9
LINE_SIZE = 1
VALUE_SIZE_PIXELS = 3

if sys.implementation.name == 'micropython':
# Define Colors
    WHITE = graphics.create_pen(255, 255, 255)
    BLACK = graphics.create_pen(0,0,0)

    BLUE = graphics.create_pen(0, 0, 255)
    RED = graphics.create_pen(255, 0, 0)
    YELLOW = graphics.create_pen(255,255,0)
    GREEN = graphics.create_pen(0,255,0)
    PURPLE = graphics.create_pen(128,0,128)
    ORANGE = graphics.create_pen(255,165,0)
    CYAN = graphics.create_pen(40,255,255)
    PINK = graphics.create_pen(255,182,193)
    TEAL = graphics.create_pen(0,100,100)
	#GOLD = graphics.create_pen(255, 215, 0)
    SALMON = graphics.create_pen(255, 99, 71)

    led_mapping = {0: BLACK, 1: RED, 2: BLUE, 3: GREEN, 4: YELLOW, 5:PINK, 6:ORANGE, 7:CYAN, 8:PURPLE, 9:SALMON}
color_mapping = {0: " ", 1: "\033[91m█\033[0m", 2: "\033[94m█\033[0m", 3: "\033[92m█\033[0m", 4: "\033[93m█\033[0m", 5: "\033[95m█\033[0m", 6: "\033[33m█\033[0m", 7: "\033[96m█\033[0m", 8: "\033[35m█\033[0m", 9: "\033[37m█\033[0m"}


# Draw a segment
def draw_value(qx,qy,sx,sy,fg,bg,square_dim):
    # graphics.set_clip(qx*17,qy*17, qx+15, qy+15)
    graphics.set_pen(fg)
    x = (qx*10) + (sx*square_dim)
    x = x + 1 if x > 8 else x
    x = x + 1 if x > 16 else x
    y = (qy*10) + (sy * square_dim)
    y = y + 1 if y > 8 else y
    y = y + 1 if y > 16 else y  
    graphics.rectangle(x+2, y+2, square_dim, square_dim)
    # graphics.remove_clip()
#     print("Drawn")
    pass

def clear_board():
    graphics.remove_clip()
    graphics.set_pen(BLACK)
    graphics.clear()
    pass


def is_valid(board, row, col, color):
    # Check if the color is already present in the row or column
    for i in range(9):
        if board[row][i] == color or board[i][col] == color:
            return False

    # Check if the color is present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == color:
                return False

    return True

def find_empty_location(board):
    # Find an empty location (cell with 0 value)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku_no_recursion2(board):
    stack = [(int(0), int(0))]  # Stack to store (row, col) pairs
    while stack:
        row, col = stack[-1]
        print("Starting Row " + str(row) + " col " + str(col))

        # Find an empty location
        while row < 9 and board[row][col] != 0:
            row, col = (row + 1, col) if col < 8 else (row + 1, 0)
        print("Row " + str(row) + " col " + str(col))

        if row == 9:  # Solved if we reach the end
            return True

        # Try placing a number from 1 to 9
        for num in range(board[row][col] + 1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                stack.append((row, col))
                display_sudoku(sudoku_board)
                break
        else:  # No valid number was found, backtrack
            board[row][col] = 0
            stack.pop()

    return False


def solve_sudoku_no_recursion(board):
    stack = [(int(0), int(0))]  # Stack to store (row, col) pairs
    while stack:
        row, col = stack.pop()

        # Find an empty location
        while row < 9 and board[row][col] != 0:
            row, col = (row + 1, col) if col < 8 else (row + 1, 0)

        print("Row " + str(row) + " col " + str(col))

        if row == 9:  # Solved if we reach the end
            return True

        # Try placing a number from 1 to 9
        for num in range(1, 10):
            print(" num " + str(num))
            if is_valid(board, row, col, num):
                board[row][col] = num
                stack.append((row, col))
                display_sudoku(sudoku_board)
                col = 0
                break
        else:  # No valid number was found, backtrack
            board[row][col] = 0

    return False

# Rest of the code remains unchanged


def solve_sudoku(board,attempt=0):
    for i in range(attempt):
        print(" ",end="")
    print("Starting depth " + str(attempt))
    # Find an empty location
    row, col = find_empty_location(board)

    # If there are no empty locations, the puzzle is solved
    if row is None:
        return True

    # Try placing a color from 1 to 9
    for color in range(1, 10):
        if is_valid(board, row, col, color):
            # Place the color if it's valid
            board[row][col] = color
                        
            if sys.implementation.name == 'micropython':
                display_sudoku(sudoku_board)
            else:
                print("\033[H", end="")
                print_sudoku(sudoku_board)

            time.sleep(0.2)

            # Recursively solve the rest of the puzzle
            if solve_sudoku(board,attempt+1):
                return True

            # If placing the current color doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No valid color was found, backtrack to the previous empty location
    return False

def display_color_chart():
    clear_board()
    for i in range(3):
        for j in range(3):
            draw_value(0,0,j,i,led_mapping[((i*3)+j)+1],BLACK,7)
            cu.update(graphics)

def display_sudoku(board):
#     print("Displaying")
    for i in range(9):
        for j in range(9):
            draw_value(0,0,j,i,led_mapping[board[i][j]],BLACK,3)
    graphics.set_pen(WHITE)
    graphics.line(11, 2, 11, 31)
    graphics.line(21, 2, 21,31)
    graphics.line(2,11,31,11)
    graphics.line(2,21,31,21)
    cu.update(graphics)
#     time.sleep(2)

def print_sudoku(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(color_mapping[board[i][j]], end=" ")
        print()

def print_sudoku_numbers(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    # sudoku_board = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]
    sudoku_board = BoardUtils.return_test_board_2()
    
    #display_color_chart()
    #sys.exit(1)
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("Original Sudoku:")
#     print_sudoku(sudoku_board)

    start_time = time.time()

#     if solve_sudoku_no_recursion(sudoku_board):
    if solve_sudoku(sudoku_board):
        if sys.implementation.name == 'micropython':
            display_sudoku(sudoku_board)
        
        print("\nSolved Sudoku:")
        print_sudoku(sudoku_board)
        print_sudoku_numbers(sudoku_board)
        
    else:
        print("\nNo solution exists.")

    print("--- %s seconds ---" % (time.time() - start_time))