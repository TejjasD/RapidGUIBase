# Built by Tejas Deolasee

#########################################################################################

class StructureArray :
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
        self.type = "S"
        self.elementSpacing = 0
        self.elementsList = []
        self.buffer = 10
        self.conversionFcator = 50

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
    
    def structuralize(self):
        totalLength = 0
        for element in self.elementsList:
            totalLength += element.button.winfo_reqwidth()
            totalLength += self.elementSpacing
        totalLength -= self.elementSpacing

        structureStart = self.startX
        if self.placement == "center":
            structureStart = (self.endX - self.startX - totalLength)/2
            posY = self.startY + (self.endY-self.startY)/2
            sticky = "center"    
        elif self.placement == "e":
            structureStart = self.endX - totalLength - self.buffer
            posY = self.startY + (self.endY-self.startY)/2
            sticky = "e"
        elif self.placement == "w":
            structureStart = self.startX + self.buffer
            posY = self.startY + (self.endY-self.startY)/2
            sticky = "w"
        elif self.placement == "s":
            structureStart = (self.endX - self.startX - totalLength)/2
            posY = self.endY
            sticky = "s"   
        elif self.placement == "n":
            structureStart = (self.endX - self.startX - totalLength)/2
            posY = self.startY
            sticky = "n"  

        
        for i in range(len(self.elementsList)):
            if i == 0:
                self.elementsList[i].pos = (structureStart, posY)
            else:
                self.elementsList[i].pos = (structureStart + i*(self.elementsList[i-1].button.winfo_reqwidth() + self.conversionFcator + self.elementSpacing), posY)
            self.elementsList[i].sticky = sticky

#########################################################################################

    
        