# Block Solve
import os
import time
import sys
import BoardUtils

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


def is_valid(board, row, col, color,debug=True):
    if debug:
        print("Working row {:d} col {:d} of color {:d}".format(row,col,color))
    # Check if the color is already present in the row or column
    for i in range(9):
        if board[row][i] == color or board[i][col] == color:
            print("Row or Col" + str(i))
            return False

    # Check if the color is present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == color:
                return False

    return True

def is_block_valid(board,this_block,row,col,block_size=3,debug=False):
    if debug:
        print("Working on this block from " + str(row) + ":" + str(col) + "->")
        BoardUtils.print_board(this_block)
    orig_block = BoardUtils.extract_block(board,row,col)
    for attempt in range(block_size*block_size):
        b_row,b_col = find_empty_location(orig_block)
        if not b_row == None and not b_col == None:
            print(" Working on space at " + str(b_row) + ":" + str(b_col) + "->" + str(this_block[b_row][b_col]))
            if not is_valid(board,b_row,b_col,this_block[b_row][b_col]):    # This won't work past square 1. b_row and b_col need to translate
                print("Block at " + str(row) + ":" + str(col) + " Was not valid")
                return False
    print("Block at " + str(row) + ":" + str(col) + " Was valid")
    return True

def find_empty_location(board):
    # Find an empty location (cell with 0 value)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board,attempt=0):
    for i in range(attempt):
        print(" ",end="")
    print("Starting depth " + str(attempt))

    # Find an empty location
    row, col = BoardUtils.find_empty_block(board)

    # If there are no empty locations, the puzzle is solved
    if row is None:
        return True
    
    #the_good_perms
    index = BoardUtils.x_y_to_int(row,col,3)
    orig_board = [row[:] for row in board]
    print("For " + str(row) + ":" + str(col) + "-> " + str(len(the_good_perms[index])) + " possibilities")
    for perm in the_good_perms[index]:
        print("Trying block")
        BoardUtils.print_board(perm)
        
        # board = BoardUtils.merge_block_if_compatible(orig_board,perm,row,col)
        if not BoardUtils.is_compatible_block(board,perm,row,col):
            print("perm wasn't compatible")
            continue

        print("Potential Board")
        BoardUtils.print_board(board)
        if is_block_valid(orig_board,perm,row,col):
            board = BoardUtils.merge_block_if_compatible(board,perm,row,col)
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
            # board[row][col] = 0   # Might not need to revert with only good permutations

    # No valid color was found, backtrack to the previous empty location
    return False

def display_color_chart():
    clear_board()
    for i in range(3):
        for j in range(3):
            draw_value(0,0,j,i,led_mapping[((i*3)+j)+1],BLACK,7)
            i75.update()

def display_sudoku(board):
    print("Displaying")
    for i in range(9):
        for j in range(9):
            draw_value(0,0,j,i,led_mapping[board[i][j]],BLACK,3)
    graphics.set_pen(WHITE)
    graphics.line(11, 2, 11, 31)
    graphics.line(21, 2, 21,31)
    graphics.line(2,11,31,11)
    graphics.line(2,21,31,21)
    i75.update()
#     time.sleep(2)

def print_sudoku(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(color_mapping[board[i][j]], end=" ")
        print()

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    #display_color_chart()
    #sys.exit(1)
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("Original Sudoku:")
#     print_sudoku(sudoku_board)
#     if solve_sudoku_no_recursion2(sudoku_board):
    
    the_good_perms = BoardUtils.reduce_board_permutations(sudoku_board)

    if solve_sudoku(sudoku_board):
        if sys.implementation.name == 'micropython':
            display_sudoku(sudoku_board)
        
        print("\nSolved Sudoku:")
        print_sudoku(sudoku_board)
        
    else:
        print("\nNo solution exists.")
