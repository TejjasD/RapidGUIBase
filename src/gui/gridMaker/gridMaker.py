# Built by Tejas Deolasee

#########################################################################################

class GridMaker:

    def __init__(self, screen, rootWidth, rootHeight, numRows , numCols):
        self.screen = screen
        self.width = rootWidth
        self.height = rootHeight
        self.numCols = numCols
        self.numRows = numRows
        self.xBuffer = 10
        self.yBuffer = 10
        self.columnWidth = 0
        self.rowHeight = 0
        self.posMatrix = [[(0, 0) for j in range(numCols)] for i in range(numRows)]


        self.calculateCellDimensions()


#########################################################################################

    def calculateCellDimensions(self):
        self.columnWidth = int((self.width - (2 * self.xBuffer)) / self.numCols)
        self.rowHeight = int((self.height - (2 * self.yBuffer)) / self.numRows)

#########################################################################################

    def getElementPos(self, columnStart, columnSpan, rowStart, rowSpan, placement):
        width = columnSpan * self.columnWidth
        height = rowSpan * self.rowHeight

        cellOrigin = self.cellPosition(columnStart, rowStart)

        pos = (0, 0)
        if placement == "center":
            pos = (cellOrigin[0] + width / 2, cellOrigin[1] + height /2)
        elif placement == "n":
            pos = (cellOrigin[0] + width / 2, cellOrigin[1])
        elif placement == "s":
            pos = (cellOrigin[0] + width / 2, cellOrigin[1] + height)
        elif placement == "e":
            pos = (cellOrigin[0] + width, cellOrigin[1] + height / 2)
        elif placement == "w":
            pos = (cellOrigin[0], cellOrigin[1] + height / 2)
        elif placement == "ne":
            pos = (cellOrigin[0], cellOrigin[1])
        elif placement == "nw":
            pos = (cellOrigin[0] + width, cellOrigin[1])
        elif placement == "sw":
            pos = (cellOrigin[0] + width, cellOrigin[1] + height)
        elif placement == "se":
            pos = (cellOrigin[0], cellOrigin[1] + height)
        else:
            print("----------------------------Invalid Placement ---------------------")
        
        return pos

#########################################################################################

    def positionElement(self, element):
        if (element.columnStart is not None):
            pos = self.getElementPos(element.columnStart, element.columnSpan, element.rowStart, element.rowSpan, element.sticky)
            element.pos = pos

#########################################################################################

    def cellPosition(self, column, row):
        if column < 0:
            column = self.screen.activeColumn + column - 1
        if row < 0:
            row = self.screen.activeRow + row - 1
        x = self.xBuffer + (column * self.columnWidth)
        y = self.yBuffer + (row * self.rowHeight)
        return (x, y)

#########################################################################################








    
