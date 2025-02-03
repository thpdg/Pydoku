
import sys
import os
from LEDColorTable import LEDColorTable

if sys.implementation.name == 'micropython':
    from cosmic import CosmicUnicorn
    from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY

else:
    class CosmicUnicorn:
        def update(self):
            pass
        def display(self):
            pass
    class PicoGraphics:
        pass

class TetrisBoardUtils:
    # TODO: Expand color table to further ANSI colors
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
            print("Clear board doing LED " + str(graphics))         
            TheColorTable = LEDColorTable.CreateColorTable(graphics)
            if TheColorTable is None:
                return None
            print("The color table: " + str(TheColorTable))
            if graphics is None: print("Can't clear screen wihtout context")
            graphics.remove_clip()
            graphics.set_pen(TheColorTable["Black"])
            graphics.clear()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def drawBoardToLEDs(boardData,clear_board = False, graphics: PicoGraphics = None, cu: CosmicUnicorn = None):
        theColorTable = LEDColorTable.CreateColorTable(graphics)
        if theColorTable is None:
            return None
        if clear_board:
            print("Clearing board")
            TetrisBoardUtils.clear_board(graphics)
        if cu is None:
            print("No LEDs. Skipping LEDs")
            return

        tempx = 0
        for row in boardData:
            tempy = 0
            for pixel in row:
                graphics.set_pen(theColorTable[pixel])
                graphics.pixel(tempy,tempx)
                print("Drew pixel at " + str(tempx) + ":" + str(tempy))
                tempy+=1
            tempx+=1

        cu.update(graphics)
        #time.sleep(1)

    @staticmethod
    def drawBoardToTerminal(boardData,clear_board = False):
        if clear_board: TetrisBoardUtils.clear_board(None)
        for row in boardData:
            for pixel in row:
                print(TetrisBoardUtils.colorTable[pixel] + TetrisBoardUtils.colorTable[pixel],end="")
            print()
            for pixel in row:
                print(TetrisBoardUtils.colorTable[pixel] + TetrisBoardUtils.colorTable[pixel],end="")    
            print()

        print("\033[92m",end="")    

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