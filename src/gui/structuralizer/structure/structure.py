# Built by Tejas Deolasee

#########################################################################################

class Structure :
    def __init__(self, row, rootWidth, rootHeight):
        self.row = row
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

        self.startX = 0
        self.endX  = 0
        self.startY = 0
        self.endY = 0
        self.placement = 0
        self.id = 0
        self.type = None
        self.elementSpacing = 0
        self.elementsList = []
        self.buffer = 10

        self.implStructure()

#########################################################################################
    
    def implStructure(self):
        self.id = self.row[0]
        self.placement = self.row[2]
        self.startX = self.row[3]
        self.endX = self.row[4]
        self.startY = self.row[5]
        self.endY = self.row[6]
        self.elementSpacing = self.row[7]

        if self.endX == -1:
            self.endX = self.rootWidth
        if self.endY == -1 :
            self.endY = self.rootHeight

#########################################################################################

    def addElement(self, element):
        self.elementsList.append(element)

#########################################################################################
    
   