from interstate75 import Interstate75
from picographics import PicoGraphics
import sys
import os
from LEDColorTable import LEDColorTable

class TetrisBoardUtils:
    colorTable = {
        0: "\033[30m\u2588",
        "R": "\033[91m\u2593",
        "Y": "\033[93m\u2593",
        "V": "\033[95m\u2593",
        "G": "\033[92m\u2593",
        "B": "\033[94m\u2593"
    }

    @staticmethod
    def clear_board(graphics=None) -> None:
        if (graphics is not None) and sys.implementation.name == 'micropython':            
            TheColorTable = LEDColorTable.CreateColorTable(graphics)
            print("The color table: " + str(TheColorTable))
            if graphics is None: print("Can't clear screen wihtout context")
            graphics.remove_clip()
            graphics.set_pen(LEDColorTable.LEDColorTable["Black"])
            graphics.clear()
        #else:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def drawBoardToScreen(boardData,clear_board = False, i75: Interstate75|None = None):
        if i75 is not None:
            graphics = i75.display
        else:
            graphics = None

        if clear_board: TetrisBoardUtils.clear_board(graphics)
        for row in boardData:
            for pixel in row:
                print(TetrisBoardUtils.colorTable[pixel] + TetrisBoardUtils.colorTable[pixel],end="")
            print()
            for pixel in row:
                print(TetrisBoardUtils.colorTable[pixel] + TetrisBoardUtils.colorTable[pixel],end="")    
            print()
        if i75 is None:
            return
        graphics = i75.display

        # print(u'\033[40m\u2503\033[91m' + ('\u25CF' if pixel == "R" else '\u25AE\u2588\u2593\u2588\u2593') + '\033[0;40m\u2503\033[m')
        # print(u'\033[40m\u2517\u2501\u251B\033[m')
        tempx = 0
        for row in boardData:
            tempy = 0
            for pixel in row:
                graphics.set_pen(LEDColorTable.LEDColorTable[pixel])
                graphics.pixel(tempx,tempy)

        i75.update()
        

    @staticmethod
    def bottomLineFilled(boardData, debug = False):
        bottomLine = boardData[-1]
        count = bottomLine.count(0)
        if debug: print("Free squares: " + str(count))
        if count == 0:
            return True
        return False

    @staticmethod
    def firstOpenInBottomLine(boardData, debug=False) -> int:
        bottomLine = boardData[-1]
        count = 0
        for pixel in bottomLine:
            if pixel == 0:
                if debug: print("Found open space in bottom line at " + str(count))
                return count
            count+=1
        if debug: print("No open space found in bottom line")
        return 99

    @staticmethod
    def highestBlock(boardData, debug=False):
        rowNumber = 0
        for row in boardData:
            for pixel in row:
                if pixel != 0:
                    if debug: print("High located block in board data is at " + str(len(boardData)-rowNumber) + "(" + str(rowNumber) + ")")
                    return len(boardData)-rowNumber
            rowNumber+=1
        return len(boardData)
    
    @staticmethod
    # Determines if board is full by examining top row for any present block
    def IsBoardFull(boardData, debug=False):
        if debug: print(boardData[0])
        for pixel in boardData[0]:
            if debug: print(pixel)
            if pixel != 0:
                return True
        return False