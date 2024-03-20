class Sprite:
    title = ""

    DEFAULT = 0

    def __init__(self, title, color, x=0,y=0,shapeData=None):
        self.title = title
        self.color = color
        if shapeData is None:
            self.shapeData = []
        else:
            self.shapeData = shapeData
        self.rotation = 0
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def __copy__(self):
        # self.normalizeArgs()
        tempSprite = Sprite(self.title, self.color, self.x, self.y, Sprite.deepCopy(self.shapeData))
        tempSprite.setSpeed(self.x,self.y)
        tempSprite.rotation = self.rotation
        return tempSprite

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

    def update(self,ticks=1, debug=False):
        for tick in range(ticks):
            if debug: print("Update sprite " + self.title + " on tick " + str(tick))
            self.x+=self.dx
            self.y+=self.dy

    def moveTo(self,new_x,new_y):
        self.x = new_x
        self.y = new_y

    def moveBy(self,delta_x,delta_y):
        return self.moveTo(self.x+delta_x,self.y+delta_y)

    def displayTo(self,context,x,y,erase_mode=True,debug=False):
        myx = x
        myy = y
        if debug: print("starting overlay at " + str(myx) + ":" + str(myy))

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
    
    # Filters not currently used
    def stopped(self,checkX=True,checkY=True, debug=False):
        if self.dx == 0:
            if self.dy == 0:
                if debug: print("Sprite " + self.title + " stopped filter (" + str(checkX) + ":" + str(checkY) + ")")
                return True
        return False
    
    def eraseUpdateRedraw(self,context,debug=False):
        context = Sprite.displayTo(self,context,self.x,self.y,True,debug)
        self.update()
        return Sprite.displayTo(self,context,self.x,self.y,False,debug)
    
    def deepCopy(object1=None, debug=False) -> list:
        if debug:
            print("Deep copying object of type " + str(type(object1)) + ":")
            print(object1)
            print(":")

        if object1 == None:
            return None
        
        if type(object1) is list:
            if type(object1[0]) is list:
                newList = []
                for thislist in object1:
                    if type(thislist) is list:
                        newList.append(thislist.copy())

                Sprite.printData("Deep copy created object of type " + str(type(newList)) + ":",newList, debug)
                return newList
            
        print("*!*!*! Deep Copy on unknown type")
        return None

    
    def checkOverlap(self,canvas, debug=False):
        if debug:
            print(" " + self.title + " checking while I'm at " + str(self.x) + ":" + str(self.y))

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
                        return [newX,newY]
                    newY+=1
                    if newY >= len(canvas[newX]):
                        break
            newX+=1
        return None
    
    def updateWouldCollide(self,oldcontext,debug=False):
        if self.dx==0 and self.dy==0:
            if debug: print("uWC: Piece not moving")
            return True
        aClone = self.__copy__()
        newContext = Sprite.deepCopy(oldcontext)
        Sprite.printData("uWC oldContext:",oldcontext, debug)
        Sprite.printData("uWC newContext:",newContext, debug)

        # Remove object from context to avoid self collision
        context = Sprite.displayTo(self,newContext,aClone.x,aClone.y,True,False)
        Sprite.printData("uWC After Removal", context, debug)

        aClone.update()

        if debug:
            print("Checking collision for object now at " + str(aClone.x) + ":" + str(aClone.y))

        newX = aClone.x
        Sprite.printData("self.shapeData",self.shapeData, debug)
        Sprite.printData("aClone.shapeData",aClone.shapeData, debug)
        for row in aClone.shapeData:
            if newX < len(context):
                if debug:
                    print("X is now " + str(newX) + " and length is " + str(len(context)))
                newY = aClone.y
                for pixel in row:
                    if debug:
                        print("  Checking for overlap at " + str(newX) + ":" + str(newY))
                    if pixel == 1:
                        try:
                            if context[newX][newY] != Sprite.DEFAULT:
                                if debug:
                                    print(" -- Overlap at " + str(newX) + ":" + str(newY) + " was " + context[newX][newY])
                                return True
                        except:
                            print("Failed to compare at " + str(newX) + ":" + str(newY))
                            Sprite.printData("Board Data Was:", context)

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

    @staticmethod
    def printData(label="", data=None):
        print(label)
        if data is None:
            return
        for i in range(len(data)):
            print("" + str(i) + ":\t", end="")
            for j in range(len(data[i])):
                print(data[i][j], end=" ")
            print()
        print()
    