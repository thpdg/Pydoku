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

def solve_sudoku(board):
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

            # Recursively solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the current color doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No valid color was found, backtrack to the previous empty location
    return False

def print_sudoku(board):
    color_mapping = {0: " ", 1: "\033[91m█\033[0m", 2: "\033[94m█\033[0m", 3: "\033[92m█\033[0m", 4: "\033[93m█\033[0m", 5: "\033[95m█\033[0m", 6: "\033[33m█\033[0m", 7: "\033[96m█\033[0m", 8: "\033[35m█\033[0m", 9: "\033[37m█\033[0m"}

    for i in range(9):
        for j in range(9):
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

    print("Original Sudoku:")
    print_sudoku(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_sudoku(sudoku_board)
    else:
        print("\nNo solution exists.")
