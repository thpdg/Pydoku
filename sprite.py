class Sprite:
    title = ""

    def __init__(self, title, color, x=0,y=0,shapeData=[]):
        self.title = title
        self.color = color
        self.shapeData = shapeData
        self.rotation = 0
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def __str__(self) -> str:
        return f"{self.title}({self.color}){self.shapeData}"

    def rotate90(self, debug=False):
        # Rotate the piece 90 degrees clockwise
        if debug:
            print("About to rotate")
            print("Rotation was " + str(self.rotation) + " " + str(self.shapeData))
        self.shapeData = [list(row) for row in zip(*self.shapeData[::-1])]
        self.rotation = (self.rotation + 1) % 4
        if debug:
            print("Rotation is now " + str(self.rotation) + " " + str(self.shapeData))
    
    def setSpeed(self,new_dx,new_dy):
        self.dx = new_dx
        self.dy = new_dy

    def update(self,ticks=1):
        self.x+=self.dx
        self.y+=self.dy

    def moveTo(self,new_x,new_y):
        self.x = new_x
        self.y = new_y

    def displayTo(self,context,x,y,erase_mode,debug=False):
        myx = x
        myy = y
        if debug:
            print("starting overlay at " + str(x) + ":" + str(y))

        for row in self.shapeData:
            myy = y
            for pixel in row:
                if debug:
                    print("Overlaying " + str(pixel) + " at " + str(x) + ":" + str(myy))
                if pixel == 1:
                    if erase_mode:
                        context[x][myy] = 0
                    else:
                        context[x][myy] = self.color
                myy+=1
                if myy >= len(context[x]):
                    break
            x+=1
            if debug:
                print("X is now " + str(x) + " and length is " + str(len(context)))
            if x >= len(context):
                return context
        return context

    def display(self,context,erase_mode=False,debug=False):
        return Sprite.displayTo(self,context,self.x,self.y,erase_mode,debug)
    
    def eraseUpdateRedraw(self,context,debug=False):
        context = Sprite.displayTo(self,context,self.x,self.y,True,debug)
        self.update()
        return Sprite.displayTo(self,context,self.x,self.y,False,debug)

    def printData(label="", data=[]):
        print(label)
        for i in range(len(data)):
            for j in range(10):
                print(data[i][j], end=" ")
            print()
        print()
    