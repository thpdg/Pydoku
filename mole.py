import os
import time
import sys
import random
import BoardUtils

BOARD_SIZE = 6
RESET = "\033[0m"
BLACK_BG = "\033[40m"

color_mapping = {
    # 0: "\033[0m  ",        # empty, 2 spaces
    0: "\033[42m  \033[0m",   # green for empty

    1: "\033[41m  \033[0m",   # red
    2: "\033[44m  \033[0m",   # blue
    3: "\033[42m  \033[0m",   # green
    4: "\033[43m  \033[0m",   # yellow
    5: "\033[105m  \033[0m",  # pink (bright magenta)
    6: "\033[103m  \033[0m",  # orange-ish (bright yellow)
    7: "\033[46m  \033[0m",   # cyan/teal
    8: "\033[45m  \033[0m",   # purple-ish (magenta)
    9: "\033[47m  \033[0m",   # white/light
}

# move cursor to 1-based (row, col)
def goto(row, col):
    sys.stdout.write(f"\033[{row};{col}H")

def clear_screen():
    sys.stdout.write("\033[2J")
    sys.stdout.write("\033[H")

# Useful Functions
def find_empty_location(board):
    # Find an empty location (cell with 0 value)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def print_mole_board(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(color_mapping[board[i][j]], end=" ")
        print()


# Main()
if __name__ == "__main__":
    clear_screen()
    # print("Hello from mole.py")

    goto(2,1)

    mole_board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    try:
        r = 0
        c = 0
        color = 0
        while True:
            
            r = random.randint(0, 3)
            c = random.randint(0, 3)
            color = random.randint(1, 8)
            duration = random.randint(1,3)
            # goto(8,1)
            # print("Oh No! Mole at " + str(r) + "," + str(c) + " as " + str(color) + "     ")
            goto(2,1)
            # print(" ")
            mole_board[r][c] = color
            print_mole_board(mole_board)
            goto(20,1)
            print(" ")
            time.sleep(duration)
            mole_board[r][c] = 0
            goto(2,1)
            print_mole_board(mole_board)
            goto(20,1)
            print(" ")
            time.sleep(random.randint(1,4))
            

    except KeyboardInterrupt:
        # goto(BOARD_TOP + 12, 1)
        print(RESET + "Done.")


    
