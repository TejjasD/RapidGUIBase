# Built by Tejas Deolasee

#########################################################################################

class StructureSingleton:
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
        self.elementsList = []

        self.implStructure()

#########################################################################################
    
    def implStructure(self):
        self.id = self.row[0]
        self.placement = self.row[2]
        self.startX = self.row[3]
        self.endX = self.row[4]
        self.startY = self.row[5]
        self.endY = self.row[6]

        if self.endX == -1:
            self.endX = self.rootWidth
        if self.endY == -1 :
            self.endY = self.rootHeight

#########################################################################################
    
    def structuralize(self):
        if self.placement == "center":
            posX = (self.endX-self.startX)/2
            posY = (self.endY-self.startY)/2
            sticky = "center"    
        elif self.placement == "e":
            posX = self.endX
            posY = (self.endY-self.startY)/2
            sticky = "e"
        elif self.placement == "w":
            posX = self.startX
            posY = (self.endY-self.startY)/2
            sticky = "w"
        elif self.placement == "s":
            posX = (self.endX-self.startX)/2
            posY = self.endY
            sticky = "s"   
        elif self.placement == "n":
            posX = (self.endX-self.startX)/2
            posY = self.startY
            sticky = "n"  

        self.elementsList[0].pos = (posX, posY)
        self.elementsList[0].sticky = sticky

#########################################################################################

    
        