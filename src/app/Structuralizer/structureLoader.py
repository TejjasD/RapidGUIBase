# Built by Tejas Deolasee

from app.Structuralizer.structureDefinition import *

#########################################################################################

class StructureLoader:
    def __init__(self, structureInstanceData, rootWidth, rootHeight):
        self.structureInstanceData = structureInstanceData
        self.structuresDictionary = {}
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

        self.loadStructures()

#########################################################################################

    def loadStructures(self):
        for i in range(0, len(self.structureInstanceData['structureId'])):
            if self.structureInstanceData['structureType'][i] == "S":
                structure = StructureSingleton(self.structureInstanceData.iloc[i], self.rootWidth, self.rootHeight)
                self.structuresDictionary[self.structureInstanceData['structureId'][i]] = structure

#########################################################################################
            


    