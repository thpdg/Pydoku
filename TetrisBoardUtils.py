import sys
import os

class TetrisBoardUtils:
    colorTable = {
        0: "\033[30m\u2588",
        "R": "\033[91m\u2593",
        "Y": "\033[93m\u2593",
        "V": "\033[95m\u2593",
        "G": "\033[92m\u2593",
        "B": "\033[94m\u2593"
    }

    def clear_board():
        if sys.implementation.name == 'micropython':
            graphics.remove_clip()
            graphics.set_pen(BLACK)
            graphics.clear()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    def drawBoardToScreen(boardData):
        TetrisBoardUtils.clear_board()
        for row in boardData:
            for pixel in row:
                print(TetrisBoardUtils.colorTable[pixel] + TetrisBoardUtils.colorTable[pixel],end="")
            print()
            for pixel in row:
                print(TetrisBoardUtils.colorTable[pixel] + TetrisBoardUtils.colorTable[pixel],end="")    
            print()
        # print(u'\033[40m\u2503\033[91m' + ('\u25CF' if pixel == "R" else '\u25AE\u2588\u2593\u2588\u2593') + '\033[0;40m\u2503\033[m')
        # print(u'\033[40m\u2517\u2501\u251B\033[m')
        pass