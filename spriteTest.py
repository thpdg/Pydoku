from sprite import Sprite
import random

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

I = [[0,1],
     [0,1],
     [0,1],
     [0,1]]

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

for m in range(2):
    sprite1 = Sprite("Test" + str(m),Colors[random.randrange(len(Colors))],0,2+m+m+m,SpriteShapes[random.randrange(len(SpriteShapes))])
    sprite1.setSpeed(1,0)
    print(sprite1)
    Sprites.append(sprite1)

# sprite1 = Sprite("Test1","R",1,1,S)
# # sprite1.rotate90()
# sprite1.setSpeed(1,0)
# Sprites.append(sprite1)

# sprite2 = Sprite("Test2", "X", 1,1,Sq)
# sprite2.setSpeed(0,1)
# Sprites.append(sprite2)

Sprite.printData("Blank:",canvas)

for z in range(8):
    for aSprite in Sprites:
        aSprite.eraseUpdateRedraw(canvas)
    Sprite.printData("Step " + str(z) + ":", canvas)



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