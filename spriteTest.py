import time
import os
from sprite import Sprite
import random
from TetrisBoardUtils import TetrisBoardUtils
from TetrisBlocks import TetrisBlocks

BOARD_SIZE = 10

Sprites = []

canvas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def clear_board():
#     if sys.implementation.name == 'micropython':
#         graphics.remove_clip()
#         graphics.set_pen(BLACK)
#         graphics.clear()
#     else:
    os.system('cls' if os.name == 'nt' else 'clear')


# Creates a new random sprite for testing
def newSprite(index = 0, debug = False) -> Sprite:
    sprite = Sprite("Block" + str(index),TetrisBlocks.RandomBlockColor(),0,random.randrange(9),TetrisBlocks.RandomBlockShape())
    sprite.setSpeed(1,0)
    if debug:
        print(sprite)
    return sprite


# Initialize piece tracking variables and game status
_mainDebug = True
_mainAutosteer = False
targetGap = 0
highestBlock = 0

if __name__ == "__main__":
    clear_board()   # Clear board and terminal to begin game

    # Create and place a starting piece
    Sprites.append(newSprite(1))

# Display initial empty board. Helps to visually confirm board shape and size
if _mainDebug: Sprite.printData("Blank:",canvas)

# Generate and move up to 2000 tetris blocks for testing
for z in range(2000):
    if TetrisBoardUtils.IsBoardFull(boardData=canvas, debug=False):
        print("Board Full at " + str(z))
        break
    moved = False
    aSprite: Sprite
    for aSprite in Sprites:
        if aSprite.stopped():   # Skip blocks that aren't moving
            continue

        if not aSprite.updateWouldCollide(canvas, True):
            aSprite.eraseUpdateRedraw(canvas)
            moved = True
        else:
            print("Piece stopped")
            aSprite.setSpeed(0,0)

        # Random rotations
        rotationCount = random.randint(0,4)
        for rc in range(rotationCount+1):
            aSprite.rotate90()

        if _mainAutosteer:
            print("Autosteer Comparing " + str(aSprite.y) + ":" + str(targetGap))
            if aSprite.y > targetGap:
                if _mainDebug: print(" Steering left")
                aSprite.moveBy(0,-1)
            else:
                if aSprite.y < targetGap:
                    if _mainDebug: print(" Steering right")
                    aSprite.moveBy(0,1)
            
    TetrisBoardUtils.drawBoardToScreen(canvas, True)
    print("Bottom line full? " + str(TetrisBoardUtils.bottomLineFilled(canvas)))
    print("First open space " + str(TetrisBoardUtils.firstOpenInBottomLine(canvas)))
    print("Target Gap is " + str(targetGap))
    print("Highest block is " + str(highestBlock))

    
    time.sleep(0.25)
    if not moved:
        print("Adding block after step " + str(z))
        new_sprite = newSprite(z, _mainDebug)
        overlaps = new_sprite.checkOverlap(canvas, _mainDebug)
        if overlaps != None:
            print(" New block would overlap at " + str(overlaps[0]) + ":" + str(overlaps[1]) + "; Ending")
            aSprite.display(canvas)
            break
        targetGap = TetrisBoardUtils.firstOpenInBottomLine(canvas)    
        highestBlock = TetrisBoardUtils.highestBlock(canvas)
        Sprites.append(newSprite())

print("Final Board:")
TetrisBoardUtils.drawBoardToScreen(canvas)
