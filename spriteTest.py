import time
import os
from sprite import Sprite
import random
import TetrisBoardUtils

BOARD_SIZE = 10

S = [[0,1],
     [1,1],
     [1,0]]

Sq = [[1,1],
     [1,1]]


Z = [[1,0],
     [1,1],
     [0,1]]

T = [[0,1],
     [1,1],
     [0,1]]

L = [[1,0],
     [1,0],
     [1,1]]

J = [[0,1],
     [0,1],
     [1,1]]

I = [[1],
     [1],
     [1],
     [1]]

SpriteShapes = [S,Sq,Z,T,L,J,I]
Colors = ["R","Y","G","B","V"]

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

def board_full(context):
    for pixel in context[0]:
        if pixel != 0:
            return True
    return False

clear_board()

def newSprite(debug = False) -> Sprite:
    sprite = Sprite("Test" + str(m),Colors[random.randrange(len(Colors))],0,random.randrange(9),SpriteShapes[random.randrange(len(SpriteShapes))])
    sprite.setSpeed(1,0)
    if debug:
        print(sprite)
    return sprite

for m in range(2):
    Sprites.append(newSprite())

# sprite1 = Sprite("Test1","R",1,1,S)
# # sprite1.rotate90()
# sprite1.setSpeed(1,0)
# Sprites.append(sprite1)

# sprite2 = Sprite("Test2", "X", 1,1,Sq)
# sprite2.setSpeed(0,1)
# Sprites.append(sprite2)

# Sprite.printData("Blank:",canvas)

targetGap = 0
highestBlock = 0
for z in range(2000):
    if board_full(canvas):
        print("Board Full at " + str(z))
        break
    moved = False
    aSprite: Sprite
    for aSprite in Sprites:
    #    print("Checking potential collision")
        if not aSprite.updateWouldCollide(canvas, False):
            aSprite.eraseUpdateRedraw(canvas)
            moved = True
        else:
            aSprite.setSpeed(0,0)

        print("Comparingg " +str(aSprite.x) + ":" + str(targetGap))
        if aSprite.x > targetGap:
            aSprite.moveBy(-1,0)
            
    # Sprite.printData("Step " + str(z) + ":", canvas)
    TetrisBoardUtils.TetrisBoardUtils.drawBoardToScreen(canvas)
    print("Bottom line full? " + str(TetrisBoardUtils.TetrisBoardUtils.bottomLineFilled(canvas)))
    print("First open space " + str(TetrisBoardUtils.TetrisBoardUtils.firstOpenInBottomLine(canvas)))
    print("Target Gap is " + str(targetGap))
    print("Highest block is " + str(highestBlock))

    
    time.sleep(0.25)
    if not moved:
        print("All stop after " + str(z))
        new_sprite = newSprite()
        overlaps = new_sprite.checkOverlap(canvas)
        if overlaps:
            print(" Would overlap; Ending")
            break
        targetGap = TetrisBoardUtils.TetrisBoardUtils.firstOpenInBottomLine(canvas)    
        highestBlock = TetrisBoardUtils.TetrisBoardUtils.highestBlock(canvas)
        Sprites.append(newSprite())

TetrisBoardUtils.TetrisBoardUtils.drawBoardToScreen(canvas)



# canvas = sprite1.display(canvas)
# Sprite.printData("Initial:",canvas)

# for z in range(7):
#     canvas = sprite1.display(canvas,True)
#     sprite1.update()
#     canvas = sprite1.display(canvas)
#     Sprite.printData("Step " + str(z) + ":", canvas)


# canvas = sprite2.display(canvas)
# Sprite.printData("2 - Step 0:", canvas)

# for z in range(7):
#     canvas = sprite2.display(canvas,True)
#     sprite2.update()
#     canvas = sprite2.display(canvas)
#     Sprite.printData("2 - Step " + str(z) + ":", canvas)


# canvas = sprite1.display(canvas,True)
# sprite1.update()
# canvas = sprite1.display(canvas)
# Sprite.printData("Step 1:", canvas)

# canvas = sprite1.display(canvas,True)
# sprite1.update()
# canvas = sprite1.display(canvas)
# Sprite.printData("Step 2:", canvas)

# canvas = sprite1.display(canvas,True)
# sprite1.update()
# canvas = sprite1.display(canvas)
# Sprite.printData("Step 3:", canvas)

# canvas = sprite1.display(canvas,True)
# sprite1.update()
# canvas = sprite1.display(canvas)
# Sprite.printData("Step 4:", canvas)

# print(sprite1)
# sprite1.rotate90()
# print(sprite1)
# Sprite.printData(canvas)

# for i in range(BOARD_SIZE):
#     for j in range(BOARD_SIZE):
#         print(canvas[i][j], end=" ")
#     print()