# Built by Tejas Deolasee

from gui.structuralizer.structure.structure import Structure

#########################################################################################

class StructureSingleton(Structure):

    def __init__(self, row, rootWidth, rootHeight):
        super().__init__(row, rootWidth, rootHeight)
        self.type = "S"

#########################################################################################
    
    def structuralize(self):
        if self.placement == "center":
            posX = (self.endX-self.startX)/2
            posY = self.startY + (self.endY-self.startY)/2
            sticky = "center"    
        elif self.placement == "e":
            posX = self.endX
            posY = self.startY + (self.endY-self.startY)/2
            sticky = "e"
        elif self.placement == "w":
            posX = self.startX
            posY = self.startY + (self.endY-self.startY)/2
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

    
        