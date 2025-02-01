class BoardSimulator:
    color_mapping = {0: " ", 1: "\033[91m█\033[0m", 2: "\033[94m█\033[0m", 3: "\033[92m█\033[0m", 4: "\033[93m█\033[0m", 5: "\033[95m█\033[0m", 6: "\033[33m█\033[0m", 7: "\033[96m█\033[0m", 8: "\033[35m█\033[0m", 9: "\033[37m█\033[0m"}
    
    def __init__(self, board_size_x, board_size_y):
        self.size_x = board_size_x
        self.size_y = board_size_y

    def clear_board(self):
        pass

    def display_color_chart(self):
        self.clear_board()
        for i in range(9):
            print(self.color_mapping[i], end=" ")
        print()

    def print_sudoku(self, board):
        for i in range(self.size_x):
            for j in range(self.size_y):
                print(self.color_mapping[board[i][j]], end=" ")
            print()

    def print_sudoku_numbers(self, board):
        for i in range(self.size_x):
            for j in range(self.size_y):
                print(board[i][j], end=" ")
            print()
