import BoardSimulator
import BoardUtils

sudoku_board = BoardUtils.return_test_board_2()
large_board = BoardUtils.return_random_board(32,32)
my_sim = BoardSimulator.BoardSimulator(32,32)
# my_sim.print_sudoku(sudoku_board)
my_sim.print_sudoku_numbers(large_board)
my_sim.print_sudoku(large_board)
my_sim.display_color_chart()
# print(sudoku_board)
# print(large_board)