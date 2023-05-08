# Built by Tejas Deolasee

from gui.tkInter.elements.element import Element
import tkinter as tk
import math

#########################################################################################


class Label(Element):
    
    def implInstanceData(self):
        self.type = "label"
        self.id = self.instanceData[0]
        self.pos = (self.instanceData[1], self.instanceData[2])
        self.rowStart = int(self.instanceData[3])
        self.rowSpan = int(self.instanceData[4]) - self.rowStart + 1
        self.columnStart = int(self.instanceData[5])
        self.columnSpan = int(self.instanceData[6]) - self.columnStart + 1
        self.sticky = self.instanceData[7]

        if not isinstance(self.sticky, str):
            if math.isnan(self.sticky):
                self.sticky = ""
    

    def createElement(self):
        self.element = tk.Label(fg = self.uiAssets[1], 
                              bg = self.uiAssets[2],
                              font = (self.uiAssets[3], self.uiAssets[4]), 
                              text = self.instanceData[8])


#########################################################################################