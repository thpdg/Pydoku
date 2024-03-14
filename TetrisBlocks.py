class TetrisBlocks:
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

    # Returns a random block color from the known colors. Allows exclusion of undesired colors (For creating pallets, most likely)
    def RandomBlockColor(exclusions=[]):
        import random

        while True:
            randomColor = TetrisBlocks.Colors[random.randrange(len(TetrisBlocks.Colors))]
            if randomColor not in exclusions:
                return randomColor
            
    # Returns a random block shape from the known collection.  Allows exclusion of undesired (for creating challenges, most likely)
    def RandomBlockShape(exclusions=[]):
        import random

        while True:
            randomShape = TetrisBlocks.SpriteShapes[random.randrange(len(TetrisBlocks.SpriteShapes))]
            if randomShape not in exclusions:
                return randomShape
