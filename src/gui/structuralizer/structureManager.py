# Built by Tejas Deolasee

from gui.structuralizer.structure.structureSingleton import StructureSingleton
from gui.structuralizer.structure.structureArray import StructureArray

#########################################################################################

class StructureManager:
    def __init__(self, structureInstanceData, rootWidth, rootHeight):
        self.structureInstanceData = structureInstanceData
        self.structureDictionary = {}
        self.rootWidth = rootWidth
        self.rootHeight = rootHeight

        self.loadStructures()

#########################################################################################

    def loadStructures(self):
        for i in range(0, len(self.structureInstanceData['structureId'])):
            if self.structureInstanceData['structureType'][i] == "S":
                structure = StructureSingleton(self.structureInstanceData.iloc[i], self.rootWidth, self.rootHeight)
                self.structureDictionary[self.structureInstanceData['structureId'][i]] = structure
            if self.structureInstanceData['structureType'][i] == "A":
                structure = StructureArray(self.structureInstanceData.iloc[i], self.rootWidth, self.rootHeight)
                self.structureDictionary[self.structureInstanceData['structureId'][i]] = structure

#########################################################################################

    def structuralize(self):
        for structure in self.structureDictionary:
            if len(self.structureDictionary[structure].elementsList) > 0:
                self.structureDictionary[structure].structuralize()

#########################################################################################

    def addElement(self, element):
        if element.structure in self.structureDictionary:
            self.structureDictionary[element.structure].addElement(element)

#########################################################################################
        
            


    