import copy

class Sprite:
    title = ""

    DEFAULT = 0

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
        return f"{self.title}({self.color}){self.shapeData} at location {self.x}:{self.y} at pace {self.dx}:{self.dy}"

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
            # if debug:
            #     print("X is now " + str(x) + " and length is " + str(len(context)))
            if x >= len(context):
                return context
        return context

    def display(self,context,erase_mode=False,debug=False):
        return Sprite.displayTo(self,context,self.x,self.y,erase_mode,debug)
    
    def eraseUpdateRedraw(self,context,debug=False):
        context = Sprite.displayTo(self,context,self.x,self.y,True,debug)
        self.update()
        return Sprite.displayTo(self,context,self.x,self.y,False,debug)
    
    def checkOverlap(self,canvas, debug=False):
        if debug:
            print("Checking collision for object now at " + str(self.x) + ":" + str(self.y))

        newX = self.x
        for row in self.shapeData:
            newY = self.y
            for pixel in row:
                if debug:
                    print("  Checking for overlap at " + str(newX) + ":" + str(newY))
                if pixel == 1:
                    if canvas[newX][newY] != Sprite.DEFAULT:
                        if debug:
                            print(" -- Overlap at " + str(newX) + ":" + str(newY) + " was " + canvas[newX][newY])
                        return True
                    newY+=1
                    if newY >= len(canvas[newX]):
                        break
            newX+=1
        pass
    
    def updateWouldCollide(self,oldcontext,debug=False):
        if self.dx==0 and self.dy==0:
            return True
        aClone = copy.deepcopy(self)
        newContext = copy.deepcopy(oldcontext)

        # Remove object from context to avoid self collision
        context = Sprite.displayTo(self,newContext,aClone.x,aClone.y,True,False)

        aClone.update()

        if debug:
            print("Checking collision for object now at " + str(aClone.x) + ":" + str(aClone.y))

        newX = aClone.x
        for row in aClone.shapeData:
            if newX < len(context):
                print("X is now " + str(newX) + " and length is " + str(len(context)))
                newY = aClone.y
                for pixel in row:
                    if debug:
                        print("  Checking for overlap at " + str(newX) + ":" + str(newY))
                    if pixel == 1:
                        if context[newX][newY] != Sprite.DEFAULT:
                            if debug:
                                print(" -- Overlap at " + str(newX) + ":" + str(newY) + " was " + context[newX][newY])
                            return True
                    newY+=1
                    if newY >= len(context[newX]):
                        break
            newX+=1
            # if debug:
            #     print("X is now " + str(newX) + " and length is " + str(len(context)))
            if newX > len(context): # Off bottom of screen
                print("  -- Off bottom of screen")
                return True
        return False

    def printData(label="", data=[]):
        print(label)
        for i in range(len(data)):
            for j in range(10):
                print(data[i][j], end=" ")
            print()
        print()
    