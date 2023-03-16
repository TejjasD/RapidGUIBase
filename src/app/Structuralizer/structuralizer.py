# Built by Tejas Deolasee

#########################################################################################

class Structuralizer:
    def __init__(self, structureDictionary):
        self.structureDictionary = structureDictionary
        self.structuralize()

#########################################################################################
    
    def structuralize(self):
        for structure in self.structureDictionary:
            if len(self.structureDictionary[structure].elementsList) > 0:
                self.structureDictionary[structure].structuralize()

#########################################################################################