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

    def clear_board(graphics=None):
        if sys.implementation.name == 'micropython':
            if graphics is not None:        
                graphics.remove_clip()
                graphics.set_pen(graphics.create_pen(0,0,0))
                graphics.clear()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    def drawBoardToScreen(boardData,clear_board = False, graphics=None):
        TetrisBoardUtils.clear_board(graphics) if clear_board else None
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

    def bottomLineFilled(boardData, debug = False):
        bottomLine = boardData[-1]
        count = bottomLine.count(0)
        print("Free squares: " + str(count))
        if count == 0:
            return True
        return False

    def firstOpenInBottomLine(boardData, debug = False):
        bottomLine = boardData[-1]
        count = 0
        for pixel in bottomLine:
            if pixel == 0:
                return count
            count+=1
        return 99

    def highestBlock(boardData, debug=False):
        rowNumber = 0
        for row in boardData:
            for pixel in row:
                if pixel != 0:
                    return len(boardData)-rowNumber
            rowNumber+=1
        return len(boardData)
    
    # Determines if board is full by examining top row for any present block
    def IsBoardFull(boardData, debug=False):
        print(boardData[0]) if debug else None
        for pixel in boardData[0]:
            print(pixel) if debug else None
            if pixel != 0:
                return True
        return False