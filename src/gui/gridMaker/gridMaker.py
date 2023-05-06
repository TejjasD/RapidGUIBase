# Built by Tejas Deolasee

#########################################################################################

class GridMaker:

    def __init__(self, rootWidth, rootHeight, numRows , numCols):
        self.width = rootWidth
        self.height = rootHeight
        self.numCols = numCols
        self.numRows = numRows
        self.buffer = 10
        self.columnWidth = 0
        self.rowHeight = 0
        self.posMatrix = [[(0, 0) for j in range(numCols)] for i in range(numRows)]


        self.calculateCellPoses()


#########################################################################################

    def calculateCellPoses(self):
        self.columnWidth = int((self.width - (2 * self.buffer)) / self.numCols)
        self.rowHeight = int((self.height - (2 * self.buffer)) / self.numRows)

        shiftedOrigin = (self.buffer, self.buffer)

        for i in range(self.numRows):
            for j in range(self.numCols):
                self.posMatrix[i][j] = (shiftedOrigin[0] + (j * self.columnWidth), shiftedOrigin[1] + (i * self.rowHeight))

#########################################################################################

    def getElementPos(self, columnStart, columnSpan, rowStart, rowSpan, placement):
        width = columnSpan * self.columnWidth
        height = rowSpan * self.rowHeight

        cellOrigin = self.posMatrix[rowStart][columnStart]

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
        pos = self.getElementPos(element.columnStart, element.columnSpan, element.rowStart, element.rowSpan, element.sticky)
        element.pos = pos

#########################################################################################







    
