# i75 LED Grid Simulator
import sys
import time
import genperm

board_rows = 32
board_cols = 32
BOARD_SIZE = 32
LED_Board = []

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

def print_LEDs(board,size=BOARD_SIZE):
    for i in range(size):
        for j in range(size):
            print(color_mapping[board[i][j]], end=" ")
        print()

def solve_blocks(board: list, size=BOARD_SIZE) -> list:
    pass

# Create blank board
def initialize_LED(board, size, color):
    board = []
    new = []
    for i in range (0, size):
        for j in range (0, size):
            new.append(color)
        board.append(new)
        new = []
    return board


# Main...

LED_Board = initialize_LED(LED_Board, BOARD_SIZE, 2)
# print_LEDs(LED_Board)

boards = []
for i in range(10):
    boards.append(initialize_LED([],BOARD_SIZE,i))

# for board in boards:
#     print("\033[H", end="")
#     print_LEDs(board)
#     time.sleep(1)
    
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

digits = '123456789'
all_permutations = genperm.generate_all_permutations(digits)
# print(all_permutations)
print(len(all_permutations))
attempt = 0
for perm in all_permutations:
    print("\033[H", end="")
    print_LEDs(perm,3)
    print("Perm " + str(attempt))
    attempt+=1
    time.sleep(.005)

final_board = solve_blocks(sudoku_board)
print_LEDs(final_board)