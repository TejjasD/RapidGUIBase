# Built by Tejas Deolasee

from gui.structuralizer.structure.structure import Structure

#########################################################################################

class StructureArray(Structure):
    def __init__(self, row, rootWidth, rootHeight):
        super().__init__(row, rootWidth, rootHeight)
        self.type = "A"

#########################################################################################
    
    def structuralize(self):
        totalLength = 0
        for element in self.elementsList:
            totalLength += element.element.winfo_reqwidth()
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
                self.elementsList[i].pos = (structureStart + i*(self.elementsList[i-1].element.winfo_reqwidth() + self.elementSpacing), posY)
            self.elementsList[i].sticky = sticky

#########################################################################################

    
        